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
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot


class HardpointsWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm

        self.layout = QVBoxLayout()

        dataLayout = QGridLayout()

        self.layout.addLayout(dataLayout)
        self.setLayout(self.layout)

        dataLayout.addWidget(QLabel("Hardpoint"), 0, 0)
        for hp in range(1, 7):
            dataLayout.addWidget(QLabel(str(hp)), 0, hp)

        self.variables = {
            "stepsQueued": "Steps queued",
            "stepsCommanded": "Steps commanded",
            "measuredForce": "Measured force",
            "encoder": "Encoder",
            "displacement": "Displacement",
        }

        row = 1
        for v, n in self.variables.items():

            def addRow(text, row):
                ret = []
                dataLayout.addWidget(QLabel(text), row, 0)
                for hp in range(6):
                    hpLabel = QLabel()
                    dataLayout.addWidget(hpLabel, row, 1 + hp)
                    ret.append(hpLabel)
                return ret

            setattr(self, v, addRow(n, row))
            row += 1

        self.forces = {
            "forceMagnitude": "Total force",
            "fx": "Force X",
            "fy": "Force Y",
            "fz": "Force Z",
            "mx": "Moment X",
            "my": "Moment Y",
            "mz": "Moment Z",
        }

        dataLayout.addWidget(QLabel(), row, 0)
        row += 1

        def addDataRow(variables, row, col=0):
            for v, n in variables.items():
                dataLayout.addWidget(QLabel(n), row, col)
                l = QLabel()
                setattr(self, v, l)
                dataLayout.addWidget(l, row + 1, col)
                col += 1

        addDataRow(self.forces, row)
        row += 2
        dataLayout.addWidget(QLabel(), row, 0)
        row += 1
        self.positions = {
            "xPosition": "Position X",
            "yPosition": "Position Y",
            "zPosition": "Position Z",
            "xRotation": "Rotation X",
            "yRotation": "Rotation Y",
            "zRotation": "Rotation Z",
        }
        addDataRow(self.positions, row, 1)

        self.layout.addStretch()

        self.comm.hardpointActuatorData.connect(self.hardpointActuatorData)

    @Slot(map)
    def hardpointActuatorData(self, data):
        def fillRow(hpData, rowLabels):
            for hp in range(6):
                rowLabels[hp].setText(f"{hpData[hp]:.02f}")

        for v in self.variables:
            fillRow(getattr(data, v), getattr(self, v))

        for v in self.forces:
            getattr(self, v).setText(str(getattr(data, v)))

        for v in self.positions:
            getattr(self, v).setText(str(getattr(data, v)))
