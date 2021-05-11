# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org). See the COPYRIGHT file at the top - level directory
# of this distribution for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

__all__ = ["BoxChartWidget", "PSDWidget"]

import TimeChart
import TimeBoxChart
from VMSGUI import ToolBar
from PySide2.QtCore import Qt, Slot, Signal, QPointF, QSettings
from PySide2.QtWidgets import (
    QWidget,
    QDockWidget,
    QTabWidget,
    QGridLayout,
    QLabel,
    QMenu,
)
from PySide2.QtCharts import QtCharts
from asyncqt import asyncSlot

import abc
import asyncio
import concurrent.futures
from datetime import datetime
import numpy as np
import time


class VMSChartView(TimeChart.TimeChartView):
    def __init__(self, title):
        super().__init__(title)
        self._maxSensor = 0

    def updateMaxSensor(self, maxSensor):
        self._maxSensor = max(self._maxSensor, maxSensor)

    def clear(self):
        self.chart().clearData()

    def addSerie(self, name):
        s = QtCharts.QBoxPlotSeries()
        s.setName(name)
        removed = []
        for os in self.chart().series():
            if os.name() > name:
                removed.append(os)
                self.removeSeries(os)

        self.chart().addSeries(s)
        for os in removed:
            self.chart().addSeries(os)

    def removeSerie(self, name):
        self.chart().remove(name)

    def contextMenuEvent(self, event):
        contextMenu = QMenu()
        zoomOut = contextMenu.addAction("Zoom out")
        clear = contextMenu.addAction("Clear")
        for s in range(1, self._maxSensor + 1):
            for a in ["X", "Y", "Z"]:
                name = f"{s} {a}"
                action = contextMenu.addAction(name)
                action.setCheckable(True)
                action.setChecked(self.chart().findSerie(name) is not None)

        action = contextMenu.exec_(event.globalPos())
        if action is None:
            return
        elif action == zoomOut:
            self.chart().zoomReset()
        elif action == clear:
            self.clear()
        else:
            name = action.text()
            if action.isChecked():
                self.addSerie(name)
            else:
                self.removeSerie(name)


class BoxChartWidget(QDockWidget):
    """Display box chart with accelerometer data.

    Parameters
    ----------
    title : `str`
        QDockWidget title and object name.
    comm : `SALComm`
        SALComm object providing data.
    channels : `[(sensor, axis)]`
        Enabled channels.
    """

    def __init__(self, title, comm, channels):
        super().__init__(title)
        self.setObjectName(title)
        self.channels = channels
        self.chart = TimeBoxChart.TimeBoxChart()
        self.chartView = VMSChartView(self.chart)
        self.setWidget(self.chartView)

        comm.data.connect(self.data)

    @Slot(map)
    def data(self, data):
        self.chartView.updateMaxSensor(data.sensor)
        for axis in ["X", "Y", "Z"]:
            name = f"{str(data.sensor)} {axis}"
            if self.chart.findSerie(name) is not None:
                self.chart.append(
                    data.timestamp,
                    "Acceleration (m/s<sup>2</sup>)",
                    name,
                    getattr(data, f"acceleration{axis}"),
                )


