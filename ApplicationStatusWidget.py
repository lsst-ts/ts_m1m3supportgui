
from MTM1M3Enumerations import SummaryStates, DetailedStates
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout

class ApplicationStatusWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.statusLayout = QGridLayout()
        self.layout.addLayout(self.statusLayout)
        self.setLayout(self.layout)

        self.summaryStateLabel = QLabel("Offline")
        self.modeStateLabel = QLabel("Automatic")
        self.mirrorStateLabel = QLabel("Parked")

        row = 0
        col = 0
        self.statusLayout.addWidget(QLabel("State"), row, col)
        self.statusLayout.addWidget(self.summaryStateLabel, row, col + 1)
        row += 1
        self.statusLayout.addWidget(QLabel("Mode"), row, col)
        self.statusLayout.addWidget(self.modeStateLabel, row, col + 1)
        row += 1
        self.statusLayout.addWidget(QLabel("Mirror State"), row, col)
        self.statusLayout.addWidget(self.mirrorStateLabel, row, col + 1)
        
        self.MTM1M3.subscribeEvent_summaryState(self.processEventSummaryState)
        self.MTM1M3.subscribeEvent_detailedState(self.processEventDetailedState)

    def processEventSummaryState(self, data):
        summaryState = data[-1].summaryState
        summaryStateText = "Unknown"
        if summaryState == SummaryStates.DisabledState:
            summaryStateText = "Disabled"
        elif summaryState == SummaryStates.EnabledState:
            summaryStateText = "Enabled"
        elif summaryState == SummaryStates.FaultState:
            summaryStateText = "Fault"
        elif summaryState == SummaryStates.OfflineState:
            summaryStateText = "Offline"
        elif summaryState == SummaryStates.StandbyState:
            summaryStateText = "Standby"

        self.summaryStateLabel.setText(summaryStateText)

    def processEventDetailedState(self, data):
        detailedState = data[-1].detailedState
        modeStateText = "Unknown"
        mirrorStateText = "Unknown"
        if detailedState == DetailedStates.DisabledState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.EnabledState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.FaultState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.OfflineState:
            modeStateText = "Offline"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.StandbyState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.ParkedState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.RaisingState:
            modeStateText = "Automatic"
            mirrorStateText = "Raising"
        elif detailedState == DetailedStates.ActiveState:
            modeStateText = "Automatic"
            mirrorStateText = "Active"
        elif detailedState == DetailedStates.LoweringState:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering"
        elif detailedState == DetailedStates.ParkedEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Parked"
        elif detailedState == DetailedStates.RaisingEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Raising"
        elif detailedState == DetailedStates.ActiveEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Active"
        elif detailedState == DetailedStates.LoweringEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Lowering"
        elif detailedState == DetailedStates.LoweringFaultState:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering"

        self.modeStateLabel.setText(modeStateText)
        self.mirrorStateLabel.setText(mirrorStateText)