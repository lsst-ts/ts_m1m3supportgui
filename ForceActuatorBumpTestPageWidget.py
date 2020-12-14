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
from FATABLE import *
from SALLogWidget import SALLogWidget
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTableWidgetSelectionRange,
    QHeaderView,
    QCheckBox,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QGroupBox,
    QProgressBar,
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

        self.xIndex = self.yIndex = self.zIndex = self.sIndex = self.testedId = None
        self._testRunning = False

        actuatorBox = QGroupBox("Actuator")
        self.actuatorsTable = QTableWidget(len(FATABLE), 3)
        self.actuatorsTable.setShowGrid(False)

        for r in range(len(FATABLE)):
            actuatorId = FATABLE[r][FATABLE_ID]

            def getItem(text):
                item = QTableWidgetItem(text)
                item.setData(Qt.UserRole, actuatorId)
                return item

            self.actuatorsTable.setItem(r, 0, getItem(str(actuatorId)))
            self.actuatorsTable.setItem(r, 1, getItem("P"))
            if FATABLE[r][FATABLE_SINDEX] is None:
                item = QTableWidgetItem("")
                item.setFlags(Qt.NoItemFlags)
                self.actuatorsTable.setItem(r, 2, item)
            else:
                self.actuatorsTable.setItem(
                    r,
                    2,
                    getItem("Y" if (FATABLE[r][FATABLE_XINDEX] is None) else "X"),
                )

        self.actuatorsTable.horizontalHeader().hide()
        self.actuatorsTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.actuatorsTable.horizontalHeader().setStretchLastSection(False)
        self.actuatorsTable.verticalHeader().hide()
        self.actuatorsTable.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )

        self.actuatorsTable.itemSelectionChanged.connect(self.itemSelectionChanged)
        self.actuatorsTable.setSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.MinimumExpanding
        )
        self.actuatorsTable.setMaximumWidth(100)
        actuatorLayout = QVBoxLayout()
        actuatorLayout.addWidget(self.actuatorsTable)
        actuatorBox.setLayout(actuatorLayout)

        def testPB():
            pb = QProgressBar()
            pb.setMaximum(6)
            return pb

        self.primaryPB = testPB()
        self.primaryLabelPB = QLabel("Primary")

        self.secondaryPB = testPB()
        self.secondaryLabelPB = QLabel("Seconday")

        self.progressGroup = QGroupBox("Test progress")
        progressLayout = QGridLayout()
        progressLayout.addWidget(self.primaryLabelPB, 0, 0)
        progressLayout.addWidget(self.primaryPB, 0, 1)
        progressLayout.addWidget(self.secondaryLabelPB, 1, 0)
        progressLayout.addWidget(self.secondaryPB, 1, 1)
        # progressLayout.addStretch(1)
        self.progressGroup.setLayout(progressLayout)
        self.progressGroup.setMaximumWidth(510)

        self.chart = TimeChart.TimeChart()
        self.chart_view = TimeChart.TimeChartView(self.chart)
        self.chart_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.bumpTestAllButton = QPushButton("Bump test all")
        self.bumpTestAllButton.clicked.connect(self.bumpTestAll)
        self.bumpTestAllButton.setEnabled(False)
        self.bumpTestButton = QPushButton("Run bump test")
        self.bumpTestButton.clicked.connect(self.issueCommandBumpTest)
        self.bumpTestButton.setEnabled(False)
        self.killBumpTestButton = QPushButton("Stop bump test")
        self.killBumpTestButton.clicked.connect(self.issueCommandKillBumpTest)
        self.killBumpTestButton.setEnabled(False)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.bumpTestAllButton)
        self.buttonLayout.addWidget(self.bumpTestButton)
        self.buttonLayout.addWidget(self.killBumpTestButton)

        self.layout = QVBoxLayout()
        self.forms = QHBoxLayout()
        self.forms.addWidget(actuatorBox)
        self.forms.addWidget(self.progressGroup)
        self.forms.addWidget(SALLogWidget(self.comm))
        self.layout.addLayout(self.forms)
        self.layout.addWidget(self.chart_view)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

        self.comm.detailedState.connect(self.detailedState)
        self.comm.forceActuatorBumpTestStatus.connect(self.forceActuatorBumpTestStatus)

    @Slot()
    def itemSelectionChanged(self):
        """Called when an actuator is selected from the list."""
        items = self.actuatorsTable.selectedItems()
        if len(items) == 0:
            return
        if len(items) > 1:
            actuators = f"{items[0].data(Qt.UserRole)}..{items[-1].data(Qt.UserRole)}"
        else:
            actuators = f"{items[0].data(Qt.UserRole)}"

        self.bumpTestButton.setEnabled(not (self._anyCylinderRunning()))
        self.bumpTestButton.setText(f"Run bump test for FA ID {actuators}")

    def toggledTest(self, toggled):
        """Called when primary or secondary tests check box are toggled."""
        self.bumpTestButton.setEnabled(
            self.actuatorsTable.currentItem() is not None
            and not (self._anyCylinderRunning())
        )

    @asyncSlot()
    async def bumpTestAll(self):
        self.actuatorsTable.setRangeSelected(
            QTableWidgetSelectionRange(0, 1, self.actuatorsTable.rowCount() - 1, 2),
            False,
        )
        self.actuatorsTable.setRangeSelected(
            QTableWidgetSelectionRange(0, 0, self.actuatorsTable.rowCount() - 1, 0),
            True,
        )
        await self._testItem(self.actuatorsTable.selectedItems()[0])
        self.bumpTestButton.setEnabled(False)

    @asyncSlot()
    async def issueCommandBumpTest(self):
        """Call M1M3 bump test command."""
        await self._testItem(self.actuatorsTable.selectedItems()[0])

    async def _testItem(self, item):
        self.chart.clearData()
        self.actuatorsTable.scrollToItem(item)
        self.testedId = item.data(Qt.UserRole)
        item.setSelected(False)
        self.zIndex = actuatorIDToIndex(self.testedId)

        self.xIndex = FATABLE[self.zIndex][FATABLE_XINDEX]
        self.yIndex = FATABLE[self.zIndex][FATABLE_YINDEX]
        self.sIndex = FATABLE[self.zIndex][FATABLE_SINDEX]

        self.progressGroup.setTitle(f"Test progress {self.testedId}")
        if self.sIndex is not None:
            self.secondaryLabelPB.setText("Y" if self.xIndex is None else "X")

        await self.comm.MTM1M3.cmd_forceActuatorBumpTest.set_start(
            actuatorId=self.testedId,
            testPrimary=not (item.text() == "X" or item.text() == "Y"),
            testSecondary=not (item.text() == "P") and self.sIndex is not None,
        )
        self.killBumpTestButton.setText(f"Stop bump test FA ID {self.testedId}")

    @asyncSlot()
    async def issueCommandKillBumpTest(self):
        """Kill bump test."""
        self.actuatorsTable.setRangeSelected(
            QTableWidgetSelectionRange(0, 0, self.actuatorsTable.rowCount() - 1, 2),
            False,
        )
        await self.comm.MTM1M3.cmd_killForceActuatorBumpTest.start()

    @Slot(map)
    def detailedState(self, data):
        """Called when detailedState event is received. Intercept to enable/disable form buttons."""
        if data.detailedState == 9:  # DetailedStates.ParkedEngineeringState
            self.bumpTestAllButton.setEnabled(True)
            self.bumpTestButton.setEnabled(
                self.actuatorsTable.currentItem() is not None
            )
            self.killBumpTestButton.setEnabled(False)
            self.xIndex = self.yIndex = self.zIndex = None
        else:
            self.bumpTestAllButton.setEnabled(False)
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
            chartData.append(
                (
                    "Force (N)",
                    "Measured X",
                    data.xForce[self.xIndex],
                )
            )
        if self.yIndex is not None:
            chartData.append(
                (
                    "Force (N)",
                    "Measured Y",
                    data.yForce[self.yIndex],
                )
            )
        if self.zIndex is not None:
            chartData.append(("Force (N)", "Measured Z", data.zForce[self.zIndex]))

        self.chart.append(data.timestamp, chartData)

    @asyncSlot(map)
    async def forceActuatorBumpTestStatus(self, data):
        """Received when an actuator finish/start running bump tests or the actuator reports progress of the bump test."""

        testProgress = [
            "Not tested",
            "Testing start zero",
            "Testing positive",
            "Positive wait zero",
            "Testing negative",
            "Negative wait zero",
            "Passed",
            "Failed",
        ]

        # test progress
        if self.zIndex is not None:
            self.primaryPB.setEnabled(True)
            val = data.primaryTest[self.zIndex]
            self.primaryPB.setFormat(f"ID {self.testedId} - {testProgress[val]} - %v")
            self.primaryPB.setValue(min(6, val))
        else:
            self.primaryPB.setEnabled(False)

        if self.sIndex is not None:
            self.secondaryPB.setEnabled(True)
            val = data.secondaryTest[self.sIndex]
            self.secondaryPB.setFormat(f"ID {self.testedId} - {testProgress[val]} - %v")
            self.secondaryPB.setValue(min(6, val))
        else:
            self.secondaryPB.setEnabled(False)

        # list display
        for index in range(156):

            def getColor(value):
                if value == 6:
                    return Qt.green
                elif value == 7:
                    return Qt.red
                elif not (value == 0):
                    return Qt.magenta
                return Qt.transparent

            pColor = getColor(data.primaryTest[index])

            self.actuatorsTable.item(index, 1).setBackground(pColor)
            sIndex = FATABLE[index][FATABLE_SINDEX]
            if sIndex is not None:
                sColor = getColor(data.secondaryTest[sIndex])
                self.actuatorsTable.item(index, 2).setBackground(sColor)
                if pColor == sColor:
                    self.actuatorsTable.item(index, 0).setBackground(pColor)
            else:
                self.actuatorsTable.item(index, 0).setBackground(pColor)

        # no tests running..
        if data.actuatorId < 0:
            selected = self.actuatorsTable.selectedItems()
            if len(selected) > 0:
                await self._testItem(selected[0])
            elif self._testRunning == True:
                self.bumpTestAllButton.setEnabled(True)
                self.bumpTestButton.setEnabled(
                    self.actuatorsTable.currentItem() is not None
                    and self._anyCylinder()
                )
                self.killBumpTestButton.setEnabled(False)
                self.xIndex = self.yIndex = self.zIndex = None
                self.comm.appliedForces.disconnect(self.appliedForces)
                self.comm.forceActuatorData.disconnect(self.forceActuatorData)
                self._testRunning = False

        elif self._testRunning is False:
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(True)
            self.comm.appliedForces.connect(self.appliedForces)
            self.comm.forceActuatorData.connect(self.forceActuatorData)
            self._testRunning = True

    # helper functions. Helps correctly enable/disable Run bump test button.
    def _anyCylinderRunning(self):
        return self._testRunning is True and self._anyCylinder()

    def _anyCylinder(self):
        return len(self.actuatorsTable.selectedItems()) > 0
