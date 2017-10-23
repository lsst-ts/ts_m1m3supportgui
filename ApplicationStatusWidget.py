
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout)

class ApplicationStatusWidget(QWidget):
    def __init__(self, mtm1m3):
        QWidget.__init__(self)
        self.mtm1m3 = mtm1m3
        self.mainLayout = QVBoxLayout()
        self.label = QLabel("Application Status")
        self.mainLayout.addWidget(self.label)
        self.gridLayout = QGridLayout()
        self.mainLayout.addLayout(self.gridLayout)     
        self.gridLayout.addWidget(QLabel("State"), 0, 0)
        self.detailedState = QLabel("Offline")
        self.gridLayout.addWidget(self.detailedState, 0, 1)
        self.gridLayout.addWidget(QLabel("B"), 1, 0)
        self.gridLayout.addWidget(QLabel("b"), 1, 1)
        self.gridLayout.addWidget(QLabel("C"), 0, 2)
        self.gridLayout.addWidget(QLabel("c"), 0, 3)
        self.setLayout(self.mainLayout)
        self.mtm1m3.subscribeEvent_detailedState(self.processEventDetailedState)

    def processEventDetailedState(self, data):
        state = data[len(data) - 1].detailedState
        states = ["Offline", "Disabled", "Enabled", "Fault", "Offline", "Standby", "Parked", "Raising", "Active", "Lowering", "Engineering", "Parked Engineering", "Raising Engineering", "Actve Engineering", "Lowering Engineering", "Lowering Fault"]
        self.detailedState.setText(states[state])