# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https: //www.lsst.org).
# See the COPYRIGHT file at the top - level directory of this distribution
# for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.If not, see < https:  // www.gnu.org/licenses/>.

import TimeChart
from FATABLE import *
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QWidget,
    QPushButton,
    QListWidget,
    QCheckBox,
    QSizePolicy,
    QFormLayout,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)
from asyncqt import asyncSlot


class ForceActuatorBumpTestPageWidget(QWidget):
    """
    Enable user to select actuator for bump test. Show graphs depicting actual
    demand and measured forces. Shows button to run a bump test and stop any
    running bump test.

    Parameters
    ----------

    comm : `SALComm object`
        SALComm communication object.
    """

    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.pageActive = False

        self.xIndex = self.yIndex = self.zIndex = None
        self._testRunning = False

        actuatorBox = QGroupBox("Actuator")
        self.actuatorId = QListWidget()
        for f in FATABLE:
            self.actuatorId.addItem(str(f[FATABLE_ID]))
        self.actuatorId.currentItemChanged.connect(self.selectedActuator)
        self.actuatorId.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        actuatorLayout = QVBoxLayout()
        actuatorLayout.addWidget(self.actuatorId)
        actuatorBox.setLayout(actuatorLayout)

        self.primaryTest = QCheckBox("Primary (Z)")
        self.primaryTest.setChecked(True)
        self.primaryTest.toggled.connect(self.toggledTest)
        self.secondaryTest = QCheckBox("Secondary (X or Y)")
        self.secondaryTest.setChecked(True)
        self.secondaryTest.toggled.connect(self.toggledTest)

        cylinders = QGroupBox("Cylinders")
        cylinderLayout = QVBoxLayout()
        cylinderLayout.addWidget(self.primaryTest)
        cylinderLayout.addWidget(self.secondaryTest)
        cylinderLayout.addStretch(1)
        cylinders.setLayout(cylinderLayout)

        self.chart = TimeChart.TimeChart()
        self.chart_view = TimeChart.TimeChartView(self.chart)
        self.chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.bumpTestButton = QPushButton("Run bump test")
        self.bumpTestButton.clicked.connect(self.issueCommandBumpTest)
        self.killBumpTestButton = QPushButton("Stop bump test")
        self.killBumpTestButton.clicked.connect(self.issueCommandKillBumpTest)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.bumpTestButton)
        self.buttonLayout.addWidget(self.killBumpTestButton)

        self.layout = QVBoxLayout()
        self.forms = QHBoxLayout()
        self.forms.addWidget(actuatorBox)
        self.forms.addSpacing(20)
        self.forms.addWidget(cylinders)
        self.forms.addStretch(1)
        self.layout.addLayout(self.forms)
        self.layout.addWidget(self.chart_view)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

        self.comm.detailedState.connect(self.detailedState)
        self.comm.forceActuatorBumpTestStatus.connect(self.forceActuatorBumpTestStatus)

    def setPageActive(self, active):
        self.pageActive = active

    def selectedActuator(self, current, previous):
        """Called when an actuator is selected from the list."""
        item = self.actuatorId.currentItem()
        if item is None:
            self.bumpTestButton.setEnabled(False)
            return

        actuatorId = int(item.text())
        index = actuatorIDToIndex(actuatorId)

        self.secondaryTest.setEnabled(FATABLE[index][FATABLE_SINDEX] is not None)

        self.bumpTestButton.setEnabled(self._anyCylinderNotRunning())

    def toggledTest(self, toggled):
        """Called when primary or secondary tests check box are toggled."""
        self.bumpTestButton.setEnabled(
             self.actuatorId.currentItem() is not None and self._anyCylinderNotRunning()
        )

    @asyncSlot()
    async def issueCommandBumpTest(self):
        """Call M1M3 bump test command."""
        actuatorId = int(self.actuatorId.currentItem().text())
        self.index = actuatorIDToIndex(actuatorId)

        self.xIndex = FATABLE[self.index][FATABLE_XINDEX]
        self.yIndex = FATABLE[self.index][FATABLE_YINDEX]
        self.zIndex = FATABLE[self.index][FATABLE_ZINDEX]

        await self.comm.MTM1M3.cmd_forceActuatorBumpTest.set_start(
            actuatorId=actuatorId,
            testPrimary=self.primaryTest.isChecked(),
            testSecondary=(
                self.secondaryTest.isEnabled() and self.secondaryTest.isChecked()
            ),
        )

    @asyncSlot()
    async def issueCommandKillBumpTest(self):
        """Kill bump test."""
        await self.comm.MTM1M3.cmd_killForceActuatorBumpTest.start()

    @Slot(map)
    def detailedState(self, data):
        """Called when detailedState event is received. Intercept to enable/disable form buttons."""
        if data.detailedState == 9:  # DetailedStates.ParkedEngineeringState
            self.bumpTestButton.setEnabled(self.actuatorId.currentItem() is not None)
            self.killBumpTestButton.setEnabled(False)
            self.xIndex = self.yIndex = self.zIndex = None
        else:
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(False)

    @Slot(map)
    def appliedForces(self, data):
        """Adds applied forces to graph."""
        chartData = []
        if self.xIndex is not None:
            chartData.append(("Force (N)", "Applied X", data.xForces[self.xIndex]))
        if self.yIndex is not None:
            chartData.append(("Force (N)", "Applied Y", data.yForces[self.yIndex]))
        if self.zIndex is not None:
            chartData.append(("Force (N)", "Applied Z", data.zForces[self.zIndex]))

        self.chart.append(data.timestamp, chartData)

    @Slot(map)
    def forceActuatorData(self, data):
        """Adds measured forces to graph."""
        chartData = []
        if self.xIndex is not None:
            chartData.append(("Force (N)", "Measured X", data.xForce[self.xIndex],))
        if self.yIndex is not None:
            chartData.append(("Force (N)", "Measured Y", data.yForce[self.yIndex],))
        if self.zIndex is not None:
            chartData.append(("Force (N)", "Measured Z", data.zForce[self.zIndex]))

        self.chart.append(data.timestamp, chartData)

    @Slot(map)
    def forceActuatorBumpTestStatus(self, data):
        """Received when an actuator finish/start running bump tests or the actuator reports progress of the bump test."""

        if data.actuatorId < 0:
            if self._testRunning == True:
                self.bumpTestButton.setEnabled(
                    self.actuatorId.currentItem() is not None and self._anyCylinder()
                )
                self.killBumpTestButton.setEnabled(False)
                self.xIndex = self.yIndex = self.zIndex = None
                self.comm.appliedForces.disconnect(self.appliedForces)
                self.comm.forceActuatorData.disconnect(self.forceActuatorData)
                self._testRunning = False

        elif self._testRunning == False:
            self.chart.clearData()
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(True)
            self.comm.appliedForces.connect(self.appliedForces)
            self.comm.forceActuatorData.connect(self.forceActuatorData)
            self._testRunning = True

    # helper functions. Helps correctly enable/disable Run bump test button.
    def _anyCylinderNotRunning(self):
        return self._testRunning == False and self._anyCylinder()

    def _anyCylinder(self):
        return self.primaryTest.isChecked() or (
            self.secondaryTest.isEnabled() and self.secondaryTest.isChecked()
        )
