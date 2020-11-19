import QTHelpers
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtCore import Slot

from asyncqt import asyncSlot
import asyncio

from lsst.ts.salobj import base
from lsst.ts.idl.enums.MTM1M3 import DetailedState


class ApplicationControlWidget(QWidget):

    TEXT_START = "&Start"
    TEXT_ENABLE = "&Enable"
    TEXT_DISABLE = "&Disable"
    TEXT_STANDBY = "&Standby"
    TEXT_RAISE = "&Raise M1M3"
    TEXT_ABORT_RAISE = "&Abort M1M3 Raise"
    TEXT_LOWER = "&Lower M1M3"
    TEXT_ENTER_ENGINEERING = "&Enter Engineering"
    TEXT_EXIT_ENGINEERING = "&Exit Engineering"
    TEXT_EXIT_CONTROL = "&Exit Control"

    def __init__(self, comm):
        super().__init__()

        self.comm = comm
        self.commandLayout = QVBoxLayout()
        self.setLayout(self.commandLayout)

        self.startButton = QPushButton(self.TEXT_START)
        self.startButton.setEnabled(False)
        self.startButton.clicked.connect(self.start)

        self.enableButton = QPushButton(self.TEXT_ENABLE)
        self.enableButton.setEnabled(False)
        self.enableButton.clicked.connect(self.enable)

        self.raiseButton = QPushButton(self.TEXT_RAISE)
        self.raiseButton.setEnabled(False)
        self.raiseButton.clicked.connect(self.raiseControl)

        self.engineeringButton = QPushButton(self.TEXT_ENTER_ENGINEERING)
        self.engineeringButton.setEnabled(False)
        self.engineeringButton.clicked.connect(self.engineering)

        self.exitButton = QPushButton(self.TEXT_STANDBY)
        self.exitButton.setEnabled(False)
        self.exitButton.clicked.connect(self.exit)

        self.commandLayout.addWidget(self.startButton)
        self.commandLayout.addWidget(self.enableButton)
        self.commandLayout.addWidget(self.raiseButton)
        self.commandLayout.addWidget(self.engineeringButton)
        self.commandLayout.addWidget(self.exitButton)

        # connect SAL signals
        self.comm.logMessage.connect(self.logMessage)
        self.comm.detailedState.connect(self.processEventDetailedState)

    async def command(self, button):
        button.setEnabled(False)
        try:
            if button.text() == self.TEXT_START:
                await self.comm.MTM1M3.cmd_start.set_start(
                    settingsToApply="Default", timeout=60
                )
            elif button.text() == self.TEXT_EXIT_CONTROL:
                await self.comm.MTM1M3.cmd_exitControl.start()
            elif button.text() == self.TEXT_ENABLE:
                await self.comm.MTM1M3.cmd_enable.start()
            elif button.text() == self.TEXT_DISABLE:
                await self.comm.MTM1M3.cmd_disable.start()
            elif button.text() == self.TEXT_RAISE:
                await self.comm.MTM1M3.cmd_raiseM1M3.set_start(
                    raiseM1M3=True, bypassReferencePosition=False
                )
            elif button.text() == self.TEXT_ABORT_RAISE:
                await self.comm.MTM1M3.cmd_abortRaiseM1M3.start()
            elif button.text() == self.TEXT_LOWER:
                await self.comm.MTM1M3.cmd_lowerM1M3.start()
            elif button.text() == self.TEXT_ENTER_ENGINEERING:
                await self.comm.MTM1M3.cmd_enterEngineering.start()
            elif button.text() == self.TEXT_EXIT_ENGINEERING:
                await self.comm.MTM1M3.cmd_exitEngineering.start()
            elif button.text() == self.TEXT_STANDBY:
                await self.comm.MTM1M3.cmd_standby.start()
        except base.AckError as ackE:
            print(str(ackE))
            button.setEnabled(True)

    @asyncSlot()
    async def start(self):
        await self.command(self.startButton)

    @asyncSlot()
    async def enable(self):
        await self.command(self.enableButton)

    @asyncSlot()
    async def raiseControl(self):
        await self.command(self.raiseButton)

    @asyncSlot()
    async def engineering(self):
        await self.command(self.engineeringButton)

    @asyncSlot()
    async def exit(self):
        await self.command(self.exitButton)

    def logMessage(self, data):
        print(
            f"{data.level} - {data.message} - {data.private_sndStamp} - {data.filePath} - {data.functionName} - {data.lineNumber}"
        )

    def _setTextEnable(self, button, text):
        button.setText(text)
        button.setEnabled(True)

    @Slot(map)
    def processEventDetailedState(self, data):
        if data.detailedState == DetailedState.DISABLED:
            self.raiseButton.setEnabled(False)
            self.engineeringButton.setEnabled(False)
            self._setTextEnable(self.enableButton, self.TEXT_ENABLE)
            self._setTextEnable(self.exitButton, self.TEXT_STANDBY)
        elif data.detailedState == DetailedState.FAULT:
            self._setTextEnable(self.startButton, self.TEXT_STANDBY)
        elif data.detailedState == DetailedState.OFFLINE:
            self.startButton.setEnabled(False)
        elif data.detailedState == DetailedState.STANDBY:
            self.enableButton.setEnabled(False)
            self._setTextEnable(self.startButton, self.TEXT_START)
            self._setTextEnable(self.exitButton, self.TEXT_EXIT_CONTROL)
        elif data.detailedState == DetailedState.PARKED:
            self._setTextEnable(self.enableButton, self.TEXT_DISABLE)
            self._setTextEnable(self.raiseButton, self.TEXT_RAISE)
            self._setTextEnable(self.engineeringButton, self.TEXT_ENTER_ENGINEERING)
        elif data.detailedState == DetailedState.RAISING:
            self._setTextEnable(self.raiseButton, self.TEXT_ABORT_RAISE)
            self.engineeringButton.setEnabled(False)
        elif data.detailedState == DetailedState.ACTIVE:
            self._setTextEnable(self.raiseButton, self.TEXT_LOWER)
            self.engineeringButton.setEnabled(True)
        elif data.detailedState == DetailedState.LOWERING:
            pass
        elif data.detailedState == DetailedState.PARKEDENGINEERING:
            self.enableButton.setEnabled(False)
            self._setTextEnable(self.raiseButton, self.TEXT_RAISE)
            self._setTextEnable(self.engineeringButton, self.TEXT_EXIT_ENGINEERING)
        elif data.detailedState == DetailedState.RAISINGENGINEERING:
            self._setTextEnable(self.raiseButton, self.TEXT_ABORT_RAISE)
            self.engineeringButton.setEnabled(False)
        elif data.detailedState == DetailedState.ACTIVEENGINEERING:
            self._setTextEnable(self.raiseButton, self.TEXT_LOWER)
            self.engineeringButton.setEnabled(True)
        elif data.detailedState == DetailedState.LOWERINGENGINEERING:
            pass
        elif data.detailedState == DetailedState.LOWERINGFAULT:
            self._setTextEnable(self.exitButton, self.TEXT_STANDBY)
        elif data.detailedState == DetailedState.PROFILEHARDPOINTCORRECTIONS:
            pass
        else:
            print(f"Unhandled detailed state {data.detailedState}")