class PSDWidget(QDockWidget):
    """Display signal PSD.

    Parameters
    ----------
    title : `str`
        QDockWidget title and object name.
    cache : `VMSCache`
        Data cache.
    channels : `[(sensor, axis)]`
        Enabled channels.
    """

    def __init__(self, title, cache, SAMPLE_TIME, channels=[]):
        super().__init__(title)
        self.setObjectName(title)
        self.SAMPLE_TIME = SAMPLE_TIME

        self.chart = QtCharts.QChart()

        # processing task. Set to done to save "is not None" check.
        self.updateTask = asyncio.Future()
        self.updateTask.set_result(None)

        self.update_after = 0

        self.cache = cache
        for channel in channels:
            self.addChannel(channel[0], channel[1])

        self.chart.createDefaultAxes()
        self.chart.axes(Qt.Horizontal)[0].setGridLineVisible(True)
        self.chart.axes(Qt.Horizontal)[0].setMinorTickCount(9)
        self.chart.axes(Qt.Horizontal)[0].setMinorGridLineVisible(True)

        self.chart.legend().setAlignment(Qt.AlignLeft)

        self.chartView = VMSChartView(self.chart)
        self.setWidget(self.chartView)

    def addChannel(self, s, a):
        serie = QtCharts.QLineSeries()
        serie.setName(str(s) + " " + a)
        self.chart.addSeries(serie)

    @Slot(int, int, float, float)
    def cacheUpdated(self, index, length, startTime, endTime):
        """Process and plot data.

        Parameters
        ----------
        index : `int`
        length : `int`
        startTime : `float`
        endTime : `float`
        """

        def downsample(psd, N):
            """Downsample PSD so no too many points are plot. Replace PSD with
            max of subarray and frequency with mean frequency.
            Parameters
            ----------
            psd : `[float]`
                Original, full scale PSD. len(psd) ~= N // 2
            N : `int`
                Size of original signal.
            """
            fMin = self.chart.axes(Qt.Horizontal)[0].min()
            fMax = self.chart.axes(Qt.Horizontal)[0].max()

            frequencies = np.fft.rfftfreq(N, self.SAMPLE_TIME)

            f = iter(frequencies)
            rMin = 0
            try:
                while next(f) < fMin:
                    rMin += 1
                rMax = rMin
                try:
                    while next(f) < fMax:
                        rMax += 1
                except StopIteration:
                    pass
                rMin = max(0, rMin - 2)
                rMax = min(len(frequencies) - 1, rMax + 2)
            except StopIteration:
                return (psd[-2:-1], frequencies[-2:-1])

            psd = psd[rMin:rMax]
            frequencies = frequencies[rMin:rMax]
            dataPerPixel = len(psd) / self.chart.plotArea().width()
            # downsample if points are less than 2 pixels apart, so the points
            # are at least 2 pixels apart
            if dataPerPixel > 0.5:
                s = int(np.floor(dataPerPixel * 2.0))
                N = len(psd)
                psd = [max(psd[i : i + s]) for i in range(0, N, s)]
                # frequencies are monotonic constant step. So to calculate
                # average, only took boundary members and divide by two
                frequencies = [
                    (frequencies[i] + frequencies[min(i + s, N - 1)]) / 2
                    for i in range(0, N, s)
                ]
            return (psd, frequencies)

        def plot(serie, signal):
            """Calculates and plot PSD - Power Spectral Density. Downsamples
            the calculated PSD so reasonable number of points is displayed.

            Parameters
            ----------
            serie : `QLineSeries`
                Line serie.
            signal : `[float]`
                Input signal.

            Returns
            -------
            min : `float`
                PSD subplot minimum value.
            max : `float`
                PSD subplot maximum value.
            """
            N = len(signal)
            # as input is real only, fft is symmetric; rfft is enough
            psd = np.abs(np.fft.rfft(signal)) ** 2 * self.SAMPLE_TIME / N

            (psd, frequencies) = downsample(psd, N)

            points = [QPointF(frequencies[r], psd[r]) for r in range(len(psd))]
            serie.replace(points)

            return min(psd), max(psd)

        def plotAll():
            """Plot all signals. Run as task in thread."""

            #   min_psd, max_psd = plot(
            #   0,
            #   np.mean(
            #      [self.cache[s + self.samples[0]] for s in ["1", "2", "3"]],
            #      axis=0,
            #   ),
            #   )
            #   self.chart.axes(Qt.Vertical)[0].setRange(min_psd, max_psd)
            min_psd = []
            max_psd = []
            for s in self.chart.series():
                min_p, max_p = plot(s, self.cache[s.name()])
                min_psd.append(min_p)
                max_psd.append(max_p)

            self.chart.axes(Qt.Vertical)[0].setRange(min(min_psd), max(max_psd))

        if not (self.update_after is None):
            if self.update_after < time.monotonic():
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    self.updateTask = pool.submit(plotAll)
                self.update_after = None
        elif self.updateTask.done():
            self.updateTask.result()
            self.update_after = time.monotonic() + 1

    @Slot(float, float)
    def frequencyChanged(self, low, high):
        self.chart.axes(Qt.Horizontal)[0].setRange(low, high)
