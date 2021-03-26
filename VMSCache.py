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

import numpy as np


class VMSCache:
    """Cache for large float data. Holds rolling time window of records. Act as
    dictionary, where keys are accelerometer number and axis (1X,1Y,1Z,..,6Z)"""

    def __init__(self, size=50000, sensors=6):
        items = [("timestamp", "f8")] + [
            (f"{s}{a}", "f8") for s in range(1, sensors + 1) for a in ["X", "Y", "Z"]
        ]
        self._size = size
        self.data = np.zeros((self._size), items)
        self.clear()

    def clear(self):
        self.current_index = 0
        self.filled = False

    def resize(self, size):
        newdata = np.zeros(size, self.data.dtype)
        rows = self.rows()
        r = 0
        for s in self.rows():
            newdata[r] = s
            r += 1
            if r >= size:
                break
        self.current_index = r
        self.filled = r >= size

        self.data = newdata
        self._size = size

    def append(self, A):
        if self.current_index >= self._size:
            self.current_index = 0
            self.filled = True
        self.data[self.current_index] = A
        self.current_index += 1

    def startTime(self):
        if self.filled is False:
            if self.current_index > 0:
                return self.data[0]["timestamp"]
            return None

        if self.current_index >= self._size:
            return self.data[0]["timestamp"]
        return self.data[self.current_index]["timestamp"]

    def endTime(self):
        if self.current_index == 0:
            if self.filled is False:
                return None
            return self.data[-1]["timestamp"]
        return self.data[self.current_index - 1]["timestamp"]

    def rows(self):
        if self.filled:
            for r in range(self.current_index + 1, self._size):
                yield self.data[r]
        for r in range(0, self.current_index):
            yield self.data[r]

    def __getitem__(self, key):
        if self.filled:
            return list(self.data[self.current_index + 1 :][key]) + list(
                self.data[: self.current_index][key]
            )
        else:
            return list(self.data[: self.current_index][key])

    def __len__(self):
        return self._size if self.filled else self.current_index
