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
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
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

        self.toolbar = QHBoxLayout()

        self.level = QComboBox()
        self.level.addItems(self.LEVELS)
        self.level.currentIndexChanged.connect(self.changeLevel)

        self.currentLevel = QLabel()

        self.toolbar.addWidget(QLabel("Level"))
        self.toolbar.addWidget(self.level)
        self.toolbar.addWidget(QLabel("Current"))
        self.toolbar.addWidget(self.currentLevel)
        self.toolbar.addStretch()

        self.salMessages = SALLogMessages(self.comm)

        self.layout.addLayout(self.toolbar)
        self.layout.addWidget(self.salMessages)

        self.comm.logLevel.connect(self.logLevel)

    def _levelToIndex(self, level):
        return min(int(level / 10), 5)

    def setPageActive(self, active):
        if self.pageActive == active:
            return

    @Slot()
    def logLevel(self, data):
        index = self._levelToIndex(data.level)
        self.currentLevel.setText(self.LEVELS[index])
        # when item wasn't selected
        if self.level.currentIndex() < 0:
            self.level.setCurrentIndex(index)

    @asyncSlot()
    async def changeLevel(self, index):
        await self.comm.MTM1M3.cmd_setLogLevel.set_start(level=index * 10)
