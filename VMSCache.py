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

__all__ = ["VMSCache"]

from TimeCache import *

import astropy.units as u
import numpy as np


class VMSCache(TimeCache):
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
        self._sensors = sensors
        items = [("timestamp", "f8")] + [
            (f"{s} {a}", "f8")
            for s in range(1, self._sensors + 1)
            for a in ["X", "Y", "Z"]
        ]

        super().__init__(size, items, window)

    def clear(self):
        """Clear cache."""
        super().clear()
        self._receiving = []

    def sensors(self):
        """Returns number of sensors stored in cache."""
        return self._sensors

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
