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
import functools

__all__ = ["create"]


def _filterEvtTel(m):
    return m.startswith("tel_") or m.startswith("evt_")


class MetaSAL(type(QObject)):
    """Metaclass for Qt<->SAL/DDS glue class. Creates Qt Signal objects for all
    read topics. Remote arguments are read from class variable _args. SALObj
    remote is accessible through 'remote' class variable."""

    def __new__(mcs, classname, bases, dictionary):
        dictionary["domain"] = Domain()

        dictionary["remote"] = Remote(dictionary["domain"], **dictionary["_args"])
        for m in filter(
            lambda m: m.startswith("tel_") or m.startswith("evt_"),
            dir(dictionary["remote"]),
        ):
            dictionary[m[4:]] = Signal(map)

        def connect_callbacks(self):
            for m in filter(_filterEvtTel, dir(self.remote)):
                getattr(self.remote, m).callback = getattr(self, m[4:]).emit

            self.remote.start_task.add_done_callback(
                functools.partial(self.reemit_remote)
            )

        def reemit_remote(self, task=None):
            """
            Re-emits all telemetry and event data from a single remote as Qt messages.

            Parameters
            ----------
            task : Object
                Optional parameter, future from Future.add_done_callback. See
                https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.add_done_callback.
            """
            for m in filter(_filterEvtTel, dir(self.remote)):
                data = getattr(self.remote, m).get()
                if data is not None:
                    getattr(self, m[4:]).emit(data)

        async def close(self):
            await self.remote.close()
            await self.domain.close()

        newclass = super(MetaSAL, mcs).__new__(mcs, classname, bases, dictionary)

        # creates class methods
        setattr(newclass, connect_callbacks.__name__, connect_callbacks)
        setattr(newclass, reemit_remote.__name__, reemit_remote)
        setattr(newclass, close.__name__, close)

        return newclass


def create(name, **kvargs):
    """Creates SALComm instance for given remote(s). The returned object
    contains PySide2.QtCore.Signal class variables. Those signals are emitted
    when SAL callback occurs, effectively linking SAL/DDS and Qt word. Signals
    can be connected to multiple Qt slots to process the incoming data.

    Class variable with the same name as SAL remote name are instances of
    lsst.ts.salobj.Remote. Those can be used to start commands (available with
    `cmd_` prefix).

    Parameters
    ----------
    name : `str`
       Remote name.
    **kvargs : `dict`
       Optional parameters passed to remote.

    Usage
    -----

    .. code-block:: python
       import SALComm

       import sys
       from asyncqt import QEventLoop
       from PySide2.QtWidgets import QApplication

       app = QApplication(sys.argv)
       loop = QEventLoop(app)
       asyncio.set_event_loop(loop)

       my_mount = SALComm.create("MTMount")

       @Slot(map)
       def update_labels_azimuth(data):
           ...

       my_mount.azimuth.connect(update_labels_azimuth)

       ...

       # should trigger callbacks with historic data
       loop.run_until_complete(my_sal.start())

       # runs start command
       await my_sal.MTMount.cmd_start.set_start(settingsToApply="Default")
    """

    class SALComm(QObject, metaclass=MetaSAL):
        """
        SAL proxy. Set callback to emit Qt signals.
        """

        _args = kvargs
        _args["name"] = name

        def __init__(self):
            super().__init__()

            self.connect_callbacks()

    return SALComm()
