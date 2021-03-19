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
from TimeChart import TimeChartView
from PySide2.QtCore import Qt, Slot, QPointF
from PySide2.QtWidgets import QWidget, QTabWidget, QGridLayout, QLabel
from PySide2.QtCharts import QtCharts
from asyncqt import asyncSlot

import asyncio
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
    def __init__(self, samples=["1X", "2X", "3X"]):
        super().__init__()

        self.samples = samples

        layout = QGridLayout()
        self.setLayout(layout)

        self.chart = QtCharts.QChart()

        self.psdSeries = []
        self.updateTasks = []

        for s in samples:
            serie = QtCharts.QLineSeries()
            serie.setName(s)
            self.psdSeries.append(serie)
            self.chart.addSeries(serie)

            task = asyncio.Future()
            task.set_result(None)
            self.updateTasks.append(task)

        self.chart.createDefaultAxes()

        layout.addWidget(TimeChartView(self.chart), 0, 0)

    def plot(self, cache):
        async def plot(serie, signal, cut=500):
            """
            signal - data
            cut - frequency cut
            """
            # sample time
            st = len(signal) * SAMPLE_TIME
            data = np.abs(np.fft.fft(signal))

            dl = len(data)

            self.psdSeries[serie].replace(
                [QPointF((r / SAMPLE_TIME) / (dl - 1), data[r]) for r in range(dl)]
            )
            self.chart.axes(Qt.Horizontal)[0].setRange(0, cut)
            self.chart.axes(Qt.Vertical)[0].setRange(min(data), max(data))

        for i in range(len(self.updateTasks)):
            if self.updateTasks[i].done():
                self.updateTasks[i] = asyncio.create_task(
                    plot(i, cache[self.samples[i]])
                )


class AccelerometersPageWidget(QTabWidget):
    SENSORS = [
        f"sensor{s}{a}Acceleration" for s in range(1, 7) for a in ["X", "Y", "Z"]
    ]

    def __init__(self, comm):
        super().__init__()

        self.timeChart = TimeChartWidget(comm)
        self.psd = PSDWidget()

        self.addTab(self.timeChart, "Box plots")
        self.addTab(self.psd, "PSD")

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

        self.psd.plot(self.cache)
