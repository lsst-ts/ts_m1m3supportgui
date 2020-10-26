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

        self.formLayout = QFormLayout()
        self.actuatorId = QListWidget()
        for f in FATABLE:
            self.actuatorId.addItem(str(f[FATABLE_ID]))
        self.formLayout.addRow("Actuator:", self.actuatorId)
        self.primaryTest = QLabel("Yes")
        self.formLayout.addRow("Primar: ", self.primaryTest)

        self.bumpTestButton = QPushButton("Run bump test")
        self.bumpTestButton.clicked.connect(self.issueCommandBumpTest)
        self.killBumpTestButton = QPushButton("Stop bump test")
        self.killBumpTestButton.clicked.connect(self.issueCommandKillBumpTest)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.bumpTestButton)
        self.buttonLayout.addWidget(self.killBumpTestButton)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formLayout)
        self.layout.addLayout(self.buttonLayout)
        self.setLayout(self.layout)

        self.comm.detailedState.connect(self.processEventDetailedState)

    def setPageActive(self, active):
        self.pageActive = active

    @asyncSlot()
    async def issueCommandBumpTest(self):
        await self.comm.MTM1M3.cmd_forceActuatorBumpTest.set_start(actuatorId=int(self.actuatorId.currentItem().text()),testPrimary=True,testSecondary=True)

    @asyncSlot()
    async def issueCommandKillBumpTest(self):
        await self.comm.MTM1M3.cmd_killForceActuatorBumpTest.start()

    @Slot(map)
    def processEventDetailedState(self, data):
        if data.detailedState == 9: # DetailedStates.ParkedEngineeringState
            self.bumpTestButton.setEnabled(True)
            self.killBumpTestButton.setEnabled(False)
        elif data.detailedState == 15: # DetailedStates.BumpTestState
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(True)
        else:
            self.bumpTestButton.setEnabled(False)
            self.killBumpTestButton.setEnabled(False)

    @Slot(map)
    def forceAcutatorBumpTestStatus(self, data):
        """
        Redraw actuators with values.
        """
        topic = self.topics.topics[topicIndex]
        field = topic.fields[fieldIndex]
        self.fieldGetter = field[1]
        self.fieldDataIndex = field[2]()
        try:
            data = topic.data.get()
            if data is None:
                self.setUnknown()
                return

            self.updateData(data)
            self.topics.changeTopic(topicIndex, self.dataCallback)
        except RuntimeError:
            pass
