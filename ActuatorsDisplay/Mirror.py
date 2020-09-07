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

from .Actuator import Actuator

from PySide2.QtWidgets import QGraphicsScene
import numpy as np


class Mirror(QGraphicsScene):
    """Graphics scene containing plot of the mirror surface with actuators.

    Actuator list is cleared with clear() method (inherited from
    QGraphicsScene). Actuators are added with addActuator() method.
    Actuators data should be updated with updateActuator() call.
    """

    def __init__(self):
        super().__init__()

    def setRange(self, min, max):
        """Set display range. Display range is used for colors displayed by the actuator.

        Parameters
        ----------
        min : `float`
               Minimal data range.
        max : `float`
               Maximal data range.
        """
        for a in self.items():
            a.setRange(min, max)

    def addActuator(self, id, x, y, data, state):
        """Adds actuator to the list.

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
        self.addItem(Actuator(id, x, y, data, state))

    def getActuator(self, id):
        """Returns actuator with given ID.

        Parameters
        ----------
        id : `int`
            Actuator ID.

        Returns
        -------
        `Actuator`
            Actuator with matched ID.

        Raises
        ------
        KeyError
            When actuator with given ID is not found.
        """
        try:
            return next(filter(lambda a: a.id == id, self.items()))
        except StopIteration:
            raise KeyError(f"Cannot find actuator with ID {id}")

    def updateActuator(self, id, data, state):
        """Updates actuator value and state.

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
        self.getActuator(id).updateData(data, state)
