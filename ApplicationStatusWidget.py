from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot
from lsst.ts.salobj import State
from SALComm import SALComm

class ApplicationStatusWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm
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

        self.comm.summaryState.connect(self.processEventSummaryState)
        self.comm.detailedState.connect(self.processEventDetailedState)

    @Slot(map)
    def processEventSummaryState(self, data):
        summaryStateText = "Unknown"
        if data.summaryState == State.DISABLED:
            summaryStateText = "Disabled"
        elif data.summaryState == State.ENABLED:
            summaryStateText = "Enabled"
        elif data.summaryState == State.FAULT:
            summaryStateText = "Fault"
        elif data.summaryState == State.OFFLINE:
            summaryStateText = "Offline"
        elif data.summaryState == State.STANDBY:
            summaryStateText = "Standby"

        self.summaryStateLabel.setText(summaryStateText)

    @Slot(map)
    def processEventDetailedState(self, data):
        modeStateText = "Unknown"
        mirrorStateText = "Unknown"
        if data.detailedState == 1: #DetailedStates.DisabledState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == 13: #DetailedStates.FaultState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        #elif data.detailedState == DetailedStates.OfflineState:
        #    modeStateText = "Offline"
        #    mirrorStateText = "Parked"
        elif data.detailedState == 4: #DetailedStates.StandbyState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == 5: #DetailedStates.ParkedState:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == 6: #DetailedStates.RaisingState:
            modeStateText = "Automatic"
            mirrorStateText = "Raising"
        elif data.detailedState == 7: #DetailedStates.ActiveState:
            modeStateText = "Automatic"
            mirrorStateText = "Active"
        elif data.detailedState == 8: #DetailedStates.LoweringState:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering"
        elif data.detailedState == 9: #DetailedStates.ParkedEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Parked"
        elif data.detailedState == 10: #DetailedStates.RaisingEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Raising"
        elif data.detailedState == 11: #DetailedStates.ActiveEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Active"
        elif data.detailedState == 12: #DetailedStates.LoweringEngineeringState:
            modeStateText = "Manual"
            mirrorStateText = "Lowering"
        elif data.detailedState == 13: #DetailedStates.LoweringFaultState:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering"

        self.modeStateLabel.setText(modeStateText)
        self.mirrorStateLabel.setText(mirrorStateText)
