
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import CellLightFlags
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

class CellLightPageWidget(QWidget):
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
        
        self.turnLightsOnButton = QPushButton("Turn Lights On")
        self.turnLightsOnButton.clicked.connect(self.issueCommandTurnLightsOn)
        self.turnLightsOffButton = QPushButton("Turn Lights Off")
        self.turnLightsOffButton.clicked.connect(self.issueCommandTurnLightsOff)
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.cellLightSensorMismatchLabel = QLabel("UNKNOWN")
        self.cellLightsCommandedOnLabel = QLabel("UNKNOWN")
        self.cellLightsOnLabel = QLabel("UNKNOWN")

        self.commandLayout.addWidget(self.turnLightsOnButton)
        self.commandLayout.addWidget(self.turnLightsOffButton)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Command / Sensor Mismatch"), row, col)
        self.warningLayout.addWidget(self.cellLightSensorMismatchLabel, row, col + 1)
        
        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Command"), row, col)
        self.dataLayout.addWidget(self.cellLightsCommandedOnLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Sensor"), row, col)
        self.dataLayout.addWidget(self.cellLightsOnLabel, row, col + 1)
        
        self.mtm1m3.subscribeEvent_cellLightWarning(self.processEventCellLightWarning)
        self.mtm1m3.subscribeEvent_cellLightStatus(self.processEventCellLightStatus)

    def issueCommandTurnLightsOn(self):
        self.mtm1m3.issueCommandThenWait_turnLightsOn(False)

    def issueCommandTurnLightsOff(self):
        self.mtm1m3.issueCommandThenWait_turnLightsOff(False)

    def processEventCellLightWarning(self, data):
        data = data[-1]
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        QTHelpers.setWarningLabel(self.cellLightSensorMismatchLabel, BitHelper.get(data.cellLightFlags, CellLightFlags.CellLightSensorMismatch))

    def processEventCellLightStatus(self, data):
        data = data[-1]
        QTHelpers.setBoolLabelOnOff(self.cellLightsCommandedOnLabel, data.cellLightsCommandedOn)
        QTHelpers.setBoolLabelOnOff(self.cellLightsOnLabel, data.cellLightsOn)