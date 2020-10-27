import QTHelpers
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
)
from asyncqt import asyncSlot


class ForceActuatorBumpTestPageWidget(QWidget):
    """
    Enable user to select actuator for bump test. Show graphs depicting actual demand and measured forces.
    """

    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.pageActive = False

        self.xIndex = self.yIndex = self.zIndex = None
        self._testRunning = False

        self.formLayoutLeft = QFormLayout()
        self.actuatorId = QListWidget()
        for f in FATABLE:
            self.actuatorId.addItem(str(f[FATABLE_ID]))
        self.actuatorId.currentItemChanged.connect(self.selectedActuator)
        self.formLayoutLeft.addRow("Actuator:", self.actuatorId)

        self.formLayoutRight = QFormLayout()
        self.primaryTest = QCheckBox()
        self.primaryTest.setChecked(True)
        self.primaryTest.toggled.connect(self.toggledTest)
        self.formLayoutRight.addRow("Primary Cylinder: ", self.primaryTest)
        self.secondaryTest = QCheckBox()
        self.secondaryTest.setChecked(True)
        self.secondaryTest.toggled.connect(self.toggledTest)
        self.formLayoutRight.addRow("Secondary Cylinder: ", self.secondaryTest)

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
        self.forms.addLayout(self.formLayoutLeft)
        self.forms.addLayout(self.formLayoutRight)
        self.layout.addLayout(self.forms)
        self.layout.addWidget(self.chart_view)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

        self.comm.detailedState.connect(self.detailedState)
        self.comm.forceActuatorBumpTestStatus.connect(self.forceActuatorBumpTestStatus)

    def setPageActive(self, active):
        self.pageActive = active

    def selectedActuator(self, current, previous):
        item = self.actuatorId.currentItem()
        if item is None:
            self.bumpTestButton.setEnabled(False)
            return

        actuatorId = int(item.text())
        index = actuatorIDToIndex(actuatorId)

        self.secondaryTest.setEnabled(FATABLE[index][FATABLE_SINDEX] is not None)

        self.bumpTestButton.setEnabled(self._anyCylinder())

    def toggledTest(self, toggled):
        self.bumpTestButton.setEnabled(
            self.actuatorId.currentItem() is not None and self._anyCylinder()
        )

    @asyncSlot()
    async def issueCommandBumpTest(self):
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
        await self.comm.MTM1M3.cmd_killForceActuatorBumpTest.start()

    @Slot(map)
    def detailedState(self, data):
        if data.detailedState == 9:  # DetailedStates.ParkedEngineeringState
            self.bumpTestButton.setEnabled(self.actuatorId.currentItem() is not None)
            self.killBumpTestButton.setEnabled(False)
            self.xIndex = self.yIndex = self.zIndex = None
        else:
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(False)

    @Slot(map)
    def appliedForces(self, data):
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
        """
        Redraw actuators with values.
        """

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

    def _anyCylinder(self):
        return self.primaryTest.isChecked() or (
            self.secondaryTest.isEnabled() and self.secondaryTest.isChecked()
        )
