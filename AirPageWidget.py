
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import AirSupplyFlags
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

class AirPageWidget(QWidget):
    def __init__(self, mtm1m3):
        QWidget.__init__(self)
        self.mtm1m3 = mtm1m3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.commandLayout = QVBoxLayout()

        self.layout.addLayout(self.commandLayout)
        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.warningLayout)
        self.setLayout(self.layout)
        
        self.turnAirOnButton = QPushButton("Turn Air On")
        self.turnAirOnButton.clicked.connect(self.issueCommandTurnAirOn)
        self.turnAirOffButton = QPushButton("Turn Air Off")
        self.turnAirOffButton.clicked.connect(self.issueCommandTurnAirOff)
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.airValveSensorMismatch = QLabel("UNKNOWN")
        self.airCommandedOnLabel = QLabel("UNKNOWN")
        self.airValveOpenedLabel = QLabel("UNKNOWN")
        self.airValveClosedLabel = QLabel("UNKNOWN")

        self.commandLayout.addWidget(self.turnAirOnButton)
        self.commandLayout.addWidget(self.turnAirOffButton)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Command / Sensor Mismatch"), row, col)
        self.warningLayout.addWidget(self.airValveSensorMismatch, row, col + 1)
        
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
        
        self.mtm1m3.subscribeEvent_airSupplyWarning(self.processEventAirSupplyWarning)
        self.mtm1m3.subscribeEvent_airSupplyStatus(self.processEventAirSupplyStatus)

    def issueCommandTurnAirOn(self):
        self.mtm1m3.issueCommandThenWait_turnAirOn(False)

    def issueCommandTurnAirOff(self):
        self.mtm1m3.issueCommandThenWait_turnAirOff(False)

    def processEventAirSupplyWarning(self, data):
        data = data[-1]
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        QTHelpers.setWarningLabel(self.airValveSensorMismatch, BitHelper.get(data.airSupplyFlags, AirSupplyFlags.AirValveSensorMismatch))

    def processEventAirSupplyStatus(self, data):
        data = data[-1]
        QTHelpers.setBoolLabelOnOff(self.airCommandedOnLabel, data.airCommandedOn)
        QTHelpers.setBoolLabelHighLow(self.airValveOpenedLabel, data.airValveOpened)
        QTHelpers.setBoolLabelHighLow(self.airValveClosedLabel, data.airValveClosed)