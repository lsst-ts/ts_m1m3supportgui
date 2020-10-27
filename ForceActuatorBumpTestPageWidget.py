import QTHelpers
import TimeChart
from FATABLE import *
from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
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

        self.xIndex = self.yIndex = self.zIndex = self.secondaryIndex = None
        self._chartConnected = False

        self.formLayout = QFormLayout()
        self.actuatorId = QListWidget()
        for f in FATABLE:
            self.actuatorId.addItem(str(f[FATABLE_ID]))
        self.formLayout.addRow("Actuator:", self.actuatorId)
        self.primaryTest = QLabel("Yes")
        self.formLayout.addRow("Primar: ", self.primaryTest)

        self.chart = TimeChart.TimeChart()
        self.chart_view = TimeChart.TimeChartView(self.chart)

        self.bumpTestButton = QPushButton("Run bump test")
        self.bumpTestButton.clicked.connect(self.issueCommandBumpTest)
        self.killBumpTestButton = QPushButton("Stop bump test")
        self.killBumpTestButton.clicked.connect(self.issueCommandKillBumpTest)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.bumpTestButton)
        self.buttonLayout.addWidget(self.killBumpTestButton)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formLayout)
        self.layout.addWidget(self.chart_view)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

        self.comm.detailedState.connect(self.detailedState)
        self.comm.forceActuatorBumpTestStatus.connect(self.forceActuatorBumpTestStatus)

    def setPageActive(self, active):
        self.pageActive = active


    @asyncSlot()
    async def issueCommandBumpTest(self):
        actuatorId = int(self.actuatorId.currentItem().text())
        self.index = actuatorIDToIndex(actuatorId)

        self.xIndex = FATABLE[self.index][FATABLE_XINDEX]
        self.yIndex = FATABLE[self.index][FATABLE_YINDEX]
        self.zIndex = FATABLE[self.index][FATABLE_ZINDEX]
        self.secondaryIndex = FATABLE[self.index][FATABLE_SINDEX]

        await self.comm.MTM1M3.cmd_forceActuatorBumpTest.set_start(
            actuatorId=actuatorId, testPrimary=True, testSecondary=True
        )

    @asyncSlot()
    async def issueCommandKillBumpTest(self):
        await self.comm.MTM1M3.cmd_killForceActuatorBumpTest.start()

    @Slot(map)
    def detailedState(self, data):
        if data.detailedState == 9:  # DetailedStates.ParkedEngineeringState
            self.bumpTestButton.setEnabled(True)
            self.killBumpTestButton.setEnabled(False)
            self.xIndex = self.yIndex = self.zIndex = self.secondaryIndex = None
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
        if self.zIndex is not None:
            chartData.append(
                ("Force (N)", "Measured Primary", data.zForce[self.zIndex])
            )

        if self.secondaryIndex is not None:
            chartData.append(
                (
                    "Force (N)",
                    "Measured Secondary",
                    data.secondaryCylinderForce[self.secondaryIndex],
                )
            )

        self.chart.append(data.timestamp, chartData)

    @Slot(map)
    def forceActuatorBumpTestStatus(self, data):
        """
        Redraw actuators with values.
        """

        if data.actuatorId < 0:
            self.bumpTestButton.setEnabled(True)
            self.killBumpTestButton.setEnabled(False)
            self.xIndex = self.yIndex = self.zIndex = self.secondaryIndex = None
            self._disconnectChart()
        else:
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(True)
            self._connectChart()

    def _connectChart(self):
        if self._chartConnected:
            return

        self.comm.appliedForces.connect(self.appliedForces)
        self.comm.forceActuatorData.connect(self.forceActuatorData)
        self._chartConnected = True

    def _disconnectChart(self):
        if not self._chartConnected:
            return

        self.comm.appliedForces.connect(self.appliedForces)
        self.comm.forceActuatorData.connect(self.forceActuatorData)
        self._chartConnected = False
