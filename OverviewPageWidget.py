
import QTHelpers
from DataCache import DataCache
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout

class OverviewPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QHBoxLayout()
        self.dataLayout = QGridLayout()
        self.layout.addLayout(self.dataLayout)
        self.setLayout(self.layout)

        self.summaryStateLabel = QLabel("UNKNOWN")
        self.mirrorStateLabel = QLabel("UNKNOWN")
        self.modeStateLabel = QLabel("UNKNOWN")
        self.interlockWarningLabel = QLabel("UNKNOWN")
        self.powerWarningLabel = QLabel("UNKNOWN")
        self.forceActuatorWarningLabel = QLabel("UNKNOWN")
        self.hardpointActuatorWarningLabel = QLabel("UNKNOWN")
        self.hardpointMonitorWarningLabel = QLabel("UNKNOWN")
        self.inclinometerWarningLabel = QLabel("UNKNOWN")
        self.accelerometerWarningLabel = QLabel("UNKNOWN")
        self.gyroWarningLabel = QLabel("UNKNOWN")
        self.airSupplyWarningLabel = QLabel("UNKNOWN")
        self.imsWarningLabel = QLabel("UNKNOWN")
        self.cellLightingWarningLabel = QLabel("UNKNOWN")
        self.faCommandedXLabel = QLabel("UNKNOWN")
        self.faCommandedYLabel = QLabel("UNKNOWN")
        self.faCommandedZLabel = QLabel("UNKNOWN")
        self.faCommandedMxLabel = QLabel("UNKNOWN")
        self.faCommandedMyLabel = QLabel("UNKNOWN")
        self.faCommandedMzLabel = QLabel("UNKNOWN")
        self.faCommandedMagLabel = QLabel("UNKNOWN")
        self.faMeasuredXLabel = QLabel("UNKNOWN")
        self.faMeasuredYLabel = QLabel("UNKNOWN")
        self.faMeasuredZLabel = QLabel("UNKNOWN")
        self.faMeasuredMxLabel = QLabel("UNKNOWN")
        self.faMeasuredMyLabel = QLabel("UNKNOWN")
        self.faMeasuredMzLabel = QLabel("UNKNOWN")
        self.faMeasuredMagLabel = QLabel("UNKNOWN")
        self.hpMeasuredXLabel = QLabel("UNKNOWN")
        self.hpMeasuredYLabel = QLabel("UNKNOWN")
        self.hpMeasuredZLabel = QLabel("UNKNOWN")
        self.hpMeasuredMxLabel = QLabel("UNKNOWN")
        self.hpMeasuredMyLabel = QLabel("UNKNOWN")
        self.hpMeasuredMzLabel = QLabel("UNKNOWN")
        self.hpMeasuredMagLabel = QLabel("UNKNOWN")
        self.hpPositionXLabel = QLabel("UNKNOWN")
        self.hpPositionYLabel = QLabel("UNKNOWN")
        self.hpPositionZLabel = QLabel("UNKNOWN")
        self.hpPositionRxLabel = QLabel("UNKNOWN")
        self.hpPositionRyLabel = QLabel("UNKNOWN")
        self.hpPositionRzLabel = QLabel("UNKNOWN")
        self.imsPositionXLabel = QLabel("UNKNOWN")
        self.imsPositionYLabel = QLabel("UNKNOWN")
        self.imsPositionZLabel = QLabel("UNKNOWN")
        self.imsPositionRxLabel = QLabel("UNKNOWN")
        self.imsPositionRyLabel = QLabel("UNKNOWN")
        self.imsPositionRzLabel = QLabel("UNKNOWN")
        self.accelationXLabel = QLabel("UNKNOWN")
        self.accelationYLabel = QLabel("UNKNOWN")
        self.accelationZLabel = QLabel("UNKNOWN")
        self.velocityXLabel = QLabel("UNKNOWN")
        self.velocityYLabel = QLabel("UNKNOWN")
        self.velocityZLabel = QLabel("UNKNOWN")
        self.airCommandLabel = QLabel("UNKNOWN")
        self.airValveLabel = QLabel("UNKNOWN")
        self.inclinometerLabel = QLabel("UNKNOWN")
        self.tmaAzimuthLabel = QLabel("UNKNOWN")
        self.tmaElevationLabel = QLabel("UNKNOWN")
        
        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Summary State"), row, col)
        self.dataLayout.addWidget(self.summaryStateLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Mirror State"), row, col)
        self.dataLayout.addWidget(self.mirrorStateLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Mode State"), row, col)
        self.dataLayout.addWidget(self.modeStateLabel, row, col + 1)
        row += 1    
        self.dataLayout.addWidget(QLabel("Warnings"), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("Interlocks"), row, col)
        self.dataLayout.addWidget(self.interlockWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Power"), row, col)
        self.dataLayout.addWidget(self.powerWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Force Actuators"), row, col)
        self.dataLayout.addWidget(self.forceActuatorWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Hardpoint Actuators"), row, col)
        self.dataLayout.addWidget(self.hardpointActuatorWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Hardpoint Monitors"), row, col)
        self.dataLayout.addWidget(self.hardpointMonitorWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Inclinometer"), row, col)
        self.dataLayout.addWidget(self.inclinometerWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Accelerometer"), row, col)
        self.dataLayout.addWidget(self.accelerometerWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Gyro"), row, col)
        self.dataLayout.addWidget(self.gyroWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Air Supply"), row, col)
        self.dataLayout.addWidget(self.airSupplyWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("IMS"), row, col)
        self.dataLayout.addWidget(self.imsWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Cell Lighting"), row, col) 
        self.dataLayout.addWidget(self.cellLightingWarningLabel, row, col + 1)

        row = 0
        col = 2
        self.dataLayout.addWidget(QLabel("Forces"), row, col)
        self.dataLayout.addWidget(QLabel("X (N)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y (N)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z (N)"), row, col + 3)
        self.dataLayout.addWidget(QLabel("Mx (Nm)"), row, col + 4)
        self.dataLayout.addWidget(QLabel("My (Nm)"), row, col + 5)
        self.dataLayout.addWidget(QLabel("Mz (Nm)"), row, col + 6)
        self.dataLayout.addWidget(QLabel("Mag (N)"), row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Commanded"), row, col)
        self.dataLayout.addWidget(self.faCommandedXLabel, row, col + 1)
        self.dataLayout.addWidget(self.faCommandedYLabel, row, col + 2)
        self.dataLayout.addWidget(self.faCommandedZLabel, row, col + 3)
        self.dataLayout.addWidget(self.faCommandedMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.faCommandedMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.faCommandedMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.faCommandedMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Measured"), row, col)
        self.dataLayout.addWidget(self.faMeasuredXLabel, row, col + 1)
        self.dataLayout.addWidget(self.faMeasuredYLabel, row, col + 2)
        self.dataLayout.addWidget(self.faMeasuredZLabel, row, col + 3)
        self.dataLayout.addWidget(self.faMeasuredMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.faMeasuredMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.faMeasuredMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.faMeasuredMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Hardpoints"), row, col)
        self.dataLayout.addWidget(self.hpMeasuredXLabel, row, col + 1)
        self.dataLayout.addWidget(self.hpMeasuredYLabel, row, col + 2)
        self.dataLayout.addWidget(self.hpMeasuredZLabel, row, col + 3)
        self.dataLayout.addWidget(self.hpMeasuredMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.hpMeasuredMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.hpMeasuredMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.hpMeasuredMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Mirror Position"), row, col)
        self.dataLayout.addWidget(QLabel("X (mm)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y (mm)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z (mm)"), row, col + 3)
        self.dataLayout.addWidget(QLabel("Rx (mrad)"), row, col + 4)
        self.dataLayout.addWidget(QLabel("Ry (mrad)"), row, col + 5)
        self.dataLayout.addWidget(QLabel("Rz (mrad)"), row, col + 6)
        row += 1
        self.dataLayout.addWidget(QLabel("Hardpoints"), row, col)
        self.dataLayout.addWidget(self.hpPositionXLabel, row, col + 1)
        self.dataLayout.addWidget(self.hpPositionYLabel, row, col + 2)
        self.dataLayout.addWidget(self.hpPositionZLabel, row, col + 3)
        self.dataLayout.addWidget(self.hpPositionRxLabel, row, col + 4)
        self.dataLayout.addWidget(self.hpPositionRyLabel, row, col + 5)
        self.dataLayout.addWidget(self.hpPositionRzLabel, row, col + 6)
        row += 1
        self.dataLayout.addWidget(QLabel("IMS"), row, col)
        self.dataLayout.addWidget(self.imsPositionXLabel, row, col + 1)
        self.dataLayout.addWidget(self.imsPositionYLabel, row, col + 2)
        self.dataLayout.addWidget(self.imsPositionZLabel, row, col + 3)
        self.dataLayout.addWidget(self.imsPositionRxLabel, row, col + 4)
        self.dataLayout.addWidget(self.imsPositionRyLabel, row, col + 5)
        self.dataLayout.addWidget(self.imsPositionRzLabel, row, col + 6)
        row += 1    
        self.dataLayout.addWidget(QLabel("Angular Acceleration"), row, col)
        self.dataLayout.addWidget(QLabel("X (?)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y (?)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z (?)"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(self.accelationXLabel, row, col + 1)
        self.dataLayout.addWidget(self.accelationYLabel, row, col + 2)
        self.dataLayout.addWidget(self.accelationZLabel, row, col + 3)
        row += 1    
        self.dataLayout.addWidget(QLabel("Angular Velocity"), row, col)
        self.dataLayout.addWidget(QLabel("X (?)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y (?)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z (?)"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(self.velocityXLabel, row, col + 1)
        self.dataLayout.addWidget(self.velocityYLabel, row, col + 2)
        self.dataLayout.addWidget(self.velocityZLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Air Supply"), row, col)
        self.dataLayout.addWidget(QLabel("Commanded"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Valve State"), row, col + 2)
        row += 1
        self.dataLayout.addWidget(self.airCommandLabel, row, col + 1)
        self.dataLayout.addWidget(self.airValveLabel, row, col + 2)       
        row += 1    
        self.dataLayout.addWidget(QLabel("M1M3"), row, col + 1)
        self.dataLayout.addWidget(QLabel("TMA"), row, col + 2)
        row += 1
        self.dataLayout.addWidget(QLabel("Azimuth (deg)"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(self.tmaAzimuthLabel, row, col + 2)
        row += 1
        self.dataLayout.addWidget(QLabel("Elevation (deg)"), row, col)
        self.dataLayout.addWidget(self.inclinometerLabel, row, col + 1)
        self.dataLayout.addWidget(self.tmaElevationLabel, row, col + 2)

        self.dataEventAccelerometerWarning = DataCache()
        self.dataEventAirSupplyWarning = DataCache()
        self.dataEventAppliedForces = DataCache()
        self.dataEventCellLightWarning = DataCache()
        self.dataEventDisplacementSensorWarning = DataCache()
        self.dataEventDetailedState = DataCache()
        self.dataEventForceActuatorWarning = DataCache()
        self.dataEventGyroWarning = DataCache()
        self.dataEventHardpointActuatorWarning = DataCache()
        self.dataEventHardpointMonitorWarning = DataCache()
        self.dataEventInclinometerSensorWarning = DataCache()
        self.dataEventInterlockWarning = DataCache()
        self.dataEventPowerWarning = DataCache()
        self.dataTelemetryAccelerometerData = DataCache()
        self.dataTelemetryForceActuatorData = DataCache()
        self.dataTelemetryGyroData = DataCache()
        self.dataTelemetryHardpointActuatorData = DataCache()
        self.dataTelemetryIMSData = DataCache()
        self.dataTelemetryInclinometerData = DataCache()
        self.dataMTMountTelemetryAzimuthData = DataCache()
        self.dataMTMountTelemetryElevationData = DataCache()

        self.MTM1M3.subscribeEvent_accelerometerWarning(self.processEventAccelerometerWarning)
        self.MTM1M3.subscribeEvent_airSupplyWarning(self.processEventAirSupplyWarning)
        self.MTM1M3.subscribeEvent_appliedForces(self.processEventAppliedForces)
        self.MTM1M3.subscribeEvent_cellLightWarning(self.processEventCellLightWarning)
        self.MTM1M3.subscribeEvent_displacementSensorWarning(self.processEventDisplacementSensorWarning)
        self.MTM1M3.subscribeEvent_detailedState(self.processEventDetailedState)
        self.MTM1M3.subscribeEvent_forceActuatorWarning(self.processEventForceActuatorWarning)
        self.MTM1M3.subscribeEvent_gyroWarning(self.processEventGyroWarning)
        self.MTM1M3.subscribeEvent_hardpointActuatorWarning(self.processEventHardpointActuatorWarning)
        self.MTM1M3.subscribeEvent_hardpointMonitorWarning(self.processEventHardpointMonitorWarning)
        self.MTM1M3.subscribeEvent_inclinometerSensorWarning(self.processEventInclinometerSensorWarning)
        self.MTM1M3.subscribeEvent_interlockWarning(self.processEventInterlockWarning)
        self.MTM1M3.subscribeEvent_powerWarning(self.processEventPowerWarning)
        self.MTM1M3.subscribeTelemetry_accelerometerData(self.processTelemetryAccelerometerData)
        self.MTM1M3.subscribeTelemetry_forceActuatorData(self.processTelemetryForceActuatorData)
        self.MTM1M3.subscribeTelemetry_gyroData(self.processTelemetryGyroData)
        self.MTM1M3.subscribeTelemetry_hardpointActuatorData(self.processTelemetryHardpointActuatorData)
        self.MTM1M3.subscribeTelemetry_imsData(self.processTelemetryIMSData)
        self.MTM1M3.subscribeTelemetry_inclinometerData(self.processTelemetryInclinometerData)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventAccelerometerWarning.hasBeenUpdated():
            data = self.dataEventAccelerometerWarning.get()
            QTHelpers.setWarningLabel(self.accelerometerWarningLabel, data.anyWarning)
        
        if self.dataEventAirSupplyWarning.hasBeenUpdated():
            data = self.dataEventAirSupplyWarning.get()
            QTHelpers.setWarningLabel(self.airSupplyWarningLabel, data.anyWarning)

        if self.dataEventAppliedForces.hasBeenUpdated():
            data = self.dataEventAppliedForces.get()
            self.faCommandedXLabel.setText("%0.3f" % (data.fx))
            self.faCommandedYLabel.setText("%0.3f" % (data.fy))
            self.faCommandedZLabel.setText("%0.3f" % (data.fz))
            self.faCommandedMxLabel.setText("%0.3f" % (data.mx))
            self.faCommandedMyLabel.setText("%0.3f" % (data.my))
            self.faCommandedMzLabel.setText("%0.3f" % (data.mz))
            self.faCommandedMagLabel.setText("%0.3f" % (data.forceMagnitude))

        if self.dataEventCellLightWarning.hasBeenUpdated():
            data = self.dataEventCellLightWarning.get()
            QTHelpers.setWarningLabel(self.cellLightingWarningLabel, data.anyWarning)

        if self.dataEventDisplacementSensorWarning.hasBeenUpdated():
            data = self.dataEventDisplacementSensorWarning.get()
            QTHelpers.setWarningLabel(self.imsWarningLabel, data.anyWarning)

        if self.dataEventDetailedState.hasBeenUpdated():
            data = self.dataEventDetailedState.get()
            state = data.detailedState
            summaryStates = ["Offline", "Disabled", "Enabled", "Fault", "Offline", "Standby", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Fault"]
            mirrorStates = ["Parked", "Parked", "Parked", "Parked", "Parked", "Parked", "Parked", "Raising", "Active", "Lowering", "Engineering", "Parked", "Raising", "Actve", "Lowering", "Lowering"]
            modeStates = ["Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Engineering", "Engineering", "Engineering", "Engineering", "Engineering", "Automatic"]
            self.summaryStateLabel.setText(summaryStates[state])
            self.mirrorStateLabel.setText(mirrorStates[state])
            self.modeStateLabel.setText(modeStates[state])

        if self.dataEventForceActuatorWarning.hasBeenUpdated():
            data = self.dataEventForceActuatorWarning.get()
            QTHelpers.setWarningLabel(self.forceActuatorWarningLabel, data.anyWarning)

        if self.dataEventGyroWarning.hasBeenUpdated():
            data = self.dataEventGyroWarning.get()
            QTHelpers.setWarningLabel(self.gyroWarningLabel, data.anyWarning)

        if self.dataEventHardpointActuatorWarning.hasBeenUpdated():
            data = self.dataEventHardpointActuatorWarning.get()
            QTHelpers.setWarningLabel(self.hardpointActuatorWarningLabel, data.anyWarning)

        if self.dataEventHardpointMonitorWarning.hasBeenUpdated():
            data = self.dataEventHardpointMonitorWarning.get()
            QTHelpers.setWarningLabel(self.hardpointMonitorWarningLabel, data.anyWarning)

        if self.dataEventInclinometerSensorWarning.hasBeenUpdated():
            data = self.dataEventInclinometerSensorWarning.get()
            QTHelpers.setWarningLabel(self.inclinometerWarningLabel, data.anyWarning)

        if self.dataEventInterlockWarning.hasBeenUpdated():
            data = self.dataEventInterlockWarning.get()
            QTHelpers.setWarningLabel(self.interlockWarningLabel, data.anyWarning)

        if self.dataEventPowerWarning.hasBeenUpdated():
            data = self.dataEventPowerWarning.get()
            QTHelpers.setWarningLabel(self.powerWarningLabel, data.anyWarning)

        if self.dataTelemetryAccelerometerData.hasBeenUpdated():
            data = self.dataTelemetryAccelerometerData.get()
            self.accelationXLabel.setText("%0.3f" % (data.angularAccelerationX))
            self.accelationYLabel.setText("%0.3f" % (data.angularAccelerationY))
            self.accelationZLabel.setText("%0.3f" % (data.angularAccelerationZ))

        if self.dataTelemetryForceActuatorData.hasBeenUpdated():
            data = self.dataTelemetryForceActuatorData.get()
            self.faMeasuredXLabel.setText("%0.3f" % (data.fx))
            self.faMeasuredYLabel.setText("%0.3f" % (data.fy))
            self.faMeasuredZLabel.setText("%0.3f" % (data.fz))
            self.faMeasuredMxLabel.setText("%0.3f" % (data.mx))
            self.faMeasuredMyLabel.setText("%0.3f" % (data.my))
            self.faMeasuredMzLabel.setText("%0.3f" % (data.mz))
            self.faMeasuredMagLabel.setText("%0.3f" % (data.forceMagnitude))

        if self.dataTelemetryGyroData.hasBeenUpdated():
            data = self.dataTelemetryGyroData.get()
            self.velocityXLabel.setText("%0.3f" % (data.angularVelocityX))
            self.velocityYLabel.setText("%0.3f" % (data.angularVelocityY))
            self.velocityZLabel.setText("%0.3f" % (data.angularVelocityZ))

        if self.dataTelemetryHardpointActuatorData.hasBeenUpdated():
            data = self.dataTelemetryHardpointActuatorData.get()
            self.hpPositionXLabel.setText("%0.3f" % (data.xPosition * 1000.0))
            self.hpPositionYLabel.setText("%0.3f" % (data.yPosition * 1000.0))
            self.hpPositionZLabel.setText("%0.3f" % (data.zPosition * 1000.0))
            self.hpPositionRxLabel.setText("%0.3f" % (data.xRotation * 1000.0))
            self.hpPositionRyLabel.setText("%0.3f" % (data.yRotation * 1000.0))
            self.hpPositionRzLabel.setText("%0.3f" % (data.zRotation * 1000.0))
            self.hpMeasuredXLabel.setText("%0.3f" % (data.fx))
            self.hpMeasuredYLabel.setText("%0.3f" % (data.fy))
            self.hpMeasuredZLabel.setText("%0.3f" % (data.fz))
            self.hpMeasuredMxLabel.setText("%0.3f" % (data.mx))
            self.hpMeasuredMyLabel.setText("%0.3f" % (data.my))
            self.hpMeasuredMzLabel.setText("%0.3f" % (data.mz))
            self.hpMeasuredMagLabel.setText("%0.3f" % (data.forceMagnitude))

        if self.dataTelemetryIMSData.hasBeenUpdated():
            data = self.dataTelemetryIMSData.get()
            self.imsPositionXLabel.setText("%0.3f" % (data.xPosition * 1000.0))
            self.imsPositionYLabel.setText("%0.3f" % (data.yPosition * 1000.0))
            self.imsPositionZLabel.setText("%0.3f" % (data.zPosition * 1000.0))
            self.imsPositionRxLabel.setText("%0.3f" % (data.xRotation * 1000.0))
            self.imsPositionRyLabel.setText("%0.3f" % (data.yRotation * 1000.0))
            self.imsPositionRzLabel.setText("%0.3f" % (data.zRotation * 1000.0))

        if self.dataTelemetryInclinometerData.hasBeenUpdated():
            data = self.dataTelemetryInclinometerData.get()
            self.inclinometerLabel.setText("%0.3f" % (data.inclinometerAngle))

        if self.dataMTMountTelemetryAzimuthData.hasBeenUpdated():
            data = self.dataMTMountTelemetryAzimuthData.get()
            self.tmaAzimuthLabel.setText("%0.3f" % (data.Azimuth_Angle_Actual))

        if self.dataMTMountTelemetryElevationData.hasBeenUpdated():
            data = self.dataMTMountTelemetryElevationData.get()
            self.tmaElevationLabel.setText("%0.3f" % (data.Elevation_Angle_Actual))

    def processEventAccelerometerWarning(self, data):
        self.dataEventAccelerometerWarning.set(data[-1])

    def processEventAirSupplyWarning(self, data):
        self.dataEventAirSupplyWarning.set(data[-1])

    def processEventAppliedForces(self, data):
        self.dataEventAppliedForces.set(data[-1])
        
    def processEventCellLightWarning(self, data):
        self.dataEventCellLightWarning.set(data[-1])        

    def processEventDisplacementSensorWarning(self, data):
        self.dataEventDisplacementSensorWarning.set(data[-1])

    def processEventDetailedState(self, data):
        self.dataEventDetailedState.set(data[-1])

    def processEventForceActuatorWarning(self, data):
        self.dataEventForceActuatorWarning.set(data[-1])        

    def processEventGyroWarning(self, data):
        self.dataEventGyroWarning.set(data[-1])

    def processEventHardpointActuatorWarning(self, data):
        self.dataEventHardpointActuatorWarning.set(data[-1])

    def processEventHardpointMonitorWarning(self, data):
        self.dataEventHardpointMonitorWarning.set(data[-1])

    def processEventInclinometerSensorWarning(self, data):
        self.dataEventInclinometerSensorWarning.set(data[-1])
    
    def processEventInterlockWarning(self, data):
        self.dataEventInterlockWarning.set(data[-1]) 

    def processEventPowerWarning(self, data):
        self.dataEventPowerWarning.set(data[-1])

    def processTelemetryAccelerometerData(self, data):
        self.dataTelemetryAccelerometerData.set(data[-1])
        
    def processTelemetryForceActuatorData(self, data):
        self.dataTelemetryForceActuatorData.set(data[-1])

    def processTelemetryGyroData(self, data):
        self.dataTelemetryGyroData.set(data[-1])
        
    def processTelemetryHardpointActuatorData(self, data):
        self.dataTelemetryHardpointActuatorData.set(data[-1])
        
    def processTelemetryIMSData(self, data):
        self.dataTelemetryIMSData.set(data[-1])
        
    def processTelemetryInclinometerData(self, data):
        self.dataTelemetryInclinometerData.set(data[-1])

    def processMTMountTelemetryAzimuthData(self, data):
        self.dataMTMountTelemetryAzimuthData.set(data[-1])

    def processMTMountTelemetryElevationData(self, data):
        self.dataMTMountTelemetryElevationData.set(data[-1])
