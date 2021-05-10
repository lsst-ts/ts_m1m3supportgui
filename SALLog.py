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

__all__ = ["LEVELS", "ToolBar", "Widget", "Dock", "Messages"]

from PySide2.QtCore import Signal, Slot
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton,
    QPlainTextEdit,
    QDockWidget,
)
from SALComm import SALCommand
from asyncqt import asyncSlot
from datetime import datetime

LEVELS = ["Trace", "Debug", "Info", "Warning", "Error", "Critical"]


def _levelToIndex(self, level):
    return min(int(level / 10), 5)


class ToolBar(QWidget):

    clear = Signal()
    changeLevel = Signal(int)
    setSize = Signal(int)

    def __init__(self, comms):
        super().__init__()
        toolbar = QHBoxLayout()

        clearButton = QPushButton("Clear")
        clearButton.clicked.connect(self.clear.emit)

        level = QComboBox()
        level.addItems(LEVELS)
        level.currentIndexChanged.connect(self.changeLevel.emit)

        maxBlock = QSpinBox()
        maxBlock.setMaximum(1000000)
        maxBlock.setSingleStep(10)
        maxBlock.valueChanged.connect(self.setSize.emit)
        maxBlock.setValue(1000)
        maxBlock.setMinimumWidth(100)

        toolbar.addWidget(clearButton)
        toolbar.addWidget(QLabel("Level"))
        toolbar.addWidget(level)
        toolbar.addWidget(QLabel("Current"))

        def addLevelLabel(comm):
            currentLevel = QLabel("---")
            toolbar.addWidget(currentLevel)
            comm.logLevel.connect(
                lambda data: currentLevel.setText(LEVELS[_levelToIndex(data.level)])
            )

        if type(comms) == list:
            for comm in comms:
                addLevelLabel(comm)
        else:
            addLevelLabel(comms)

        toolbar.addWidget(QLabel("Max lines"))
        toolbar.addWidget(maxBlock)
        toolbar.addStretch()

        self.setLayout(toolbar)


class Messages(QPlainTextEdit):
    """Displays log messages."""

    LEVELS_IDS = [
        "<font color='gray'>T</font></font>",
        "<font color='darkcyan'>D</font>",
        "<font color='green'>I</font>",
        "<font color='goldenrod'>W</font>",
        "<font color='red'>E</font>",
        "<font color='purple'>C</font>",
    ]

    LEVEL_TEXT_STYLE = [
        "color:gray; font-weight:normal;",
        "color:black; font-weight:normal;",
        "font-weight:bold;",
        "font-weight:bold;",
        "font-weight:bold;",
        "color:red; font-weight:bold;",
    ]

    def __init__(self, comms):
        super().__init__()
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setCenterOnScroll(True)
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.setFont(font)

        if type(comms) == list:
            for comm in comms:
                comm.logMessage.connect(self.logMessage)
        else:
            comms.logMessage.connect(self.logMessage)

    @Slot()
    def logMessage(self, data):
        date = datetime.fromtimestamp(data.private_sndStamp).isoformat(
            sep=" ", timespec="milliseconds"
        )
        level = min(int(data.level / 10), 5)
        self.appendHtml(
            f"{date} [<b>{self.LEVELS_IDS[level]}</b>] <span style='{self.LEVEL_TEXT_STYLE[level]}'>{data.message}</span>"
        )
        self.ensureCursorVisible()

class Widget(QWidget):
    """Display SAL logs."""

    def __init__(self, comms):
        super().__init__()

        self.comms = comms
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.salMessages = Messages(self.comms)

        toolbar = ToolBar(comms)
        toolbar.clear.connect(messages.clearM)
        toolbar.changeLevel.connect(self.changeLevel)
        toolbar.setSize.connect(self.setMessageSize)

        self.layout.addWidget(toolbar)
        self.layout.addWidget(self.salMessages)

    @Slot()
    def setMessageSize(self, i):
        self.salMessages.setMaximumBlockCount(i)

    @SALCommand
    def _changeIt(self, **kwargs):
        return self.comms.remote.cmd_setLogLevel

    @asyncSlot()
    async def changeLevel(self, index):
        await self._changeIt(level=index * 10)


class Dock(QDockWidget):
    """Dock with SAL messages.

    Parameters
    ----------
    comms : `[SALComm]` or `SALComm`
    """

    def __init__(self, comms):
        super().__init__("SAL Log")

        self.messages = Messages(comms)

        toolbar = ToolBar(comms)
        toolbar.clear.connect(self.messages.clear)
        toolbar.changeLevel.connect(self.changeLevel)
        toolbar.setSize.connect(self.setMessageSize)

        self.setTitleBarWidget(toolbar)
        self.setWidget(self.messages)

    @Slot()
    def setMessageSize(self, i):
        self.messages.setMaximumBlockCount(i)

    @SALCommand
    def _changeIt(self, **kwargs):
        return self.comms.remote.cmd_setLogLevel

    @asyncSlot()
    async def changeLevel(self, index):
        await self._changeIt(level=index * 10)
