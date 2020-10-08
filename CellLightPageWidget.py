import QTHelpers
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot
from asyncqt import asyncSlot

class CellLightPageWidget(QWidget):
    def __init__(self, comm):
        QWidget.__init__(self)
        self.comm = comm
        self.pageActive = False

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.commandLayout = QVBoxLayout()
        self.layout.addLayout(self.commandLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.setLayout(self.layout)
        self.setFixedHeight(300)
        
        self.turnLightsOnButton = QPushButton("Turn Lights On")
        self.turnLightsOnButton.clicked.connect(self.issueCommandTurnLightsOn)
        self.turnLightsOnButton.setFixedWidth(256)
        self.turnLightsOffButton = QPushButton("Turn Lights Off")
        self.turnLightsOffButton.clicked.connect(self.issueCommandTurnLightsOff)
        self.turnLightsOffButton.setFixedWidth(256)

        self.cellLightsCommandedOnLabel = QLabel("UNKNOWN")
        self.cellLightsOnLabel = QLabel("UNKNOWN")

        self.anyWarningLabel = QLabel("UNKNOWN")
        self.cellLightSensorMismatchLabel = QLabel("UNKNOWN")

        self.commandLayout.addWidget(self.turnLightsOnButton)
        self.commandLayout.addWidget(self.turnLightsOffButton)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Command"), row, col)
        self.dataLayout.addWidget(self.cellLightsCommandedOnLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Sensor"), row, col)
        self.dataLayout.addWidget(self.cellLightsOnLabel, row, col + 1)
        
        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Command / Sensor Mismatch"), row, col)
        self.warningLayout.addWidget(self.cellLightSensorMismatchLabel, row, col + 1)

    def setPageActive(self, active):
        if self.pageActive == active:
            return 

        if active:
            self.comm.cellLightWarning.connect(self.cellLightWarning)
            self.comm.cellLightStatus.connect(self.cellLightStatus)
        else:
            self.comm.cellLightWarning.disconnect(self.cellLightWarning)
            self.comm.cellLightStatus.disconnect(self.cellLightStatus)

        self.pageActive = active

    @Slot(map)
    def cellLightWarning(self, data):
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            # TODO QTHelpers.setWarningLabel(self.cellLightSensorMismatchLabel, BitHelper.get(data.cellLightFlags, CellLightFlags.CellLightSensorMismatch))

    @Slot(map)
    def cellLightStatus(self, data):
        QTHelpers.setBoolLabelOnOff(self.cellLightsCommandedOnLabel, data.cellLightsCommandedOn)
        QTHelpers.setBoolLabelOnOff(self.cellLightsOnLabel, data.cellLightsOn)

    @asyncSlot()
    async def issueCommandTurnLightsOn(self):
        await self.comm.MTM1M3.cmd_turnLightsOn.start()

    @asyncSlot()
    async def issueCommandTurnLightsOff(self):
        await self.comm.MTM1M3.cmd_turnLightsOff.start()
