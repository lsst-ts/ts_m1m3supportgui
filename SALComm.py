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

__all__ = ["create"]


def _filterEvtTel(m):
    return m.startswith("tel_") or m.startswith("evt_")


class MetaSAL(type(QObject)):
    """Metaclass for Qt<->SAL/DDS glue class. Creates Qt Signal objects for all
    read topics. Names of remotes to use are read from class _remotes hash. The
    _remotes hash key is remote name, value is array of included topics or None
    for including all found topics.
    """

    def __new__(mcs, classname, bases, dictionary):
        dictionary["domain"] = Domain()

        def create_signals(remote):
            for m in filter(
                lambda m: m.startswith("tel_") or m.startswith("evt_"), dir(remote)
            ):
                dictionary[m[4:]] = Signal(map)

        for remote, includes in dictionary["_remotes"].items():
            dictionary[remote] = Remote(dictionary["domain"], remote, include=includes)
            create_signals(dictionary[remote])

        def connect_callbacks(self):
            def set_callbacks(remote):
                for m in filter(_filterEvtTel, dir(remote)):
                    getattr(remote, m).callback = getattr(self, m[4:]).emit

            for remote in self._remotes.keys():
                set_callbacks(getattr(self, remote))

        async def start(self):
            for remote in self._remotes.keys():
                await getattr(self, remote).start_task

        def reemit_all(self):
            for remote in self._remotes.keys():
                self.reemit_remote(remote)

        def reemit_remote(self, remote):
            for m in filter(_filterEvtTel, dir(getattr(self, remote))):
                data = getattr(getattr(self, remote), m).get()
                if data is not None:
                    getattr(self, m[4:]).emit(data)

        async def close(self):
            for remote in list(self._remotes.keys())[::-1]:
                await getattr(self, remote).close()

            await self.domain.close()

        newclass = super(MetaSAL, mcs).__new__(mcs, classname, bases, dictionary)

        setattr(newclass, connect_callbacks.__name__, connect_callbacks)
        setattr(newclass, start.__name__, start)
        setattr(newclass, reemit_all.__name__, reemit_all)
        setattr(newclass, reemit_remote.__name__, reemit_remote)
        setattr(newclass, close.__name__, close)
        return newclass


def create(remotes):
    """Creates SALComm instance for given remote(s). The returned object
    contains PySide2.QtCore.Signal class variables. Those signals are emitted
    when SAL callback occurs, effectively linking SAL/DDS and Qt word. Signals
    can be connected to multiple Qt slots to process the incoming data.

    Class variable with the same name as SAL remote name are instances of
    lsst.ts.salobj.Remote. Those can be used to start commands (available with
    `cmd_` prefix).

    Parameters
    ----------
    remotes : `hash`
       Keys are names of the SAL remotes to be connected. Values are either
       None to connect all read topics, or an array of strings containing
       name(s) of topics to include.

    Usage
    -----

    .. code-block:: python
       import SALComm

       my_sal = SALComm.create("MTMount": None, "M2Hexapod": "Position")
       loop.run_until_complete(my_sal.start())

       @Slot(map)
       def update_labels_position(data):
           ...

       my_sal.Position.connect(update_labels_position)

       await my_sal.MTMount.cmd_start.set_start(settingsToApply="Default")
    """

    class SALComm(QObject, metaclass=MetaSAL):
        """
        SAL proxy. Set callback to emit Qt signals.
        """

        _remotes = remotes

        def __init__(self):
            super().__init__()

            self.connect_callbacks()

    return SALComm()
