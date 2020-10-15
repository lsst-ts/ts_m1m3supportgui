import QTHelpers
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot
from asyncqt import asyncSlot


class AirPageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
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

        self.turnAirOnButton = QPushButton("Turn Air On")
        self.turnAirOnButton.clicked.connect(self.issueCommandTurnAirOn)
        self.turnAirOnButton.setFixedWidth(256)
        self.turnAirOffButton = QPushButton("Turn Air Off")
        self.turnAirOffButton.clicked.connect(self.issueCommandTurnAirOff)
        self.turnAirOffButton.setFixedWidth(256)

        self.airCommandedOnLabel = QLabel("UNKNOWN")
        self.airValveOpenedLabel = QLabel("UNKNOWN")
        self.airValveClosedLabel = QLabel("UNKNOWN")

        self.anyWarningLabel = QLabel("UNKNOWN")
        self.airValveSensorMismatch = QLabel("UNKNOWN")

        self.commandLayout.addWidget(self.turnAirOnButton)
        self.commandLayout.addWidget(self.turnAirOffButton)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Commanded On"), row, col)
        self.dataLayout.addWidget(self.airCommandedOnLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Valve Opened"), row, col)
        self.dataLayout.addWidget(self.airValveOpenedLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Valve Closed"), row, col)
        self.dataLayout.addWidget(self.airValveClosedLabel, row, col + 1)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Command / Sensor Mismatch"), row, col)
        self.warningLayout.addWidget(self.airValveSensorMismatch, row, col + 1)

    def setPageActive(self, active):
        if self.pageActive == active:
            return

        if active:
            self.comm.airSupplyWarning.connect(self.airSupplyWarning)
            self.comm.airSupplyStatus.connect(self.airSupplyStatus)
        else:
            self.comm.airSupplyWarning.disconnect(self.airSupplyWarning)
            self.comm.airSupplyStatus.disconnect(self.airSupplyStatus)

        self.pageActive = active

    @Slot(map)
    def airSupplyWarning(self, data):
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        # TODO QTHelpers.setWarningLabel(self.airValveSensorMismatch, BitHelper.get(data.airSupplyFlags, AirSupplyFlags.AirValveSensorMismatch))

    @Slot(map)
    def airSupplyStatus(self, data):
        QTHelpers.setBoolLabelOnOff(self.airCommandedOnLabel, data.airCommandedOn)
        QTHelpers.setBoolLabelHighLow(self.airValveOpenedLabel, data.airValveOpened)
        QTHelpers.setBoolLabelHighLow(self.airValveClosedLabel, data.airValveClosed)

    @asyncSlot()
    async def issueCommandTurnAirOn(self):
        await self.comm.MTM1M3.cmd_turnAirOn.start()

    @asyncSlot()
    async def issueCommandTurnAirOff(self):
        await self.comm.MTM1M3.cmd_turnAirOff.start()
