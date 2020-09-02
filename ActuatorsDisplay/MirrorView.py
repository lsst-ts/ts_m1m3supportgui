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

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QGraphicsView
from . import Mirror


class MirrorView(QGraphicsView):

    selectChanged = Signal(object)

    def __init__(self):
        self._mirror = Mirror()
        super().__init__(self._mirror)
        self._selected = None
        self._selectedPos = None

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, s):
        if self._selected is not None:
            self._selected.setSelected(False)
        self._selected = s
        if self._selected is not None:
            self._selected.setSelected(True)
        self.selectChanged.emit(self._selected)

    def setRange(self, min, max):
        self._mirror.setRange(min, max)

    def clear(self):
        self.selected = None
        self._mirror.clear()

    def scaleHints(self):
        s = min(self.width() / 8400, self.height() / 8400)
        return (s, s)

    def addActuator(self, id, x, y, data, warning):
        self._mirror.addActuator(id, x, y, data, warning)

    def mousePressEvent(self, event):
        self._selectedPos = event.pos()
        self.selected = self.itemAt(self._selectedPos)
