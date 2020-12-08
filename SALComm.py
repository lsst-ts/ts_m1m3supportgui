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

# Generated from MTM1M3_Events, MTM1M3_Telemetry and MTMount_Telemetry
import abc
from PySide2.QtCore import QObject, Signal
from lsst.ts.salobj import Domain, Remote


class MetaSAL(type(QObject)):
    def __new__(mcs, classname, bases, dictionary):

        dictionary["domain"] = Domain()

        def createSignals(remote):
            for m in filter(
                lambda m: m.startswith("tel_") or m.startswith("evt_"), dir(remote)
            ):
                dictionary[m[4:]] = Signal(map)

        for remote, includes in dictionary["remotes"].items():
            dictionary[remote] = Remote(dictionary["domain"], remote, include=includes)
            createSignals(dictionary[remote])

        return super(MetaSAL, mcs).__new__(mcs, classname, bases, dictionary)


class SALComm(QObject, metaclass=MetaSAL):
    """
    SAL proxy. Set callback to emit Qt signals.
    """

    remotes = {"MTM1M3": None, "MTMount": ["Azimuth", "Elevation"]}

    def __init__(self):
        super().__init__()

        def setCallbacks(remote):
            for m in filter(
                lambda m: m.startswith("tel_") or m.startswith("evt_"), dir(remote)
            ):
                getattr(remote, m).callback = getattr(self, m[4:]).emit

        for remote in self.remotes.keys():
            setCallbacks(getattr(self, remote))

    async def start(self):
        for remote in self.remotes.keys():
            await getattr(self, remote).start_task

    async def close(self):
        for remote in list(self.remotes.keys())[::-1]:
            await getattr(self, remote).close()

        await self.domain.close()
