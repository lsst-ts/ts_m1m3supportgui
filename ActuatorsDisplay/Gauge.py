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
from PySide2.QtGui import QPen, QPainter, QColor, QBrush
from PySide2.QtWidgets import QWidget


class Gauge(QWidget):
    """Draws guage with color scale.
    """

    def __init__(self):
        super().__init__()
        self._min = None
        self._max = None
        self.setMinimumSize(100, 100)
        self.setMaximumWidth(200)

    def setRange(self, min, max):
        """Set value range. Color is mapped between min and max values, using change in hue.

        Parameters
        ----------
        min : `float`
               Minimal data range.
        max : `float`
               Maximal data range.
        """
        self._min = min
        self._max = max
        self.update()

    def sizeHint(self):
        """Overloaded method.
        """
        return QSize(100, 100)

    def paintEvent(self, event):
        """Overloaded method. Paint gauge as serie of lines, and adds text labels.
        """
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        swidth = max(self.width() - 100, 20)
        if self._min == self._max:
            painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
            painter.drawRect(0, 0, swidth, self.height())
            painter.setPen(Qt.black)
            painter.drawText(
                0,
                0,
                self.width() - swidth,
                self.height(),
                Qt.AlignCenter,
                "{0:.2f}".format(self._min),
            )
            return

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
            "{0:.2f}".format(self._min),
        )
        painter.drawText(
            0,
            self.height() - 30,
            self.width() - swidth,
            30,
            Qt.AlignCenter,
            "{0:.2f}".format(self._max),
        )
