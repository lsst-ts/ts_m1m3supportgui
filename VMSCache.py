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
    dictionary, where keys are accelerometer number and axis
    (1X,1Y,1Z,..,<sensors>Z). [] and len operators are supported.

    Parameters
    ----------
    size : `int`
        Cache size.
    sensors : `int`
        Number of sensors.
    window : `int`, optional
        Receiving window size. Defaults to 3.
    """

    def __init__(self, size, sensors, window=3):
        self._size = size
        self._window = window
        self._sensors = sensors
        items = [("timestamp", "f8")] + [
            (f"{s} {a}", "f8")
            for s in range(1, self._sensors + 1)
            for a in ["X", "Y", "Z"]
        ]
        self.data = np.zeros((self._size), items, order="F")
        self.clear()

    def clear(self):
        """Clear cache."""
        self.current_index = 0
        self.filled = False
        self._receiving = []

    def resize(self, size):
        """Change cache size. Data are preserved - either all rows are used
        when expanding, or the most recent ones are stored when shrinking.

        Parameters
        ----------
        size : `int`
            New size.
        """
        clength = len(self)
        if size == clength:
            return
        newdata = np.zeros(size, self.data.dtype)
        n_current = r = min(clength, size)
        for s in self.rows_reverse():
            r -= 1
            newdata[r] = s
            if r == 0:
                break
        self.filled = (n_current == size) and (clength > 0)
        self.current_index = n_current

        self.data = newdata
        self._size = size

    def append(self, data):
        """Append new row to end of data.

        Parameters
        ----------
        data : `tupple`
            New row data.
        """
        if self.current_index >= self._size:
            self.current_index = 0
            self.filled = True
        self.data[self.current_index] = data
        self.current_index += 1

    def newChunk(self, data, sample_period):
        """Add new data chunk. Append data to cache if all sensors are
        received. Keeps window cache, removes old entries if over window.

        Parameters
        ----------
        data : `MTVMS_Telemetry_data`
            Data arriving from SAL.
        sample_period : `float`
            Sample period in seconds.

        Returns
        -------
        added : `bool`
            True if new data were added to data array (e.g. all data were
            received with this chunk).
        chunk_removed : `bool`
            True if chunk was removed (indicating network problem, as sensor(s)
            chunks were missing for too long)."""
        added = False
        found = False
        for r in self._receiving:
            if r[0] == data.timestamp:
                r[1][data.sensor - 1] = data
                found = True
                break
        if found is False:
            self._receiving.append((data.timestamp, [None] * self._sensors))
            self._receiving[-1][1][data.sensor - 1] = data
            self._receiving.sort(key=lambda x: x[0])

        # all data for given timestamp received
        while len(self._receiving) > 0:
            r = self._receiving[0]
            if r[1].count(None) > 0:
                break
            dl = len(data.accelerationX)
            timestamps = np.arange(r[0], r[0] + sample_period * dl, sample_period)

            def copy_data(start, l):
                self.data["timestamp"][
                    self.current_index : self.current_index + l
                ] = timestamps[start : start + l]
                for s in range(1, self._sensors + 1):
                    self.data[f"{s} X"][
                        self.current_index : self.current_index + l
                    ] = r[1][s - 1].accelerationX[start : start + l]
                    self.data[f"{s} Y"][
                        self.current_index : self.current_index + l
                    ] = r[1][s - 1].accelerationY[start : start + l]
                    self.data[f"{s} Z"][
                        self.current_index : self.current_index + l
                    ] = r[1][s - 1].accelerationZ[start : start + l]

            l = min(dl, self._size - self.current_index)
            if l > 0:
                copy_data(0, l)
                self.current_index += l
                dl -= l

            if dl > 0:
                self.current_index = 0
                self.filled = True
                copy_data(l, dl)
                self.current_index = dl

            self._receiving.remove(r)
            added = True

        chunk_removed = False
        if len(self._receiving) > self._window:
            self._receiving = self._receiving[1:]
            chunk_removed = True
        return (added, chunk_removed)

    def startTime(self):
        """Return timestamp of the last data point.

        Returns
        -------
        endTime : `float`
            None if cache is empty. Otherwise timestamp of the first data point."""
        if self.filled is False:
            if self.current_index > 0:
                return self.data[0]["timestamp"]
            return None

        if self.current_index >= self._size:
            return self.data[0]["timestamp"]
        return self.data[self.current_index]["timestamp"]

    def endTime(self):
        """Return timestamp of the last data point.

        Returns
        -------
        endTime : `float`
            None if cache is empty. Otherwise timestamp of the last data point."""
        if self.current_index == 0:
            if self.filled is False:
                return None
            return self.data[-1]["timestamp"]
        return self.data[self.current_index - 1]["timestamp"]

    def rows_reverse(self):
        """Yelds reversed row iterator."""
        for r in range(self.current_index - 1, -1, -1):
            yield self.data[r]
        if self.filled:
            for r in range(self._size - 1, self.current_index - 1, -1):
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
