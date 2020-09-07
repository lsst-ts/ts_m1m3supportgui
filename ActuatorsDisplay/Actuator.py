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

from PySide2.QtCore import QRect, Qt, QPointF
from PySide2.QtGui import QPen, QPainter, QColor, QBrush, QTransform
from PySide2.QtWidgets import QGraphicsItem


class Actuator(QGraphicsItem):
    """Combines graphical display of an actuator with its data. Record if an
    actuator is selected by a mouse click.

    Actuator can be selected - then it is drawn with highlighting, showing it
    is the selected actuator. 

    Parameters
    ----------

    id : `int`
         Actuator identification number. Starting with 101, the first number
         identified segment (1-4). The value ranges up to 443.
    x : `float`
         Actuator X coordinate (in mm).
    y : `float`
         Actuator Y coordinate (in mm).
    data : `float`
         Data associated with the actuator (actual force, calculated force, ..).
    state : `int`
         Actuator state. 0 for inactive/unused, 1 for active OK, 2 for active
         warning.
    """

    STATE_INACTIVE = 0
    STATE_ACTIVE = 1
    STATE_WARNING = 2

    def __init__(self, id, x, y, data, state):
        super().__init__()
        self.id = id
        # actuator position
        self._center = QPointF(x, y)
        # actuator data
        self._data = data
        self._selected = False
        self._state = state
        # minimum and maximum values. Used for translating value into color code
        self._min = None
        self._max = None
        # scalign factor. The actuator default size is 20x20 units. As
        # actuators are placed on mirror, the size needs to be adjusted to show
        # properly actuator on display in e.g. mm (where X and Y ranges are
        # ~-4400 .. +4400).
        self._scale = 25

    def updateData(self, data, state):
        """Updates actuator data.

        If new data differs from the current data, calls update() to force actuator redraw.

        Parameters
        ----------
        data : `float`
             New data associated with the actuator (actual force, calculated force, ..).
        state : `state`
             New actuator state value.
        """
        if self._data != data or self._state != state:
            self._data = data
            self._state = state
            self.update()

    def setSelected(self, selected):
        """Set actuator selection status."""
        self._selected = selected
        self.update()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        self.update()

    @property
    def warning(self):
        return self._state == self.STATE_WARNING

    def setRange(self, min, max):
        self._min = min
        self._max = max
        self.update()

    def boundingRect(self):
        return QRect(
            self._center.x() - 10 * self._scale,
            self._center.y() - 10 * self._scale,
            20 * self._scale,
            20 * self._scale,
        )

    def paint(self, painter, option, widget):
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        if self._state == self.STATE_INACTIVE:
            painter.setPen(QPen(Qt.gray, 2 * self._scale, Qt.DotLine))
            painter.drawEllipse(self._center, 10 * self._scale, 10 * self._scale)
            return
        if self._selected:
            painter.setPen(QPen(Qt.black, 2 * self._scale))
            painter.drawRect(self.boundingRect())
        else:
            painter.setPen(QPen(Qt.red, 2 * self._scale))

        if self._state == self.STATE_WARNING:
            painter.setBrush(Qt.red)
        elif self._min is None or self._max is None:
            painter.setBrush(Qt.yellow)
        elif self._min == self._max:
            brush = QBrush(Qt.red, Qt.DiagCrossPattern)
            brush.setTransform(QTransform().scale(self._scale / 3, self._scale / 3))
            painter.setBrush(brush)
        else:
            painter.setBrush(
                QColor.fromHsvF(
                    ((self._data - self._min) / (self._max - self._min)) * 179 / 255,
                    1,
                    1,
                )
            )
        painter.drawEllipse(self._center, 10 * self._scale, 10 * self._scale)
        font = painter.font()
        font.setPixelSize(8 * self._scale)
        painter.setPen(Qt.black)
        painter.setFont(font)
        painter.drawText(
            self._center.x() - 10 * self._scale,
            self._center.y() - 10 * self._scale,
            20 * self._scale,
            20 * self._scale,
            Qt.AlignCenter,
            str(self.id),
        )
