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
        self.pageActive = False

        self.layout = QVBoxLayout()

        dataLayout = QGridLayout()

        self.layout.addLayout(dataLayout)
        self.setLayout(self.layout)

        row = 0

        def addRow(text, row):
            ret = []
            dataLayout.addWidget(QLabel(text), row, 0)
            for hp in range(6):
                hpLabel = QLabel()
                dataLayout.addWidget(hpLabel, row, 1 + hp)
                ret.append(hpLabel)
            return ret

        self.stepsQueued = addRow("Steps queued", row)
        row += 1
        self.stepsCommanded = addRow("Steps commanded", row)

        self.layout.addStretch()

    def setPageActive(self, active):
        if self.pageActive == active:
            return

        if active:
            self.comm.hardpointActuatorData.connect(self.hardpointActuatorData)
        else:
            self.comm.hardpointActuatorData.disconnect(self.hardpointActuatorData)

        self.pageActive = active

    @Slot(map)
    def hardpointActuatorData(self, data):
        def fillRow(hpData, rowLabels):
            for hp in range(6):
                rowLabels[hp].setText(f"{hpData[hp]:.02f}")

        fillRow(data.stepsQueued, self.stepsQueued)
        fillRow(data.stepsCommanded, self.stepsCommanded)
