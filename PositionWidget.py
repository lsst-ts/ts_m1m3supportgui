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
#
# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

import TimeChart
from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QDoubleSpinBox,
    QPushButton,
)
from PySide2.QtCore import Slot
from asyncqt import asyncSlot

from CustomLabels import *
from UnitsConversions import *
from DirectionPadWidget import *

from lsst.ts.salobj import base
from lsst.ts.idl.enums.MTM1M3 import DetailedState

import QTHelpers


class PositionWidget(QWidget):
    """Displays position data - measured and target position, allows to offset (jog) the mirror.

    POSITIONS
    ---------
        Array containing name of positions. Used to name variables and as
        arguments names for positionM1M3 command.

    Parameters
    ----------
    comm : `SALComm`
        Proxy class for SAL/DDS communication. See SALComm.py for details.
    """

    POSITIONS = [
        "xPosition",
        "yPosition",
        "zPosition",
        "xRotation",
        "yRotation",
        "zRotation",
    ]

    def __init__(self, comm):
        super().__init__()
        self.comm = comm

        self._hpData = None
        self._imsData = None

        self.layout = QVBoxLayout()

        dataLayout = QGridLayout()

        self.layout.addLayout(dataLayout)
        self.setLayout(self.layout)

        directions = ["X", "Y", "Z", "Rotation X", "Rotation Y", "Rotation Z"]

        row = 0

        for d in range(6):
            dataLayout.addWidget(QLabel(f"<b>{directions[d]}</b>"), row, d + 1)

        def createXYZR():
            return {
                "xPosition": Mm(),
                "yPosition": Mm(),
                "zPosition": Mm(),
                "xRotation": Arcsec(),
                "yRotation": Arcsec(),
                "zRotation": Arcsec(),
            }

        def createXYZRWarning():
            return {
                "xPosition": MmWarning(),
                "yPosition": MmWarning(),
                "zPosition": MmWarning(),
                "xRotation": ArcsecWarning(),
                "yRotation": ArcsecWarning(),
                "zRotation": ArcsecWarning(),
            }

        self.hpVariables = createXYZR()

        self.imsVariables = createXYZR()

        self.diffs = createXYZRWarning()

        def addDataRow(variables, row, col=1):
            for k, v in variables.items():
                dataLayout.addWidget(v, row, col)
                col += 1

        row += 1
        dataLayout.addWidget(QLabel("<b>HP</b>"), row, 0)
        addDataRow(self.hpVariables, row)

        row += 1
        dataLayout.addWidget(QLabel("<b>IMS</b>"), row, 0)
        addDataRow(self.imsVariables, row)

        row += 1
        dataLayout.addWidget(QLabel("<b>Diff</b>"), row, 0)
        addDataRow(self.diffs, row)

        row += 1
        dataLayout.addWidget(QLabel("<b>Target</b>"), row, 0)

        col = 1
        for p in self.POSITIONS:
            sb = QDoubleSpinBox()
            if p[1:] == "Position":
                sb.setRange(-10, 10)
                sb.setDecimals(3)
                sb.setSingleStep(0.001)
            else:
                sb.setRange(-300, 300)
                sb.setDecimals(2)
                sb.setSingleStep(0.01)

            dataLayout.addWidget(sb, row, col)
            setattr(self, "target_" + p, sb)
            col += 1

        row += 1

        self.moveMirrorButton = QPushButton("Move Mirror")
        self.moveMirrorButton.setEnabled(False)
        self.moveMirrorButton.clicked.connect(self._moveMirror)
        self.moveMirrorButton.setDefault(True)

        dataLayout.addWidget(self.moveMirrorButton, row, 1, 1, 3)

        self.copyCurrentButton = QPushButton("Copy Current")
        self.copyCurrentButton.setEnabled(False)
        self.copyCurrentButton.clicked.connect(self._copyCurrent)

        dataLayout.addWidget(self.copyCurrentButton, row, 4, 1, 3)

        row += 1
        self.dirPad = DirectionPadWidget()
        self.dirPad.setEnabled(False)
        self.dirPad.positionChanged.connect(self._positionChanged)
        dataLayout.addWidget(self.dirPad, row, 1, 3, 3)

        self.layout.addStretch()

        self.comm.hardpointActuatorData.connect(self._hardpointActuatorDataCallback)
        self.comm.imsData.connect(self._imsDataCallback)
        self.comm.detailedState.connect(self._detailedStateCallback)

    async def moveMirror(self, **kwargs):
        """Move mirror. Calls positionM1M3 command.

        Parameters
        ----------
        **kwargs : `dict`
            New target position. Needs to have POSITIONS keys. Passed to
            positionM1M3 command.
        """
        try:
            await self.comm.MTM1M3.cmd_positionM1M3.set_start(**kwargs)
        except base.AckError as ackE:
            await QTHelpers.warning(
                self, f"Error executing positionM1M3({kwargs})", ackE.ackcmd.result,
            )
        except RuntimeError as rte:
            await QTHelpers.warning(
                self, f"Error executing positionM1M3({kwargs})", str(rte),
            )

    def _getScale(self, label):
        return MM2M if label[1:] == "Position" else ARCSEC2R

    def getTargets(self):
        """Return current target values (from form target box).

        Returns
        -------
        args : `dict`
            Current target values. Contains POSITIONS keys. In default units
            (mm, rad).
        """
        args = {}
        for p in self.POSITIONS:
            scale = MM2M if p[1:] == "Position" else ARCSEC2R
            args[p] = getattr(self, "target_" + p).value() * self._getScale(p)
        return args

    def setTargets(self, targets):
        """Set current target values.

        Parameters
        ----------
        targets : `dict`
            Target values. Dictionary with POSITIONS keys.
        """
        for k, v in targets.items():
            getattr(self, "target_" + k).setValue(v / self._getScale(k))

    @asyncSlot()
    async def _moveMirror(self):
        targets = self.getTargets()
        self.dirPad.setPosition(map(lambda p: targets[p], self.POSITIONS))
        await self.moveMirror(**self.getTargets())

    @Slot()
    def _copyCurrent(self):
        args = {k: getattr(self._hpData, k) for k in self.POSITIONS}
        self.setTargets(args)
        self.dirPad.setPosition(map(lambda p: args[p], self.POSITIONS))

    @asyncSlot()
    async def _positionChanged(self, offsets):
        args = {}
        for i in range(6):
            args[self.POSITIONS[i]] = offsets[i]
        self.setTargets(args)
        await self.moveMirror(**args)

    def _fillRow(self, variables, data):
        for k, v in variables.items():
            v.setValue(getattr(data, k))

    def _updateDiffs(self):
        if self._hpData is None or self._imsData is None:
            return
        for k, v in self.diffs.items():
            v.setValue(getattr(self._hpData, k) - getattr(self._imsData, k))

    @Slot(map)
    def _hardpointActuatorDataCallback(self, data):
        self._fillRow(self.hpVariables, data)
        self._hpData = data
        self.copyCurrentButton.setEnabled(True)
        self._updateDiffs()

    @Slot(map)
    def _imsDataCallback(self, data):
        self._fillRow(self.imsVariables, data)
        self._imsData = data
        self._updateDiffs()

    @Slot(map)
    def _detailedStateCallback(self, data):
        enabled = data.detailedState in (
            DetailedState.ACTIVEENGINEERING,
            DetailedState.ACTIVE,
        )

        self.moveMirrorButton.setEnabled(enabled)
        self.dirPad.setEnabled(enabled)
