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
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QSpinBox, QPushButton
from PySide2.QtCore import Slot
import astropy.units as u

from lsst.ts.idl.enums.MTM1M3 import HardpointActuatorMotionStates


class HardpointsWidget(QWidget):
    """Displays hardpoint data - encoders and calculated position, hardpoint
    state, and M1M3 displacement."""

    def __init__(self, comm):
        super().__init__()
        self.comm = comm

        self.layout = QVBoxLayout()

        dataLayout = QGridLayout()

        self.layout.addLayout(dataLayout)
        self.setLayout(self.layout)

        dataLayout.addWidget(QLabel("<b>Hardpoint</b>"), 0, 0)
        for hp in range(1, 7):
            dataLayout.addWidget(QLabel(f"<b>{hp}</b>"), 0, hp)

        class ValueFormat:
            def __init__(self, label, fmt, scale=None):
                self.label = label
                self.fmt = fmt
                self.scale = scale

            def toString(self, data):
                if self.scale is None:
                    return f"{data:{self.fmt}}"
                else:
                    return f"{(self.scale(data)):{self.fmt}}"

        class Force(ValueFormat):
            def __init__(self, label, fmt=".02f"):
                super().__init__(label, fmt, lambda x: x * u.N)

        class Mm(ValueFormat):
            def __init__(self, label):
                super().__init__(label, ".04f", lambda x: (x * u.meter).to(u.mm))

        class WarningLabel(ValueFormat):
            def __init__(self, label):
                super().__init__(label, "b")

        self.variables = {
            "stepsQueued": ValueFormat("Steps queued", "d"),
            "stepsCommanded": ValueFormat("Steps commanded", "d"),
            "encoder": ValueFormat("Encoder", "d"),
            "measuredForce": Force("Measured force", ".03f"),
            "displacement": Mm("Displacement"),
        }

        row = 1

        def addRow(text, row):
            ret = []
            dataLayout.addWidget(QLabel(text), row, 0)
            for hp in range(6):
                hpLabel = QLabel()
                dataLayout.addWidget(hpLabel, row, 1 + hp)
                ret.append(hpLabel)
            return ret

        for k, v in self.variables.items():
            setattr(self, k, addRow(v.label, row))
            row += 1

        dataLayout.addWidget(QLabel("Encoder targets"), row, 0)
        self.hpTargets = []
        for hp in range(6):
            sb = QSpinBox()
            sb.setRange(-66000, 66000)
            sb.setSingleStep(100)
            dataLayout.addWidget(sb, row, 1 + hp)
            self.hpTargets.append(sb)
        row += 1

        setFromCurrent = QPushButton("Set current")
        setFromCurrent.clicked.connect(self._setFromCurrent)
        dataLayout.addWidget(setFromCurrent, row, 1, 1, 2)

        row += 1
            
        self.monitorData = {
            "breakawayLVDT": ValueFormat("Breakaway LVDT", ".02f"),
            "displacementLVDT": ValueFormat("Displacement LVDT", ".02f"),
            "breakawayPressure": ValueFormat("Breakaway Pressure", ".02f"),
            "pressureSensor1": ValueFormat("Pressure Sensor 1", ".04f"),
            "pressureSensor2": ValueFormat("Pressure Sensor 2", ".04f"),
            "pressureSensor3": ValueFormat("Pressure Sensor 3", ".04f"),
        }

        for k, v in self.monitorData.items():
            setattr(self, k, addRow(v.label, row))
            row += 1

        self.warnings = {
            "majorFault": WarningLabel("Major fault"),
            "minorFault": WarningLabel("Minor fault"),
            "faultOverride": WarningLabel("Fault override"),
            "mainCalibrationError": WarningLabel("Main calibration error"),
            "backupCalibrationError": WarningLabel("Backup calibration error"),
            "limitSwitch1Operated": WarningLabel("Limit switch 1"),
            "limitSwitch2Operated": WarningLabel("Limit switch 2"),
        }

        for k, v in self.warnings.items():
            setattr(self, k, addRow(v.label, row))
            row += 1

        dataLayout.addWidget(QLabel("Motion state"), row, 0)
        self.hpStates = []
        for hp in range(6):
            self.hpStates.append(QLabel())
            dataLayout.addWidget(self.hpStates[hp], row, hp + 1)
        row += 1

        self.forces = {
            "forceMagnitude": Force("Total force"),
            "fx": Force("Force X"),
            "fy": Force("Force Y"),
            "fz": Force("Force Z"),
            "mx": Force("Moment X"),
            "my": Force("Moment Y"),
            "mz": Force("Moment Z"),
        }

        dataLayout.addWidget(QLabel(), row, 0)
        row += 1

        def addDataRow(variables, row, col=0):
            for k, v in variables.items():
                dataLayout.addWidget(QLabel(f"<b>{v.label}</b>"), row, col)
                l = QLabel()
                setattr(self, k, l)
                dataLayout.addWidget(l, row + 1, col)
                col += 1

        addDataRow(self.forces, row)
        row += 2
        dataLayout.addWidget(QLabel(), row, 0)
        row += 1
        self.positions = {
            "xPosition": Mm("Position X"),
            "yPosition": Mm("Position Y"),
            "zPosition": Mm("Position Z"),
            "xRotation": Mm("Rotation X"),
            "yRotation": Mm("Rotation Y"),
            "zRotation": Mm("Rotation Z"),
        }
        addDataRow(self.positions, row, 1)

        self.layout.addStretch()

        self.comm.hardpointActuatorData.connect(self.hardpointActuatorData)
        self.comm.hardpointActuatorState.connect(self.hardpointActuatorState)
        self.comm.hardpointMonitorData.connect(self.hardpointMonitorData)
        self.comm.hardpointActuatorWarning.connect(self.hardpointActuatorWarning)

    @Slot()
    def _setFromCurrent(self):
        hpData = self.comm.MTM1M3.tel_hardpointActuatorData.get()
        for hp in range(6):
            self.hpTargets[hp].setValue(hpData.encoder[hp])

    def _fillRow(self, hpData, rowLabels, transform):
        for hp in range(6):
            rowLabels[hp].setText(transform(hpData[hp]))

    @Slot(map)
    def hardpointActuatorData(self, data):
        for k, v in self.variables.items():
            self._fillRow(getattr(data, k), getattr(self, k), v.toString)

        for k, v in self.forces.items():
            getattr(self, k).setText(v.toString(getattr(data, k)))

        for k, v in self.positions.items():
            getattr(self, k).setText(v.toString(getattr(data, k)))

    @Slot(map)
    def hardpointActuatorState(self, data):
        states = {
            HardpointActuatorMotionStates.STANDBY: "Standby",
            HardpointActuatorMotionStates.CHASING: "Chasing",
            HardpointActuatorMotionStates.STEPPING: "Stepping",
            HardpointActuatorMotionStates.QUICKPOSITIONING: "Quick positioning",
            HardpointActuatorMotionStates.FINEPOSITIONING: "Fine positioning",
        }

        def getHpState(state):
            try:
                return states[state]
            except KeyError:
                return f"Invalid {state}"

        for hp in range(6):
            self.hpStates[hp].setText(getHpState(data.motionState[hp]))

    @Slot(map)
    def hardpointMonitorData(self, data):
        for k, v in self.monitorData.items():
            self._fillRow(getattr(data, k), getattr(self, k), v.toString)

    @Slot(map)
    def hardpointActuatorWarning(self, data):
        for k, v in self.warnings.items():
            self._fillRow(getattr(data, k), getattr(self, k), v.toString)
