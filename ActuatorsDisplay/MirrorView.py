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
    """View on mirror populated by actuators.
    """

    selectionChanged = Signal(object)
    """Signal raised when another actuator is selected by a mouse click.

    Parameters
    ----------
    object
        Selected actuator.
    """

    def __init__(self):
        self._mirror = Mirror()
        super().__init__(self._mirror)
        self._selectedId = None

    @property
    def selected(self):
        """Selected actuator or None if no actuator selected (Actuator).
        """
        try:
            return self._mirror.getActuator(self._selectedId)
        except KeyError:
            return None

    @selected.setter
    def selected(self, s):
        if self.selected is not None:
            self.selected.setSelected(False)
        if s is None:
            self._selectedId = None
            return None
        self._selectedId = s.id
        s.setSelected(True)
        self.selectionChanged.emit(s)

    def setRange(self, min, max):
        """Sets range used for color scaling.

        Parameters
        ----------
        min : `float`
           Minimal value.
        max : `float`
           Maximal value.
        """
        self._mirror.setRange(min, max)

    def clear(self):
        """Removes all actuators from the view.
        """
        self._mirror.clear()

    def scaleHints(self):
        """Returns preferred scaling. Overloaded method.
        """
        s = min(self.width() / 8600, self.height() / 8600)
        return (s, s)

    def addActuator(self, id, x, y, data, state):
        """Adds actuator.

        Parameters
        ----------
        id : `int`
            Actuator ID. Actuators are matched by ID.
        x : `float`
            Actuator X position (in mm).
        y :  `float`
            Actuator y position (in mm).
        data : `float`
            Actuator value.
        state : `int`
            Actuator state. Actuator.STATE_INVALID, Actuator.STATE_VALID or
            Actuator.STATE_WARNING.
        """
        self._mirror.addActuator(id, x, y, data, state, id == self._selectedId)

    def updateActuator(self, id, data, state):
        """Update actuator value and state.

        Parameters
        ----------
        id : `int`
            Actuator ID number.
        data : `float`
            Update actuator value.
        state : `int`
            Updated actuator state. Actuator.STATE_INVALID, Actuator.STATE_VALID, Actuator.STATE_WARNING.

        Raises
        ------
        KeyError
            If actuator with the given ID cannot be found.
        """
        self._mirror.updateActuator(id, data, state)
        if self._selectedId == id:
            self.selectionChanged.emit(self.selected)

    def mousePressEvent(self, event):
        self.selected = self.itemAt(event.pos())
