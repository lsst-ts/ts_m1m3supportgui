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

from SALLogWidget import SALLogWidget
import TimeChart
import TimeBoxChart
from VMSCache import *
from VMSGUI import ToolBar
from TimeChart import TimeChartView
from PySide2.QtCore import Qt, Slot, Signal, QPointF
from PySide2.QtWidgets import QWidget, QTabWidget, QGridLayout, QLabel
from PySide2.QtCharts import QtCharts
from asyncqt import asyncSlot

import asyncio
import concurrent.futures
from datetime import datetime
import numpy as np
import time

SAMPLE_TIME = 0.001
"""Sample time (seconds)"""


class TimeChartWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.chart = []

        for sensor in range(6):
            self.chart.append(TimeBoxChart.TimeBoxChart())
            self.layout.addWidget(
                TimeChart.TimeChartView(self.chart[sensor]), sensor / 2, sensor % 2
            )

        comm.m1m3.connect(self.m1m3)

    @Slot(map)
    def m1m3(self, data):
        for sensor in range(1, 7):
            self.chart[sensor - 1].append(
                data.timestamp,
                [
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}X",
                        getattr(data, f"sensor{sensor}XAcceleration"),
                    ),
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}Y",
                        getattr(data, f"sensor{sensor}YAcceleration"),
                    ),
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}Z",
                        getattr(data, f"sensor{sensor}ZAcceleration"),
                    ),
                ],
            )


class PSDWidget(QWidget):
    def __init__(self, samples):
        super().__init__()

        self.samples = samples

        layout = QGridLayout()
        self.setLayout(layout)

        self.chart = QtCharts.QChart()

        self.psdSeries = []
        self.updateTask = asyncio.Future()
        self.updateTask.set_result(None)

        self.update_after = 0

        for s in samples:
            serie = QtCharts.QLineSeries()
            serie.setName(s)
            self.psdSeries.append(serie)
            self.chart.addSeries(serie)

        self.chart.createDefaultAxes()

        self.chart.legend().setAlignment(Qt.AlignLeft)

        layout.addWidget(TimeChartView(self.chart), 0, 0)

    def data(self, cache, mean=False):
        def plot(serie, signal):
            """
            signal - data
            """
            data = np.abs(np.fft.fft(signal)) ** 2
            if len(data) > 4000:
                s = int(len(data) / 2000)
                data = [np.average(data[i : i + s]) for i in range(0, len(data), s)]

            self.chart.axes(Qt.Vertical)[0].setRange(min(data), max(data))

            dl = len(data)
            points = [QPointF((r / SAMPLE_TIME) / (dl - 1), data[r]) for r in range(dl)]
            self.psdSeries[serie].replace(points)

        def plotAll(cache, mean):
            if mean:
                plot(
                    0,
                    np.mean(
                        [cache[s + self.samples[0]] for s in ["1", "2", "3"]], axis=0
                    ),
                )
                return

            for i in range(len(self.samples)):
                plot(i, cache[self.samples[i]])

        if not (self.update_after is None):
            if self.update_after < time.monotonic():
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    self.updateTask = pool.submit(plotAll, cache, mean)
                self.update_after = None
        elif self.updateTask.done():
            self.updateTask.result()
            self.update_after = time.monotonic() + 1

    @Slot(float, float)
    def frequencyChanged(self, low, high):
        self.chart.axes(Qt.Horizontal)[0].setRange(low, high)


class AccelerometersPageWidget(QTabWidget):
    SENSORS = [
        f"sensor{s}{a}Acceleration" for s in range(1, 7) for a in ["X", "Y", "Z"]
    ]

    cacheUpdated = Signal(int, float, float)

    def __init__(self, comm, toolbar):
        super().__init__()

        self.timeChart = TimeChartWidget(comm)
        self.samples = [[i + axis for i in ["1", "2", "3"]] for axis in ["X", "Y", "Z"]]
        self.psds = [PSDWidget(spls) for spls in self.samples]
        for w in self.psds:
            toolbar.frequencyChanged.connect(w.frequencyChanged)

        self.addTab(self.timeChart, "Box plots")

        allPSDs = QWidget()
        gridLayout = QGridLayout()
        for r in range(3):
            gridLayout.addWidget(self.psds[r], r, 0)
        allPSDs.setLayout(gridLayout)
        self.addTab(allPSDs, "PSD")

        self.meanPSDs = [PSDWidget([a]) for a in ["X", "Y", "Z"]]
        for w in self.meanPSDs:
            toolbar.frequencyChanged.connect(w.frequencyChanged)

        allMeans = QWidget()
        gridLayout = QGridLayout()
        for r in range(3):
            gridLayout.addWidget(self.meanPSDs[r], r, 0)
        allMeans.setLayout(gridLayout)
        self.addTab(allMeans, "Mean PSD")

        log = SALLogWidget(comm)
        self.addTab(log, "SAL Log")

        self.cache = VMSCache()

        comm.m1m3.connect(self.m1m3)

    @Slot(map)
    def m1m3(self, data):
        ts = data.timestamp
        for i in range(len(getattr(data, self.SENSORS[0]))):
            row = (ts,)
            ts += SAMPLE_TIME
            row += tuple([getattr(data, s)[i] for s in self.SENSORS])
            self.cache.append(row)

        self.cacheUpdated.emit(
            len(self.cache), self.cache.startTime(), self.cache.endTime()
        )

        for i in range(len(self.psds)):
            self.psds[i].data(self.cache)

        for i in range(len(self.meanPSDs)):
            self.meanPSDs[i].data(self.cache, True)
