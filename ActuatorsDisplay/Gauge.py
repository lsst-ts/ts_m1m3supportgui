# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPen, QPainter, QColor
from PySide2.QtWidgets import QWidget


class Gauge(QWidget):
    """Draws guage with color scale.
    """

    def __init__(self):
        super().__init__()
        self._range = (0, 100)
        self.setMinimumSize(100, 100)
        self.setMaximumWidth(200)

    def setRange(self, min, max):
        self._range = (min, max)
        self.update()

    def sizeHint(self):
        return QSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        swidth = max(self.width() - 100, 20)
        for x in range(0, self.height()):
            painter.setPen(QColor.fromHsvF(x / self.height() * 179 / 255, 1, 1))
            painter.drawLine(0, x, swidth, x)

        painter.setPen(Qt.black)
        painter.drawText(
            0,
            0,
            self.width() - swidth,
            30,
            Qt.AlignCenter,
            "{0:.2f}".format(self._range[0]),
        )
        painter.drawText(
            0,
            self.height() - 30,
            self.width() - swidth,
            30,
            Qt.AlignCenter,
            "{0:.2f}".format(self._range[1]),
        )
