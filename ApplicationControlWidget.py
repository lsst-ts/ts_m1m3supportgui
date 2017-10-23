
import QTHelpers
from MTM1M3Enumerations import DetailedStates
from PySide2.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout)

class ApplicationControlWidget(QWidget):
    def __init__(self, mtm1m3):
        QWidget.__init__(self)
        self.mtm1m3 = mtm1m3
        self.label = QLabel("Application Control")
        self.button1 = QPushButton("Button1")
        QTHelpers.updateSizePolicy(self.button1)
        self.button1.clicked.connect(QTHelpers.doNothing)
        self.button2 = QPushButton("Button2")
        QTHelpers.updateSizePolicy(self.button2)
        self.button2.clicked.connect(QTHelpers.doNothing)
        self.button3 = QPushButton("Button3")
        QTHelpers.updateSizePolicy(self.button3)
        self.button3.clicked.connect(QTHelpers.doNothing)
        self.button4 = QPushButton("Button4")
        QTHelpers.updateSizePolicy(self.button4)
        self.button4.clicked.connect(QTHelpers.doNothing)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.setLayout(self.layout)
        self.mtm1m3.subscribeEvent_detailedState(self.processEventDetailedState)

    def issueCommandStart(self):
        self.mtm1m3.issueCommandThenWait_start("Simulator")

    def issueCommandEnable(self):
        self.mtm1m3.issueCommandThenWait_enable(False)

    def issueCommandRaiseM1M3(self):
        self.mtm1m3.issueCommandThenWait_raiseM1M3(False)

    def issueCommandAbortRaiseM1M3(self):
        self.mtm1m3.issueCommandThenWait_abortRaiseM1M3(False)

    def issueCommandLowerM1M3(self):
        self.mtm1m3.issueCommandThenWait_lowerM1M3(False)

    def issueCommandEnterEngineering(self):
        self.mtm1m3.issueCommandThenWait_enterEngineering(False)

    def issueCommandExitEngineering(self):
        self.mtm1m3.issueCommandThenWait_exitEngineering(False)

    def issueCommandDisable(self):
        self.mtm1m3.issueCommandThenWait_disable(False)

    def issueCommandStandby(self):
        self.mtm1m3.issueCommandThenWait_standby(False)

    def issueCommandShutdown(self):
        self.mtm1m3.issueCommandThenWait_shutdown(False)

    def processEventDetailedState(self, data):
        state = data[len(data) - 1].detailedState
        if state == DetailedStates.StandbyState:
            QTHelpers.updateButton(self.button1, "Start", self.issueCommandStart)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Shutdown", self.issueCommandShutdown)
        elif state == DetailedStates.DisabledState:
            QTHelpers.updateButton(self.button1, "Enable", self.issueCommandEnable)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Standby", self.issueCommandStandby)
        elif state == DetailedStates.EnabledState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Disable", self.issueCommandDisable)
        elif state == DetailedStates.ParkedState:
            QTHelpers.updateButton(self.button1, "Raise M1M3", self.issueCommandRaiseM1M3)
            QTHelpers.updateButton(self.button2, "Enter Engineering", self.issueCommandEnterEngineering)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Disable", self.issueCommandDisable)
        elif state == DetailedStates.RaisingState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Abort Raise M1M3", self.issueCommandAbortRaiseM1M3)
        elif state == DetailedStates.ActiveState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.updateButton(self.button2, "Enter Engineering", self.issueCommandEnterEngineering)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Lower M1M3", self.issueCommandLowerM1M3) 
        elif state == DetailedStates.LoweringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.hideButton(self.button4)
        elif state == DetailedStates.ParkedEngineeringState:
            QTHelpers.updateButton(self.button1, "Raise M1M3", self.issueCommandRaiseM1M3)
            QTHelpers.hideButton(self.button2)
            QTHelpers.updateButton(self.button3, "Exit Engineering", self.issueCommandExitEngineering)
            QTHelpers.updateButton(self.button4, "Disable", self.issueCommandDisable)    
        elif state == DetailedStates.RaisingEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Abort Raise M1M3", self.issueCommandAbortRaiseM1M3)
        elif state == DetailedStates.ActiveEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.updateButton(self.button3, "Exit Engineering", self.issueCommandExitEngineering)
            QTHelpers.updateButton(self.button4, "Lower M1M3", self.issueCommandLowerM1M3)    
        elif state == DetailedStates.LoweringEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.hideButton(self.button4)
        elif state == DetailedStates.FaultState or state == DetailedStates.LoweringFaultState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Standby", self.issueCommandStandby)