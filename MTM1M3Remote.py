import time
from SALPY_MTM1M3 import *

class MTM1M3Remote:
    def __init__(self):
        self.sal = SAL_MTM1M3()
        self.sal.setDebugLevel(0)
        self.sal.salCommand("MTM1M3_command_abort")
        self.sal.salCommand("MTM1M3_command_enable")
        self.sal.salCommand("MTM1M3_command_disable")
        self.sal.salCommand("MTM1M3_command_standby")
        self.sal.salCommand("MTM1M3_command_exitControl")
        self.sal.salCommand("MTM1M3_command_start")
        self.sal.salCommand("MTM1M3_command_enterControl")
        self.sal.salCommand("MTM1M3_command_setValue")
        self.sal.salCommand("MTM1M3_command_abortRaiseM1M3")
        self.sal.salCommand("MTM1M3_command_applyAberrationForces")
        self.sal.salCommand("MTM1M3_command_applyAberrationForcesByBendingModes")
        self.sal.salCommand("MTM1M3_command_applyActiveOpticForces")
        self.sal.salCommand("MTM1M3_command_applyActiveOpticForcesByBendingModes")
        self.sal.salCommand("MTM1M3_command_applyOffsetForces")
        self.sal.salCommand("MTM1M3_command_applyOffsetForcesByMirrorForce")
        self.sal.salCommand("MTM1M3_command_clearAberrationForces")
        self.sal.salCommand("MTM1M3_command_clearActiveOpticForces")
        self.sal.salCommand("MTM1M3_command_clearOffsetForces")
        self.sal.salCommand("MTM1M3_command_disableHardpointChase")
        self.sal.salCommand("MTM1M3_command_disableHardpointCorrections")
        self.sal.salCommand("MTM1M3_command_enableHardpointChase")
        self.sal.salCommand("MTM1M3_command_enableHardpointCorrections")
        self.sal.salCommand("MTM1M3_command_enterEngineering")
        self.sal.salCommand("MTM1M3_command_exitEngineering")
        self.sal.salCommand("MTM1M3_command_lowerM1M3")
        self.sal.salCommand("MTM1M3_command_modbusTransmit")
        self.sal.salCommand("MTM1M3_command_moveHardpointActuators")
        self.sal.salCommand("MTM1M3_command_positionM1M3")
        self.sal.salCommand("MTM1M3_command_programILC")
        self.sal.salCommand("MTM1M3_command_raiseM1M3")
        self.sal.salCommand("MTM1M3_command_resetPID")
        self.sal.salCommand("MTM1M3_command_shutdown")
        self.sal.salCommand("MTM1M3_command_stopHardpointMotion")
        self.sal.salCommand("MTM1M3_command_testAir")
        self.sal.salCommand("MTM1M3_command_testForceActuator")
        self.sal.salCommand("MTM1M3_command_testHardpoint")
        self.sal.salCommand("MTM1M3_command_translateM1M3")
        self.sal.salCommand("MTM1M3_command_turnAirOff")
        self.sal.salCommand("MTM1M3_command_turnAirOn")
        self.sal.salCommand("MTM1M3_command_turnLightsOff")
        self.sal.salCommand("MTM1M3_command_turnLightsOn")
        self.sal.salCommand("MTM1M3_command_turnPowerOff")
        self.sal.salCommand("MTM1M3_command_turnPowerOn")
        self.sal.salCommand("MTM1M3_command_updatePID")

        self.sal.salEventSub("MTM1M3_logevent_accelerometerWarning")
        self.sal.salEventSub("MTM1M3_logevent_airSupplyStatus")
        self.sal.salEventSub("MTM1M3_logevent_airSupplyWarning")
        self.sal.salEventSub("MTM1M3_logevent_appliedAberrationForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedAccelerationForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedActiveOpticForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedAzimuthForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedBalanceForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedCylinderForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedElevationForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedOffsetForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedStaticForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedThermalForces")
        self.sal.salEventSub("MTM1M3_logevent_appliedVelocityForces")
        self.sal.salEventSub("MTM1M3_logevent_cellLightStatus")
        self.sal.salEventSub("MTM1M3_logevent_cellLightWarning")
        self.sal.salEventSub("MTM1M3_logevent_detailedState")
        self.sal.salEventSub("MTM1M3_logevent_displacementSensorWarning")
        self.sal.salEventSub("MTM1M3_logevent_forceActuatorInfo")
        self.sal.salEventSub("MTM1M3_logevent_forceActuatorState")
        self.sal.salEventSub("MTM1M3_logevent_forceActuatorWarning")
        self.sal.salEventSub("MTM1M3_logevent_gyroWarning")
        self.sal.salEventSub("MTM1M3_logevent_hardpointActuatorInfo")
        self.sal.salEventSub("MTM1M3_logevent_hardpointActuatorState")
        self.sal.salEventSub("MTM1M3_logevent_hardpointActuatorWarning")
        self.sal.salEventSub("MTM1M3_logevent_hardpointMonitorInfo")
        self.sal.salEventSub("MTM1M3_logevent_hardpointMonitorState")
        self.sal.salEventSub("MTM1M3_logevent_hardpointMonitorWarning")
        self.sal.salEventSub("MTM1M3_logevent_inclinometerSensorWarning")
        self.sal.salEventSub("MTM1M3_logevent_interlockStatus")
        self.sal.salEventSub("MTM1M3_logevent_interlockWarning")
        self.sal.salEventSub("MTM1M3_logevent_modbusResponse")
        self.sal.salEventSub("MTM1M3_logevent_pidInfo")
        self.sal.salEventSub("MTM1M3_logevent_powerStatus")
        self.sal.salEventSub("MTM1M3_logevent_powerWarning")
        self.sal.salEventSub("MTM1M3_logevent_rejectedAberrationForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedAccelerationForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedActiveOpticForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedAzimuthForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedBalanceForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedCylinderForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedElevationForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedOffsetForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedStaticForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedThermalForces")
        self.sal.salEventSub("MTM1M3_logevent_rejectedVelocityForces")
        self.sal.salEventSub("MTM1M3_logevent_summaryState")

        self.sal.salTelemetrySub("MTM1M3_accelerometerData")
        self.sal.salTelemetrySub("MTM1M3_forceActuatorData")
        self.sal.salTelemetrySub("MTM1M3_gyroData")
        self.sal.salTelemetrySub("MTM1M3_hardpointActuatorData")
        self.sal.salTelemetrySub("MTM1M3_hardpointMonitorData")
        self.sal.salTelemetrySub("MTM1M3_imsData")
        self.sal.salTelemetrySub("MTM1M3_inclinometerData")
        self.sal.salTelemetrySub("MTM1M3_outerLoopData")
        self.sal.salTelemetrySub("MTM1M3_pidData")
        self.sal.salTelemetrySub("MTM1M3_powerSupplyData")

        self.eventSubscribers_settingVersions = []
        self.eventSubscribers_errorCode = []
        self.eventSubscribers_summaryState = []
        self.eventSubscribers_appliedSettingsMatchStart = []
        self.eventSubscribers_accelerometerWarning = []
        self.eventSubscribers_airSupplyStatus = []
        self.eventSubscribers_airSupplyWarning = []
        self.eventSubscribers_appliedAberrationForces = []
        self.eventSubscribers_appliedAccelerationForces = []
        self.eventSubscribers_appliedActiveOpticForces = []
        self.eventSubscribers_appliedAzimuthForces = []
        self.eventSubscribers_appliedBalanceForces = []
        self.eventSubscribers_appliedCylinderForces = []
        self.eventSubscribers_appliedElevationForces = []
        self.eventSubscribers_appliedForces = []
        self.eventSubscribers_appliedHardpointSteps = []
        self.eventSubscribers_appliedOffsetForces = []
        self.eventSubscribers_appliedStaticForces = []
        self.eventSubscribers_appliedThermalForces = []
        self.eventSubscribers_appliedVelocityForces = []
        self.eventSubscribers_cellLightStatus = []
        self.eventSubscribers_cellLightWarning = []
        self.eventSubscribers_detailedState = []
        self.eventSubscribers_displacementSensorWarning = []
        self.eventSubscribers_forceActuatorBackupCalibrationInfo = []
        self.eventSubscribers_forceActuatorILCInfo = []
        self.eventSubscribers_forceActuatorIdInfo = []
        self.eventSubscribers_forceActuatorMainCalibrationInfo = []
        self.eventSubscribers_forceActuatorMezzanineCalibrationInfo = []
        self.eventSubscribers_forceActuatorPositionInfo = []
        self.eventSubscribers_forceActuatorState = []
        self.eventSubscribers_forceActuatorWarning = []
        self.eventSubscribers_gyroWarning = []
        self.eventSubscribers_hardpointActuatorInfo = []
        self.eventSubscribers_hardpointActuatorState = []
        self.eventSubscribers_hardpointActuatorWarning = []
        self.eventSubscribers_hardpointMonitorInfo = []
        self.eventSubscribers_hardpointMonitorState = []
        self.eventSubscribers_hardpointMonitorWarning = []
        self.eventSubscribers_inclinometerSensorWarning = []
        self.eventSubscribers_interlockStatus = []
        self.eventSubscribers_interlockWarning = []
        self.eventSubscribers_modbusResponse = []
        self.eventSubscribers_modbusWarning = []
        self.eventSubscribers_pidInfo = []
        self.eventSubscribers_powerStatus = []
        self.eventSubscribers_powerWarning = []
        self.eventSubscribers_rejectedAberrationForces = []
        self.eventSubscribers_rejectedAccelerationForces = []
        self.eventSubscribers_rejectedActiveOpticForces = []
        self.eventSubscribers_rejectedAzimuthForces = []
        self.eventSubscribers_rejectedBalanceForces = []
        self.eventSubscribers_rejectedCylinderForces = []
        self.eventSubscribers_rejectedElevationForces = []
        self.eventSubscribers_rejectedForces = []
        self.eventSubscribers_rejectedOffsetForces = []
        self.eventSubscribers_rejectedStaticForces = []
        self.eventSubscribers_rejectedThermalForces = []
        self.eventSubscribers_rejectedVelocityForces = []

        self.telemetrySubscribers_accelerometerData = []
        self.telemetrySubscribers_forceActuatorData = []
        self.telemetrySubscribers_forceActuatorPressure = []
        self.telemetrySubscribers_gyroData = []
        self.telemetrySubscribers_hardpointActuatorData = []
        self.telemetrySubscribers_hardpointMonitorData = []
        self.telemetrySubscribers_imsData = []
        self.telemetrySubscribers_inclinometerData = []
        self.telemetrySubscribers_outerLoopData = []
        self.telemetrySubscribers_pidData = []
        self.telemetrySubscribers_powerData = []

        self.topicsSubscribedToo = {}

    def close(self):
        time.sleep(1)
        self.sal.salShutdown()

    def flush(self, action):
        result, data = action()
        while result >= 0:
            result, data = action()
            
    def checkForSubscriber(self, action, subscribers):
        buffer = []
        result, data = action()
        while result == 0:
            buffer.append(data)
            result, data = action()
        if len(buffer) > 0:
            for subscriber in subscribers:
                subscriber(buffer)
            
    def runSubscriberChecks(self):
        for subscribedTopic in self.topicsSubscribedToo:
            action = self.topicsSubscribedToo[subscribedTopic][0]
            subscribers = self.topicsSubscribedToo[subscribedTopic][1]
            self.checkForSubscriber(action, subscribers)
            
    def getEvent(self, action):
        lastResult, lastData = action()
        while lastResult >= 0:
            result, data = action()
            if result >= 0:
                lastResult = result
                lastData = data
            elif result < 0:
                break
        return lastResult, lastData

    def getTimestamp(self):
        return self.sal.getCurrentTime()

    def issueCommand_abort(self, value):
        data = MTM1M3_command_abortC()
        data.value = value

        return self.sal.issueCommand_abort(data)

    def getResponse_abort(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_abort(data)
        return result, data
        
    def waitForCompletion_abort(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_abort(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_abort()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_abort(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_abort(value)
        return self.waitForCompletion_abort(cmdId, timeoutInSeconds)

    def issueCommand_enable(self, value):
        data = MTM1M3_command_enableC()
        data.value = value

        return self.sal.issueCommand_enable(data)

    def getResponse_enable(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_enable(data)
        return result, data
        
    def waitForCompletion_enable(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_enable(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_enable()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_enable(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_enable(value)
        return self.waitForCompletion_enable(cmdId, timeoutInSeconds)

    def issueCommand_disable(self, value):
        data = MTM1M3_command_disableC()
        data.value = value

        return self.sal.issueCommand_disable(data)

    def getResponse_disable(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_disable(data)
        return result, data
        
    def waitForCompletion_disable(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_disable(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_disable()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_disable(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_disable(value)
        return self.waitForCompletion_disable(cmdId, timeoutInSeconds)

    def issueCommand_standby(self, value):
        data = MTM1M3_command_standbyC()
        data.value = value

        return self.sal.issueCommand_standby(data)

    def getResponse_standby(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_standby(data)
        return result, data
        
    def waitForCompletion_standby(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_standby(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_standby()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_standby(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_standby(value)
        return self.waitForCompletion_standby(cmdId, timeoutInSeconds)

    def issueCommand_exitControl(self, value):
        data = MTM1M3_command_exitControlC()
        data.value = value

        return self.sal.issueCommand_exitControl(data)

    def getResponse_exitControl(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_exitControl(data)
        return result, data
        
    def waitForCompletion_exitControl(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_exitControl(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_exitControl()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_exitControl(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_exitControl(value)
        return self.waitForCompletion_exitControl(cmdId, timeoutInSeconds)

    def issueCommand_start(self, settingsToApply):
        data = MTM1M3_command_startC()
        data.settingsToApply = settingsToApply

        return self.sal.issueCommand_start(data)

    def getResponse_start(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_start(data)
        return result, data
        
    def waitForCompletion_start(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_start(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_start()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_start(self, settingsToApply, timeoutInSeconds = 10):
        cmdId = self.issueCommand_start(settingsToApply)
        return self.waitForCompletion_start(cmdId, timeoutInSeconds)

    def issueCommand_enterControl(self, value):
        data = MTM1M3_command_enterControlC()
        data.value = value

        return self.sal.issueCommand_enterControl(data)

    def getResponse_enterControl(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_enterControl(data)
        return result, data
        
    def waitForCompletion_enterControl(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_enterControl(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_enterControl()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_enterControl(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_enterControl(value)
        return self.waitForCompletion_enterControl(cmdId, timeoutInSeconds)

    def issueCommand_setValue(self, parametersAndValues):
        data = MTM1M3_command_setValueC()
        data.parametersAndValues = parametersAndValues

        return self.sal.issueCommand_setValue(data)

    def getResponse_setValue(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_setValue(data)
        return result, data
        
    def waitForCompletion_setValue(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_setValue(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_setValue()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_setValue(self, parametersAndValues, timeoutInSeconds = 10):
        cmdId = self.issueCommand_setValue(parametersAndValues)
        return self.waitForCompletion_setValue(cmdId, timeoutInSeconds)

    def issueCommand_abortRaiseM1M3(self, value):
        data = MTM1M3_command_abortRaiseM1M3C()
        data.value = value

        return self.sal.issueCommand_abortRaiseM1M3(data)

    def getResponse_abortRaiseM1M3(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_abortRaiseM1M3(data)
        return result, data
        
    def waitForCompletion_abortRaiseM1M3(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_abortRaiseM1M3(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_abortRaiseM1M3()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_abortRaiseM1M3(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_abortRaiseM1M3(value)
        return self.waitForCompletion_abortRaiseM1M3(cmdId, timeoutInSeconds)

    def issueCommand_applyAberrationForces(self, zForces):
        data = MTM1M3_command_applyAberrationForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]

        return self.sal.issueCommand_applyAberrationForces(data)

    def getResponse_applyAberrationForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyAberrationForces(data)
        return result, data
        
    def waitForCompletion_applyAberrationForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyAberrationForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyAberrationForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyAberrationForces(self, zForces, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyAberrationForces(zForces)
        return self.waitForCompletion_applyAberrationForces(cmdId, timeoutInSeconds)

    def issueCommand_applyAberrationForcesByBendingModes(self, coefficients):
        data = MTM1M3_command_applyAberrationForcesByBendingModesC()
        for i in range(22):
            data.coefficients[i] = coefficients[i]

        return self.sal.issueCommand_applyAberrationForcesByBendingModes(data)

    def getResponse_applyAberrationForcesByBendingModes(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyAberrationForcesByBendingModes(data)
        return result, data
        
    def waitForCompletion_applyAberrationForcesByBendingModes(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyAberrationForcesByBendingModes(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyAberrationForcesByBendingModes()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyAberrationForcesByBendingModes(self, coefficients, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyAberrationForcesByBendingModes(coefficients)
        return self.waitForCompletion_applyAberrationForcesByBendingModes(cmdId, timeoutInSeconds)

    def issueCommand_applyActiveOpticForces(self, zForces):
        data = MTM1M3_command_applyActiveOpticForcesC()
        for i in range(156):
            data.zForces[i] = zForces[i]

        return self.sal.issueCommand_applyActiveOpticForces(data)

    def getResponse_applyActiveOpticForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyActiveOpticForces(data)
        return result, data
        
    def waitForCompletion_applyActiveOpticForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyActiveOpticForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyActiveOpticForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyActiveOpticForces(self, zForces, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyActiveOpticForces(zForces)
        return self.waitForCompletion_applyActiveOpticForces(cmdId, timeoutInSeconds)

    def issueCommand_applyActiveOpticForcesByBendingModes(self, coefficients):
        data = MTM1M3_command_applyActiveOpticForcesByBendingModesC()
        for i in range(22):
            data.coefficients[i] = coefficients[i]

        return self.sal.issueCommand_applyActiveOpticForcesByBendingModes(data)

    def getResponse_applyActiveOpticForcesByBendingModes(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyActiveOpticForcesByBendingModes(data)
        return result, data
        
    def waitForCompletion_applyActiveOpticForcesByBendingModes(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyActiveOpticForcesByBendingModes(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyActiveOpticForcesByBendingModes()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyActiveOpticForcesByBendingModes(self, coefficients, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyActiveOpticForcesByBendingModes(coefficients)
        return self.waitForCompletion_applyActiveOpticForcesByBendingModes(cmdId, timeoutInSeconds)

    def issueCommand_applyOffsetForces(self, xForces, yForces, zForces):
        data = MTM1M3_command_applyOffsetForcesC()
        for i in range(12):
            data.xForces[i] = xForces[i]
        for i in range(100):
            data.yForces[i] = yForces[i]
        for i in range(156):
            data.zForces[i] = zForces[i]

        return self.sal.issueCommand_applyOffsetForces(data)

    def getResponse_applyOffsetForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyOffsetForces(data)
        return result, data
        
    def waitForCompletion_applyOffsetForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyOffsetForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyOffsetForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyOffsetForces(self, xForces, yForces, zForces, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyOffsetForces(xForces, yForces, zForces)
        return self.waitForCompletion_applyOffsetForces(cmdId, timeoutInSeconds)

    def issueCommand_applyOffsetForcesByMirrorForce(self, xForce, yForce, zForce, xMoment, yMoment, zMoment):
        data = MTM1M3_command_applyOffsetForcesByMirrorForceC()
        data.xForce = xForce
        data.yForce = yForce
        data.zForce = zForce
        data.xMoment = xMoment
        data.yMoment = yMoment
        data.zMoment = zMoment

        return self.sal.issueCommand_applyOffsetForcesByMirrorForce(data)

    def getResponse_applyOffsetForcesByMirrorForce(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_applyOffsetForcesByMirrorForce(data)
        return result, data
        
    def waitForCompletion_applyOffsetForcesByMirrorForce(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_applyOffsetForcesByMirrorForce(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_applyOffsetForcesByMirrorForce()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_applyOffsetForcesByMirrorForce(self, xForce, yForce, zForce, xMoment, yMoment, zMoment, timeoutInSeconds = 10):
        cmdId = self.issueCommand_applyOffsetForcesByMirrorForce(xForce, yForce, zForce, xMoment, yMoment, zMoment)
        return self.waitForCompletion_applyOffsetForcesByMirrorForce(cmdId, timeoutInSeconds)

    def issueCommand_clearAberrationForces(self, value):
        data = MTM1M3_command_clearAberrationForcesC()
        data.value = value

        return self.sal.issueCommand_clearAberrationForces(data)

    def getResponse_clearAberrationForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_clearAberrationForces(data)
        return result, data
        
    def waitForCompletion_clearAberrationForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_clearAberrationForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_clearAberrationForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_clearAberrationForces(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_clearAberrationForces(value)
        return self.waitForCompletion_clearAberrationForces(cmdId, timeoutInSeconds)

    def issueCommand_clearActiveOpticForces(self, value):
        data = MTM1M3_command_clearActiveOpticForcesC()
        data.value = value

        return self.sal.issueCommand_clearActiveOpticForces(data)

    def getResponse_clearActiveOpticForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_clearActiveOpticForces(data)
        return result, data
        
    def waitForCompletion_clearActiveOpticForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_clearActiveOpticForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_clearActiveOpticForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_clearActiveOpticForces(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_clearActiveOpticForces(value)
        return self.waitForCompletion_clearActiveOpticForces(cmdId, timeoutInSeconds)

    def issueCommand_clearOffsetForces(self, value):
        data = MTM1M3_command_clearOffsetForcesC()
        data.value = value

        return self.sal.issueCommand_clearOffsetForces(data)

    def getResponse_clearOffsetForces(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_clearOffsetForces(data)
        return result, data
        
    def waitForCompletion_clearOffsetForces(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_clearOffsetForces(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_clearOffsetForces()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_clearOffsetForces(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_clearOffsetForces(value)
        return self.waitForCompletion_clearOffsetForces(cmdId, timeoutInSeconds)

    def issueCommand_disableHardpointChase(self, hardpointActuator):
        data = MTM1M3_command_disableHardpointChaseC()
        data.hardpointActuator = hardpointActuator

        return self.sal.issueCommand_disableHardpointChase(data)

    def getResponse_disableHardpointChase(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_disableHardpointChase(data)
        return result, data
        
    def waitForCompletion_disableHardpointChase(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_disableHardpointChase(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_disableHardpointChase()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_disableHardpointChase(self, hardpointActuator, timeoutInSeconds = 10):
        cmdId = self.issueCommand_disableHardpointChase(hardpointActuator)
        return self.waitForCompletion_disableHardpointChase(cmdId, timeoutInSeconds)

    def issueCommand_disableHardpointCorrections(self, value):
        data = MTM1M3_command_disableHardpointCorrectionsC()
        data.value = value

        return self.sal.issueCommand_disableHardpointCorrections(data)

    def getResponse_disableHardpointCorrections(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_disableHardpointCorrections(data)
        return result, data
        
    def waitForCompletion_disableHardpointCorrections(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_disableHardpointCorrections(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_disableHardpointCorrections()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_disableHardpointCorrections(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_disableHardpointCorrections(value)
        return self.waitForCompletion_disableHardpointCorrections(cmdId, timeoutInSeconds)

    def issueCommand_enableHardpointChase(self, hardpointActuator):
        data = MTM1M3_command_enableHardpointChaseC()
        data.hardpointActuator = hardpointActuator

        return self.sal.issueCommand_enableHardpointChase(data)

    def getResponse_enableHardpointChase(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_enableHardpointChase(data)
        return result, data
        
    def waitForCompletion_enableHardpointChase(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_enableHardpointChase(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_enableHardpointChase()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_enableHardpointChase(self, hardpointActuator, timeoutInSeconds = 10):
        cmdId = self.issueCommand_enableHardpointChase(hardpointActuator)
        return self.waitForCompletion_enableHardpointChase(cmdId, timeoutInSeconds)

    def issueCommand_enableHardpointCorrections(self, value):
        data = MTM1M3_command_enableHardpointCorrectionsC()
        data.value = value

        return self.sal.issueCommand_enableHardpointCorrections(data)

    def getResponse_enableHardpointCorrections(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_enableHardpointCorrections(data)
        return result, data
        
    def waitForCompletion_enableHardpointCorrections(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_enableHardpointCorrections(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_enableHardpointCorrections()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_enableHardpointCorrections(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_enableHardpointCorrections(value)
        return self.waitForCompletion_enableHardpointCorrections(cmdId, timeoutInSeconds)

    def issueCommand_enterEngineering(self, value):
        data = MTM1M3_command_enterEngineeringC()
        data.value = value

        return self.sal.issueCommand_enterEngineering(data)

    def getResponse_enterEngineering(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_enterEngineering(data)
        return result, data
        
    def waitForCompletion_enterEngineering(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_enterEngineering(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_enterEngineering()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_enterEngineering(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_enterEngineering(value)
        return self.waitForCompletion_enterEngineering(cmdId, timeoutInSeconds)

    def issueCommand_exitEngineering(self, value):
        data = MTM1M3_command_exitEngineeringC()
        data.value = value

        return self.sal.issueCommand_exitEngineering(data)

    def getResponse_exitEngineering(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_exitEngineering(data)
        return result, data
        
    def waitForCompletion_exitEngineering(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_exitEngineering(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_exitEngineering()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_exitEngineering(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_exitEngineering(value)
        return self.waitForCompletion_exitEngineering(cmdId, timeoutInSeconds)

    def issueCommand_lowerM1M3(self, value):
        data = MTM1M3_command_lowerM1M3C()
        data.value = value

        return self.sal.issueCommand_lowerM1M3(data)

    def getResponse_lowerM1M3(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_lowerM1M3(data)
        return result, data
        
    def waitForCompletion_lowerM1M3(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_lowerM1M3(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_lowerM1M3()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_lowerM1M3(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_lowerM1M3(value)
        return self.waitForCompletion_lowerM1M3(cmdId, timeoutInSeconds)

    def issueCommand_modbusTransmit(self, actuatorId, functionCode, data, dataLength):
        data = MTM1M3_command_modbusTransmitC()
        data.actuatorId = actuatorId
        data.functionCode = functionCode
        for i in range(252):
            data.data[i] = data[i]
        data.dataLength = dataLength

        return self.sal.issueCommand_modbusTransmit(data)

    def getResponse_modbusTransmit(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_modbusTransmit(data)
        return result, data
        
    def waitForCompletion_modbusTransmit(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_modbusTransmit(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_modbusTransmit()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_modbusTransmit(self, actuatorId, functionCode, data, dataLength, timeoutInSeconds = 10):
        cmdId = self.issueCommand_modbusTransmit(actuatorId, functionCode, data, dataLength)
        return self.waitForCompletion_modbusTransmit(cmdId, timeoutInSeconds)

    def issueCommand_moveHardpointActuators(self, steps):
        data = MTM1M3_command_moveHardpointActuatorsC()
        for i in range(6):
            data.steps[i] = steps[i]

        return self.sal.issueCommand_moveHardpointActuators(data)

    def getResponse_moveHardpointActuators(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_moveHardpointActuators(data)
        return result, data
        
    def waitForCompletion_moveHardpointActuators(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_moveHardpointActuators(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_moveHardpointActuators()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_moveHardpointActuators(self, steps, timeoutInSeconds = 10):
        cmdId = self.issueCommand_moveHardpointActuators(steps)
        return self.waitForCompletion_moveHardpointActuators(cmdId, timeoutInSeconds)

    def issueCommand_positionM1M3(self, xPosition, yPosition, zPosition, xRotation, yRotation, zRotation):
        data = MTM1M3_command_positionM1M3C()
        data.xPosition = xPosition
        data.yPosition = yPosition
        data.zPosition = zPosition
        data.xRotation = xRotation
        data.yRotation = yRotation
        data.zRotation = zRotation

        return self.sal.issueCommand_positionM1M3(data)

    def getResponse_positionM1M3(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_positionM1M3(data)
        return result, data
        
    def waitForCompletion_positionM1M3(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_positionM1M3(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_positionM1M3()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_positionM1M3(self, xPosition, yPosition, zPosition, xRotation, yRotation, zRotation, timeoutInSeconds = 10):
        cmdId = self.issueCommand_positionM1M3(xPosition, yPosition, zPosition, xRotation, yRotation, zRotation)
        return self.waitForCompletion_positionM1M3(cmdId, timeoutInSeconds)

    def issueCommand_programILC(self, actuatorId, filePath):
        data = MTM1M3_command_programILCC()
        data.actuatorId = actuatorId
        data.filePath = filePath

        return self.sal.issueCommand_programILC(data)

    def getResponse_programILC(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_programILC(data)
        return result, data
        
    def waitForCompletion_programILC(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_programILC(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_programILC()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_programILC(self, actuatorId, filePath, timeoutInSeconds = 10):
        cmdId = self.issueCommand_programILC(actuatorId, filePath)
        return self.waitForCompletion_programILC(cmdId, timeoutInSeconds)

    def issueCommand_raiseM1M3(self, bypassReferencePosition):
        data = MTM1M3_command_raiseM1M3C()
        data.bypassReferencePosition = bypassReferencePosition

        return self.sal.issueCommand_raiseM1M3(data)

    def getResponse_raiseM1M3(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_raiseM1M3(data)
        return result, data
        
    def waitForCompletion_raiseM1M3(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_raiseM1M3(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_raiseM1M3()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_raiseM1M3(self, bypassReferencePosition, timeoutInSeconds = 10):
        cmdId = self.issueCommand_raiseM1M3(bypassReferencePosition)
        return self.waitForCompletion_raiseM1M3(cmdId, timeoutInSeconds)

    def issueCommand_resetPID(self, pid):
        data = MTM1M3_command_resetPIDC()
        data.pid = pid

        return self.sal.issueCommand_resetPID(data)

    def getResponse_resetPID(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_resetPID(data)
        return result, data
        
    def waitForCompletion_resetPID(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_resetPID(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_resetPID()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_resetPID(self, pid, timeoutInSeconds = 10):
        cmdId = self.issueCommand_resetPID(pid)
        return self.waitForCompletion_resetPID(cmdId, timeoutInSeconds)

    def issueCommand_shutdown(self, value):
        data = MTM1M3_command_shutdownC()
        data.value = value

        return self.sal.issueCommand_shutdown(data)

    def getResponse_shutdown(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_shutdown(data)
        return result, data
        
    def waitForCompletion_shutdown(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_shutdown(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_shutdown()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_shutdown(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_shutdown(value)
        return self.waitForCompletion_shutdown(cmdId, timeoutInSeconds)

    def issueCommand_stopHardpointMotion(self, value):
        data = MTM1M3_command_stopHardpointMotionC()
        data.value = value

        return self.sal.issueCommand_stopHardpointMotion(data)

    def getResponse_stopHardpointMotion(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_stopHardpointMotion(data)
        return result, data
        
    def waitForCompletion_stopHardpointMotion(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_stopHardpointMotion(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_stopHardpointMotion()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_stopHardpointMotion(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_stopHardpointMotion(value)
        return self.waitForCompletion_stopHardpointMotion(cmdId, timeoutInSeconds)

    def issueCommand_testAir(self, value):
        data = MTM1M3_command_testAirC()
        data.value = value

        return self.sal.issueCommand_testAir(data)

    def getResponse_testAir(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_testAir(data)
        return result, data
        
    def waitForCompletion_testAir(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_testAir(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_testAir()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_testAir(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_testAir(value)
        return self.waitForCompletion_testAir(cmdId, timeoutInSeconds)

    def issueCommand_testForceActuator(self, forceActuator):
        data = MTM1M3_command_testForceActuatorC()
        data.forceActuator = forceActuator

        return self.sal.issueCommand_testForceActuator(data)

    def getResponse_testForceActuator(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_testForceActuator(data)
        return result, data
        
    def waitForCompletion_testForceActuator(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_testForceActuator(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_testForceActuator()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_testForceActuator(self, forceActuator, timeoutInSeconds = 10):
        cmdId = self.issueCommand_testForceActuator(forceActuator)
        return self.waitForCompletion_testForceActuator(cmdId, timeoutInSeconds)

    def issueCommand_testHardpoint(self, hardpointActuator):
        data = MTM1M3_command_testHardpointC()
        data.hardpointActuator = hardpointActuator

        return self.sal.issueCommand_testHardpoint(data)

    def getResponse_testHardpoint(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_testHardpoint(data)
        return result, data
        
    def waitForCompletion_testHardpoint(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_testHardpoint(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_testHardpoint()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_testHardpoint(self, hardpointActuator, timeoutInSeconds = 10):
        cmdId = self.issueCommand_testHardpoint(hardpointActuator)
        return self.waitForCompletion_testHardpoint(cmdId, timeoutInSeconds)

    def issueCommand_translateM1M3(self, xTranslation, yTranslation, zTranslation, xRotation, yRotation, zRotation):
        data = MTM1M3_command_translateM1M3C()
        data.xTranslation = xTranslation
        data.yTranslation = yTranslation
        data.zTranslation = zTranslation
        data.xRotation = xRotation
        data.yRotation = yRotation
        data.zRotation = zRotation

        return self.sal.issueCommand_translateM1M3(data)

    def getResponse_translateM1M3(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_translateM1M3(data)
        return result, data
        
    def waitForCompletion_translateM1M3(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_translateM1M3(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_translateM1M3()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_translateM1M3(self, xTranslation, yTranslation, zTranslation, xRotation, yRotation, zRotation, timeoutInSeconds = 10):
        cmdId = self.issueCommand_translateM1M3(xTranslation, yTranslation, zTranslation, xRotation, yRotation, zRotation)
        return self.waitForCompletion_translateM1M3(cmdId, timeoutInSeconds)

    def issueCommand_turnAirOff(self, value):
        data = MTM1M3_command_turnAirOffC()
        data.value = value

        return self.sal.issueCommand_turnAirOff(data)

    def getResponse_turnAirOff(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnAirOff(data)
        return result, data
        
    def waitForCompletion_turnAirOff(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnAirOff(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnAirOff()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnAirOff(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnAirOff(value)
        return self.waitForCompletion_turnAirOff(cmdId, timeoutInSeconds)

    def issueCommand_turnAirOn(self, value):
        data = MTM1M3_command_turnAirOnC()
        data.value = value

        return self.sal.issueCommand_turnAirOn(data)

    def getResponse_turnAirOn(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnAirOn(data)
        return result, data
        
    def waitForCompletion_turnAirOn(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnAirOn(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnAirOn()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnAirOn(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnAirOn(value)
        return self.waitForCompletion_turnAirOn(cmdId, timeoutInSeconds)

    def issueCommand_turnLightsOff(self, value):
        data = MTM1M3_command_turnLightsOffC()
        data.value = value

        return self.sal.issueCommand_turnLightsOff(data)

    def getResponse_turnLightsOff(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnLightsOff(data)
        return result, data
        
    def waitForCompletion_turnLightsOff(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnLightsOff(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnLightsOff()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnLightsOff(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnLightsOff(value)
        return self.waitForCompletion_turnLightsOff(cmdId, timeoutInSeconds)

    def issueCommand_turnLightsOn(self, value):
        data = MTM1M3_command_turnLightsOnC()
        data.value = value

        return self.sal.issueCommand_turnLightsOn(data)

    def getResponse_turnLightsOn(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnLightsOn(data)
        return result, data
        
    def waitForCompletion_turnLightsOn(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnLightsOn(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnLightsOn()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnLightsOn(self, value, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnLightsOn(value)
        return self.waitForCompletion_turnLightsOn(cmdId, timeoutInSeconds)

    def issueCommand_turnPowerOff(self, turnPowerNetworkAOff, turnPowerNetworkBOff, turnPowerNetworkCOff, turnPowerNetworkDOff, turnAuxPowerNetworkAOff, turnAuxPowerNetworkBOff, turnAuxPowerNetworkCOff, turnAuxPowerNetworkDOff):
        data = MTM1M3_command_turnPowerOffC()
        data.turnPowerNetworkAOff = turnPowerNetworkAOff
        data.turnPowerNetworkBOff = turnPowerNetworkBOff
        data.turnPowerNetworkCOff = turnPowerNetworkCOff
        data.turnPowerNetworkDOff = turnPowerNetworkDOff
        data.turnAuxPowerNetworkAOff = turnAuxPowerNetworkAOff
        data.turnAuxPowerNetworkBOff = turnAuxPowerNetworkBOff
        data.turnAuxPowerNetworkCOff = turnAuxPowerNetworkCOff
        data.turnAuxPowerNetworkDOff = turnAuxPowerNetworkDOff

        return self.sal.issueCommand_turnPowerOff(data)

    def getResponse_turnPowerOff(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnPowerOff(data)
        return result, data
        
    def waitForCompletion_turnPowerOff(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnPowerOff(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnPowerOff()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnPowerOff(self, turnPowerNetworkAOff, turnPowerNetworkBOff, turnPowerNetworkCOff, turnPowerNetworkDOff, turnAuxPowerNetworkAOff, turnAuxPowerNetworkBOff, turnAuxPowerNetworkCOff, turnAuxPowerNetworkDOff, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnPowerOff(turnPowerNetworkAOff, turnPowerNetworkBOff, turnPowerNetworkCOff, turnPowerNetworkDOff, turnAuxPowerNetworkAOff, turnAuxPowerNetworkBOff, turnAuxPowerNetworkCOff, turnAuxPowerNetworkDOff)
        return self.waitForCompletion_turnPowerOff(cmdId, timeoutInSeconds)

    def issueCommand_turnPowerOn(self, turnPowerNetworkAOn, turnPowerNetworkBOn, turnPowerNetworkCOn, turnPowerNetworkDOn, turnAuxPowerNetworkAOn, turnAuxPowerNetworkBOn, turnAuxPowerNetworkCOn, turnAuxPowerNetworkDOn):
        data = MTM1M3_command_turnPowerOnC()
        data.turnPowerNetworkAOn = turnPowerNetworkAOn
        data.turnPowerNetworkBOn = turnPowerNetworkBOn
        data.turnPowerNetworkCOn = turnPowerNetworkCOn
        data.turnPowerNetworkDOn = turnPowerNetworkDOn
        data.turnAuxPowerNetworkAOn = turnAuxPowerNetworkAOn
        data.turnAuxPowerNetworkBOn = turnAuxPowerNetworkBOn
        data.turnAuxPowerNetworkCOn = turnAuxPowerNetworkCOn
        data.turnAuxPowerNetworkDOn = turnAuxPowerNetworkDOn

        return self.sal.issueCommand_turnPowerOn(data)

    def getResponse_turnPowerOn(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_turnPowerOn(data)
        return result, data
        
    def waitForCompletion_turnPowerOn(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_turnPowerOn(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_turnPowerOn()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_turnPowerOn(self, turnPowerNetworkAOn, turnPowerNetworkBOn, turnPowerNetworkCOn, turnPowerNetworkDOn, turnAuxPowerNetworkAOn, turnAuxPowerNetworkBOn, turnAuxPowerNetworkCOn, turnAuxPowerNetworkDOn, timeoutInSeconds = 10):
        cmdId = self.issueCommand_turnPowerOn(turnPowerNetworkAOn, turnPowerNetworkBOn, turnPowerNetworkCOn, turnPowerNetworkDOn, turnAuxPowerNetworkAOn, turnAuxPowerNetworkBOn, turnAuxPowerNetworkCOn, turnAuxPowerNetworkDOn)
        return self.waitForCompletion_turnPowerOn(cmdId, timeoutInSeconds)

    def issueCommand_updatePID(self, pid, timestep, p, i, d, n):
        data = MTM1M3_command_updatePIDC()
        data.pid = pid
        data.timestep = timestep
        data.p = p
        data.i = i
        data.d = d
        data.n = n

        return self.sal.issueCommand_updatePID(data)

    def getResponse_updatePID(self):
        data = MTM1M3_ackcmdC()
        result = self.sal.getResponse_updatePID(data)
        return result, data
        
    def waitForCompletion_updatePID(self, cmdId, timeoutInSeconds = 10):
        waitResult = self.sal.waitForCompletion_updatePID(cmdId, timeoutInSeconds)
        #ackResult, ack = self.getResponse_updatePID()
        #return waitResult, ackResult, ack
        return waitResult
        
    def issueCommandThenWait_updatePID(self, pid, timestep, p, i, d, n, timeoutInSeconds = 10):
        cmdId = self.issueCommand_updatePID(pid, timestep, p, i, d, n)
        return self.waitForCompletion_updatePID(cmdId, timeoutInSeconds)



    def getNextEvent_settingVersions(self):
        data = MTM1M3_logevent_settingVersionsC()
        result = self.sal.getEvent_settingVersions(data)
        return result, data
        
    def getEvent_settingVersions(self):
        return self.getEvent(self.getNextEvent_settingVersions)
        
    def subscribeEvent_settingVersions(self, action):
        self.eventSubscribers_settingVersions.append(action)
        if "event_settingVersions" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_settingVersions"] = [self.getNextEvent_settingVersions, self.eventSubscribers_settingVersions]

    def getNextEvent_errorCode(self):
        data = MTM1M3_logevent_errorCodeC()
        result = self.sal.getEvent_errorCode(data)
        return result, data
        
    def getEvent_errorCode(self):
        return self.getEvent(self.getNextEvent_errorCode)
        
    def subscribeEvent_errorCode(self, action):
        self.eventSubscribers_errorCode.append(action)
        if "event_errorCode" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_errorCode"] = [self.getNextEvent_errorCode, self.eventSubscribers_errorCode]

    def getNextEvent_summaryState(self):
        data = MTM1M3_logevent_summaryStateC()
        result = self.sal.getEvent_summaryState(data)
        return result, data
        
    def getEvent_summaryState(self):
        return self.getEvent(self.getNextEvent_summaryState)
        
    def subscribeEvent_summaryState(self, action):
        self.eventSubscribers_summaryState.append(action)
        if "event_summaryState" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_summaryState"] = [self.getNextEvent_summaryState, self.eventSubscribers_summaryState]

    def getNextEvent_appliedSettingsMatchStart(self):
        data = MTM1M3_logevent_appliedSettingsMatchStartC()
        result = self.sal.getEvent_appliedSettingsMatchStart(data)
        return result, data
        
    def getEvent_appliedSettingsMatchStart(self):
        return self.getEvent(self.getNextEvent_appliedSettingsMatchStart)
        
    def subscribeEvent_appliedSettingsMatchStart(self, action):
        self.eventSubscribers_appliedSettingsMatchStart.append(action)
        if "event_appliedSettingsMatchStart" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedSettingsMatchStart"] = [self.getNextEvent_appliedSettingsMatchStart, self.eventSubscribers_appliedSettingsMatchStart]

    def getNextEvent_accelerometerWarning(self):
        data = MTM1M3_logevent_accelerometerWarningC()
        result = self.sal.getEvent_accelerometerWarning(data)
        return result, data
        
    def getEvent_accelerometerWarning(self):
        return self.getEvent(self.getNextEvent_accelerometerWarning)
        
    def subscribeEvent_accelerometerWarning(self, action):
        self.eventSubscribers_accelerometerWarning.append(action)
        if "event_accelerometerWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_accelerometerWarning"] = [self.getNextEvent_accelerometerWarning, self.eventSubscribers_accelerometerWarning]

    def getNextEvent_airSupplyStatus(self):
        data = MTM1M3_logevent_airSupplyStatusC()
        result = self.sal.getEvent_airSupplyStatus(data)
        return result, data
        
    def getEvent_airSupplyStatus(self):
        return self.getEvent(self.getNextEvent_airSupplyStatus)
        
    def subscribeEvent_airSupplyStatus(self, action):
        self.eventSubscribers_airSupplyStatus.append(action)
        if "event_airSupplyStatus" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_airSupplyStatus"] = [self.getNextEvent_airSupplyStatus, self.eventSubscribers_airSupplyStatus]

    def getNextEvent_airSupplyWarning(self):
        data = MTM1M3_logevent_airSupplyWarningC()
        result = self.sal.getEvent_airSupplyWarning(data)
        return result, data
        
    def getEvent_airSupplyWarning(self):
        return self.getEvent(self.getNextEvent_airSupplyWarning)
        
    def subscribeEvent_airSupplyWarning(self, action):
        self.eventSubscribers_airSupplyWarning.append(action)
        if "event_airSupplyWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_airSupplyWarning"] = [self.getNextEvent_airSupplyWarning, self.eventSubscribers_airSupplyWarning]

    def getNextEvent_appliedAberrationForces(self):
        data = MTM1M3_logevent_appliedAberrationForcesC()
        result = self.sal.getEvent_appliedAberrationForces(data)
        return result, data
        
    def getEvent_appliedAberrationForces(self):
        return self.getEvent(self.getNextEvent_appliedAberrationForces)
        
    def subscribeEvent_appliedAberrationForces(self, action):
        self.eventSubscribers_appliedAberrationForces.append(action)
        if "event_appliedAberrationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedAberrationForces"] = [self.getNextEvent_appliedAberrationForces, self.eventSubscribers_appliedAberrationForces]

    def getNextEvent_appliedAccelerationForces(self):
        data = MTM1M3_logevent_appliedAccelerationForcesC()
        result = self.sal.getEvent_appliedAccelerationForces(data)
        return result, data
        
    def getEvent_appliedAccelerationForces(self):
        return self.getEvent(self.getNextEvent_appliedAccelerationForces)
        
    def subscribeEvent_appliedAccelerationForces(self, action):
        self.eventSubscribers_appliedAccelerationForces.append(action)
        if "event_appliedAccelerationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedAccelerationForces"] = [self.getNextEvent_appliedAccelerationForces, self.eventSubscribers_appliedAccelerationForces]

    def getNextEvent_appliedActiveOpticForces(self):
        data = MTM1M3_logevent_appliedActiveOpticForcesC()
        result = self.sal.getEvent_appliedActiveOpticForces(data)
        return result, data
        
    def getEvent_appliedActiveOpticForces(self):
        return self.getEvent(self.getNextEvent_appliedActiveOpticForces)
        
    def subscribeEvent_appliedActiveOpticForces(self, action):
        self.eventSubscribers_appliedActiveOpticForces.append(action)
        if "event_appliedActiveOpticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedActiveOpticForces"] = [self.getNextEvent_appliedActiveOpticForces, self.eventSubscribers_appliedActiveOpticForces]

    def getNextEvent_appliedAzimuthForces(self):
        data = MTM1M3_logevent_appliedAzimuthForcesC()
        result = self.sal.getEvent_appliedAzimuthForces(data)
        return result, data
        
    def getEvent_appliedAzimuthForces(self):
        return self.getEvent(self.getNextEvent_appliedAzimuthForces)
        
    def subscribeEvent_appliedAzimuthForces(self, action):
        self.eventSubscribers_appliedAzimuthForces.append(action)
        if "event_appliedAzimuthForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedAzimuthForces"] = [self.getNextEvent_appliedAzimuthForces, self.eventSubscribers_appliedAzimuthForces]

    def getNextEvent_appliedBalanceForces(self):
        data = MTM1M3_logevent_appliedBalanceForcesC()
        result = self.sal.getEvent_appliedBalanceForces(data)
        return result, data
        
    def getEvent_appliedBalanceForces(self):
        return self.getEvent(self.getNextEvent_appliedBalanceForces)
        
    def subscribeEvent_appliedBalanceForces(self, action):
        self.eventSubscribers_appliedBalanceForces.append(action)
        if "event_appliedBalanceForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedBalanceForces"] = [self.getNextEvent_appliedBalanceForces, self.eventSubscribers_appliedBalanceForces]

    def getNextEvent_appliedCylinderForces(self):
        data = MTM1M3_logevent_appliedCylinderForcesC()
        result = self.sal.getEvent_appliedCylinderForces(data)
        return result, data
        
    def getEvent_appliedCylinderForces(self):
        return self.getEvent(self.getNextEvent_appliedCylinderForces)
        
    def subscribeEvent_appliedCylinderForces(self, action):
        self.eventSubscribers_appliedCylinderForces.append(action)
        if "event_appliedCylinderForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedCylinderForces"] = [self.getNextEvent_appliedCylinderForces, self.eventSubscribers_appliedCylinderForces]

    def getNextEvent_appliedElevationForces(self):
        data = MTM1M3_logevent_appliedElevationForcesC()
        result = self.sal.getEvent_appliedElevationForces(data)
        return result, data
        
    def getEvent_appliedElevationForces(self):
        return self.getEvent(self.getNextEvent_appliedElevationForces)
        
    def subscribeEvent_appliedElevationForces(self, action):
        self.eventSubscribers_appliedElevationForces.append(action)
        if "event_appliedElevationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedElevationForces"] = [self.getNextEvent_appliedElevationForces, self.eventSubscribers_appliedElevationForces]

    def getNextEvent_appliedForces(self):
        data = MTM1M3_logevent_appliedForcesC()
        result = self.sal.getEvent_appliedForces(data)
        return result, data
        
    def getEvent_appliedForces(self):
        return self.getEvent(self.getNextEvent_appliedForces)
        
    def subscribeEvent_appliedForces(self, action):
        self.eventSubscribers_appliedForces.append(action)
        if "event_appliedForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedForces"] = [self.getNextEvent_appliedForces, self.eventSubscribers_appliedForces]

    def getNextEvent_appliedHardpointSteps(self):
        data = MTM1M3_logevent_appliedHardpointStepsC()
        result = self.sal.getEvent_appliedHardpointSteps(data)
        return result, data
        
    def getEvent_appliedHardpointSteps(self):
        return self.getEvent(self.getNextEvent_appliedHardpointSteps)
        
    def subscribeEvent_appliedHardpointSteps(self, action):
        self.eventSubscribers_appliedHardpointSteps.append(action)
        if "event_appliedHardpointSteps" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedHardpointSteps"] = [self.getNextEvent_appliedHardpointSteps, self.eventSubscribers_appliedHardpointSteps]

    def getNextEvent_appliedOffsetForces(self):
        data = MTM1M3_logevent_appliedOffsetForcesC()
        result = self.sal.getEvent_appliedOffsetForces(data)
        return result, data
        
    def getEvent_appliedOffsetForces(self):
        return self.getEvent(self.getNextEvent_appliedOffsetForces)
        
    def subscribeEvent_appliedOffsetForces(self, action):
        self.eventSubscribers_appliedOffsetForces.append(action)
        if "event_appliedOffsetForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedOffsetForces"] = [self.getNextEvent_appliedOffsetForces, self.eventSubscribers_appliedOffsetForces]

    def getNextEvent_appliedStaticForces(self):
        data = MTM1M3_logevent_appliedStaticForcesC()
        result = self.sal.getEvent_appliedStaticForces(data)
        return result, data
        
    def getEvent_appliedStaticForces(self):
        return self.getEvent(self.getNextEvent_appliedStaticForces)
        
    def subscribeEvent_appliedStaticForces(self, action):
        self.eventSubscribers_appliedStaticForces.append(action)
        if "event_appliedStaticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedStaticForces"] = [self.getNextEvent_appliedStaticForces, self.eventSubscribers_appliedStaticForces]

    def getNextEvent_appliedThermalForces(self):
        data = MTM1M3_logevent_appliedThermalForcesC()
        result = self.sal.getEvent_appliedThermalForces(data)
        return result, data
        
    def getEvent_appliedThermalForces(self):
        return self.getEvent(self.getNextEvent_appliedThermalForces)
        
    def subscribeEvent_appliedThermalForces(self, action):
        self.eventSubscribers_appliedThermalForces.append(action)
        if "event_appliedThermalForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedThermalForces"] = [self.getNextEvent_appliedThermalForces, self.eventSubscribers_appliedThermalForces]

    def getNextEvent_appliedVelocityForces(self):
        data = MTM1M3_logevent_appliedVelocityForcesC()
        result = self.sal.getEvent_appliedVelocityForces(data)
        return result, data
        
    def getEvent_appliedVelocityForces(self):
        return self.getEvent(self.getNextEvent_appliedVelocityForces)
        
    def subscribeEvent_appliedVelocityForces(self, action):
        self.eventSubscribers_appliedVelocityForces.append(action)
        if "event_appliedVelocityForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_appliedVelocityForces"] = [self.getNextEvent_appliedVelocityForces, self.eventSubscribers_appliedVelocityForces]

    def getNextEvent_cellLightStatus(self):
        data = MTM1M3_logevent_cellLightStatusC()
        result = self.sal.getEvent_cellLightStatus(data)
        return result, data
        
    def getEvent_cellLightStatus(self):
        return self.getEvent(self.getNextEvent_cellLightStatus)
        
    def subscribeEvent_cellLightStatus(self, action):
        self.eventSubscribers_cellLightStatus.append(action)
        if "event_cellLightStatus" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_cellLightStatus"] = [self.getNextEvent_cellLightStatus, self.eventSubscribers_cellLightStatus]

    def getNextEvent_cellLightWarning(self):
        data = MTM1M3_logevent_cellLightWarningC()
        result = self.sal.getEvent_cellLightWarning(data)
        return result, data
        
    def getEvent_cellLightWarning(self):
        return self.getEvent(self.getNextEvent_cellLightWarning)
        
    def subscribeEvent_cellLightWarning(self, action):
        self.eventSubscribers_cellLightWarning.append(action)
        if "event_cellLightWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_cellLightWarning"] = [self.getNextEvent_cellLightWarning, self.eventSubscribers_cellLightWarning]

    def getNextEvent_detailedState(self):
        data = MTM1M3_logevent_detailedStateC()
        result = self.sal.getEvent_detailedState(data)
        return result, data
        
    def getEvent_detailedState(self):
        return self.getEvent(self.getNextEvent_detailedState)
        
    def subscribeEvent_detailedState(self, action):
        self.eventSubscribers_detailedState.append(action)
        if "event_detailedState" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_detailedState"] = [self.getNextEvent_detailedState, self.eventSubscribers_detailedState]

    def getNextEvent_displacementSensorWarning(self):
        data = MTM1M3_logevent_displacementSensorWarningC()
        result = self.sal.getEvent_displacementSensorWarning(data)
        return result, data
        
    def getEvent_displacementSensorWarning(self):
        return self.getEvent(self.getNextEvent_displacementSensorWarning)
        
    def subscribeEvent_displacementSensorWarning(self, action):
        self.eventSubscribers_displacementSensorWarning.append(action)
        if "event_displacementSensorWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_displacementSensorWarning"] = [self.getNextEvent_displacementSensorWarning, self.eventSubscribers_displacementSensorWarning]

    def getNextEvent_forceActuatorBackupCalibrationInfo(self):
        data = MTM1M3_logevent_forceActuatorBackupCalibrationInfoC()
        result = self.sal.getEvent_forceActuatorBackupCalibrationInfo(data)
        return result, data
        
    def getEvent_forceActuatorBackupCalibrationInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorBackupCalibrationInfo)
        
    def subscribeEvent_forceActuatorBackupCalibrationInfo(self, action):
        self.eventSubscribers_forceActuatorBackupCalibrationInfo.append(action)
        if "event_forceActuatorBackupCalibrationInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorBackupCalibrationInfo"] = [self.getNextEvent_forceActuatorBackupCalibrationInfo, self.eventSubscribers_forceActuatorBackupCalibrationInfo]

    def getNextEvent_forceActuatorILCInfo(self):
        data = MTM1M3_logevent_forceActuatorILCInfoC()
        result = self.sal.getEvent_forceActuatorILCInfo(data)
        return result, data
        
    def getEvent_forceActuatorILCInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorILCInfo)
        
    def subscribeEvent_forceActuatorILCInfo(self, action):
        self.eventSubscribers_forceActuatorILCInfo.append(action)
        if "event_forceActuatorILCInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorILCInfo"] = [self.getNextEvent_forceActuatorILCInfo, self.eventSubscribers_forceActuatorILCInfo]

    def getNextEvent_forceActuatorIdInfo(self):
        data = MTM1M3_logevent_forceActuatorIdInfoC()
        result = self.sal.getEvent_forceActuatorIdInfo(data)
        return result, data
        
    def getEvent_forceActuatorIdInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorIdInfo)
        
    def subscribeEvent_forceActuatorIdInfo(self, action):
        self.eventSubscribers_forceActuatorIdInfo.append(action)
        if "event_forceActuatorIdInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorIdInfo"] = [self.getNextEvent_forceActuatorIdInfo, self.eventSubscribers_forceActuatorIdInfo]

    def getNextEvent_forceActuatorMainCalibrationInfo(self):
        data = MTM1M3_logevent_forceActuatorMainCalibrationInfoC()
        result = self.sal.getEvent_forceActuatorMainCalibrationInfo(data)
        return result, data
        
    def getEvent_forceActuatorMainCalibrationInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorMainCalibrationInfo)
        
    def subscribeEvent_forceActuatorMainCalibrationInfo(self, action):
        self.eventSubscribers_forceActuatorMainCalibrationInfo.append(action)
        if "event_forceActuatorMainCalibrationInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorMainCalibrationInfo"] = [self.getNextEvent_forceActuatorMainCalibrationInfo, self.eventSubscribers_forceActuatorMainCalibrationInfo]

    def getNextEvent_forceActuatorMezzanineCalibrationInfo(self):
        data = MTM1M3_logevent_forceActuatorMezzanineCalibrationInfoC()
        result = self.sal.getEvent_forceActuatorMezzanineCalibrationInfo(data)
        return result, data
        
    def getEvent_forceActuatorMezzanineCalibrationInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorMezzanineCalibrationInfo)
        
    def subscribeEvent_forceActuatorMezzanineCalibrationInfo(self, action):
        self.eventSubscribers_forceActuatorMezzanineCalibrationInfo.append(action)
        if "event_forceActuatorMezzanineCalibrationInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorMezzanineCalibrationInfo"] = [self.getNextEvent_forceActuatorMezzanineCalibrationInfo, self.eventSubscribers_forceActuatorMezzanineCalibrationInfo]

    def getNextEvent_forceActuatorPositionInfo(self):
        data = MTM1M3_logevent_forceActuatorPositionInfoC()
        result = self.sal.getEvent_forceActuatorPositionInfo(data)
        return result, data
        
    def getEvent_forceActuatorPositionInfo(self):
        return self.getEvent(self.getNextEvent_forceActuatorPositionInfo)
        
    def subscribeEvent_forceActuatorPositionInfo(self, action):
        self.eventSubscribers_forceActuatorPositionInfo.append(action)
        if "event_forceActuatorPositionInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorPositionInfo"] = [self.getNextEvent_forceActuatorPositionInfo, self.eventSubscribers_forceActuatorPositionInfo]

    def getNextEvent_forceActuatorState(self):
        data = MTM1M3_logevent_forceActuatorStateC()
        result = self.sal.getEvent_forceActuatorState(data)
        return result, data
        
    def getEvent_forceActuatorState(self):
        return self.getEvent(self.getNextEvent_forceActuatorState)
        
    def subscribeEvent_forceActuatorState(self, action):
        self.eventSubscribers_forceActuatorState.append(action)
        if "event_forceActuatorState" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorState"] = [self.getNextEvent_forceActuatorState, self.eventSubscribers_forceActuatorState]

    def getNextEvent_forceActuatorWarning(self):
        data = MTM1M3_logevent_forceActuatorWarningC()
        result = self.sal.getEvent_forceActuatorWarning(data)
        return result, data
        
    def getEvent_forceActuatorWarning(self):
        return self.getEvent(self.getNextEvent_forceActuatorWarning)
        
    def subscribeEvent_forceActuatorWarning(self, action):
        self.eventSubscribers_forceActuatorWarning.append(action)
        if "event_forceActuatorWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_forceActuatorWarning"] = [self.getNextEvent_forceActuatorWarning, self.eventSubscribers_forceActuatorWarning]

    def getNextEvent_gyroWarning(self):
        data = MTM1M3_logevent_gyroWarningC()
        result = self.sal.getEvent_gyroWarning(data)
        return result, data
        
    def getEvent_gyroWarning(self):
        return self.getEvent(self.getNextEvent_gyroWarning)
        
    def subscribeEvent_gyroWarning(self, action):
        self.eventSubscribers_gyroWarning.append(action)
        if "event_gyroWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_gyroWarning"] = [self.getNextEvent_gyroWarning, self.eventSubscribers_gyroWarning]

    def getNextEvent_hardpointActuatorInfo(self):
        data = MTM1M3_logevent_hardpointActuatorInfoC()
        result = self.sal.getEvent_hardpointActuatorInfo(data)
        return result, data
        
    def getEvent_hardpointActuatorInfo(self):
        return self.getEvent(self.getNextEvent_hardpointActuatorInfo)
        
    def subscribeEvent_hardpointActuatorInfo(self, action):
        self.eventSubscribers_hardpointActuatorInfo.append(action)
        if "event_hardpointActuatorInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointActuatorInfo"] = [self.getNextEvent_hardpointActuatorInfo, self.eventSubscribers_hardpointActuatorInfo]

    def getNextEvent_hardpointActuatorState(self):
        data = MTM1M3_logevent_hardpointActuatorStateC()
        result = self.sal.getEvent_hardpointActuatorState(data)
        return result, data
        
    def getEvent_hardpointActuatorState(self):
        return self.getEvent(self.getNextEvent_hardpointActuatorState)
        
    def subscribeEvent_hardpointActuatorState(self, action):
        self.eventSubscribers_hardpointActuatorState.append(action)
        if "event_hardpointActuatorState" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointActuatorState"] = [self.getNextEvent_hardpointActuatorState, self.eventSubscribers_hardpointActuatorState]

    def getNextEvent_hardpointActuatorWarning(self):
        data = MTM1M3_logevent_hardpointActuatorWarningC()
        result = self.sal.getEvent_hardpointActuatorWarning(data)
        return result, data
        
    def getEvent_hardpointActuatorWarning(self):
        return self.getEvent(self.getNextEvent_hardpointActuatorWarning)
        
    def subscribeEvent_hardpointActuatorWarning(self, action):
        self.eventSubscribers_hardpointActuatorWarning.append(action)
        if "event_hardpointActuatorWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointActuatorWarning"] = [self.getNextEvent_hardpointActuatorWarning, self.eventSubscribers_hardpointActuatorWarning]

    def getNextEvent_hardpointMonitorInfo(self):
        data = MTM1M3_logevent_hardpointMonitorInfoC()
        result = self.sal.getEvent_hardpointMonitorInfo(data)
        return result, data
        
    def getEvent_hardpointMonitorInfo(self):
        return self.getEvent(self.getNextEvent_hardpointMonitorInfo)
        
    def subscribeEvent_hardpointMonitorInfo(self, action):
        self.eventSubscribers_hardpointMonitorInfo.append(action)
        if "event_hardpointMonitorInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointMonitorInfo"] = [self.getNextEvent_hardpointMonitorInfo, self.eventSubscribers_hardpointMonitorInfo]

    def getNextEvent_hardpointMonitorState(self):
        data = MTM1M3_logevent_hardpointMonitorStateC()
        result = self.sal.getEvent_hardpointMonitorState(data)
        return result, data
        
    def getEvent_hardpointMonitorState(self):
        return self.getEvent(self.getNextEvent_hardpointMonitorState)
        
    def subscribeEvent_hardpointMonitorState(self, action):
        self.eventSubscribers_hardpointMonitorState.append(action)
        if "event_hardpointMonitorState" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointMonitorState"] = [self.getNextEvent_hardpointMonitorState, self.eventSubscribers_hardpointMonitorState]

    def getNextEvent_hardpointMonitorWarning(self):
        data = MTM1M3_logevent_hardpointMonitorWarningC()
        result = self.sal.getEvent_hardpointMonitorWarning(data)
        return result, data
        
    def getEvent_hardpointMonitorWarning(self):
        return self.getEvent(self.getNextEvent_hardpointMonitorWarning)
        
    def subscribeEvent_hardpointMonitorWarning(self, action):
        self.eventSubscribers_hardpointMonitorWarning.append(action)
        if "event_hardpointMonitorWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_hardpointMonitorWarning"] = [self.getNextEvent_hardpointMonitorWarning, self.eventSubscribers_hardpointMonitorWarning]

    def getNextEvent_inclinometerSensorWarning(self):
        data = MTM1M3_logevent_inclinometerSensorWarningC()
        result = self.sal.getEvent_inclinometerSensorWarning(data)
        return result, data
        
    def getEvent_inclinometerSensorWarning(self):
        return self.getEvent(self.getNextEvent_inclinometerSensorWarning)
        
    def subscribeEvent_inclinometerSensorWarning(self, action):
        self.eventSubscribers_inclinometerSensorWarning.append(action)
        if "event_inclinometerSensorWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_inclinometerSensorWarning"] = [self.getNextEvent_inclinometerSensorWarning, self.eventSubscribers_inclinometerSensorWarning]

    def getNextEvent_interlockStatus(self):
        data = MTM1M3_logevent_interlockStatusC()
        result = self.sal.getEvent_interlockStatus(data)
        return result, data
        
    def getEvent_interlockStatus(self):
        return self.getEvent(self.getNextEvent_interlockStatus)
        
    def subscribeEvent_interlockStatus(self, action):
        self.eventSubscribers_interlockStatus.append(action)
        if "event_interlockStatus" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_interlockStatus"] = [self.getNextEvent_interlockStatus, self.eventSubscribers_interlockStatus]

    def getNextEvent_interlockWarning(self):
        data = MTM1M3_logevent_interlockWarningC()
        result = self.sal.getEvent_interlockWarning(data)
        return result, data
        
    def getEvent_interlockWarning(self):
        return self.getEvent(self.getNextEvent_interlockWarning)
        
    def subscribeEvent_interlockWarning(self, action):
        self.eventSubscribers_interlockWarning.append(action)
        if "event_interlockWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_interlockWarning"] = [self.getNextEvent_interlockWarning, self.eventSubscribers_interlockWarning]

    def getNextEvent_modbusResponse(self):
        data = MTM1M3_logevent_modbusResponseC()
        result = self.sal.getEvent_modbusResponse(data)
        return result, data
        
    def getEvent_modbusResponse(self):
        return self.getEvent(self.getNextEvent_modbusResponse)
        
    def subscribeEvent_modbusResponse(self, action):
        self.eventSubscribers_modbusResponse.append(action)
        if "event_modbusResponse" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_modbusResponse"] = [self.getNextEvent_modbusResponse, self.eventSubscribers_modbusResponse]

    def getNextEvent_modbusWarning(self):
        data = MTM1M3_logevent_modbusWarningC()
        result = self.sal.getEvent_modbusWarning(data)
        return result, data
        
    def getEvent_modbusWarning(self):
        return self.getEvent(self.getNextEvent_modbusWarning)
        
    def subscribeEvent_modbusWarning(self, action):
        self.eventSubscribers_modbusWarning.append(action)
        if "event_modbusWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_modbusWarning"] = [self.getNextEvent_modbusWarning, self.eventSubscribers_modbusWarning]

    def getNextEvent_pidInfo(self):
        data = MTM1M3_logevent_pidInfoC()
        result = self.sal.getEvent_pidInfo(data)
        return result, data
        
    def getEvent_pidInfo(self):
        return self.getEvent(self.getNextEvent_pidInfo)
        
    def subscribeEvent_pidInfo(self, action):
        self.eventSubscribers_pidInfo.append(action)
        if "event_pidInfo" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_pidInfo"] = [self.getNextEvent_pidInfo, self.eventSubscribers_pidInfo]

    def getNextEvent_powerStatus(self):
        data = MTM1M3_logevent_powerStatusC()
        result = self.sal.getEvent_powerStatus(data)
        return result, data
        
    def getEvent_powerStatus(self):
        return self.getEvent(self.getNextEvent_powerStatus)
        
    def subscribeEvent_powerStatus(self, action):
        self.eventSubscribers_powerStatus.append(action)
        if "event_powerStatus" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_powerStatus"] = [self.getNextEvent_powerStatus, self.eventSubscribers_powerStatus]

    def getNextEvent_powerWarning(self):
        data = MTM1M3_logevent_powerWarningC()
        result = self.sal.getEvent_powerWarning(data)
        return result, data
        
    def getEvent_powerWarning(self):
        return self.getEvent(self.getNextEvent_powerWarning)
        
    def subscribeEvent_powerWarning(self, action):
        self.eventSubscribers_powerWarning.append(action)
        if "event_powerWarning" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_powerWarning"] = [self.getNextEvent_powerWarning, self.eventSubscribers_powerWarning]

    def getNextEvent_rejectedAberrationForces(self):
        data = MTM1M3_logevent_rejectedAberrationForcesC()
        result = self.sal.getEvent_rejectedAberrationForces(data)
        return result, data
        
    def getEvent_rejectedAberrationForces(self):
        return self.getEvent(self.getNextEvent_rejectedAberrationForces)
        
    def subscribeEvent_rejectedAberrationForces(self, action):
        self.eventSubscribers_rejectedAberrationForces.append(action)
        if "event_rejectedAberrationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedAberrationForces"] = [self.getNextEvent_rejectedAberrationForces, self.eventSubscribers_rejectedAberrationForces]

    def getNextEvent_rejectedAccelerationForces(self):
        data = MTM1M3_logevent_rejectedAccelerationForcesC()
        result = self.sal.getEvent_rejectedAccelerationForces(data)
        return result, data
        
    def getEvent_rejectedAccelerationForces(self):
        return self.getEvent(self.getNextEvent_rejectedAccelerationForces)
        
    def subscribeEvent_rejectedAccelerationForces(self, action):
        self.eventSubscribers_rejectedAccelerationForces.append(action)
        if "event_rejectedAccelerationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedAccelerationForces"] = [self.getNextEvent_rejectedAccelerationForces, self.eventSubscribers_rejectedAccelerationForces]

    def getNextEvent_rejectedActiveOpticForces(self):
        data = MTM1M3_logevent_rejectedActiveOpticForcesC()
        result = self.sal.getEvent_rejectedActiveOpticForces(data)
        return result, data
        
    def getEvent_rejectedActiveOpticForces(self):
        return self.getEvent(self.getNextEvent_rejectedActiveOpticForces)
        
    def subscribeEvent_rejectedActiveOpticForces(self, action):
        self.eventSubscribers_rejectedActiveOpticForces.append(action)
        if "event_rejectedActiveOpticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedActiveOpticForces"] = [self.getNextEvent_rejectedActiveOpticForces, self.eventSubscribers_rejectedActiveOpticForces]

    def getNextEvent_rejectedAzimuthForces(self):
        data = MTM1M3_logevent_rejectedAzimuthForcesC()
        result = self.sal.getEvent_rejectedAzimuthForces(data)
        return result, data
        
    def getEvent_rejectedAzimuthForces(self):
        return self.getEvent(self.getNextEvent_rejectedAzimuthForces)
        
    def subscribeEvent_rejectedAzimuthForces(self, action):
        self.eventSubscribers_rejectedAzimuthForces.append(action)
        if "event_rejectedAzimuthForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedAzimuthForces"] = [self.getNextEvent_rejectedAzimuthForces, self.eventSubscribers_rejectedAzimuthForces]

    def getNextEvent_rejectedBalanceForces(self):
        data = MTM1M3_logevent_rejectedBalanceForcesC()
        result = self.sal.getEvent_rejectedBalanceForces(data)
        return result, data
        
    def getEvent_rejectedBalanceForces(self):
        return self.getEvent(self.getNextEvent_rejectedBalanceForces)
        
    def subscribeEvent_rejectedBalanceForces(self, action):
        self.eventSubscribers_rejectedBalanceForces.append(action)
        if "event_rejectedBalanceForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedBalanceForces"] = [self.getNextEvent_rejectedBalanceForces, self.eventSubscribers_rejectedBalanceForces]

    def getNextEvent_rejectedCylinderForces(self):
        data = MTM1M3_logevent_rejectedCylinderForcesC()
        result = self.sal.getEvent_rejectedCylinderForces(data)
        return result, data
        
    def getEvent_rejectedCylinderForces(self):
        return self.getEvent(self.getNextEvent_rejectedCylinderForces)
        
    def subscribeEvent_rejectedCylinderForces(self, action):
        self.eventSubscribers_rejectedCylinderForces.append(action)
        if "event_rejectedCylinderForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedCylinderForces"] = [self.getNextEvent_rejectedCylinderForces, self.eventSubscribers_rejectedCylinderForces]

    def getNextEvent_rejectedElevationForces(self):
        data = MTM1M3_logevent_rejectedElevationForcesC()
        result = self.sal.getEvent_rejectedElevationForces(data)
        return result, data
        
    def getEvent_rejectedElevationForces(self):
        return self.getEvent(self.getNextEvent_rejectedElevationForces)
        
    def subscribeEvent_rejectedElevationForces(self, action):
        self.eventSubscribers_rejectedElevationForces.append(action)
        if "event_rejectedElevationForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedElevationForces"] = [self.getNextEvent_rejectedElevationForces, self.eventSubscribers_rejectedElevationForces]

    def getNextEvent_rejectedForces(self):
        data = MTM1M3_logevent_rejectedForcesC()
        result = self.sal.getEvent_rejectedForces(data)
        return result, data
        
    def getEvent_rejectedForces(self):
        return self.getEvent(self.getNextEvent_rejectedForces)
        
    def subscribeEvent_rejectedForces(self, action):
        self.eventSubscribers_rejectedForces.append(action)
        if "event_rejectedForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedForces"] = [self.getNextEvent_rejectedForces, self.eventSubscribers_rejectedForces]

    def getNextEvent_rejectedOffsetForces(self):
        data = MTM1M3_logevent_rejectedOffsetForcesC()
        result = self.sal.getEvent_rejectedOffsetForces(data)
        return result, data
        
    def getEvent_rejectedOffsetForces(self):
        return self.getEvent(self.getNextEvent_rejectedOffsetForces)
        
    def subscribeEvent_rejectedOffsetForces(self, action):
        self.eventSubscribers_rejectedOffsetForces.append(action)
        if "event_rejectedOffsetForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedOffsetForces"] = [self.getNextEvent_rejectedOffsetForces, self.eventSubscribers_rejectedOffsetForces]

    def getNextEvent_rejectedStaticForces(self):
        data = MTM1M3_logevent_rejectedStaticForcesC()
        result = self.sal.getEvent_rejectedStaticForces(data)
        return result, data
        
    def getEvent_rejectedStaticForces(self):
        return self.getEvent(self.getNextEvent_rejectedStaticForces)
        
    def subscribeEvent_rejectedStaticForces(self, action):
        self.eventSubscribers_rejectedStaticForces.append(action)
        if "event_rejectedStaticForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedStaticForces"] = [self.getNextEvent_rejectedStaticForces, self.eventSubscribers_rejectedStaticForces]

    def getNextEvent_rejectedThermalForces(self):
        data = MTM1M3_logevent_rejectedThermalForcesC()
        result = self.sal.getEvent_rejectedThermalForces(data)
        return result, data
        
    def getEvent_rejectedThermalForces(self):
        return self.getEvent(self.getNextEvent_rejectedThermalForces)
        
    def subscribeEvent_rejectedThermalForces(self, action):
        self.eventSubscribers_rejectedThermalForces.append(action)
        if "event_rejectedThermalForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedThermalForces"] = [self.getNextEvent_rejectedThermalForces, self.eventSubscribers_rejectedThermalForces]

    def getNextEvent_rejectedVelocityForces(self):
        data = MTM1M3_logevent_rejectedVelocityForcesC()
        result = self.sal.getEvent_rejectedVelocityForces(data)
        return result, data
        
    def getEvent_rejectedVelocityForces(self):
        return self.getEvent(self.getNextEvent_rejectedVelocityForces)
        
    def subscribeEvent_rejectedVelocityForces(self, action):
        self.eventSubscribers_rejectedVelocityForces.append(action)
        if "event_rejectedVelocityForces" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["event_rejectedVelocityForces"] = [self.getNextEvent_rejectedVelocityForces, self.eventSubscribers_rejectedVelocityForces]



    def getNextSample_accelerometerData(self):
        data = MTM1M3_accelerometerDataC()
        result = self.sal.getNextSample_accelerometerData(data)
        return result, data

    def getSample_accelerometerData(self):
        data = MTM1M3_accelerometerDataC()
        result = self.sal.getSample_accelerometerData(data)
        return result, data
        
    def subscribeTelemetry_accelerometerData(self, action):
        self.telemetrySubscribers_accelerometerData.append(action)
        if "telemetry_accelerometerData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_accelerometerData"] = [self.getNextSample_accelerometerData, self.telemetrySubscribers_accelerometerData]

    def getNextSample_forceActuatorData(self):
        data = MTM1M3_forceActuatorDataC()
        result = self.sal.getNextSample_forceActuatorData(data)
        return result, data

    def getSample_forceActuatorData(self):
        data = MTM1M3_forceActuatorDataC()
        result = self.sal.getSample_forceActuatorData(data)
        return result, data
        
    def subscribeTelemetry_forceActuatorData(self, action):
        self.telemetrySubscribers_forceActuatorData.append(action)
        if "telemetry_forceActuatorData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_forceActuatorData"] = [self.getNextSample_forceActuatorData, self.telemetrySubscribers_forceActuatorData]

    def getNextSample_forceActuatorPressure(self):
        data = MTM1M3_forceActuatorPressureC()
        result = self.sal.getNextSample_forceActuatorPressure(data)
        return result, data

    def getSample_forceActuatorPressure(self):
        data = MTM1M3_forceActuatorPressureC()
        result = self.sal.getSample_forceActuatorPressure(data)
        return result, data
        
    def subscribeTelemetry_forceActuatorPressure(self, action):
        self.telemetrySubscribers_forceActuatorPressure.append(action)
        if "telemetry_forceActuatorPressure" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_forceActuatorPressure"] = [self.getNextSample_forceActuatorPressure, self.telemetrySubscribers_forceActuatorPressure]

    def getNextSample_gyroData(self):
        data = MTM1M3_gyroDataC()
        result = self.sal.getNextSample_gyroData(data)
        return result, data

    def getSample_gyroData(self):
        data = MTM1M3_gyroDataC()
        result = self.sal.getSample_gyroData(data)
        return result, data
        
    def subscribeTelemetry_gyroData(self, action):
        self.telemetrySubscribers_gyroData.append(action)
        if "telemetry_gyroData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_gyroData"] = [self.getNextSample_gyroData, self.telemetrySubscribers_gyroData]

    def getNextSample_hardpointActuatorData(self):
        data = MTM1M3_hardpointActuatorDataC()
        result = self.sal.getNextSample_hardpointActuatorData(data)
        return result, data

    def getSample_hardpointActuatorData(self):
        data = MTM1M3_hardpointActuatorDataC()
        result = self.sal.getSample_hardpointActuatorData(data)
        return result, data
        
    def subscribeTelemetry_hardpointActuatorData(self, action):
        self.telemetrySubscribers_hardpointActuatorData.append(action)
        if "telemetry_hardpointActuatorData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_hardpointActuatorData"] = [self.getNextSample_hardpointActuatorData, self.telemetrySubscribers_hardpointActuatorData]

    def getNextSample_hardpointMonitorData(self):
        data = MTM1M3_hardpointMonitorDataC()
        result = self.sal.getNextSample_hardpointMonitorData(data)
        return result, data

    def getSample_hardpointMonitorData(self):
        data = MTM1M3_hardpointMonitorDataC()
        result = self.sal.getSample_hardpointMonitorData(data)
        return result, data
        
    def subscribeTelemetry_hardpointMonitorData(self, action):
        self.telemetrySubscribers_hardpointMonitorData.append(action)
        if "telemetry_hardpointMonitorData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_hardpointMonitorData"] = [self.getNextSample_hardpointMonitorData, self.telemetrySubscribers_hardpointMonitorData]

    def getNextSample_imsData(self):
        data = MTM1M3_imsDataC()
        result = self.sal.getNextSample_imsData(data)
        return result, data

    def getSample_imsData(self):
        data = MTM1M3_imsDataC()
        result = self.sal.getSample_imsData(data)
        return result, data
        
    def subscribeTelemetry_imsData(self, action):
        self.telemetrySubscribers_imsData.append(action)
        if "telemetry_imsData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_imsData"] = [self.getNextSample_imsData, self.telemetrySubscribers_imsData]

    def getNextSample_inclinometerData(self):
        data = MTM1M3_inclinometerDataC()
        result = self.sal.getNextSample_inclinometerData(data)
        return result, data

    def getSample_inclinometerData(self):
        data = MTM1M3_inclinometerDataC()
        result = self.sal.getSample_inclinometerData(data)
        return result, data
        
    def subscribeTelemetry_inclinometerData(self, action):
        self.telemetrySubscribers_inclinometerData.append(action)
        if "telemetry_inclinometerData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_inclinometerData"] = [self.getNextSample_inclinometerData, self.telemetrySubscribers_inclinometerData]

    def getNextSample_outerLoopData(self):
        data = MTM1M3_outerLoopDataC()
        result = self.sal.getNextSample_outerLoopData(data)
        return result, data

    def getSample_outerLoopData(self):
        data = MTM1M3_outerLoopDataC()
        result = self.sal.getSample_outerLoopData(data)
        return result, data
        
    def subscribeTelemetry_outerLoopData(self, action):
        self.telemetrySubscribers_outerLoopData.append(action)
        if "telemetry_outerLoopData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_outerLoopData"] = [self.getNextSample_outerLoopData, self.telemetrySubscribers_outerLoopData]

    def getNextSample_pidData(self):
        data = MTM1M3_pidDataC()
        result = self.sal.getNextSample_pidData(data)
        return result, data

    def getSample_pidData(self):
        data = MTM1M3_pidDataC()
        result = self.sal.getSample_pidData(data)
        return result, data
        
    def subscribeTelemetry_pidData(self, action):
        self.telemetrySubscribers_pidData.append(action)
        if "telemetry_pidData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_pidData"] = [self.getNextSample_pidData, self.telemetrySubscribers_pidData]

    def getNextSample_powerData(self):
        data = MTM1M3_powerDataC()
        result = self.sal.getNextSample_powerData(data)
        return result, data

    def getSample_powerData(self):
        data = MTM1M3_powerDataC()
        result = self.sal.getSample_powerData(data)
        return result, data
        
    def subscribeTelemetry_powerData(self, action):
        self.telemetrySubscribers_powerData.append(action)
        if "telemetry_powerData" not in self.topicsSubscribedToo:
            self.topicsSubscribedToo["telemetry_powerData"] = [self.getNextSample_powerData, self.telemetrySubscribers_powerData]

