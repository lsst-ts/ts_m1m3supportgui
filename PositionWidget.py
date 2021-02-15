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
    QLineEdit,
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
    """Displays position data - measured and target position, allows to offset (jog) the mirror."""

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
            if p[1:] == "Position":
                le = QLineEdit("+0.000")
                le.setInputMask("#9.999")
            else:
                le = QLineEdit("+00.00")
                le.setInputMask("#99.99")
            dataLayout.addWidget(le, row, col)
            setattr(self, "target_" + p, le)
            col += 1

        row += 1

        self.moveMirrorButton = QPushButton("Move Mirror")
        self.moveMirrorButton.clicked.connect(self._moveMirror)

        dataLayout.addWidget(self.moveMirrorButton, row, 1, 1, 3)

        row += 1
        dataLayout.addWidget(DirectionPadWidget(), row, 1, 2, 2)

        self.layout.addStretch()

        self.comm.hardpointActuatorData.connect(self.hardpointActuatorData)
        self.comm.imsData.connect(self.imsData)
        self.comm.detailedState.connect(self.detailedState)

    @asyncSlot()
    async def _moveMirror(self):
        args = {}
        try:
            for p in self.POSITIONS:
                scale = MM2M if p[1:] == "Position" else ARCSEC2R
                args[p] = float(getattr(self, "target_" + p).text()) * scale
            await self.comm.MTM1M3.cmd_positionM1M3.set_start(**args)
        except base.AckError as ackE:
            await QTHelpers.warning(
                self, f"Error executing positionM1M3({args})", ackE.ackcmd.result,
            )
        except RuntimeError as rte:
            await QTHelpers.warning(
                self, f"Error executing positionM1M3({args})", str(rte),
            )

    def _fillRow(self, variables, data):
        for k, v in variables.items():
            v.setValue(getattr(data, k))

    def _updateDiffs(self):
        if self._hpData is None or self._imsData is None:
            return
        for k, v in self.diffs.items():
            v.setValue(getattr(self._hpData, k) - getattr(self._imsData, k))

    @Slot(map)
    def hardpointActuatorData(self, data):
        self._fillRow(self.hpVariables, data)
        self._hpData = data
        self._updateDiffs()

    @Slot(map)
    def imsData(self, data):
        self._fillRow(self.imsVariables, data)
        self._imsData = data
        self._updateDiffs()

    @Slot(map)
    def detailedState(self, data):
        self.moveMirrorButton.setEnabled(
            data.detailedState
            in (DetailedState.ACTIVEENGINEERING, DetailedState.ACTIVE)
        )
