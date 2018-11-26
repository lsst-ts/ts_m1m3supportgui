
import QTHelpers
from PySide2.QtWidgets import (QWidget, QLabel, QGridLayout)

class OverviewPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QGridLayout()
        
        row = 0
        col = 0
        self.summaryStateLabel = QLabel("UNKNOWN")
        self.mirrorStateLabel = QLabel("UNKNOWN")
        self.modeStateLabel = QLabel("UNKNOWN")
        self.layout.addWidget(QLabel("Summary State:"), row, col)
        self.layout.addWidget(self.summaryStateLabel, row, col + 1)
        self.layout.addWidget(QLabel("Mirror State:"), row + 1, col)
        self.layout.addWidget(self.mirrorStateLabel, row + 1, col + 1)
        self.layout.addWidget(QLabel("Mode State:"), row + 2, col)
        self.layout.addWidget(self.modeStateLabel, row + 2, col + 1)

        row = 3
        col = 0
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
        self.layout.addWidget(QLabel("Warnings:"), row, col)
        self.layout.addWidget(QLabel("Interlocks"), row + 1, col)
        self.layout.addWidget(self.interlockWarningLabel, row + 1, col + 1)
        self.layout.addWidget(QLabel("Power"), row + 2, col)
        self.layout.addWidget(self.powerWarningLabel, row + 2, col + 1)
        self.layout.addWidget(QLabel("Force Actuators"), row + 3, col)
        self.layout.addWidget(self.forceActuatorWarningLabel, row + 3, col + 1)
        self.layout.addWidget(QLabel("Hardpoint Actuators"), row + 4, col)
        self.layout.addWidget(self.hardpointActuatorWarningLabel, row + 4, col + 1)
        self.layout.addWidget(QLabel("Hardpoint Monitors"), row + 5, col)
        self.layout.addWidget(self.hardpointMonitorWarningLabel, row + 5, col + 1)
        self.layout.addWidget(QLabel("Inclinometer"), row + 6, col)
        self.layout.addWidget(self.inclinometerWarningLabel, row + 6, col + 1)
        self.layout.addWidget(QLabel("Accelerometer"), row + 7, col)
        self.layout.addWidget(self.accelerometerWarningLabel, row + 7, col + 1)
        self.layout.addWidget(QLabel("Gyro"), row + 8, col)
        self.layout.addWidget(self.gyroWarningLabel, row + 8, col + 1)
        self.layout.addWidget(QLabel("Air Supply"), row + 9, col)
        self.layout.addWidget(self.airSupplyWarningLabel, row + 9, col + 1)
        self.layout.addWidget(QLabel("IMS"), row + 10, col)
        self.layout.addWidget(self.imsWarningLabel, row + 10, col + 1)
        self.layout.addWidget(QLabel("Cell Lighting"), row + 11, col) 
        self.layout.addWidget(self.cellLightingWarningLabel, row + 11, col + 1)

        row = 0
        col = 2
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
        self.layout.addWidget(QLabel("Forces:"), row, col)
        self.layout.addWidget(QLabel("X (N)"), row, col + 1)
        self.layout.addWidget(QLabel("Y (N)"), row, col + 2)
        self.layout.addWidget(QLabel("Z (N)"), row, col + 3)
        self.layout.addWidget(QLabel("Mx (Nm)"), row, col + 4)
        self.layout.addWidget(QLabel("My (Nm)"), row, col + 5)
        self.layout.addWidget(QLabel("Mz (Nm)"), row, col + 6)
        self.layout.addWidget(QLabel("Mag (N)"), row, col + 7)
        self.layout.addWidget(QLabel("Commanded"), row + 1, col)
        self.layout.addWidget(self.faCommandedXLabel, row + 1, col + 1)
        self.layout.addWidget(self.faCommandedYLabel, row + 1, col + 2)
        self.layout.addWidget(self.faCommandedZLabel, row + 1, col + 3)
        self.layout.addWidget(self.faCommandedMxLabel, row + 1, col + 4)
        self.layout.addWidget(self.faCommandedMyLabel, row + 1, col + 5)
        self.layout.addWidget(self.faCommandedMzLabel, row + 1, col + 6)
        self.layout.addWidget(self.faCommandedMagLabel, row + 1, col + 7)
        self.layout.addWidget(QLabel("Measured"), row + 2, col)
        self.layout.addWidget(self.faMeasuredXLabel, row + 2, col + 1)
        self.layout.addWidget(self.faMeasuredYLabel, row + 2, col + 2)
        self.layout.addWidget(self.faMeasuredZLabel, row + 2, col + 3)
        self.layout.addWidget(self.faMeasuredMxLabel, row + 2, col + 4)
        self.layout.addWidget(self.faMeasuredMyLabel, row + 2, col + 5)
        self.layout.addWidget(self.faMeasuredMzLabel, row + 2, col + 6)
        self.layout.addWidget(self.faMeasuredMagLabel, row + 2, col + 7)
        self.layout.addWidget(QLabel("Hardpoints"), row + 3, col)
        self.layout.addWidget(self.hpMeasuredXLabel, row + 3, col + 1)
        self.layout.addWidget(self.hpMeasuredYLabel, row + 3, col + 2)
        self.layout.addWidget(self.hpMeasuredZLabel, row + 3, col + 3)
        self.layout.addWidget(self.hpMeasuredMxLabel, row + 3, col + 4)
        self.layout.addWidget(self.hpMeasuredMyLabel, row + 3, col + 5)
        self.layout.addWidget(self.hpMeasuredMzLabel, row + 3, col + 6)
        self.layout.addWidget(self.hpMeasuredMagLabel, row + 3, col + 7)
        
        row = 4
        col = 2
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
        self.layout.addWidget(QLabel("Mirror Position:"), row, col)
        self.layout.addWidget(QLabel("X (mm)"), row, col + 1)
        self.layout.addWidget(QLabel("Y (mm)"), row, col + 2)
        self.layout.addWidget(QLabel("Z (mm)"), row, col + 3)
        self.layout.addWidget(QLabel("Rx (mrad)"), row, col + 4)
        self.layout.addWidget(QLabel("Ry (mrad)"), row, col + 5)
        self.layout.addWidget(QLabel("Rz (mrad)"), row, col + 6)
        self.layout.addWidget(QLabel("Hardpoints:"), row + 1, col)
        self.layout.addWidget(self.hpPositionXLabel, row + 1, col + 1)
        self.layout.addWidget(self.hpPositionYLabel, row + 1, col + 2)
        self.layout.addWidget(self.hpPositionZLabel, row + 1, col + 3)
        self.layout.addWidget(self.hpPositionRxLabel, row + 1, col + 4)
        self.layout.addWidget(self.hpPositionRyLabel, row + 1, col + 5)
        self.layout.addWidget(self.hpPositionRzLabel, row + 1, col + 6)
        self.layout.addWidget(QLabel("IMS:"), row + 2, col)
        self.layout.addWidget(self.imsPositionXLabel, row + 2, col + 1)
        self.layout.addWidget(self.imsPositionYLabel, row + 2, col + 2)
        self.layout.addWidget(self.imsPositionZLabel, row + 2, col + 3)
        self.layout.addWidget(self.imsPositionRxLabel, row + 2, col + 4)
        self.layout.addWidget(self.imsPositionRyLabel, row + 2, col + 5)
        self.layout.addWidget(self.imsPositionRzLabel, row + 2, col + 6)

        row = 7
        col = 2
        self.accelationXLabel = QLabel("UNKNOWN")
        self.accelationYLabel = QLabel("UNKNOWN")
        self.accelationZLabel = QLabel("UNKNOWN")
        self.layout.addWidget(QLabel("Angular Acceleration:"), row, col)
        self.layout.addWidget(QLabel("X (?)"), row, col + 1)
        self.layout.addWidget(QLabel("Y (?)"), row, col + 2)
        self.layout.addWidget(QLabel("Z (?)"), row, col + 3)
        self.layout.addWidget(self.accelationXLabel, row + 1, col + 1)
        self.layout.addWidget(self.accelationYLabel, row + 1, col + 2)
        self.layout.addWidget(self.accelationZLabel, row + 1, col + 3)

        row = 9
        col = 2
        self.velocityXLabel = QLabel("UNKNOWN")
        self.velocityYLabel = QLabel("UNKNOWN")
        self.velocityZLabel = QLabel("UNKNOWN")
        self.layout.addWidget(QLabel("Angular Velocity:"), row, col)
        self.layout.addWidget(QLabel("X (?)"), row, col + 1)
        self.layout.addWidget(QLabel("Y (?)"), row, col + 2)
        self.layout.addWidget(QLabel("Z (?)"), row, col + 3)
        self.layout.addWidget(self.velocityXLabel, row + 1, col + 1)
        self.layout.addWidget(self.velocityYLabel, row + 1, col + 2)
        self.layout.addWidget(self.velocityZLabel, row + 1, col + 3)

        row = 11
        col = 2
        self.airCommandLabel = QLabel("UNKNOWN")
        self.airValveLabel = QLabel("UNKNOWN")
        self.layout.addWidget(QLabel("Air Supply"), row, col)
        self.layout.addWidget(QLabel("Commanded"), row, col + 1)
        self.layout.addWidget(QLabel("Valve State"), row, col + 2)
        self.layout.addWidget(self.airCommandLabel, row + 1, col + 1)
        self.layout.addWidget(self.airValveLabel, row + 1, col + 2)       

        row = 13
        col = 2
        self.inclinometerLabel = QLabel("UNKNOWN")
        self.tmaAzimuthLabel = QLabel("UNKNOWN")
        self.tmaElevationLabel = QLabel("UNKNOWN")
        self.layout.addWidget(QLabel("M1M3"), row, col + 1)
        self.layout.addWidget(QLabel("TMA"), row, col + 2)
        self.layout.addWidget(QLabel("Azimuth (deg)"), row + 1, col)
        self.layout.addWidget(QLabel("-"), row + 1, col + 1)
        self.layout.addWidget(self.tmaAzimuthLabel, row + 1, col + 2)
        self.layout.addWidget(QLabel("Elevation (deg)"), row + 2, col)
        self.layout.addWidget(self.inclinometerLabel, row + 2, col + 1)
        self.layout.addWidget(self.tmaElevationLabel, row + 2, col + 2)

        self.setLayout(self.layout)
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
        self.MTM1M3.subscribeEvent_powerWarning(self.processEventPowerWarning)
        self.MTM1M3.subscribeTelemetry_accelerometerData(self.processTelemetryAccelerometerData)
        self.MTM1M3.subscribeTelemetry_forceActuatorData(self.processTelemetryForceActuatorData)
        self.MTM1M3.subscribeTelemetry_gyroData(self.processTelemetryGyroData)
        self.MTM1M3.subscribeTelemetry_hardpointActuatorData(self.processTelemetryHardpointActuatorData)
        self.MTM1M3.subscribeTelemetry_imsData(self.processTelemetryIMSData)
        self.MTM1M3.subscribeTelemetry_inclinometerData(self.processTelemetryInclinometerData)

    def processEventAccelerometerWarning(self, data):
        QTHelpers.setWarningLabel(self.accelerometerWarningLabel, data[-1].anyWarning)

    def processEventAirSupplyWarning(self, data):
        QTHelpers.setWarningLabel(self.airSupplyWarningLabel, data[-1].anyWarning)

    def processEventAppliedForces(self, data):
        data = data[-1]
        self.faCommandedXLabel.setText("%0.3f" % (data.fX))
        self.faCommandedYLabel.setText("%0.3f" % (data.fY))
        self.faCommandedZLabel.setText("%0.3f" % (data.fZ))
        self.faCommandedMxLabel.setText("%0.3f" % (data.mX))
        self.faCommandedMyLabel.setText("%0.3f" % (data.mY))
        self.faCommandedMzLabel.setText("%0.3f" % (data.mZ))
        self.faCommandedMagLabel.setText("%0.3f" % (data.forceMagnitude))

    def processEventCellLightWarning(self, data):
        QTHelpers.setWarningLabel(self.cellLightingWarningLabel, data[-1].anyWarning)

    def processEventDisplacementSensorWarning(self, data):
        QTHelpers.setWarningLabel(self.imsWarningLabel, data[-1].anyWarning)

    def processEventDetailedState(self, data):
        state = data[-1].detailedState
        summaryStates = ["Offline", "Disabled", "Enabled", "Fault", "Offline", "Standby", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Enabled", "Fault"]
        mirrorStates = ["Parked", "Parked", "Parked", "Parked", "Parked", "Parked", "Parked", "Raising", "Active", "Lowering", "Engineering", "Parked", "Raising", "Actve", "Lowering", "Lowering"]
        modeStates = ["Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Automatic", "Engineering", "Engineering", "Engineering", "Engineering", "Engineering", "Automatic"]
        self.summaryStateLabel.setText(summaryStates[state])
        self.mirrorStateLabel.setText(mirrorStates[state])
        self.modeStateLabel.setText(modeStates[state])

    def processEventForceActuatorWarning(self, data):
        QTHelpers.setWarningLabel(self.forceActuatorWarningLabel, data[-1].anyWarning)

    def processEventGyroWarning(self, data):
        QTHelpers.setWarningLabel(self.gyroWarningLabel, data[-1].anyWarning)

    def processEventHardpointActuatorWarning(self, data):
        QTHelpers.setWarningLabel(self.hardpointActuatorWarningLabel, data[-1].anyWarning)

    def processEventHardpointMonitorWarning(self, data):
        QTHelpers.setWarningLabel(self.hardpointMonitorWarningLabel, data[-1].anyWarning)

    def processEventInclinometerSensorWarning(self, data):
        QTHelpers.setWarningLabel(self.inclinometerWarningLabel, data[-1].anyWarning)
    
    def processEventInterlockWarning(self, data):
        QTHelpers.setWarningLabel(self.interlockWarningLabel, data[-1].anyWarning)

    def processEventPowerWarning(self, data):
        QTHelpers.setWarningLabel(self.powerWarningLabel, data[-1].anyWarning)

    def processTelemetryAccelerometerData(self, data):
        data = data[-1]
        self.accelationXLabel.setText("%0.3f" % (data.angularAccelerationX))
        self.accelationYLabel.setText("%0.3f" % (data.angularAccelerationY))
        self.accelationZLabel.setText("%0.3f" % (data.angularAccelerationZ))

    def processTelemetryForceActuatorData(self, data):
        data = data[-1]
        self.faMeasuredXLabel.setText("%0.3f" % (data.fX))
        self.faMeasuredYLabel.setText("%0.3f" % (data.fY))
        self.faMeasuredZLabel.setText("%0.3f" % (data.fZ))
        self.faMeasuredMxLabel.setText("%0.3f" % (data.mX))
        self.faMeasuredMyLabel.setText("%0.3f" % (data.mY))
        self.faMeasuredMzLabel.setText("%0.3f" % (data.mZ))
        self.faMeasuredMagLabel.setText("%0.3f" % (data.forceMagnitude))

    def processTelemetryGyroData(self, data):
        data = data[-1]
        self.velocityXLabel.setText("%0.3f" % (data.angularVelocityX))
        self.velocityYLabel.setText("%0.3f" % (data.angularVelocityY))
        self.velocityZLabel.setText("%0.3f" % (data.angularVelocityZ))

    def processTelemetryHardpointActuatorData(self, data):
        data = data[-1]
        self.hpPositionXLabel.setText("%0.3f" % (data.xPosition * 1000.0))
        self.hpPositionYLabel.setText("%0.3f" % (data.yPosition * 1000.0))
        self.hpPositionZLabel.setText("%0.3f" % (data.zPosition * 1000.0))
        self.hpPositionRxLabel.setText("%0.3f" % (data.xRotation * 1000.0))
        self.hpPositionRyLabel.setText("%0.3f" % (data.yRotation * 1000.0))
        self.hpPositionRzLabel.setText("%0.3f" % (data.zRotation * 1000.0))
        self.hpMeasuredXLabel.setText("%0.3f" % (data.fX))
        self.hpMeasuredYLabel.setText("%0.3f" % (data.fY))
        self.hpMeasuredZLabel.setText("%0.3f" % (data.fZ))
        self.hpMeasuredMxLabel.setText("%0.3f" % (data.mX))
        self.hpMeasuredMyLabel.setText("%0.3f" % (data.mY))
        self.hpMeasuredMzLabel.setText("%0.3f" % (data.mZ))
        self.hpMeasuredMagLabel.setText("%0.3f" % (data.forceMagnitude))

    def processTelemetryIMSData(self, data):
        data = data[-1]
        self.imsPositionXLabel.setText("%0.3f" % (data.xPosition * 1000.0))
        self.imsPositionYLabel.setText("%0.3f" % (data.yPosition * 1000.0))
        self.imsPositionZLabel.setText("%0.3f" % (data.zPosition * 1000.0))
        self.imsPositionRxLabel.setText("%0.3f" % (data.xRotation * 1000.0))
        self.imsPositionRyLabel.setText("%0.3f" % (data.yRotation * 1000.0))
        self.imsPositionRzLabel.setText("%0.3f" % (data.zRotation * 1000.0))

    def processTelemetryInclinometerData(self, data):
        data = data[-1]
        self.inclinometerLabel.setText("%0.3f" % (data.inclinometerAngle))

    def processMTMountTelemetryAzimuthData(self, data):
        data = data[-1]
        self.tmaAzimuthLabel.setText("%0.3f" % (data.Azimuth_Angle_Actual))

    def processMTMountTelemetryElevationData(self, data):
        data = data[-1]
        self.tmaElevationLabel.setText("%0.3f" % (data.Elevation_Angle_Actual))