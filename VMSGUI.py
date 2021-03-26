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

# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

__all__ = ["ToolBar", "CacheStatusWidget"]

from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QWidget, QLabel, QToolBar, QStyle, QDoubleSpinBox

from datetime import datetime

import AccelerometersPageWidget


class ToolBar(QToolBar):

    frequencyChanged = Signal(float, float)
    intervalChanged = Signal(float)

    def __init__(self):
        super().__init__()

        self.setObjectName("VMSToolBar")

        self.addAction(self.style().standardIcon(QStyle.SP_MediaStop), "Stop")

        self.addWidget(QLabel("Frequency"))

        self.minFreq = QDoubleSpinBox()
        self.minFreq.setDecimals(1)
        self.minFreq.setRange(0, 10000)
        self.minFreq.setSingleStep(5)
        self.minFreq.setValue(0)
        self.minFreq.editingFinished.connect(self.minMaxChanged)
        self.addWidget(self.minFreq)

        self.addWidget(QLabel("-"))

        self.maxFreq = QDoubleSpinBox()
        self.maxFreq.setDecimals(1)
        self.maxFreq.setRange(0.1, 10000)
        self.maxFreq.setSingleStep(5)
        self.maxFreq.setValue(200)
        self.maxFreq.editingFinished.connect(self.minMaxChanged)
        self.addWidget(self.maxFreq)

        self.addWidget(QLabel("Interval:"))

        self.interval = QDoubleSpinBox()
        self.interval.setDecimals(3)
        self.interval.setRange(0.001, 3600)
        self.interval.setSingleStep(0.1)
        self.interval.setValue(50)
        self.interval.editingFinished.connect(self.newInterval)
        self.addWidget(self.interval)

        self.frequencyChanged.emit(self.minFreq.value(), self.maxFreq.value())

    @Slot()
    def minMaxChanged(self):
        self.frequencyChanged.emit(*self.getFrequencyRange())

    @Slot()
    def newInterval(self):
        self.intervalChanged.emit(self.interval.value())

    def getFrequencyRange(self):
        return (self.minFreq.value(), self.maxFreq.value())


class CacheStatusWidget(QLabel):
    def __init__(self):
        super().__init__("Size: 0 --- - ---")

    @Slot(int, float, float)
    def cacheUpdated(self, length, start, end):
        self.setText(
            f"Size: {length} {datetime.fromtimestamp(start).strftime('%H:%M:%S.%f')} - {datetime.fromtimestamp(end).strftime('%H:%M:%S.%f')} {end-start+AccelerometersPageWidget.SAMPLE_TIME:.03f}s"
        )
