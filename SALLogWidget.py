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

from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton,
)
from SALLogMessages import SALLogMessages
from asyncqt import asyncSlot


class SALLogWidget(QWidget):
    """Display SAL logs."""

    LEVELS = ["Trace", "Debug", "Info", "Warning", "Error", "Critical"]

    def __init__(self, comm):
        super().__init__()

        self.pageActive = False

        self.comm = comm
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.salMessages = SALLogMessages(self.comm)

        self.toolbar = QHBoxLayout()

        self.clearButton = QPushButton("Clear")
        self.clearButton.clicked.connect(self.salMessages.clear)

        self.level = QComboBox()
        self.level.addItems(self.LEVELS)
        self.level.currentIndexChanged.connect(self.changeLevel)

        self.currentLevel = QLabel()

        self.maxBlock = QSpinBox()
        self.maxBlock.setSingleStep(10)
        self.maxBlock.valueChanged.connect(self.setMaxBlock)
        self.maxBlock.setValue(100)
        self.maxBlock.setMinimumWidth(100)
        self.maxBlock.setMaximum(1000000)

        self.toolbar.addWidget(self.clearButton)
        self.toolbar.addWidget(QLabel("Level"))
        self.toolbar.addWidget(self.level)
        self.toolbar.addWidget(QLabel("Current"))
        self.toolbar.addWidget(self.currentLevel)
        self.toolbar.addWidget(QLabel("Max lines"))
        self.toolbar.addWidget(self.maxBlock)
        self.toolbar.addStretch()

        self.layout.addLayout(self.toolbar)
        self.layout.addWidget(self.salMessages)

        self.comm.logLevel.connect(self.logLevel)

    def _levelToIndex(self, level):
        return min(int(level / 10), 5)

    def setPageActive(self, active):
        if self.pageActive == active:
            return
        self.pageActive = active

        if self.pageActive:
            data = self.comm.MTM1M3.evt_logLevel.get()
            if data is not None:
                self.logLevel(data)
                self.level.setCurrentIndex(self._levelToIndex(data.level))

    @Slot()
    def setMaxBlock(self, i):
        self.salMessages.setMaximumBlockCount(i)

    @Slot()
    def logLevel(self, data):
        self.currentLevel.setText(self.LEVELS[self._levelToIndex(data.level)])

    @asyncSlot()
    async def changeLevel(self, index):
        await self.comm.MTM1M3.cmd_setLogLevel.set_start(level=index * 10)
