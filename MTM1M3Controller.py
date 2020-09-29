import time
from SALPY_MTM1M3 import *

class MTM1M3Controller:
    def __init__(self):
        self.sal = SAL_MTM1M3()
        self.sal.setDebugLevel(0)
        self.sal.salProcessor("MTM1M3_command_abort")
        self.sal.salProcessor("MTM1M3_command_enable")
        self.sal.salProcessor("MTM1M3_command_disable")
        self.sal.salProcessor("MTM1M3_command_standby")
        self.sal.salProcessor("MTM1M3_command_exitControl")
        self.sal.salProcessor("MTM1M3_command_start")
        self.sal.salProcessor("MTM1M3_command_enterControl")
        self.sal.salProcessor("MTM1M3_command_setValue")
        self.sal.salProcessor("MTM1M3_command_abortRaiseM1M3")
        self.sal.salProcessor("MTM1M3_command_applyAberrationForces")
        self.sal.salProcessor("MTM1M3_command_applyAberrationForcesByBendingModes")
        self.sal.salProcessor("MTM1M3_command_applyActiveOpticForces")
        self.sal.salProcessor("MTM1M3_command_applyActiveOpticForcesByBendingModes")
        self.sal.salProcessor("MTM1M3_command_applyOffsetForces")
        self.sal.salProcessor("MTM1M3_command_applyOffsetForcesByMirrorForce")
        self.sal.salProcessor("MTM1M3_command_clearAberrationForces")
        self.sal.salProcessor("MTM1M3_command_clearActiveOpticForces")
        self.sal.salProcessor("MTM1M3_command_clearOffsetForces")
        self.sal.salProcessor("MTM1M3_command_disableHardpointChase")
        self.sal.salProcessor("MTM1M3_command_disableHardpointCorrections")
        self.sal.salProcessor("MTM1M3_command_enableHardpointChase")
        self.sal.salProcessor("MTM1M3_command_enableHardpointCorrections")
        self.sal.salProcessor("MTM1M3_command_enterEngineering")
        self.sal.salProcessor("MTM1M3_command_exitEngineering")
        self.sal.salProcessor("MTM1M3_command_lowerM1M3")
        self.sal.salProcessor("MTM1M3_command_modbusTransmit")
        self.sal.salProcessor("MTM1M3_command_moveHardpointActuators")
        self.sal.salProcessor("MTM1M3_command_positionM1M3")
        self.sal.salProcessor("MTM1M3_command_programILC")
        self.sal.salProcessor("MTM1M3_command_raiseM1M3")
        self.sal.salProcessor("MTM1M3_command_resetPID")
        self.sal.salProcessor("MTM1M3_command_shutdown")
        self.sal.salProcessor("MTM1M3_command_stopHardpointMotion")
        self.sal.salProcessor("MTM1M3_command_testAir")
        self.sal.salProcessor("MTM1M3_command_testForceActuator")
        self.sal.salProcessor("MTM1M3_command_testHardpoint")
        self.sal.salProcessor("MTM1M3_command_translateM1M3")
        self.sal.salProcessor("MTM1M3_command_turnAirOff")
        self.sal.salProcessor("MTM1M3_command_turnAirOn")
        self.sal.salProcessor("MTM1M3_command_turnLightsOff")
        self.sal.salProcessor("MTM1M3_command_turnLightsOn")
        self.sal.salProcessor("MTM1M3_command_turnPowerOff")
        self.sal.salProcessor("MTM1M3_command_turnPowerOn")
        self.sal.salProcessor("MTM1M3_command_updatePID")

        self.sal.salEventPub("MTM1M3_logevent_settingVersions")
        self.sal.salEventPub("MTM1M3_logevent_errorCode")
        self.sal.salEventPub("MTM1M3_logevent_summaryState")
        self.sal.salEventPub("MTM1M3_logevent_appliedSettingsMatchStart")
        self.sal.salEventPub("MTM1M3_logevent_accelerometerWarning")
        self.sal.salEventPub("MTM1M3_logevent_airSupplyStatus")
        self.sal.salEventPub("MTM1M3_logevent_airSupplyWarning")
        self.sal.salEventPub("MTM1M3_logevent_appliedAberrationForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedAccelerationForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedActiveOpticForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedAzimuthForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedBalanceForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedCylinderForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedElevationForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedHardpointSteps")
        self.sal.salEventPub("MTM1M3_logevent_appliedOffsetForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedStaticForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedThermalForces")
        self.sal.salEventPub("MTM1M3_logevent_appliedVelocityForces")
        self.sal.salEventPub("MTM1M3_logevent_cellLightStatus")
        self.sal.salEventPub("MTM1M3_logevent_cellLightWarning")
        self.sal.salEventPub("MTM1M3_logevent_detailedState")
        self.sal.salEventPub("MTM1M3_logevent_displacementSensorWarning")
        self.sal.salEventPub("MTM1M3_logevent_forceActuatorInfo")
        self.sal.salEventPub("MTM1M3_logevent_forceActuatorState")
        self.sal.salEventPub("MTM1M3_logevent_forceActuatorWarning")
        self.sal.salEventPub("MTM1M3_logevent_gyroWarning")
        self.sal.salEventPub("MTM1M3_logevent_hardpointActuatorInfo")
        self.sal.salEventPub("MTM1M3_logevent_hardpointActuatorState")
        self.sal.salEventPub("MTM1M3_logevent_hardpointActuatorWarning")
        self.sal.salEventPub("MTM1M3_logevent_hardpointMonitorInfo")
        self.sal.salEventPub("MTM1M3_logevent_hardpointMonitorState")
        self.sal.salEventPub("MTM1M3_logevent_hardpointMonitorWarning")
        self.sal.salEventPub("MTM1M3_logevent_inclinometerSensorWarning")
        self.sal.salEventPub("MTM1M3_logevent_interlockStatus")
        self.sal.salEventPub("MTM1M3_logevent_interlockWarning")
        self.sal.salEventPub("MTM1M3_logevent_modbusResponse")
        self.sal.salEventPub("MTM1M3_logevent_modbusWarning")
        self.sal.salEventPub("MTM1M3_logevent_pidInfo")
        self.sal.salEventPub("MTM1M3_logevent_powerStatus")
        self.sal.salEventPub("MTM1M3_logevent_powerWarning")
        self.sal.salEventPub("MTM1M3_logevent_preclippedAberrationForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedAccelerationForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedActiveOpticForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedAzimuthForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedBalanceForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedCylinderForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedElevationForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedOffsetForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedStaticForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedThermalForces")
        self.sal.salEventPub("MTM1M3_logevent_preclippedVelocityForces")

        self.sal.salTelemetryPub("MTM1M3_accelerometerData")
        self.sal.salTelemetryPub("MTM1M3_forceActuatorData")
        self.sal.salTelemetryPub("MTM1M3_forceActuatorPressure")
        self.sal.salTelemetryPub("MTM1M3_gyroData")
        self.sal.salTelemetryPub("MTM1M3_hardpointActuatorData")
        self.sal.salTelemetryPub("MTM1M3_hardpointMonitorData")
        self.sal.salTelemetryPub("MTM1M3_imsData")
        self.sal.salTelemetryPub("MTM1M3_inclinometerData")
        self.sal.salTelemetryPub("MTM1M3_outerLoopData")
        self.sal.salTelemetryPub("MTM1M3_pidData")
        self.sal.salTelemetryPub("MTM1M3_powerData")

        self.commandSubscribers_abort = []
        self.commandSubscribers_enable = []
        self.commandSubscribers_disable = []
        self.commandSubscribers_standby = []
        self.commandSubscribers_exitControl = []
        self.commandSubscribers_start = []
        self.commandSubscribers_enterControl = []
        self.commandSubscribers_setValue = []
        self.commandSubscribers_abortRaiseM1M3 = []
        self.commandSubscribers_applyAberrationForces = []
        self.commandSubscribers_applyAberrationForcesByBendingModes = []
        self.commandSubscribers_applyActiveOpticForces = []
        self.commandSubscribers_applyActiveOpticForcesByBendingModes = []
        self.commandSubscribers_applyOffsetForces = []
        self.commandSubscribers_applyOffsetForcesByMirrorForce = []
        self.commandSubscribers_clearAberrationForces = []
        self.commandSubscribers_clearActiveOpticForces = []
        self.commandSubscribers_clearOffsetForces = []
        self.commandSubscribers_disableHardpointChase = []
        self.commandSubscribers_disableHardpointCorrections = []
        self.commandSubscribers_enableHardpointChase = []
        self.commandSubscribers_enableHardpointCorrections = []
        self.commandSubscribers_enterEngineering = []
        self.commandSubscribers_exitEngineering = []
        self.commandSubscribers_lowerM1M3 = []
        self.commandSubscribers_modbusTransmit = []
        self.commandSubscribers_moveHardpointActuators = []
        self.commandSubscribers_positionM1M3 = []
        self.commandSubscribers_programILC = []
        self.commandSubscribers_raiseM1M3 = []
        self.commandSubscribers_resetPID = []
        self.commandSubscribers_shutdown = []
        self.commandSubscribers_stopHardpointMotion = []
        self.commandSubscribers_testAir = []
        self.commandSubscribers_testForceActuator = []
        self.commandSubscribers_testHardpoint = []
        self.commandSubscribers_translateM1M3 = []
        self.commandSubscribers_turnAirOff = []
        self.commandSubscribers_turnAirOn = []
        self.commandSubscribers_turnLightsOff = []
        self.commandSubscribers_turnLightsOn = []
        self.commandSubscribers_turnPowerOff = []
        self.commandSubscribers_turnPowerOn = []
        self.commandSubscribers_updatePID = []

        self.topicsSubscribedToo = {}

    def close(self):
        time.sleep(1)
        self.sal.salShutdown()

    def flush(self, action):
        result, data = action()
        while result >= 0:
            result, data = action()
            
    def checkForSubscriber(self, action, subscribers):
        result, data = action()
        if result > 0:
            for subscriber in subscribers:
                subscriber(result, data)
            
    def runSubscriberChecks(self):
        for subscribedTopic in self.topicsSubscribedToo:
            action = self.topicsSubscribedToo[subscribedTopic][0]
            subscribers = self.topicsSubscribedToo[subscribedTopic][1]
            self.checkForSubscriber(action, subscribers)


    def acceptCommand_abort(self):
        data = MTM1M3_command_abortC()
        result = self.sal.acceptCommand_abort(data)
        return result, data

    def ackCommand_abort(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_abort(cmdId, ackCode, errorCode, description)

    def subscribeCommand_abort(self, action):
        self.commandSubscribers_abort.append(action)
        if "command_abort" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_abort"] = [self.acceptCommand_abort, self.commandSubscribers_abort]

    def acceptCommand_enable(self):
        data = MTM1M3_command_enableC()
        result = self.sal.acceptCommand_enable(data)
        return result, data

    def ackCommand_enable(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_enable(cmdId, ackCode, errorCode, description)

    def subscribeCommand_enable(self, action):
        self.commandSubscribers_enable.append(action)
        if "command_enable" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_enable"] = [self.acceptCommand_enable, self.commandSubscribers_enable]

    def acceptCommand_disable(self):
        data = MTM1M3_command_disableC()
        result = self.sal.acceptCommand_disable(data)
        return result, data

    def ackCommand_disable(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_disable(cmdId, ackCode, errorCode, description)

    def subscribeCommand_disable(self, action):
        self.commandSubscribers_disable.append(action)
        if "command_disable" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_disable"] = [self.acceptCommand_disable, self.commandSubscribers_disable]

    def acceptCommand_standby(self):
        data = MTM1M3_command_standbyC()
        result = self.sal.acceptCommand_standby(data)
        return result, data

    def ackCommand_standby(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_standby(cmdId, ackCode, errorCode, description)

    def subscribeCommand_standby(self, action):
        self.commandSubscribers_standby.append(action)
        if "command_standby" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_standby"] = [self.acceptCommand_standby, self.commandSubscribers_standby]

    def acceptCommand_exitControl(self):
        data = MTM1M3_command_exitControlC()
        result = self.sal.acceptCommand_exitControl(data)
        return result, data

    def ackCommand_exitControl(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_exitControl(cmdId, ackCode, errorCode, description)

    def subscribeCommand_exitControl(self, action):
        self.commandSubscribers_exitControl.append(action)
        if "command_exitControl" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_exitControl"] = [self.acceptCommand_exitControl, self.commandSubscribers_exitControl]

    def acceptCommand_start(self):
        data = MTM1M3_command_startC()
        result = self.sal.acceptCommand_start(data)
        return result, data

    def ackCommand_start(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_start(cmdId, ackCode, errorCode, description)

    def subscribeCommand_start(self, action):
        self.commandSubscribers_start.append(action)
        if "command_start" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_start"] = [self.acceptCommand_start, self.commandSubscribers_start]

    def acceptCommand_enterControl(self):
        data = MTM1M3_command_enterControlC()
        result = self.sal.acceptCommand_enterControl(data)
        return result, data

    def ackCommand_enterControl(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_enterControl(cmdId, ackCode, errorCode, description)

    def subscribeCommand_enterControl(self, action):
        self.commandSubscribers_enterControl.append(action)
        if "command_enterControl" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_enterControl"] = [self.acceptCommand_enterControl, self.commandSubscribers_enterControl]

    def acceptCommand_setValue(self):
        data = MTM1M3_command_setValueC()
        result = self.sal.acceptCommand_setValue(data)
        return result, data

    def ackCommand_setValue(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_setValue(cmdId, ackCode, errorCode, description)

    def subscribeCommand_setValue(self, action):
        self.commandSubscribers_setValue.append(action)
        if "command_setValue" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_setValue"] = [self.acceptCommand_setValue, self.commandSubscribers_setValue]

    def acceptCommand_abortRaiseM1M3(self):
        data = MTM1M3_command_abortRaiseM1M3C()
        result = self.sal.acceptCommand_abortRaiseM1M3(data)
        return result, data

    def ackCommand_abortRaiseM1M3(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_abortRaiseM1M3(cmdId, ackCode, errorCode, description)

    def subscribeCommand_abortRaiseM1M3(self, action):
        self.commandSubscribers_abortRaiseM1M3.append(action)
        if "command_abortRaiseM1M3" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_abortRaiseM1M3"] = [self.acceptCommand_abortRaiseM1M3, self.commandSubscribers_abortRaiseM1M3]

    def acceptCommand_applyAberrationForces(self):
        data = MTM1M3_command_applyAberrationForcesC()
        result = self.sal.acceptCommand_applyAberrationForces(data)
        return result, data

    def ackCommand_applyAberrationForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyAberrationForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyAberrationForces(self, action):
        self.commandSubscribers_applyAberrationForces.append(action)
        if "command_applyAberrationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyAberrationForces"] = [self.acceptCommand_applyAberrationForces, self.commandSubscribers_applyAberrationForces]

    def acceptCommand_applyAberrationForcesByBendingModes(self):
        data = MTM1M3_command_applyAberrationForcesByBendingModesC()
        result = self.sal.acceptCommand_applyAberrationForcesByBendingModes(data)
        return result, data

    def ackCommand_applyAberrationForcesByBendingModes(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyAberrationForcesByBendingModes(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyAberrationForcesByBendingModes(self, action):
        self.commandSubscribers_applyAberrationForcesByBendingModes.append(action)
        if "command_applyAberrationForcesByBendingModes" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyAberrationForcesByBendingModes"] = [self.acceptCommand_applyAberrationForcesByBendingModes, self.commandSubscribers_applyAberrationForcesByBendingModes]

    def acceptCommand_applyActiveOpticForces(self):
        data = MTM1M3_command_applyActiveOpticForcesC()
        result = self.sal.acceptCommand_applyActiveOpticForces(data)
        return result, data

    def ackCommand_applyActiveOpticForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyActiveOpticForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyActiveOpticForces(self, action):
        self.commandSubscribers_applyActiveOpticForces.append(action)
        if "command_applyActiveOpticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyActiveOpticForces"] = [self.acceptCommand_applyActiveOpticForces, self.commandSubscribers_applyActiveOpticForces]

    def acceptCommand_applyActiveOpticForcesByBendingModes(self):
        data = MTM1M3_command_applyActiveOpticForcesByBendingModesC()
        result = self.sal.acceptCommand_applyActiveOpticForcesByBendingModes(data)
        return result, data

    def ackCommand_applyActiveOpticForcesByBendingModes(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyActiveOpticForcesByBendingModes(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyActiveOpticForcesByBendingModes(self, action):
        self.commandSubscribers_applyActiveOpticForcesByBendingModes.append(action)
        if "command_applyActiveOpticForcesByBendingModes" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyActiveOpticForcesByBendingModes"] = [self.acceptCommand_applyActiveOpticForcesByBendingModes, self.commandSubscribers_applyActiveOpticForcesByBendingModes]

    def acceptCommand_applyOffsetForces(self):
        data = MTM1M3_command_applyOffsetForcesC()
        result = self.sal.acceptCommand_applyOffsetForces(data)
        return result, data

    def ackCommand_applyOffsetForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyOffsetForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyOffsetForces(self, action):
        self.commandSubscribers_applyOffsetForces.append(action)
        if "command_applyOffsetForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyOffsetForces"] = [self.acceptCommand_applyOffsetForces, self.commandSubscribers_applyOffsetForces]

    def acceptCommand_applyOffsetForcesByMirrorForce(self):
        data = MTM1M3_command_applyOffsetForcesByMirrorForceC()
        result = self.sal.acceptCommand_applyOffsetForcesByMirrorForce(data)
        return result, data

    def ackCommand_applyOffsetForcesByMirrorForce(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_applyOffsetForcesByMirrorForce(cmdId, ackCode, errorCode, description)

    def subscribeCommand_applyOffsetForcesByMirrorForce(self, action):
        self.commandSubscribers_applyOffsetForcesByMirrorForce.append(action)
        if "command_applyOffsetForcesByMirrorForce" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_applyOffsetForcesByMirrorForce"] = [self.acceptCommand_applyOffsetForcesByMirrorForce, self.commandSubscribers_applyOffsetForcesByMirrorForce]

    def acceptCommand_clearAberrationForces(self):
        data = MTM1M3_command_clearAberrationForcesC()
        result = self.sal.acceptCommand_clearAberrationForces(data)
        return result, data

    def ackCommand_clearAberrationForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_clearAberrationForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_clearAberrationForces(self, action):
        self.commandSubscribers_clearAberrationForces.append(action)
        if "command_clearAberrationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_clearAberrationForces"] = [self.acceptCommand_clearAberrationForces, self.commandSubscribers_clearAberrationForces]

    def acceptCommand_clearActiveOpticForces(self):
        data = MTM1M3_command_clearActiveOpticForcesC()
        result = self.sal.acceptCommand_clearActiveOpticForces(data)
        return result, data

    def ackCommand_clearActiveOpticForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_clearActiveOpticForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_clearActiveOpticForces(self, action):
        self.commandSubscribers_clearActiveOpticForces.append(action)
        if "command_clearActiveOpticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_clearActiveOpticForces"] = [self.acceptCommand_clearActiveOpticForces, self.commandSubscribers_clearActiveOpticForces]

    def acceptCommand_clearOffsetForces(self):
        data = MTM1M3_command_clearOffsetForcesC()
        result = self.sal.acceptCommand_clearOffsetForces(data)
        return result, data

    def ackCommand_clearOffsetForces(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_clearOffsetForces(cmdId, ackCode, errorCode, description)

    def subscribeCommand_clearOffsetForces(self, action):
        self.commandSubscribers_clearOffsetForces.append(action)
        if "command_clearOffsetForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_clearOffsetForces"] = [self.acceptCommand_clearOffsetForces, self.commandSubscribers_clearOffsetForces]

    def acceptCommand_disableHardpointChase(self):
        data = MTM1M3_command_disableHardpointChaseC()
        result = self.sal.acceptCommand_disableHardpointChase(data)
        return result, data

    def ackCommand_disableHardpointChase(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_disableHardpointChase(cmdId, ackCode, errorCode, description)

    def subscribeCommand_disableHardpointChase(self, action):
        self.commandSubscribers_disableHardpointChase.append(action)
        if "command_disableHardpointChase" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_disableHardpointChase"] = [self.acceptCommand_disableHardpointChase, self.commandSubscribers_disableHardpointChase]

    def acceptCommand_disableHardpointCorrections(self):
        data = MTM1M3_command_disableHardpointCorrectionsC()
        result = self.sal.acceptCommand_disableHardpointCorrections(data)
        return result, data

    def ackCommand_disableHardpointCorrections(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_disableHardpointCorrections(cmdId, ackCode, errorCode, description)

    def subscribeCommand_disableHardpointCorrections(self, action):
        self.commandSubscribers_disableHardpointCorrections.append(action)
        if "command_disableHardpointCorrections" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_disableHardpointCorrections"] = [self.acceptCommand_disableHardpointCorrections, self.commandSubscribers_disableHardpointCorrections]

    def acceptCommand_enableHardpointChase(self):
        data = MTM1M3_command_enableHardpointChaseC()
        result = self.sal.acceptCommand_enableHardpointChase(data)
        return result, data

    def ackCommand_enableHardpointChase(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_enableHardpointChase(cmdId, ackCode, errorCode, description)

    def subscribeCommand_enableHardpointChase(self, action):
        self.commandSubscribers_enableHardpointChase.append(action)
        if "command_enableHardpointChase" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_enableHardpointChase"] = [self.acceptCommand_enableHardpointChase, self.commandSubscribers_enableHardpointChase]

    def acceptCommand_enableHardpointCorrections(self):
        data = MTM1M3_command_enableHardpointCorrectionsC()
        result = self.sal.acceptCommand_enableHardpointCorrections(data)
        return result, data

    def ackCommand_enableHardpointCorrections(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_enableHardpointCorrections(cmdId, ackCode, errorCode, description)

    def subscribeCommand_enableHardpointCorrections(self, action):
        self.commandSubscribers_enableHardpointCorrections.append(action)
        if "command_enableHardpointCorrections" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_enableHardpointCorrections"] = [self.acceptCommand_enableHardpointCorrections, self.commandSubscribers_enableHardpointCorrections]

    def acceptCommand_enterEngineering(self):
        data = MTM1M3_command_enterEngineeringC()
        result = self.sal.acceptCommand_enterEngineering(data)
        return result, data

    def ackCommand_enterEngineering(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_enterEngineering(cmdId, ackCode, errorCode, description)

    def subscribeCommand_enterEngineering(self, action):
        self.commandSubscribers_enterEngineering.append(action)
        if "command_enterEngineering" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_enterEngineering"] = [self.acceptCommand_enterEngineering, self.commandSubscribers_enterEngineering]

    def acceptCommand_exitEngineering(self):
        data = MTM1M3_command_exitEngineeringC()
        result = self.sal.acceptCommand_exitEngineering(data)
        return result, data

    def ackCommand_exitEngineering(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_exitEngineering(cmdId, ackCode, errorCode, description)

    def subscribeCommand_exitEngineering(self, action):
        self.commandSubscribers_exitEngineering.append(action)
        if "command_exitEngineering" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_exitEngineering"] = [self.acceptCommand_exitEngineering, self.commandSubscribers_exitEngineering]

    def acceptCommand_lowerM1M3(self):
        data = MTM1M3_command_lowerM1M3C()
        result = self.sal.acceptCommand_lowerM1M3(data)
        return result, data

    def ackCommand_lowerM1M3(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_lowerM1M3(cmdId, ackCode, errorCode, description)

    def subscribeCommand_lowerM1M3(self, action):
        self.commandSubscribers_lowerM1M3.append(action)
        if "command_lowerM1M3" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_lowerM1M3"] = [self.acceptCommand_lowerM1M3, self.commandSubscribers_lowerM1M3]

    def acceptCommand_modbusTransmit(self):
        data = MTM1M3_command_modbusTransmitC()
        result = self.sal.acceptCommand_modbusTransmit(data)
        return result, data

    def ackCommand_modbusTransmit(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_modbusTransmit(cmdId, ackCode, errorCode, description)

    def subscribeCommand_modbusTransmit(self, action):
        self.commandSubscribers_modbusTransmit.append(action)
        if "command_modbusTransmit" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_modbusTransmit"] = [self.acceptCommand_modbusTransmit, self.commandSubscribers_modbusTransmit]

    def acceptCommand_moveHardpointActuators(self):
        data = MTM1M3_command_moveHardpointActuatorsC()
        result = self.sal.acceptCommand_moveHardpointActuators(data)
        return result, data

    def ackCommand_moveHardpointActuators(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_moveHardpointActuators(cmdId, ackCode, errorCode, description)

    def subscribeCommand_moveHardpointActuators(self, action):
        self.commandSubscribers_moveHardpointActuators.append(action)
        if "command_moveHardpointActuators" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_moveHardpointActuators"] = [self.acceptCommand_moveHardpointActuators, self.commandSubscribers_moveHardpointActuators]

    def acceptCommand_positionM1M3(self):
        data = MTM1M3_command_positionM1M3C()
        result = self.sal.acceptCommand_positionM1M3(data)
        return result, data

    def ackCommand_positionM1M3(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_positionM1M3(cmdId, ackCode, errorCode, description)

    def subscribeCommand_positionM1M3(self, action):
        self.commandSubscribers_positionM1M3.append(action)
        if "command_positionM1M3" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_positionM1M3"] = [self.acceptCommand_positionM1M3, self.commandSubscribers_positionM1M3]

    def acceptCommand_programILC(self):
        data = MTM1M3_command_programILCC()
        result = self.sal.acceptCommand_programILC(data)
        return result, data

    def ackCommand_programILC(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_programILC(cmdId, ackCode, errorCode, description)

    def subscribeCommand_programILC(self, action):
        self.commandSubscribers_programILC.append(action)
        if "command_programILC" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_programILC"] = [self.acceptCommand_programILC, self.commandSubscribers_programILC]

    def acceptCommand_raiseM1M3(self):
        data = MTM1M3_command_raiseM1M3C()
        result = self.sal.acceptCommand_raiseM1M3(data)
        return result, data

    def ackCommand_raiseM1M3(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_raiseM1M3(cmdId, ackCode, errorCode, description)

    def subscribeCommand_raiseM1M3(self, action):
        self.commandSubscribers_raiseM1M3.append(action)
        if "command_raiseM1M3" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_raiseM1M3"] = [self.acceptCommand_raiseM1M3, self.commandSubscribers_raiseM1M3]

    def acceptCommand_resetPID(self):
        data = MTM1M3_command_resetPIDC()
        result = self.sal.acceptCommand_resetPID(data)
        return result, data

    def ackCommand_resetPID(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_resetPID(cmdId, ackCode, errorCode, description)

    def subscribeCommand_resetPID(self, action):
        self.commandSubscribers_resetPID.append(action)
        if "command_resetPID" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_resetPID"] = [self.acceptCommand_resetPID, self.commandSubscribers_resetPID]

    def acceptCommand_shutdown(self):
        data = MTM1M3_command_shutdownC()
        result = self.sal.acceptCommand_shutdown(data)
        return result, data

    def ackCommand_shutdown(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_shutdown(cmdId, ackCode, errorCode, description)

    def subscribeCommand_shutdown(self, action):
        self.commandSubscribers_shutdown.append(action)
        if "command_shutdown" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_shutdown"] = [self.acceptCommand_shutdown, self.commandSubscribers_shutdown]

    def acceptCommand_stopHardpointMotion(self):
        data = MTM1M3_command_stopHardpointMotionC()
        result = self.sal.acceptCommand_stopHardpointMotion(data)
        return result, data

    def ackCommand_stopHardpointMotion(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_stopHardpointMotion(cmdId, ackCode, errorCode, description)

    def subscribeCommand_stopHardpointMotion(self, action):
        self.commandSubscribers_stopHardpointMotion.append(action)
        if "command_stopHardpointMotion" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_stopHardpointMotion"] = [self.acceptCommand_stopHardpointMotion, self.commandSubscribers_stopHardpointMotion]

    def acceptCommand_testAir(self):
        data = MTM1M3_command_testAirC()
        result = self.sal.acceptCommand_testAir(data)
        return result, data

    def ackCommand_testAir(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_testAir(cmdId, ackCode, errorCode, description)

    def subscribeCommand_testAir(self, action):
        self.commandSubscribers_testAir.append(action)
        if "command_testAir" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_testAir"] = [self.acceptCommand_testAir, self.commandSubscribers_testAir]

    def acceptCommand_testForceActuator(self):
        data = MTM1M3_command_testForceActuatorC()
        result = self.sal.acceptCommand_testForceActuator(data)
        return result, data

    def ackCommand_testForceActuator(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_testForceActuator(cmdId, ackCode, errorCode, description)

    def subscribeCommand_testForceActuator(self, action):
        self.commandSubscribers_testForceActuator.append(action)
        if "command_testForceActuator" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_testForceActuator"] = [self.acceptCommand_testForceActuator, self.commandSubscribers_testForceActuator]

    def acceptCommand_testHardpoint(self):
        data = MTM1M3_command_testHardpointC()
        result = self.sal.acceptCommand_testHardpoint(data)
        return result, data

    def ackCommand_testHardpoint(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_testHardpoint(cmdId, ackCode, errorCode, description)

    def subscribeCommand_testHardpoint(self, action):
        self.commandSubscribers_testHardpoint.append(action)
        if "command_testHardpoint" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_testHardpoint"] = [self.acceptCommand_testHardpoint, self.commandSubscribers_testHardpoint]

    def acceptCommand_translateM1M3(self):
        data = MTM1M3_command_translateM1M3C()
        result = self.sal.acceptCommand_translateM1M3(data)
        return result, data

    def ackCommand_translateM1M3(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_translateM1M3(cmdId, ackCode, errorCode, description)

    def subscribeCommand_translateM1M3(self, action):
        self.commandSubscribers_translateM1M3.append(action)
        if "command_translateM1M3" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_translateM1M3"] = [self.acceptCommand_translateM1M3, self.commandSubscribers_translateM1M3]

    def acceptCommand_turnAirOff(self):
        data = MTM1M3_command_turnAirOffC()
        result = self.sal.acceptCommand_turnAirOff(data)
        return result, data

    def ackCommand_turnAirOff(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnAirOff(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnAirOff(self, action):
        self.commandSubscribers_turnAirOff.append(action)
        if "command_turnAirOff" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnAirOff"] = [self.acceptCommand_turnAirOff, self.commandSubscribers_turnAirOff]

    def acceptCommand_turnAirOn(self):
        data = MTM1M3_command_turnAirOnC()
        result = self.sal.acceptCommand_turnAirOn(data)
        return result, data

    def ackCommand_turnAirOn(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnAirOn(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnAirOn(self, action):
        self.commandSubscribers_turnAirOn.append(action)
        if "command_turnAirOn" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnAirOn"] = [self.acceptCommand_turnAirOn, self.commandSubscribers_turnAirOn]

    def acceptCommand_turnLightsOff(self):
        data = MTM1M3_command_turnLightsOffC()
        result = self.sal.acceptCommand_turnLightsOff(data)
        return result, data

    def ackCommand_turnLightsOff(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnLightsOff(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnLightsOff(self, action):
        self.commandSubscribers_turnLightsOff.append(action)
        if "command_turnLightsOff" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnLightsOff"] = [self.acceptCommand_turnLightsOff, self.commandSubscribers_turnLightsOff]

    def acceptCommand_turnLightsOn(self):
        data = MTM1M3_command_turnLightsOnC()
        result = self.sal.acceptCommand_turnLightsOn(data)
        return result, data

    def ackCommand_turnLightsOn(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnLightsOn(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnLightsOn(self, action):
        self.commandSubscribers_turnLightsOn.append(action)
        if "command_turnLightsOn" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnLightsOn"] = [self.acceptCommand_turnLightsOn, self.commandSubscribers_turnLightsOn]

    def acceptCommand_turnPowerOff(self):
        data = MTM1M3_command_turnPowerOffC()
        result = self.sal.acceptCommand_turnPowerOff(data)
        return result, data

    def ackCommand_turnPowerOff(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnPowerOff(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnPowerOff(self, action):
        self.commandSubscribers_turnPowerOff.append(action)
        if "command_turnPowerOff" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnPowerOff"] = [self.acceptCommand_turnPowerOff, self.commandSubscribers_turnPowerOff]

    def acceptCommand_turnPowerOn(self):
        data = MTM1M3_command_turnPowerOnC()
        result = self.sal.acceptCommand_turnPowerOn(data)
        return result, data

    def ackCommand_turnPowerOn(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_turnPowerOn(cmdId, ackCode, errorCode, description)

    def subscribeCommand_turnPowerOn(self, action):
        self.commandSubscribers_turnPowerOn.append(action)
        if "command_turnPowerOn" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_turnPowerOn"] = [self.acceptCommand_turnPowerOn, self.commandSubscribers_turnPowerOn]

    def acceptCommand_updatePID(self):
        data = MTM1M3_command_updatePIDC()
        result = self.sal.acceptCommand_updatePID(data)
        return result, data

    def ackCommand_updatePID(self, cmdId, ackCode, errorCode, description):
        return self.sal.ackCommand_updatePID(cmdId, ackCode, errorCode, description)

    def subscribeCommand_updatePID(self, action):
        self.commandSubscribers_updatePID.append(action)
        if "command_updatePID" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["command_updatePID"] = [self.acceptCommand_updatePID, self.commandSubscribers_updatePID]



    def logEvent_settingVersions(self, recommendedSettingsVersion, recommendedSettingsLabels, priority = 0):
        data = MTM1M3_logevent_settingVersionsC()
        data.recommendedSettingsVersion = recommendedSettingsVersion
        data.recommendedSettingsLabels = recommendedSettingsLabels

        return self.sal.logEvent_settingVersions(data, priority)

    def logEvent_errorCode(self, errorCode, errorReport, traceback, priority = 0):
        data = MTM1M3_logevent_errorCodeC()
        data.errorCode = errorCode
        data.errorReport = errorReport
        data.traceback = traceback

        return self.sal.logEvent_errorCode(data, priority)

    def logEvent_summaryState(self, summaryState, priority = 0):
        data = MTM1M3_logevent_summaryStateC()
        data.summaryState = summaryState

        return self.sal.logEvent_summaryState(data, priority)

    def logEvent_appliedSettingsMatchStart(self, appliedSettingsMatchStartIsTrue, priority = 0):
        data = MTM1M3_logevent_appliedSettingsMatchStartC()
        data.appliedSettingsMatchStartIsTrue = appliedSettingsMatchStartIsTrue

        return self.sal.logEvent_appliedSettingsMatchStart(data, priority)

    def logEvent_accelerometerWarning(self, anyWarning, accelerometerFlags, priority = 0):
        data = MTM1M3_logevent_accelerometerWarningC()
        data.anyWarning = anyWarning
        data.accelerometerFlags = accelerometerFlags

        return self.sal.logEvent_accelerometerWarning(data, priority)

    def logEvent_airSupplyStatus(self, airCommandedOn, airValveOpened, airValveClosed, priority = 0):
        data = MTM1M3_logevent_airSupplyStatusC()
        data.airCommandedOn = airCommandedOn
        data.airValveOpened = airValveOpened
        data.airValveClosed = airValveClosed

        return self.sal.logEvent_airSupplyStatus(data, priority)

    def logEvent_airSupplyWarning(self, anyWarning, airSupplyFlags, priority = 0):
        data = MTM1M3_logevent_airSupplyWarningC()
        data.anyWarning = anyWarning
        data.airSupplyFlags = airSupplyFlags

        return self.sal.logEvent_airSupplyWarning(data, priority)

    def logEvent_appliedAberrationForces(self, zForces, fZ, mX, mY, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedAberrationForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedAberrationForces(data, priority)

    def logEvent_appliedAccelerationForces(self, xForces, yForces, zForces, fY, fX, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedAccelerationForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fY = fY
        data.fX = fX
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedAccelerationForces(data, priority)

    def logEvent_appliedActiveOpticForces(self, zForces, fZ, mX, mY, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedActiveOpticForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedActiveOpticForces(data, priority)

    def logEvent_appliedAzimuthForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedAzimuthForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedAzimuthForces(data, priority)

    def logEvent_appliedBalanceForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedBalanceForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedBalanceForces(data, priority)

    def logEvent_appliedCylinderForces(self, secondaryCylinderForces, primaryCylinderForces, priority = 0):
        data = MTM1M3_logevent_appliedCylinderForcesC()
        for i in range(112):
            data.secondaryCylinderForces[i] = secondaryCylinderForces[i]
        for i in range(156):
            data.primaryCylinderForces[i] = primaryCylinderForces[i]

        return self.sal.logEvent_appliedCylinderForces(data, priority)

    def logEvent_appliedElevationForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedElevationForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedElevationForces(data, priority)

    def logEvent_appliedForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedForces(data, priority)

    def logEvent_appliedHardpointSteps(self, targetEncoderValues, queuedSteps, commandedSteps, priority = 0):
        data = MTM1M3_logevent_appliedHardpointStepsC()
        for i in range(6):
            data.targetEncoderValues[i] = targetEncoderValues[i]
        for i in range(6):
            data.queuedSteps[i] = queuedSteps[i]
        for i in range(6):
            data.commandedSteps[i] = commandedSteps[i]

        return self.sal.logEvent_appliedHardpointSteps(data, priority)

    def logEvent_appliedOffsetForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedOffsetForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedOffsetForces(data, priority)

    def logEvent_appliedStaticForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedStaticForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedStaticForces(data, priority)

    def logEvent_appliedThermalForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedThermalForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedThermalForces(data, priority)

    def logEvent_appliedVelocityForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_appliedVelocityForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_appliedVelocityForces(data, priority)

    def logEvent_cellLightStatus(self, cellLightsCommandedOn, cellLightsOn, priority = 0):
        data = MTM1M3_logevent_cellLightStatusC()
        data.cellLightsCommandedOn = cellLightsCommandedOn
        data.cellLightsOn = cellLightsOn

        return self.sal.logEvent_cellLightStatus(data, priority)

    def logEvent_cellLightWarning(self, anyWarning, cellLightFlags, priority = 0):
        data = MTM1M3_logevent_cellLightWarningC()
        data.anyWarning = anyWarning
        data.cellLightFlags = cellLightFlags

        return self.sal.logEvent_cellLightWarning(data, priority)

    def logEvent_detailedState(self, detailedState, priority = 0):
        data = MTM1M3_logevent_detailedStateC()
        data.detailedState = detailedState

        return self.sal.logEvent_detailedState(data, priority)

    def logEvent_displacementSensorWarning(self, anyWarning, displacementSensorFlags, priority = 0):
        data = MTM1M3_logevent_displacementSensorWarningC()
        data.anyWarning = anyWarning
        data.displacementSensorFlags = displacementSensorFlags

        return self.sal.logEvent_displacementSensorWarning(data, priority)

    def logEvent_forceActuatorInfo(self, modbusSubnet, modbusAddress, ilcStatus, mezzanineStatus, priority = 0):
        data = MTM1M3_logevent_forceActuatorInfoC()
        for i in range(156):
            data.modbusSubnet[i] = modbusSubnet[i]
        for i in range(156):
            data.modbusAddress[i] = modbusAddress[i]
        for i in range(156):
            data.ilcStatus[i] = ilcStatus[i]
        for i in range(156):
            data.mezzanineStatus[i] = mezzanineStatus[i]
        for i in range(156):
            data.actuatorType[i] = actuatorType[i]
        for i in range(156):
            data.actuatorOrientation[i] = actuatorOrientation[i]
        for i in range(156):
            data.xPosition[i] = xPosition[i]
        for i in range(156):
            data.yPosition[i] = yPosition[i]
        for i in range(156):
            data.zPosition[i] = zPosition[i]

        return self.sal.logEvent_forceActuatorInfo(data, priority)

    def logEvent_forceActuatorState(self, ilcState, slewFlag, staticForcesApplied, elevationForcesApplied, azimuthForcesApplied, thermalForcesApplied, offsetForcesApplied, accelerationForcesApplied, velocityForcesApplied, activeOpticForcesApplied, aberrationForcesApplied, balanceForcesApplied, supportPercentage, priority = 0):
        data = MTM1M3_logevent_forceActuatorStateC()
        for i in range(156):
            data.ilcState[i] = ilcState[i]
        data.slewFlag = slewFlag
        data.staticForcesApplied = staticForcesApplied
        data.elevationForcesApplied = elevationForcesApplied
        data.azimuthForcesApplied = azimuthForcesApplied
        data.thermalForcesApplied = thermalForcesApplied
        data.offsetForcesApplied = offsetForcesApplied
        data.accelerationForcesApplied = accelerationForcesApplied
        data.velocityForcesApplied = velocityForcesApplied
        data.activeOpticForcesApplied = activeOpticForcesApplied
        data.aberrationForcesApplied = aberrationForcesApplied
        data.balanceForcesApplied = balanceForcesApplied
        data.supportPercentage = supportPercentage

        return self.sal.logEvent_forceActuatorState(data, priority)

    def logEvent_forceActuatorWarning(self, anyWarning, globalWarningFlags, anyForceActuatorFlags, forceActuatorFlags, priority = 0):
        data = MTM1M3_logevent_forceActuatorWarningC()
        data.anyWarning = anyWarning
        data.globalWarningFlags = globalWarningFlags
        data.anyForceActuatorFlags = anyForceActuatorFlags
        for i in range(156):
            data.forceActuatorFlags[i] = forceActuatorFlags[i]

        return self.sal.logEvent_forceActuatorWarning(data, priority)

    def logEvent_gyroWarning(self, anyWarning, gyroSensorFlags, priority = 0):
        data = MTM1M3_logevent_gyroWarningC()
        data.anyWarning = anyWarning
        data.gyroSensorFlags = gyroSensorFlags

        return self.sal.logEvent_gyroWarning(data, priority)

    def logEvent_hardpointActuatorInfo(self, referenceId, referencePosition, modbusSubnet, modbusAddress, xPosition, yPosition, zPosition, ilcUniqueId, ilcApplicationType, networkNodeType, ilcSelectedOptions, networkNodeOptions, majorRevision, minorRevision, adcScanRate, mainLoadCellCoefficient, mainLoadCellOffset, mainLoadCellSensitivity, backupLoadCellCoefficient, backupLoadCellOffset, backupLoadCellSensitivity, priority = 0):
        data = MTM1M3_logevent_hardpointActuatorInfoC()
        for i in range(6):
            data.referenceId[i] = referenceId[i]
        for i in range(6):
            data.referencePosition[i] = referencePosition[i]
        for i in range(6):
            data.modbusSubnet[i] = modbusSubnet[i]
        for i in range(6):
            data.modbusAddress[i] = modbusAddress[i]
        for i in range(6):
            data.xPosition[i] = xPosition[i]
        for i in range(6):
            data.yPosition[i] = yPosition[i]
        for i in range(6):
            data.zPosition[i] = zPosition[i]
        for i in range(6):
            data.ilcUniqueId[i] = ilcUniqueId[i]
        for i in range(6):
            data.ilcApplicationType[i] = ilcApplicationType[i]
        for i in range(6):
            data.networkNodeType[i] = networkNodeType[i]
        for i in range(6):
            data.ilcSelectedOptions[i] = ilcSelectedOptions[i]
        for i in range(6):
            data.networkNodeOptions[i] = networkNodeOptions[i]
        for i in range(6):
            data.majorRevision[i] = majorRevision[i]
        for i in range(6):
            data.minorRevision[i] = minorRevision[i]
        for i in range(6):
            data.adcScanRate[i] = adcScanRate[i]
        for i in range(6):
            data.mainLoadCellCoefficient[i] = mainLoadCellCoefficient[i]
        for i in range(6):
            data.mainLoadCellOffset[i] = mainLoadCellOffset[i]
        for i in range(6):
            data.mainLoadCellSensitivity[i] = mainLoadCellSensitivity[i]
        for i in range(6):
            data.backupLoadCellCoefficient[i] = backupLoadCellCoefficient[i]
        for i in range(6):
            data.backupLoadCellOffset[i] = backupLoadCellOffset[i]
        for i in range(6):
            data.backupLoadCellSensitivity[i] = backupLoadCellSensitivity[i]

        return self.sal.logEvent_hardpointActuatorInfo(data, priority)

    def logEvent_hardpointActuatorState(self, ilcState, motionState, priority = 0):
        data = MTM1M3_logevent_hardpointActuatorStateC()
        for i in range(6):
            data.ilcState[i] = ilcState[i]
        for i in range(6):
            data.motionState[i] = motionState[i]

        return self.sal.logEvent_hardpointActuatorState(data, priority)

    def logEvent_hardpointActuatorWarning(self, anyWarning, anyHardpointActuatorFlags, hardpointActuatorFlags, priority = 0):
        data = MTM1M3_logevent_hardpointActuatorWarningC()
        data.anyWarning = anyWarning
        data.anyHardpointActuatorFlags = anyHardpointActuatorFlags
        for i in range(6):
            data.hardpointActuatorFlags[i] = hardpointActuatorFlags[i]

        return self.sal.logEvent_hardpointActuatorWarning(data, priority)

    def logEvent_hardpointMonitorInfo(self, referenceId, modbusSubnet, modbusAddress, ilcUniqueId, ilcApplicationType, networkNodeType, majorRevision, minorRevision, mezzanineUniqueId, mezzanineFirmwareType, mezzanineMajorRevision, mezzanineMinorRevision, priority = 0):
        data = MTM1M3_logevent_hardpointMonitorInfoC()
        for i in range(6):
            data.referenceId[i] = referenceId[i]
        for i in range(6):
            data.modbusSubnet[i] = modbusSubnet[i]
        for i in range(6):
            data.modbusAddress[i] = modbusAddress[i]
        for i in range(6):
            data.ilcUniqueId[i] = ilcUniqueId[i]
        for i in range(6):
            data.ilcApplicationType[i] = ilcApplicationType[i]
        for i in range(6):
            data.networkNodeType[i] = networkNodeType[i]
        for i in range(6):
            data.majorRevision[i] = majorRevision[i]
        for i in range(6):
            data.minorRevision[i] = minorRevision[i]
        for i in range(6):
            data.mezzanineUniqueId[i] = mezzanineUniqueId[i]
        for i in range(6):
            data.mezzanineFirmwareType[i] = mezzanineFirmwareType[i]
        for i in range(6):
            data.mezzanineMajorRevision[i] = mezzanineMajorRevision[i]
        for i in range(6):
            data.mezzanineMinorRevision[i] = mezzanineMinorRevision[i]

        return self.sal.logEvent_hardpointMonitorInfo(data, priority)

    def logEvent_hardpointMonitorState(self, ilcState, priority = 0):
        data = MTM1M3_logevent_hardpointMonitorStateC()
        for i in range(6):
            data.ilcState[i] = ilcState[i]

        return self.sal.logEvent_hardpointMonitorState(data, priority)

    def logEvent_hardpointMonitorWarning(self, anyWarning, anyHardpointMonitorFlags, hardpointMonitorFlags, priority = 0):
        data = MTM1M3_logevent_hardpointMonitorWarningC()
        data.anyWarning = anyWarning
        data.anyHardpointMonitorFlags = anyHardpointMonitorFlags
        for i in range(6):
            data.hardpointMonitorFlags[i] = hardpointMonitorFlags[i]

        return self.sal.logEvent_hardpointMonitorWarning(data, priority)

    def logEvent_inclinometerSensorWarning(self, anyWarning, inclinometerSensorFlags, priority = 0):
        data = MTM1M3_logevent_inclinometerSensorWarningC()
        data.anyWarning = anyWarning
        data.inclinometerSensorFlags = inclinometerSensorFlags

        return self.sal.logEvent_inclinometerSensorWarning(data, priority)

    def logEvent_interlockStatus(self, heartbeatCommandedState, priority = 0):
        data = MTM1M3_logevent_interlockStatusC()
        data.heartbeatCommandedState = heartbeatCommandedState

        return self.sal.logEvent_interlockStatus(data, priority)

    def logEvent_interlockWarning(self, anyWarning, interlockSystemFlags, priority = 0):
        data = MTM1M3_logevent_interlockWarningC()
        data.anyWarning = anyWarning
        data.interlockSystemFlags = interlockSystemFlags

        return self.sal.logEvent_interlockWarning(data, priority)

    def logEvent_modbusResponse(self, responseValid, address, functionCode, dataLength, data, crc, priority = 0):
        data = MTM1M3_logevent_modbusResponseC()
        data.responseValid = responseValid
        data.address = address
        data.functionCode = functionCode
        data.dataLength = dataLength
        for i in range(252):
            data.data[i] = data[i]
        data.crc = crc

        return self.sal.logEvent_modbusResponse(data, priority)

    def logEvent_modbusWarning(self, anyWarning, modbusSystemFlags, anySubnetFlags, subnetFlags, priority = 0):
        data = MTM1M3_logevent_modbusWarningC()
        data.anyWarning = anyWarning
        data.modbusSystemFlags = modbusSystemFlags
        data.anySubnetFlags = anySubnetFlags
        for i in range(5):
            data.subnetFlags[i] = subnetFlags[i]

        return self.sal.logEvent_modbusWarning(data, priority)

    def logEvent_pidInfo(self, timestep, p, i, d, n, calculatedA, calculatedB, calculatedC, calculatedD, calculatedE, priority = 0):
        data = MTM1M3_logevent_pidInfoC()
        for i in range(6):
            data.timestep[i] = timestep[i]
        for i in range(6):
            data.p[i] = p[i]
        for i in range(6):
            data.i[i] = i[i]
        for i in range(6):
            data.d[i] = d[i]
        for i in range(6):
            data.n[i] = n[i]
        for i in range(6):
            data.calculatedA[i] = calculatedA[i]
        for i in range(6):
            data.calculatedB[i] = calculatedB[i]
        for i in range(6):
            data.calculatedC[i] = calculatedC[i]
        for i in range(6):
            data.calculatedD[i] = calculatedD[i]
        for i in range(6):
            data.calculatedE[i] = calculatedE[i]

        return self.sal.logEvent_pidInfo(data, priority)

    def logEvent_powerStatus(self, powerNetworkACommandedOn, powerNetworkBCommandedOn, powerNetworkCCommandedOn, powerNetworkDCommandedOn, auxPowerNetworkACommandedOn, auxPowerNetworkBCommandedOn, auxPowerNetworkCCommandedOn, auxPowerNetworkDCommandedOn, priority = 0):
        data = MTM1M3_logevent_powerStatusC()
        data.powerNetworkACommandedOn = powerNetworkACommandedOn
        data.powerNetworkBCommandedOn = powerNetworkBCommandedOn
        data.powerNetworkCCommandedOn = powerNetworkCCommandedOn
        data.powerNetworkDCommandedOn = powerNetworkDCommandedOn
        data.auxPowerNetworkACommandedOn = auxPowerNetworkACommandedOn
        data.auxPowerNetworkBCommandedOn = auxPowerNetworkBCommandedOn
        data.auxPowerNetworkCCommandedOn = auxPowerNetworkCCommandedOn
        data.auxPowerNetworkDCommandedOn = auxPowerNetworkDCommandedOn

        return self.sal.logEvent_powerStatus(data, priority)

    def logEvent_powerWarning(self, anyWarning, powerSystemFlags, priority = 0):
        data = MTM1M3_logevent_powerWarningC()
        data.anyWarning = anyWarning
        data.powerSystemFlags = powerSystemFlags

        return self.sal.logEvent_powerWarning(data, priority)

    def logEvent_preclippedAberrationForces(self, zForces, fZ, mX, mY, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedAberrationForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedAberrationForces(data, priority)

    def logEvent_preclippedAccelerationForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedAccelerationForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedAccelerationForces(data, priority)

    def logEvent_preclippedActiveOpticForces(self, zForces, fZ, mX, mY, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedActiveOpticForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedActiveOpticForces(data, priority)

    def logEvent_preclippedAzimuthForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedAzimuthForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedAzimuthForces(data, priority)

    def logEvent_preclippedBalanceForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedBalanceForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedBalanceForces(data, priority)

    def logEvent_preclippedCylinderForces(self, secondaryCylinderForces, primaryCylinderForces, priority = 0):
        data = MTM1M3_logevent_preclippedCylinderForcesC()
        for i in range(112):
            data.secondaryCylinderForces[i] = secondaryCylinderForces[i]
        for i in range(156):
            data.primaryCylinderForces[i] = primaryCylinderForces[i]

        return self.sal.logEvent_preclippedCylinderForces(data, priority)

    def logEvent_preclippedElevationForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedElevationForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedElevationForces(data, priority)

    def logEvent_preclippedForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedForces(data, priority)

    def logEvent_preclippedOffsetForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedOffsetForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedOffsetForces(data, priority)

    def logEvent_preclippedStaticForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedStaticForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedStaticForces(data, priority)

    def logEvent_preclippedThermalForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedThermalForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedThermalForces(data, priority)

    def logEvent_preclippedVelocityForces(self, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude, priority = 0):
        data = MTM1M3_logevent_preclippedVelocityForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.logEvent_preclippedVelocityForces(data, priority)



    def putSample_accelerometerData(self, timestamp, rawAccelerometers, accelerometers, angularAccelerationX, angularAccelerationY, angularAccelerationZ):
        data = MTM1M3_accelerometerDataC()
        data.timestamp = timestamp
        for i in range(8):
            data.rawAccelerometers[i] = rawAccelerometers[i]
        for i in range(8):
            data.accelerometers[i] = accelerometers[i]
        data.angularAccelerationX = angularAccelerationX
        data.angularAccelerationY = angularAccelerationY
        data.angularAccelerationZ = angularAccelerationZ

        return self.sal.putSample_accelerometerData(data)

    def putSample_forceActuatorData(self, timestamp, primaryCylinderForces, secondaryCylinderForces, xForces, yForces, zForces, fX, fY, fZ, mX, mY, mZ, forceMagnitude):
        data = MTM1M3_forceActuatorDataC()
        data.timestamp = timestamp
        for i in range(156):
            data.primaryCylinderForces[i] = primaryCylinderForces[i]
        for i in range(112):
            data.secondaryCylinderForces[i] = secondaryCylinderForces[i]
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude

        return self.sal.putSample_forceActuatorData(data)

    def putSample_forceActuatorPressure(self, timestamps, primaryCylinderPushPressures, primaryCylinderPullPressures, secondaryCylinderPushPressures, secondaryCylinderPullPressures):
        data = MTM1M3_forceActuatorPressureC()
        for i in range(156):
            data.timestamps[i] = timestamps[i]
        for i in range(156):
            data.primaryCylinderPushPressures[i] = primaryCylinderPushPressures[i]
        for i in range(156):
            data.primaryCylinderPullPressures[i] = primaryCylinderPullPressures[i]
        for i in range(112):
            data.secondaryCylinderPushPressures[i] = secondaryCylinderPushPressures[i]
        for i in range(112):
            data.secondaryCylinderPullPressures[i] = secondaryCylinderPullPressures[i]

        return self.sal.putSample_forceActuatorPressure(data)

    def putSample_gyroData(self, timestamp, angularVelocityX, angularVelocityY, angularVelocityZ, sequenceNumber, temperature):
        data = MTM1M3_gyroDataC()
        data.timestamp = timestamp
        data.angularVelocityX = angularVelocityX
        data.angularVelocityY = angularVelocityY
        data.angularVelocityZ = angularVelocityZ
        data.sequenceNumber = sequenceNumber
        data.temperature = temperature

        return self.sal.putSample_gyroData(data)

    def putSample_hardpointActuatorData(self, timestamp, measuredForce, encoder, displacement, fX, fY, fZ, mX, mY, mZ, forceMagnitude, xPosition, yPosition, zPosition, xRotation, yRotation, zRotation):
        data = MTM1M3_hardpointActuatorDataC()
        data.timestamp = timestamp
        for i in range(6):
            data.measuredForce[i] = measuredForce[i]
        for i in range(6):
            data.encoder[i] = encoder[i]
        for i in range(6):
            data.displacement[i] = displacement[i]
        data.fX = fX
        data.fY = fY
        data.fZ = fZ
        data.mX = mX
        data.mY = mY
        data.mZ = mZ
        data.forceMagnitude = forceMagnitude
        data.xPosition = xPosition
        data.yPosition = yPosition
        data.zPosition = zPosition
        data.xRotation = xRotation
        data.yRotation = yRotation
        data.zRotation = zRotation

        return self.sal.putSample_hardpointActuatorData(data)

    def putSample_hardpointMonitorData(self, timestamp, breakawayLVDT, displacementLVDT, breakawayPressure, pressureSensor1, pressureSensor2, pressureSensor3):
        data = MTM1M3_hardpointMonitorDataC()
        data.timestamp = timestamp
        for i in range(6):
            data.breakawayLVDT[i] = breakawayLVDT[i]
        for i in range(6):
            data.displacementLVDT[i] = displacementLVDT[i]
        for i in range(6):
            data.breakawayPressure[i] = breakawayPressure[i]
        for i in range(6):
            data.pressureSensor1[i] = pressureSensor1[i]
        for i in range(6):
            data.pressureSensor2[i] = pressureSensor2[i]
        for i in range(6):
            data.pressureSensor3[i] = pressureSensor3[i]

        return self.sal.putSample_hardpointMonitorData(data)

    def putSample_imsData(self, timestamp, rawSensorData, xPosition, yPosition, zPosition, xRotation, yRotation, zRotation):
        data = MTM1M3_imsDataC()
        data.timestamp = timestamp
        for i in range(8):
            data.rawSensorData[i] = rawSensorData[i]
        data.xPosition = xPosition
        data.yPosition = yPosition
        data.zPosition = zPosition
        data.xRotation = xRotation
        data.yRotation = yRotation
        data.zRotation = zRotation

        return self.sal.putSample_imsData(data)

    def putSample_inclinometerData(self, timestamp, inclinometerAngle):
        data = MTM1M3_inclinometerDataC()
        data.timestamp = timestamp
        data.inclinometerAngle = inclinometerAngle

        return self.sal.putSample_inclinometerData(data)

    def putSample_outerLoopData(self, timestamp, broadcastCounter, executionTime):
        data = MTM1M3_outerLoopDataC()
        data.timestamp = timestamp
        data.broadcastCounter = broadcastCounter
        data.executionTime = executionTime

        return self.sal.putSample_outerLoopData(data)

    def putSample_pidData(self, timestamp, setpoint, measurement, error, errorT1, errorT2, control, controlT1, controlT2):
        data = MTM1M3_pidDataC()
        data.timestamp = timestamp
        for i in range(6):
            data.setpoint[i] = setpoint[i]
        for i in range(6):
            data.measurement[i] = measurement[i]
        for i in range(6):
            data.error[i] = error[i]
        for i in range(6):
            data.errorT1[i] = errorT1[i]
        for i in range(6):
            data.errorT2[i] = errorT2[i]
        for i in range(6):
            data.control[i] = control[i]
        for i in range(6):
            data.controlT1[i] = controlT1[i]
        for i in range(6):
            data.controlT2[i] = controlT2[i]

        return self.sal.putSample_pidData(data)

    def putSample_powerData(self, timestamp, powerNetworkACurrent, powerNetworkBCurrent, powerNetworkCCurrent, powerNetworkDCurrent, lightPowerNetworkCurrent, controlsPowerNetworkCurrent):
        data = MTM1M3_powerDataC()
        data.timestamp = timestamp
        data.powerNetworkACurrent = powerNetworkACurrent
        data.powerNetworkBCurrent = powerNetworkBCurrent
        data.powerNetworkCCurrent = powerNetworkCCurrent
        data.powerNetworkDCurrent = powerNetworkDCurrent
        data.lightPowerNetworkCurrent = lightPowerNetworkCurrent
        data.controlsPowerNetworkCurrent = controlsPowerNetworkCurrent

        return self.sal.putSample_powerData(data)

