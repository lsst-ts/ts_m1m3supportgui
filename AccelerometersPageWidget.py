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
import TimeBoxChart
from PySide2.QtWidgets import QWidget, QGridLayout
from PySide2.QtCore import Slot
from asyncqt import asyncSlot


class AccelerometersPageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.chart = []

        for sensor in range(6):
            self.chart.append(TimeBoxChart.TimeBoxChart())
            self.layout.addWidget(
                TimeChart.TimeChartView(self.chart[sensor]), sensor / 2, sensor % 2
            )

        comm.m1m3.connect(self.m1m3)

    @Slot(map)
    def m1m3(self, data):
        for sensor in range(1, 7):
            self.chart[sensor - 1].append(
                data.timestamp,
                [
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}X",
                        getattr(data, f"sensor{sensor}XAcceleration"),
                    ),
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}Y",
                        getattr(data, f"sensor{sensor}YAcceleration"),
                    ),
                    (
                        "Acceleration (m/s<sup>2</sup>)",
                        f"{sensor}Z",
                        getattr(data, f"sensor{sensor}ZAcceleration"),
                    ),
                ],
            )
