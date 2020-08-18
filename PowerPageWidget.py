
import QTHelpers
import TimeChart
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

class PowerPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.commandLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.commandLayout)
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.turnMainAOnButton = QPushButton("Turn Main A On")
        self.turnMainAOnButton.setFixedWidth(256)
        self.turnMainAOnButton.clicked.connect(self.issueCommandTurnMainAOn)
        self.turnMainAOffButton = QPushButton("Turn Main A Off")
        self.turnMainAOffButton.setFixedWidth(256)
        self.turnMainAOffButton.clicked.connect(self.issueCommandTurnMainAOff)
        self.turnMainBOnButton = QPushButton("Turn Main B On")
        self.turnMainBOnButton.setFixedWidth(256)
        self.turnMainBOnButton.clicked.connect(self.issueCommandTurnMainBOn)
        self.turnMainBOffButton = QPushButton("Turn Main B Off")
        self.turnMainBOffButton.setFixedWidth(256)
        self.turnMainBOffButton.clicked.connect(self.issueCommandTurnMainBOff)
        self.turnMainCOnButton = QPushButton("Turn Main C On")
        self.turnMainCOnButton.setFixedWidth(256)
        self.turnMainCOnButton.clicked.connect(self.issueCommandTurnMainCOn)
        self.turnMainCOffButton = QPushButton("Turn Main C Off")
        self.turnMainCOffButton.setFixedWidth(256)
        self.turnMainCOffButton.clicked.connect(self.issueCommandTurnMainCOff)
        self.turnMainDOnButton = QPushButton("Turn Main D On")
        self.turnMainDOnButton.setFixedWidth(256)
        self.turnMainDOnButton.clicked.connect(self.issueCommandTurnMainDOn)
        self.turnMainDOffButton = QPushButton("Turn Main D Off")
        self.turnMainDOffButton.setFixedWidth(256)
        self.turnMainDOffButton.clicked.connect(self.issueCommandTurnMainDOff)
        self.turnAuxAOnButton = QPushButton("Turn Aux A On")
        self.turnAuxAOnButton.setFixedWidth(256)
        self.turnAuxAOnButton.clicked.connect(self.issueCommandTurnAuxAOn)
        self.turnAuxAOffButton = QPushButton("Turn Aux A Off")
        self.turnAuxAOffButton.setFixedWidth(256)
        self.turnAuxAOffButton.clicked.connect(self.issueCommandTurnAuxAOff)
        self.turnAuxBOnButton = QPushButton("Turn Aux B On")
        self.turnAuxBOnButton.setFixedWidth(256)
        self.turnAuxBOnButton.clicked.connect(self.issueCommandTurnAuxBOn)
        self.turnAuxBOffButton = QPushButton("Turn Aux B Off")
        self.turnAuxBOffButton.setFixedWidth(256)
        self.turnAuxBOffButton.clicked.connect(self.issueCommandTurnAuxBOff)
        self.turnAuxCOnButton = QPushButton("Turn Aux C On")
        self.turnAuxCOnButton.setFixedWidth(256)
        self.turnAuxCOnButton.clicked.connect(self.issueCommandTurnAuxCOn)
        self.turnAuxCOffButton = QPushButton("Turn Aux C Off")
        self.turnAuxCOffButton.setFixedWidth(256)
        self.turnAuxCOffButton.clicked.connect(self.issueCommandTurnAuxCOff)
        self.turnAuxDOnButton = QPushButton("Turn Aux D On")
        self.turnAuxDOnButton.setFixedWidth(256)
        self.turnAuxDOnButton.clicked.connect(self.issueCommandTurnAuxDOn)
        self.turnAuxDOffButton = QPushButton("Turn Aux D Off")
        self.turnAuxDOffButton.setFixedWidth(256)
        self.turnAuxDOffButton.clicked.connect(self.issueCommandTurnAuxDOff)

        self.anyWarningLabel = QLabel("UNKNOWN")
        self.rcpMirrorCellUtility220VAC1StatusLabel = QLabel("UNKNOWN")
        self.rcpCabinetUtility220VACStatusLabel = QLabel("UNKNOWN")
        self.rcpExternalEquipment220VACStatusLabel = QLabel("UNKNOWN")
        self.rcpMirrorCellUtility220VAC2StatusLabel = QLabel("UNKNOWN")
        self.rcpMirrorCellUtility220VAC3StatusLabel = QLabel("UNKNOWN")
        self.powerNetworkARedundancyControlStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkBRedundancyControlStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkCRedundancyControlStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkDRedundancyControlStatusLabel = QLabel("UNKNOWN")
        self.controlsPowerNetworkRedundancyControlStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkAStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkARedundantStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkBStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkBRedundantStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkCStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkCRedundantStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkDStatusLabel = QLabel("UNKNOWN")
        self.powerNetworkDRedundantStatusLabel = QLabel("UNKNOWN")
        self.controlsPowerNetworkStatusLabel = QLabel("UNKNOWN")
        self.controlsPowerNetworkRedundantStatusLabel = QLabel("UNKNOWN")
        self.lightPowerNetworkStatusLabel = QLabel("UNKNOWN")
        self.externalEquipmentPowerNetworkStatusLabel = QLabel("UNKNOWN")
        self.laserTrackerPowerNetworkStatusLabel = QLabel("UNKNOWN")
        
        self.powerNetworkACurrentLabel = QLabel("UNKNOWN")
        self.powerNetworkBCurrentLabel = QLabel("UNKNOWN")
        self.powerNetworkCCurrentLabel = QLabel("UNKNOWN")
        self.powerNetworkDCurrentLabel = QLabel("UNKNOWN")
        self.lightPowerNetworkCurrentLabel = QLabel("UNKNOWN")
        self.controlsPowerNetworkCurrentLabel = QLabel("UNKNOWN")
        self.powerNetworkACommandedOnLabel = QLabel("UNKNOWN")
        self.powerNetworkBCommandedOnLabel = QLabel("UNKNOWN")
        self.powerNetworkCCommandedOnLabel = QLabel("UNKNOWN")
        self.powerNetworkDCommandedOnLabel = QLabel("UNKNOWN")
        self.auxPowerNetworkACommandedOnLabel = QLabel("UNKNOWN")
        self.auxPowerNetworkBCommandedOnLabel = QLabel("UNKNOWN")
        self.auxPowerNetworkCCommandedOnLabel = QLabel("UNKNOWN")
        self.auxPowerNetworkDCommandedOnLabel = QLabel("UNKNOWN")

        self.chart = TimeChart.TimeChart()
        self.chartView = TimeChart.TimeChartView(self.chart)

        row = 0
        col = 0
        self.commandLayout.addWidget(QLabel("Main"), row, col)
        self.commandLayout.addWidget(QLabel("Aux"), row, col + 2)
        self.commandLayout.addWidget(self.turnMainAOnButton, row + 1, col)
        self.commandLayout.addWidget(self.turnMainAOffButton, row + 1, col + 1)
        self.commandLayout.addWidget(self.turnAuxAOnButton, row + 1, col + 2)
        self.commandLayout.addWidget(self.turnAuxAOffButton, row + 1, col + 3)
        self.commandLayout.addWidget(self.turnMainBOnButton, row + 2, col)
        self.commandLayout.addWidget(self.turnMainBOffButton, row + 2, col + 1)
        self.commandLayout.addWidget(self.turnAuxBOnButton, row + 2, col + 2)
        self.commandLayout.addWidget(self.turnAuxBOffButton, row + 2, col + 3)
        self.commandLayout.addWidget(self.turnMainCOnButton, row + 3, col)
        self.commandLayout.addWidget(self.turnMainCOffButton, row + 3, col + 1)
        self.commandLayout.addWidget(self.turnAuxCOnButton, row + 3, col + 2)
        self.commandLayout.addWidget(self.turnAuxCOffButton, row + 3, col + 3)
        self.commandLayout.addWidget(self.turnMainDOnButton, row + 4, col)
        self.commandLayout.addWidget(self.turnMainDOffButton, row + 4, col + 1)
        self.commandLayout.addWidget(self.turnAuxDOnButton, row + 4, col + 2)
        self.commandLayout.addWidget(self.turnAuxDOffButton, row + 4, col + 3)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Main (ON/OFF)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Aux (ON/OFF)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Current (A)"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Power Network A"), row, col)
        self.dataLayout.addWidget(self.powerNetworkACommandedOnLabel, row, col + 1)
        self.dataLayout.addWidget(self.auxPowerNetworkACommandedOnLabel, row, col + 2)
        self.dataLayout.addWidget(self.powerNetworkACurrentLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Power Network B"), row, col)
        self.dataLayout.addWidget(self.powerNetworkBCommandedOnLabel, row, col + 1)
        self.dataLayout.addWidget(self.auxPowerNetworkBCommandedOnLabel, row, col + 2)
        self.dataLayout.addWidget(self.powerNetworkBCurrentLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Power Network C"), row, col)
        self.dataLayout.addWidget(self.powerNetworkCCommandedOnLabel, row, col + 1)
        self.dataLayout.addWidget(self.auxPowerNetworkCCommandedOnLabel, row, col + 2)
        self.dataLayout.addWidget(self.powerNetworkCCurrentLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Power Network D"), row, col)
        self.dataLayout.addWidget(self.powerNetworkDCommandedOnLabel, row, col + 1)
        self.dataLayout.addWidget(self.auxPowerNetworkDCommandedOnLabel, row, col + 2)
        self.dataLayout.addWidget(self.powerNetworkDCurrentLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Light Network"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-"), row, col + 2)
        self.dataLayout.addWidget(self.lightPowerNetworkCurrentLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Controls Network"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-"), row, col + 2)
        self.dataLayout.addWidget(self.controlsPowerNetworkCurrentLabel, row, col + 3)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("RCP Utility 220VAC 1 Status"), row, col)
        self.warningLayout.addWidget(self.rcpMirrorCellUtility220VAC1StatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("RCP Utility 220VAC 2 Status"), row, col)
        self.warningLayout.addWidget(self.rcpMirrorCellUtility220VAC2StatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("RCP Utility 220VAC 3 Status"), row, col)
        self.warningLayout.addWidget(self.rcpMirrorCellUtility220VAC3StatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("RCP Cabinet Utility 220VAC Status"), row, col)
        self.warningLayout.addWidget(self.rcpCabinetUtility220VACStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("RCP External Equipment 220VAC Status"), row, col)
        self.warningLayout.addWidget(self.rcpExternalEquipment220VACStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("A Redundancy Control Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkARedundancyControlStatusLabel, row, col + 1)
        
        row = 1
        col = 2
        self.warningLayout.addWidget(QLabel("B Redundancy Control Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkBRedundancyControlStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("C Redundancy Control Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkCRedundancyControlStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("D Redundancy Control Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkDRedundancyControlStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Controls Redundancy Control Status"), row, col)
        self.warningLayout.addWidget(self.controlsPowerNetworkRedundancyControlStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("A Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkAStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("A Redundant Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkARedundantStatusLabel, row, col + 1)
        
        row = 1
        col = 4
        self.warningLayout.addWidget(QLabel("B Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkBStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("B Redundant Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkBRedundantStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("C Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkCStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("C Redundant Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkCRedundantStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("D Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkDStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("D Redundant Status"), row, col)
        self.warningLayout.addWidget(self.powerNetworkDRedundantStatusLabel, row, col + 1)
        
        row = 1
        col = 6
        self.warningLayout.addWidget(QLabel("Controls Status"), row, col)
        self.warningLayout.addWidget(self.controlsPowerNetworkStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Controls Redundant Status"), row, col)
        self.warningLayout.addWidget(self.controlsPowerNetworkRedundantStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Light Status"), row, col)
        self.warningLayout.addWidget(self.lightPowerNetworkStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("External Equipment Status"), row, col)
        self.warningLayout.addWidget(self.externalEquipmentPowerNetworkStatusLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Laser Tracker Status"), row, col)
        self.warningLayout.addWidget(self.laserTrackerPowerNetworkStatusLabel, row, col + 1)

        self.plotLayout.addWidget(self.chartView)

        self.dataEventPowerWarning = DataCache()
        self.dataEventPowerStatus = DataCache()
        self.dataTelemetryPowerSupplyData = DataCache()
        
        self.MTM1M3.subscribeEvent_powerWarning(self.processEventPowerWarning)
        self.MTM1M3.subscribeEvent_powerStatus(self.processEventPowerStatus)
        self.MTM1M3.subscribeTelemetry_powerSupplyData(self.processTelemetryPowerSupplyData)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventPowerWarning.hasBeenUpdated():
            data = self.dataEventPowerWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            #TODO QTHelpers.setWarningLabel(self.rcpMirrorCellUtility220VAC1StatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.RCPMirrorCellUtility220VAC1Status))
            #TODO QTHelpers.setWarningLabel(self.rcpCabinetUtility220VACStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.RCPCabinetUtility220VACStatus))
            #TODO QTHelpers.setWarningLabel(self.rcpExternalEquipment220VACStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.RCPExternalEquipment220VACStatus))
            #TODO QTHelpers.setWarningLabel(self.rcpMirrorCellUtility220VAC2StatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.RCPMirrorCellUtility220VAC2Status))
            #TODO QTHelpers.setWarningLabel(self.rcpMirrorCellUtility220VAC3StatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.RCPMirrorCellUtility220VAC3Status))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkARedundancyControlStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkARedundancyControlStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkBRedundancyControlStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkBRedundancyControlStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkCRedundancyControlStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkCRedundancyControlStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkDRedundancyControlStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkDRedundancyControlStatus))
            #TODO QTHelpers.setWarningLabel(self.controlsPowerNetworkRedundancyControlStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.ControlsPowerNetworkRedundancyControlStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkAStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkAStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkARedundantStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkARedundantStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkBStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkBStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkBRedundantStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkBRedundantStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkCStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkCStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkCRedundantStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkCRedundantStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkDStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkDStatus))
            #TODO QTHelpers.setWarningLabel(self.powerNetworkDRedundantStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.PowerNetworkDRedundantStatus))
            #TODO QTHelpers.setWarningLabel(self.controlsPowerNetworkStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.ControlsPowerNetworkStatus))
            #TODO QTHelpers.setWarningLabel(self.controlsPowerNetworkRedundantStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.ControlsPowerNetworkRedundantStatus))
            #TODO QTHelpers.setWarningLabel(self.lightPowerNetworkStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.LightPowerNetworkStatus))
            #TODO QTHelpers.setWarningLabel(self.externalEquipmentPowerNetworkStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.ExternalEquipmentPowerNetworkStatus))
            #TODO QTHelpers.setWarningLabel(self.laserTrackerPowerNetworkStatusLabel, BitHelper.get(data.powerSystemFlags, PowerSystemFlags.LaserTrackerPowerNetworkStatus))

        if self.dataEventPowerStatus.hasBeenUpdated():
            data = self.dataEventPowerStatus.get()
            QTHelpers.setBoolLabelOnOff(self.powerNetworkACommandedOnLabel, data.powerNetworkACommandedOn)
            QTHelpers.setBoolLabelOnOff(self.powerNetworkBCommandedOnLabel, data.powerNetworkBCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.powerNetworkCCommandedOnLabel, data.powerNetworkCCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.powerNetworkDCommandedOnLabel, data.powerNetworkDCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.auxPowerNetworkACommandedOnLabel, data.auxPowerNetworkACommandedOn)
            QTHelpers.setBoolLabelOnOff(self.auxPowerNetworkBCommandedOnLabel, data.auxPowerNetworkBCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.auxPowerNetworkCCommandedOnLabel, data.auxPowerNetworkCCommandedOn)
            QTHelpers.setBoolLabelOnOff(self.auxPowerNetworkDCommandedOnLabel, data.auxPowerNetworkDCommandedOn)

        if self.dataTelemetryPowerSupplyData.hasBeenUpdated():
            data = self.dataTelemetryPowerSupplyData.get()
            self.powerNetworkACurrentLabel.setText("%0.3f" % data.powerNetworkACurrent)
            self.powerNetworkBCurrentLabel.setText("%0.3f" % data.powerNetworkBCurrent)
            self.powerNetworkCCurrentLabel.setText("%0.3f" % data.powerNetworkCCurrent)
            self.powerNetworkDCurrentLabel.setText("%0.3f" % data.powerNetworkDCurrent)
            self.lightPowerNetworkCurrentLabel.setText("%0.3f" % data.lightPowerNetworkCurrent)
            self.controlsPowerNetworkCurrentLabel.setText("%0.3f" % data.controlsPowerNetworkCurrent)

    def issueCommandTurnMainAOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(True, False, False, False, False, False, False, False)

    def issueCommandTurnMainAOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(True, False, False, False, False, False, False, False)

    def issueCommandTurnMainBOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, True, False, False, False, False, False, False)

    def issueCommandTurnMainBOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, True, False, False, False, False, False, False)

    def issueCommandTurnMainCOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, True, False, False, False, False, False)

    def issueCommandTurnMainCOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, True, False, False, False, False, False)

    def issueCommandTurnMainDOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, False, True, False, False, False, False)

    def issueCommandTurnMainDOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, False, True, False, False, False, False)

    def issueCommandTurnAuxAOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, False, False, True, False, False, False)

    def issueCommandTurnAuxAOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, False, False, True, False, False, False)

    def issueCommandTurnAuxBOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, False, False, False, True, False, False)

    def issueCommandTurnAuxBOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, False, False, False, True, False, False)

    def issueCommandTurnAuxCOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, False, False, False, False, True, False)

    def issueCommandTurnAuxCOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, False, False, False, False, True, False)

    def issueCommandTurnAuxDOn(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOn(False, False, False, False, False, False, False, True)

    def issueCommandTurnAuxDOff(self):
        self.MTM1M3.issueCommandThenWait_turnPowerOff(False, False, False, False, False, False, False, True)

    def processEventPowerWarning(self, data):
        self.dataEventPowerWarning.set(data[-1])

    def processEventPowerStatus(self, data):
        self.dataEventPowerStatus.set(data[-1])

    def processTelemetryPowerSupplyData(self, data):
        self.chart.append('Current (A)', 'A', [(x.timestamp, x.powerNetworkACurrent) for x in data])
        self.chart.append('Current (A)', 'B', [(x.timestamp, x.powerNetworkBCurrent) for x in data])
        self.chart.append('Current (A)', 'C', [(x.timestamp, x.powerNetworkCCurrent) for x in data])
        self.chart.append('Current (A)', 'D', [(x.timestamp, x.powerNetworkDCurrent) for x in data])
        self.chart.append('Current (A)', 'Lights', [(x.timestamp, x.lightPowerNetworkCurrent) for x in data])
        self.chart.append('Current (A)', 'Controls', [(x.timestamp, x.controlsPowerNetworkCurrent) for x in data])
        self.dataTelemetryPowerSupplyData.set(data[-1])
