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

import TimeChart
import TimeBoxChart
from VMSCache import *
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

import astropy.units as u
import asyncio
import concurrent.futures
from datetime import datetime
import numpy as np
import time

SAMPLE_TIME = 1 * u.ms.to(u.s)
"""Sample time (seconds)"""


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
    numSensors : `int`
        Number of sensors (and hence number of charts). Chart is created to
        display X,Y and Z values per sensor."""

    def __init__(self, title, comm, channels):
        super().__init__(title)
        self.setObjectName(title)
        self.channels = channels
        self.maxSensor = 0
        self.chart = TimeBoxChart.TimeBoxChart()
        self.setWidget(TimeChart.TimeChartView(self.chart))

        comm.data.connect(self.data)

    @Slot(map)
    def data(self, data):
        if data.sensor > self.maxSensor:
            self.maxSensor = data.sensor
        for ch in self.channels:
            if ch[0] == data.sensor:
                self.chart.append(
                    data.timestamp,
                    "Acceleration (m/s<sup>2</sup>)",
                    f"{data.sensor} {ch[1]}",
                    getattr(data, f"acceleration{ch[1]}"),
                )

    def contextMenuEvent(self, event):
        contextMenu = QMenu("Test")
        clear = contextMenu.addAction("Clear")
        for s in range(1, self.maxSensor + 1):
            for a in ["X", "Y", "Z"]:
                action = contextMenu.addAction(f"{s} {a}")
                action.setCheckable(True)
                action.setChecked(self.channels.count((s, a)))

        action = contextMenu.exec_(event.globalPos())
        if action is None:
            return
        if action == clear:
            self.channels = []
            self.chart.clearData()
            return

        item = (int(action.text()[0]), action.text()[2])
        if action.isChecked():
            self.channels.append(item)
        else:
            self.channels.remove(item)
            self.chart.remove(action.text())


class PSDWidget(QWidget):
    """Display signal PSD.

    Parameters
    ----------
    title : `str`
        QDockWidget title and object name.
    samples : `[str]`
        Name of cache columns which will be displayed. Cache columns are two
        letters n[XYZ], where n is sensor (1 to 3 or to 6 for 6 channels) and
        X, Y or Z is sensor axis.
    cache : `VMSCache`
        Data cache.
    """

    def __init__(self, samples, cache):
        super().__init__()

        self.samples = samples
        self.cache = cache

        layout = QGridLayout()
        self.setLayout(layout)

        self.chart = QtCharts.QChart()

        self.psdSeries = []
        # processing task. Set to done to save "is not None" check.
        self.updateTask = asyncio.Future()
        self.updateTask.set_result(None)

        self.update_after = 0

        for s in samples:
            serie = QtCharts.QLineSeries()
            serie.setName(s)
            self.psdSeries.append(serie)
            self.chart.addSeries(serie)

        self.chart.createDefaultAxes()
        self.chart.axes(Qt.Horizontal)[0].setGridLineVisible(True)
        self.chart.axes(Qt.Horizontal)[0].setMinorTickCount(9)
        self.chart.axes(Qt.Horizontal)[0].setMinorGridLineVisible(True)

        self.chart.legend().setAlignment(Qt.AlignLeft)

        layout.addWidget(TimeChart.TimeChartView(self.chart), 0, 0)

    def data(self, mean=False):
        """Process and plot data.

        Parameters
        ----------
        mean : `bool`
            Instead of plotting PSD from all channels, plot PSD from mean of
            the channels."""

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

            frequencies = np.fft.rfftfreq(N, SAMPLE_TIME)

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
            serie : `int`
                PSD number.
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
            psd = np.abs(np.fft.rfft(signal)) ** 2 * SAMPLE_TIME / N

            (psd, frequencies) = downsample(psd, N)

            points = [QPointF(frequencies[r], psd[r]) for r in range(len(psd))]
            self.psdSeries[serie].replace(points)

            return min(psd), max(psd)

        def plotAll(mean):
            """Plot all signals. Run as task in thread.

            Parameters
            ----------
            mean : `bool`
                Use mean of input signals instead of independent signals."""

            if mean:
                min_psd, max_psd = plot(
                    0,
                    np.mean(
                        [self.cache[s + self.samples[0]] for s in ["1", "2", "3"]],
                        axis=0,
                    ),
                )
                self.chart.axes(Qt.Vertical)[0].setRange(min_psd, max_psd)

            else:
                min_psd = []
                max_psd = []
                for i in range(len(self.samples)):
                    min_p, max_p = plot(i, self.cache[self.samples[i]])
                    min_psd.append(min_p)
                    max_psd.append(max_p)

                self.chart.axes(Qt.Vertical)[0].setRange(min(min_psd), max(max_psd))

        if not (self.update_after is None):
            if self.update_after < time.monotonic():
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    self.updateTask = pool.submit(plotAll, mean)
                self.update_after = None
        elif self.updateTask.done():
            self.updateTask.result()
            self.update_after = time.monotonic() + 1

    @Slot(float, float)
    def frequencyChanged(self, low, high):
        self.chart.axes(Qt.Horizontal)[0].setRange(low, high)


class AccelerometersPageWidget(QDockWidget):
    """Displays all VMS widgets.

    TODO: replace with a generic widget, allowing user to customize what
    he/she would like to see."""

    SENSORS = [
        f"acceleration{a}Sensor{s}" for s in range(1, 4) for a in ["X", "Y", "Z"]
    ]

    cacheUpdated = Signal(int, float, float)

    def __init__(self, comm, module, toolbar):
        super().__init__("PSD")
        self.setObjectName("PSD")

        if module == "M2":
            numSensors = 6
            self.samples = [
                [i + axis for i in ["1", "2", "3", "4", "5", "6"]]
                for axis in ["X", "Y", "Z"]
            ]
        else:
            numSensors = 3
            self.samples = [
                [i + axis for i in ["1", "2", "3"]] for axis in ["X", "Y", "Z"]
            ]

        self.SENSORS = [
            f"acceleration{a}Sensor{s}"
            for s in range(1, numSensors + 1)
            for a in ["X", "Y", "Z"]
        ]

        self.cache = VMSCache(0, numSensors)

        self.psds = [PSDWidget(spls, self.cache) for spls in self.samples]
        for w in self.psds:
            toolbar.frequencyChanged.connect(w.frequencyChanged)

        self.tabs = QTabWidget()

        allPSDs = QWidget()
        gridLayout = QGridLayout()
        for r in range(3):
            gridLayout.addWidget(self.psds[r], r, 0)
        allPSDs.setLayout(gridLayout)
        self.tabs.addTab(allPSDs, "PSD")

        self.meanPSDs = [PSDWidget([a], self.cache) for a in ["X", "Y", "Z"]]
        for w in self.meanPSDs:
            toolbar.frequencyChanged.connect(w.frequencyChanged)

        allMeans = QWidget()
        gridLayout = QGridLayout()
        for r in range(3):
            gridLayout.addWidget(self.meanPSDs[r], r, 0)
        allMeans.setLayout(gridLayout)
        self.tabs.addTab(allMeans, "Mean PSD")

        toolbar.intervalChanged.connect(self.intervalChanged)

        toolbar.frequencyChanged.emit(*toolbar.getFrequencyRange())
        toolbar.intervalChanged.emit(toolbar.interval.value())

        toolbar.intervalChanged.connect(self.intervalChanged)

        toolbar.frequencyChanged.emit(*toolbar.getFrequencyRange())
        toolbar.intervalChanged.emit(toolbar.interval.value())

        comm.data.connect(self.data)

        self.setWidget(self.tabs)

    @Slot(map)
    def data(self, data):
        ts = data.timestamp
        added, chunk_removed = self.cache.newChunk(data, SAMPLE_TIME)
        if added:
            self.cacheUpdated.emit(
                len(self.cache), self.cache.startTime(), self.cache.endTime()
            )

            for i in range(len(self.psds)):
                self.psds[i].data()

            for i in range(len(self.meanPSDs)):
                self.meanPSDs[i].data(True)

    @Slot(float)
    def intervalChanged(self, interval):
        self.cache.resize(int(np.ceil(interval / SAMPLE_TIME)))
