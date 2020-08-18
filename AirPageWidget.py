
import QTHelpers
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

class AirPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
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

        self.dataEventAirSupplyWarning = DataCache()
        self.dataEventAirSupplyStatus = DataCache()
        
        self.MTM1M3.subscribeEvent_airSupplyWarning(self.processEventAirSupplyWarning)
        self.MTM1M3.subscribeEvent_airSupplyStatus(self.processEventAirSupplyStatus)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventAirSupplyWarning.hasBeenUpdated():
            data = self.dataEventAirSupplyWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            # TODO QTHelpers.setWarningLabel(self.airValveSensorMismatch, BitHelper.get(data.airSupplyFlags, AirSupplyFlags.AirValveSensorMismatch))

        if self.dataEventAirSupplyStatus.hasBeenUpdated():
            data = self.dataEventAirSupplyStatus.get()
            QTHelpers.setBoolLabelOnOff(self.airCommandedOnLabel, data.airCommandedOn)
            QTHelpers.setBoolLabelHighLow(self.airValveOpenedLabel, data.airValveOpened)
            QTHelpers.setBoolLabelHighLow(self.airValveClosedLabel, data.airValveClosed)

    def issueCommandTurnAirOn(self):
        self.MTM1M3.issueCommandThenWait_turnAirOn(False)

    def issueCommandTurnAirOff(self):
        self.MTM1M3.issueCommandThenWait_turnAirOff(False)

    def processEventAirSupplyWarning(self, data):
        self.dataEventAirSupplyWarning.set(data[-1])
        
    def processEventAirSupplyStatus(self, data):
        self.dataEventAirSupplyStatus.set(data[-1])
