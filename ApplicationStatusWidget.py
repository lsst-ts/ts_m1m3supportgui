from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot, Qt
from lsst.ts.salobj import State
from lsst.ts.idl.enums import MTM1M3
from SALComm import SALComm
import QTHelpers


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
    def forceActuatorState(self, data):
        detailedData = self.comm.MTM1M3.evt_detailedState.get()
        if detailedData is None:
            return
        if (
            detailedData.detailedState == MTM1M3.DetailedState.RAISING
            or detailedData.detailedState == MTM1M3.DetailedState.RAISINGENGINEERING
        ):
            self.mirrorStateLabel.setText(
                f"Raising ({data.supportPercentage * 100:.02f} %)"
            )
        elif (
            detailedData.detailedState == MTM1M3.DetailedState.LOWERING
            or detailedData.detailedState == MTM1M3.DetailedState.LOWERINGENGINEERING
            or detailedData.detailedState == MTM1M3.DetailedState.LOWERINGFAULT
        ):
            self.mirrorStateLabel.setText(
                f"Lowering ({data.supportPercentage * 100:.02f} %)"
            )

    @Slot(map)
    def processEventDetailedState(self, data):
        modeStateText = "Unknown"
        mirrorStateText = "Unknown"
        if data.detailedState == MTM1M3.DetailedState.DISABLED:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == MTM1M3.DetailedState.FAULT:
            modeStateText = "Automatic"
            mirrorStateText = "Fault"
        elif data.detailedState == MTM1M3.DetailedState.OFFLINE:
            modeStateText = "Offline"
            mirrorStateText = "Parked"
        elif data.detailedState == MTM1M3.DetailedState.STANDBY:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == MTM1M3.DetailedState.PARKED:
            modeStateText = "Automatic"
            mirrorStateText = "Parked"
        elif data.detailedState == MTM1M3.DetailedState.RAISING:
            modeStateText = "Automatic"
            mirrorStateText = f"Raising ({self.comm.MTM1M3.evt_forceActuatorState.get().supportPercentage * 100:.03f}%)"
            self.comm.forceActuatorState.connect(
                self.forceActuatorState, Qt.UniqueConnection
            )
        elif data.detailedState == MTM1M3.DetailedState.ACTIVE:
            modeStateText = "Automatic"
            mirrorStateText = "Active"
            self.forceActuatorState.disconnect(self.forceActuatorState)
        elif data.detailedState == MTM1M3.DetailedState.LOWERING:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering"
        elif data.detailedState == MTM1M3.DetailedState.PARKEDENGINEERING:
            modeStateText = "Manual"
            mirrorStateText = "Parked"
        elif data.detailedState == MTM1M3.DetailedState.RAISINGENGINEERING:
            modeStateText = "Manual"
            mirrorStateText = "Raising"
        elif data.detailedState == MTM1M3.DetailedState.ACTIVEENGINEERING:
            modeStateText = "Manual"
            mirrorStateText = "Active"
        elif data.detailedState == MTM1M3.DetailedState.LOWERINGENGINEERING:
            modeStateText = "Manual"
            mirrorStateText = "Lowering"
        elif data.detailedState == MTM1M3.DetailedState.LOWERINGFAULT:
            modeStateText = "Automatic"
            mirrorStateText = "Lowering (fault)"
        elif data.detailedState == MTM1M3.DetailedState.PROFILEHARDPOINTCORRECTIONS:
            modeStateText = "Profile hardpoint corrections"
            mirrorStateText = "Active"
        else:
            QTHelpers.warning(
                self, "Unknow state", f"Unknow state received - {data.detailedState}"
            )
            return

        self.modeStateLabel.setText(modeStateText)
        self.mirrorStateLabel.setText(mirrorStateText)
