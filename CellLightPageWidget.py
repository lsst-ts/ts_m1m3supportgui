
import QTHelpers
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

class CellLightPageWidget(QWidget):
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

        self.dataEventCellLightWarning = DataCache()
        self.dataEventCellLightStatus = DataCache()
        
        self.MTM1M3.subscribeEvent_cellLightWarning(self.processEventCellLightWarning)
        self.MTM1M3.subscribeEvent_cellLightStatus(self.processEventCellLightStatus)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventCellLightWarning.hasBeenUpdated():
            data = self.dataEventCellLightWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            # TODO QTHelpers.setWarningLabel(self.cellLightSensorMismatchLabel, BitHelper.get(data.cellLightFlags, CellLightFlags.CellLightSensorMismatch))

        if self.dataEventCellLightStatus.hasBeenUpdated():
            data = self.dataEventCellLightStatus.get()
            QTHelpers.setBoolLabelOnOff(self.cellLightsCommandedOnLabel, data.cellLightsCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.cellLightsOnLabel, data.cellLightsOn)

    def issueCommandTurnLightsOn(self):
        self.MTM1M3.issueCommandThenWait_turnLightsOn(False)

    def issueCommandTurnLightsOff(self):
        self.MTM1M3.issueCommandThenWait_turnLightsOff(False)

    def processEventCellLightWarning(self, data):
        self.dataEventCellLightWarning.set(data[-1])
        
    def processEventCellLightStatus(self, data):
        self.dataEventCellLightStatus.set(data[-1])
