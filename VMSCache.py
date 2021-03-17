# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top - level directory of this distribution
# for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import Slot
import numpy as np


class VMSCache:
    """Cache for large float data. Holds rolling time window of records."""

    def __init__(self, size=50000, sensors=6):
        items = []
        for s in range(1, sensors + 1):
            for a in ["X", "Y", "Z"]:
                items.append((str(s) + a, "f8"))
        self.size = size
        self.data = np.zeros((self.size), [("timestamp", "f8")] + items)
        self.current_index = 0
        self.filled = False

    def append(self, A):
        if self.current_index >= self.size:
            self.current_index = 0
            self.filled = True
        self.data[self.current_index] = A
        self.current_index += 1

    def column(self, column):
        if self.filled:
            return list(self.data[self.current_index + 1 :][column]) + list(
                self.data[: self.current_index][column]
            )
        else:
            return list(self.data[: self.current_index][column])
