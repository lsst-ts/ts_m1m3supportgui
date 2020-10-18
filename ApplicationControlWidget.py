import QTHelpers
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtCore import Slot
from asyncqt import asyncSlot
from lsst.ts.salobj import State


class ApplicationControlWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.layout = QVBoxLayout()
        self.commandLayout = QVBoxLayout()
        self.layout.addLayout(self.commandLayout)
        self.setLayout(self.layout)

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

        self.commandLayout.addWidget(self.button1)
        self.commandLayout.addWidget(self.button2)
        self.commandLayout.addWidget(self.button3)
        self.commandLayout.addWidget(self.button4)

        QTHelpers.hideButton(self.button1)
        QTHelpers.hideButton(self.button2)
        QTHelpers.hideButton(self.button3)
        QTHelpers.hideButton(self.button4)

        # connect SAL signals
        self.comm.detailedState.connect(self.processEventDetailedState)

    @asyncSlot()
    async def issueCommandStart(self):
        await self.comm.MTM1M3.cmd_start.set_start(
            settingsToApply="Default", timeout=60
        )

    @asyncSlot()
    async def issueCommandEnable(self):
        await self.comm.MTM1M3.cmd_enable.start()

    @asyncSlot()
    async def issueCommandRaiseM1M3(self):
        await self.comm.MTM1M3.cmd_raiseM1M3.set_start(
            raiseM1M3=True, bypassReferencePosition=False
        )

    @asyncSlot()
    async def issueCommandAbortRaiseM1M3(self):
        await self.comm.MTM1M3.cmd_abortRaiseM1M3.start()

    @asyncSlot()
    async def issueCommandLowerM1M3(self):
        await self.comm.MTM1M3.cmd_lowerM1M3.start()

    @asyncSlot()
    async def issueCommandEnterEngineering(self):
        await self.comm.MTM1M3.cmd_enterEngineering.start()

    @asyncSlot()
    async def issueCommandExitEngineering(self):
        await self.comm.MTM1M3.cmd_exitEngineering.start()

    @asyncSlot()
    async def issueCommandDisable(self):
        await self.comm.MTM1M3.cmd_disable.start()

    @asyncSlot()
    async def issueCommandStandby(self):
        await self.comm.MTM1M3.cmd_standby.start()

    @asyncSlot()
    async def issueCommandExitControl(self):
        await self.comm.MTM1M3.cmd_exitControl.start()

    @Slot(map)
    def processEventDetailedState(self, data):
        if data.detailedState == 4:  # DetailedStates.StandbyState:
            QTHelpers.updateButton(self.button1, "Start", self.issueCommandStart)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(
                self.button4, "Exit Control", self.issueCommandExitControl
            )
        elif data.detailedState == 1:  # DetailedStates.DisabledState:
            QTHelpers.updateButton(self.button1, "Enable", self.issueCommandEnable)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Standby", self.issueCommandStandby)
        elif data.detailedState == 5:  # DetailedStates.ParkedState:
            QTHelpers.updateButton(
                self.button1, "Raise M1M3", self.issueCommandRaiseM1M3
            )
            QTHelpers.updateButton(
                self.button2, "Enter Engineering", self.issueCommandEnterEngineering
            )
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Disable", self.issueCommandDisable)
        elif data.detailedState == 6:  # DetailedStates.RaisingState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(
                self.button4, "Abort Raise M1M3", self.issueCommandAbortRaiseM1M3
            )
        elif data.detailedState == 7:  # DetailedStates.ActiveState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.updateButton(
                self.button2, "Enter Engineering", self.issueCommandEnterEngineering
            )
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(
                self.button4, "Lower M1M3", self.issueCommandLowerM1M3
            )
        elif data.detailedState == 8:  # DetailedStates.LoweringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.hideButton(self.button4)
        elif data.detailedState == 9:  # DetailedStates.ParkedEngineeringState:
            QTHelpers.updateButton(
                self.button1, "Raise M1M3", self.issueCommandRaiseM1M3
            )
            QTHelpers.hideButton(self.button2)
            QTHelpers.updateButton(
                self.button3, "Exit Engineering", self.issueCommandExitEngineering
            )
            QTHelpers.updateButton(self.button4, "Disable", self.issueCommandDisable)
        elif data.detailedState == 10:  # DetailedStates.RaisingEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(
                self.button4, "Abort Raise M1M3", self.issueCommandAbortRaiseM1M3
            )
        elif data.detailedState == 11:  # DetailedStates.ActiveEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.updateButton(
                self.button3, "Exit Engineering", self.issueCommandExitEngineering
            )
            QTHelpers.updateButton(
                self.button4, "Lower M1M3", self.issueCommandLowerM1M3
            )
        elif data.detailedState == 12:  # DetailedStates.LoweringEngineeringState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.hideButton(self.button4)
        elif (
            data.detailedState == 13
        ):  # DetailedStates.FaultState or data.detailedState == DetailedStates.LoweringFaultState:
            QTHelpers.hideButton(self.button1)
            QTHelpers.hideButton(self.button2)
            QTHelpers.hideButton(self.button3)
            QTHelpers.updateButton(self.button4, "Standby", self.issueCommandStandby)
