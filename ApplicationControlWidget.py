# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org). See the COPYRIGHT file at the top - level directory
# of this distribution for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

import QTHelpers
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PySide2.QtCore import Slot

from asyncqt import asyncSlot
import asyncio

from lsst.ts.salobj import base
from lsst.ts.idl.enums.MTM1M3 import DetailedState


class ApplicationControlWidget(QWidget):
    """Widget with control buttons for M1M3 operations. Buttons are disabled/enabled and reasonable defaults sets on DetailedState changes."""

    TEXT_START = "&Start"
    """Constants for button titles. Titles are used to select command send to SAL."""
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
        self.lastEnabled = None
        self.commandLayout = QVBoxLayout()
        self.setLayout(self.commandLayout)

        def _addButton(text, onClick, default=False):
            button = QPushButton(text)
            button.clicked.connect(onClick)
            button.setEnabled(False)
            button.setAutoDefault(default)
            return button

        self.startButton = _addButton(self.TEXT_START, self.start, True)
        self.enableButton = _addButton(self.TEXT_ENABLE, self.enable, True)
        self.raiseButton = _addButton(self.TEXT_RAISE, self.raiseControl, True)
        self.engineeringButton = _addButton(
            self.TEXT_ENTER_ENGINEERING, self.engineering
        )
        self.exitButton = _addButton(self.TEXT_STANDBY, self.exit)

        self.commandLayout.addWidget(self.startButton)
        self.commandLayout.addWidget(self.enableButton)
        self.commandLayout.addWidget(self.raiseButton)
        self.commandLayout.addWidget(self.engineeringButton)
        self.commandLayout.addWidget(self.exitButton)

        # connect SAL signals
        self.comm.detailedState.connect(self.processEventDetailedState)

    def disableAllButtons(self):
        if self.lastEnabled is None:
            self.lastEnabled = [
                self.startButton.isEnabled(),
                self.enableButton.isEnabled(),
                self.raiseButton.isEnabled(),
                self.engineeringButton.isEnabled(),
                self.exitButton.isEnabled(),
            ]
        self.startButton.setEnabled(False)
        self.enableButton.setEnabled(False)
        self.raiseButton.setEnabled(False)
        self.engineeringButton.setEnabled(False)
        self.exitButton.setEnabled(False)

    def restoreEnabled(self):
        self.startButton.setEnabled(self.lastEnabled[0])
        self.enableButton.setEnabled(self.lastEnabled[1])
        self.raiseButton.setEnabled(self.lastEnabled[2])
        self.engineeringButton.setEnabled(self.lastEnabled[3])
        self.exitButton.setEnabled(self.lastEnabled[4])
        self.lastEnabled = None

    async def command(self, button):
        self.disableAllButtons()
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
            await QTHelpers.warning(
                self, f"Error executing {button.text()}", ackE.ackcmd.result,
            )
            self.restoreEnabled()

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

    def _setTextEnable(self, button, text):
        button.setText(text)
        button.setEnabled(True)

    @Slot(map)
    def processEventDetailedState(self, data):
        self.lastEnabled = None
        if data.detailedState == DetailedState.DISABLED:
            self.raiseButton.setEnabled(False)
            self.engineeringButton.setEnabled(False)
            self._setTextEnable(self.enableButton, self.TEXT_ENABLE)
            self._setTextEnable(self.exitButton, self.TEXT_STANDBY)
            self.enableButton.setDefault(True)
        elif data.detailedState == DetailedState.FAULT:
            self._setTextEnable(self.startButton, self.TEXT_STANDBY)
            self.startButton.setDefault(True)
        elif data.detailedState == DetailedState.OFFLINE:
            self.startButton.setEnabled(False)
        elif data.detailedState == DetailedState.STANDBY:
            self.enableButton.setEnabled(False)
            self._setTextEnable(self.startButton, self.TEXT_START)
            self._setTextEnable(self.exitButton, self.TEXT_EXIT_CONTROL)
            self.startButton.setDefault(True)
        elif data.detailedState == DetailedState.PARKED:
            self._setTextEnable(self.enableButton, self.TEXT_DISABLE)
            self._setTextEnable(self.raiseButton, self.TEXT_RAISE)
            self._setTextEnable(self.engineeringButton, self.TEXT_ENTER_ENGINEERING)
            self.exitButton.setEnabled(False)
            self.raiseButton.setDefault(True)
        elif data.detailedState == DetailedState.RAISING:
            self._setTextEnable(self.raiseButton, self.TEXT_ABORT_RAISE)
            self.engineeringButton.setEnabled(False)
            self.raiseButton.setDefault(True)
        elif data.detailedState == DetailedState.ACTIVE:
            self._setTextEnable(self.raiseButton, self.TEXT_LOWER)
            self._setTextEnable(self.engineeringButton, self.TEXT_ENTER_ENGINEERING)
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
            self._setTextEnable(self.engineeringButton, self.TEXT_EXIT_ENGINEERING)
        elif data.detailedState == DetailedState.LOWERINGENGINEERING:
            pass
        elif data.detailedState == DetailedState.LOWERINGFAULT:
            self._setTextEnable(self.exitButton, self.TEXT_STANDBY)
        elif data.detailedState == DetailedState.PROFILEHARDPOINTCORRECTIONS:
            pass
        else:
            print(f"Unhandled detailed state {data.detailedState}")
