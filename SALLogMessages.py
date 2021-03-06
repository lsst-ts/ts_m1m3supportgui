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

from PySide2.QtCore import Slot, QPoint
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QPlainTextEdit

from datetime import datetime


class SALLogMessages(QPlainTextEdit):
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

    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.setReadOnly(True)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.setFont(font)

        self.comm.logMessage.connect(self.logMessage)

    @Slot()
    def logMessage(self, data):
        date = datetime.fromtimestamp(data.private_sndStamp).isoformat(
            sep=" ", timespec="milliseconds"
        )
        level = min(int(data.level / 10), 5)
        self.appendHtml(
            f"{date} [<b>{self.LEVELS_IDS[level]}</b>] <span style='{self.LEVEL_TEXT_STYLE[level]}'>{data.message}</span>"
        )
