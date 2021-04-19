# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org). See the COPYRIGHT file at the top - level directory
# of this distribution for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

from CustomLabels import Heartbeat

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QStatusBar, QLabel, QWidget, QHBoxLayout

from lsst.ts.idl.enums import MTM1M3

__all__ = ["StatusBar", "detailedStateString"]


def detailedStateString(detailedState):
    """Returns string description of mirror state.

    Parameters
    ----------
    detailedState : `int`
        M1M3 detailed state.

    Returns
    -------
    stateString : `str`
        HTML string (usable in Qt) description of detailed state."""
    _map = {
        MTM1M3.DetailedState.DISABLED: "Disabled",
        MTM1M3.DetailedState.FAULT: "<font color='red'>Fault</font>",
        MTM1M3.DetailedState.OFFLINE: "<font color='red'>Offline</font>",
        MTM1M3.DetailedState.STANDBY: "Standby",
        MTM1M3.DetailedState.PARKED: "<font color='green'>Parked</font>",
        MTM1M3.DetailedState.RAISING: "<font color='magenta'>Raising</font>",
        MTM1M3.DetailedState.ACTIVE: "<font color='blue'>Active</font>",
        MTM1M3.DetailedState.LOWERING: "<font color='magenta'>Lowering</font>",
        MTM1M3.DetailedState.PARKEDENGINEERING: "<font color='green'>Parked Engineering</font>",
        MTM1M3.DetailedState.RAISINGENGINEERING: "<font color='magenta'>Raising Engineering</font>",
        MTM1M3.DetailedState.ACTIVEENGINEERING: "<font color='blue'>Active Engineering</font>",
        MTM1M3.DetailedState.LOWERINGENGINEERING: "<font color='magenta'>Lowering Engineering</font>",
        MTM1M3.DetailedState.LOWERINGFAULT: "<font color='red'>Lowering Fault</font>",
        MTM1M3.DetailedState.PROFILEHARDPOINTCORRECTIONS: "<font color='red'>Profile Hardpoint Corrections</font>",
    }
    try:
        return _map[detailedState]
    except KeyError:
        return f"<font color='red'>Unknow : {detailedState}</font>"


class StatusBar(QStatusBar):
    """M1M3 Status bar. Shows heartbeats, errors, log lines.
    Parameters
    ----------
    m1m3 : `SALComm`
        M1M3 SS SALComm
    mtmount : `SALComm`
        MT Mount SALComm
    """

    def __init__(self, m1m3, mtmount):
        super().__init__()

        self.detailedStateLabel = QLabel("---")
        self.addWidget(self.detailedStateLabel)

        hbWidget = QWidget()
        hbLayout = QHBoxLayout()
        hbWidget.setLayout(hbLayout)

        hbLayout.addWidget(QLabel("M1M3"))
        m1m3HeartBeatLabel = Heartbeat(indicator=False)
        hbLayout.addWidget(m1m3HeartBeatLabel)

        hbLayout.addWidget(QLabel("MT Mount"))
        mtMountHeartBeatLabel = Heartbeat(indicator=False)
        hbLayout.addWidget(mtMountHeartBeatLabel)

        self.addPermanentWidget(hbWidget)

        m1m3.detailedState.connect(self.detailedState)
        m1m3.heartbeat.connect(m1m3HeartBeatLabel.heartbeat)

        mtmount.heartbeat.connect(mtMountHeartBeatLabel.heartbeat)

    @Slot(map)
    def detailedState(self, data):
        self.detailedStateLabel.setText(detailedStateString(data.detailedState))
