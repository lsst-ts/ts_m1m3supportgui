# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Generated from MTM1M3_Events, MTM1M3_Telemetry and MTMount_Telemetry

from PySide2.QtCore import QObject, Signal
from lsst.ts.salobj import Domain, Remote

class SALComm(QObject):
    """
    SAL proxy. Set callback to emit Qt signals.
    """

    # M1M3 event signals
    accelerometerWarning = Signal(map)
    airSupplyStatus = Signal(map)
    airSupplyWarning = Signal(map)
    appliedAberrationForces = Signal(map)
    appliedAccelerationForces = Signal(map)
    appliedActiveOpticForces = Signal(map)
    appliedAzimuthForces = Signal(map)
    appliedBalanceForces = Signal(map)
    appliedCylinderForces = Signal(map)
    appliedElevationForces = Signal(map)
    appliedForces = Signal(map)
    appliedOffsetForces = Signal(map)
    appliedStaticForces = Signal(map)
    appliedThermalForces = Signal(map)
    appliedVelocityForces = Signal(map)
    cellLightStatus = Signal(map)
    cellLightWarning = Signal(map)
    commandRejectionWarning = Signal(map)
    detailedState = Signal(map)
    displacementSensorWarning = Signal(map)
    forceActuatorForceWarning = Signal(map)
    forceActuatorInfo = Signal(map)
    forceActuatorState = Signal(map)
    forceActuatorWarning = Signal(map)
    forceSetpointWarning = Signal(map)
    gyroWarning = Signal(map)
    hardpointActuatorInfo = Signal(map)
    hardpointActuatorState = Signal(map)
    hardpointActuatorWarning = Signal(map)
    hardpointMonitorInfo = Signal(map)
    hardpointMonitorState = Signal(map)
    hardpointMonitorWarning = Signal(map)
    heartbeat = Signal(map)
    ilcWarning = Signal(map)
    inclinometerSensorWarning = Signal(map)
    interlockStatus = Signal(map)
    interlockWarning = Signal(map)
    modbusResponse = Signal(map)
    pidInfo = Signal(map)
    powerStatus = Signal(map)
    powerSupplyStatus = Signal(map)
    powerWarning = Signal(map)
    preclippedAberrationForces = Signal(map)
    preclippedAccelerationForces = Signal(map)
    preclippedActiveOpticForces = Signal(map)
    preclippedAzimuthForces = Signal(map)
    preclippedBalanceForces = Signal(map)
    preclippedCylinderForces = Signal(map)
    preclippedElevationForces = Signal(map)
    preclippedForces = Signal(map)
    preclippedOffsetForces = Signal(map)
    preclippedStaticForces = Signal(map)
    preclippedThermalForces = Signal(map)
    preclippedVelocityForces = Signal(map)
    summaryState = Signal(map)

    # M1M3 telemetry signals
    accelerometerData = Signal(map)
    forceActuatorData = Signal(map)
    gyroData = Signal(map)
    hardpointActuatorData = Signal(map)
    hardpointMonitorData = Signal(map)
    imsData = Signal(map)
    inclinometerData = Signal(map)
    outerLoopData = Signal(map)
    pidData = Signal(map)
    powerSupplyData = Signal(map)

    # MTMount telemetry signals
    Azimuth = Signal(map)
    Elevation = Signal(map)

    def __init__(self):
        super().__init__()
        self.domain = Domain()
        self.MTM1M3 = Remote(self.domain, "MTM1M3")
        self.MTMount = Remote(self.domain, "MTMount")

        self.MTM1M3.evt_accelerometerWarning.callback = self.accelerometerWarning.emit
        self.MTM1M3.evt_airSupplyStatus.callback = self.airSupplyStatus.emit
        self.MTM1M3.evt_airSupplyWarning.callback = self.airSupplyWarning.emit
        self.MTM1M3.evt_appliedAberrationForces.callback = self.appliedAberrationForces.emit
        self.MTM1M3.evt_appliedAccelerationForces.callback = self.appliedAccelerationForces.emit
        self.MTM1M3.evt_appliedActiveOpticForces.callback = self.appliedActiveOpticForces.emit
        self.MTM1M3.evt_appliedAzimuthForces.callback = self.appliedAzimuthForces.emit
        self.MTM1M3.evt_appliedBalanceForces.callback = self.appliedBalanceForces.emit
        self.MTM1M3.evt_appliedCylinderForces.callback = self.appliedCylinderForces.emit
        self.MTM1M3.evt_appliedElevationForces.callback = self.appliedElevationForces.emit
        self.MTM1M3.evt_appliedForces.callback = self.appliedForces.emit
        self.MTM1M3.evt_appliedOffsetForces.callback = self.appliedOffsetForces.emit
        self.MTM1M3.evt_appliedStaticForces.callback = self.appliedStaticForces.emit
        self.MTM1M3.evt_appliedThermalForces.callback = self.appliedThermalForces.emit
        self.MTM1M3.evt_appliedVelocityForces.callback = self.appliedVelocityForces.emit
        self.MTM1M3.evt_cellLightStatus.callback = self.cellLightStatus.emit
        self.MTM1M3.evt_cellLightWarning.callback = self.cellLightWarning.emit
        self.MTM1M3.evt_commandRejectionWarning.callback = self.commandRejectionWarning.emit
        self.MTM1M3.evt_detailedState.callback = self.detailedState.emit
        self.MTM1M3.evt_displacementSensorWarning.callback = self.displacementSensorWarning.emit
        self.MTM1M3.evt_forceActuatorForceWarning.callback = self.forceActuatorForceWarning.emit
        self.MTM1M3.evt_forceActuatorInfo.callback = self.forceActuatorInfo.emit
        self.MTM1M3.evt_forceActuatorState.callback = self.forceActuatorState.emit
        self.MTM1M3.evt_forceActuatorWarning.callback = self.forceActuatorWarning.emit
        self.MTM1M3.evt_forceSetpointWarning.callback = self.forceSetpointWarning.emit
        self.MTM1M3.evt_gyroWarning.callback = self.gyroWarning.emit
        self.MTM1M3.evt_hardpointActuatorInfo.callback = self.hardpointActuatorInfo.emit
        self.MTM1M3.evt_hardpointActuatorState.callback = self.hardpointActuatorState.emit
        self.MTM1M3.evt_hardpointActuatorWarning.callback = self.hardpointActuatorWarning.emit
        self.MTM1M3.evt_hardpointMonitorInfo.callback = self.hardpointMonitorInfo.emit
        self.MTM1M3.evt_hardpointMonitorState.callback = self.hardpointMonitorState.emit
        self.MTM1M3.evt_hardpointMonitorWarning.callback = self.hardpointMonitorWarning.emit
        self.MTM1M3.evt_heartbeat.callback = self.heartbeat.emit
        self.MTM1M3.evt_ilcWarning.callback = self.ilcWarning.emit
        self.MTM1M3.evt_inclinometerSensorWarning.callback = self.inclinometerSensorWarning.emit
        self.MTM1M3.evt_interlockStatus.callback = self.interlockStatus.emit
        self.MTM1M3.evt_interlockWarning.callback = self.interlockWarning.emit
        self.MTM1M3.evt_modbusResponse.callback = self.modbusResponse.emit
        self.MTM1M3.evt_pidInfo.callback = self.pidInfo.emit
        self.MTM1M3.evt_powerStatus.callback = self.powerStatus.emit
        self.MTM1M3.evt_powerSupplyStatus.callback = self.powerSupplyStatus.emit
        self.MTM1M3.evt_powerWarning.callback = self.powerWarning.emit
        self.MTM1M3.evt_preclippedAberrationForces.callback = self.preclippedAberrationForces.emit
        self.MTM1M3.evt_preclippedAccelerationForces.callback = self.preclippedAccelerationForces.emit
        self.MTM1M3.evt_preclippedActiveOpticForces.callback = self.preclippedActiveOpticForces.emit
        self.MTM1M3.evt_preclippedAzimuthForces.callback = self.preclippedAzimuthForces.emit
        self.MTM1M3.evt_preclippedBalanceForces.callback = self.preclippedBalanceForces.emit
        self.MTM1M3.evt_preclippedCylinderForces.callback = self.preclippedCylinderForces.emit
        self.MTM1M3.evt_preclippedElevationForces.callback = self.preclippedElevationForces.emit
        self.MTM1M3.evt_preclippedForces.callback = self.preclippedForces.emit
        self.MTM1M3.evt_preclippedOffsetForces.callback = self.preclippedOffsetForces.emit
        self.MTM1M3.evt_preclippedStaticForces.callback = self.preclippedStaticForces.emit
        self.MTM1M3.evt_preclippedThermalForces.callback = self.preclippedThermalForces.emit
        self.MTM1M3.evt_preclippedVelocityForces.callback = self.preclippedVelocityForces.emit
        self.MTM1M3.evt_summaryState.callback = self.summaryState.emit

        self.MTM1M3.tel_accelerometerData.callback = self.accelerometerData.emit
        self.MTM1M3.tel_forceActuatorData.callback = self.forceActuatorData.emit
        self.MTM1M3.tel_gyroData.callback = self.gyroData.emit
        self.MTM1M3.tel_hardpointActuatorData.callback = self.hardpointActuatorData.emit
        self.MTM1M3.tel_hardpointMonitorData.callback = self.hardpointMonitorData.emit
        self.MTM1M3.tel_imsData.callback = self.imsData.emit
        self.MTM1M3.tel_inclinometerData.callback = self.inclinometerData.emit
        self.MTM1M3.tel_outerLoopData.callback = self.outerLoopData.emit
        self.MTM1M3.tel_pidData.callback = self.pidData.emit
        self.MTM1M3.tel_powerSupplyData.callback = self.powerSupplyData.emit

        self.MTMount.tel_Azimuth.callback = self.Azimuth.emit
        self.MTMount.tel_Elevation.callback = self.Elevation.emit
