import QTHelpers
from datetime import datetime
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout
from PySide2.QtCore import Slot


class OverviewPageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm

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
        self.cellLightWarningLabel = QLabel("UNKNOWN")
        self.heartbeatLabel = QLabel("UNKNOWN")
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
        self.dataLayout.addWidget(QLabel("Cell Light"), row, col)
        self.dataLayout.addWidget(self.cellLightWarningLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Heartbeat"), row, col)
        self.dataLayout.addWidget(self.heartbeatLabel, row, col + 1)

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

        self.comm.accelerometerWarning.connect(self.accelerometerWarning)
        self.comm.airSupplyWarning.connect(self.airSupplyWarning)
        self.comm.appliedForces.connect(self.appliedForces)
        self.comm.cellLightWarning.connect(self.cellLightWarning)
        self.comm.detailedState.connect(self.detailedState)
        self.comm.displacementSensorWarning.connect(self.displacementSensorWarning)
        self.comm.forceActuatorWarning.connect(self.forceActuatorWarning)
        self.comm.gyroWarning.connect(self.gyroWarning)
        self.comm.hardpointActuatorWarning.connect(self.hardpointActuatorWarning)
        self.comm.hardpointMonitorWarning.connect(self.hardpointMonitorWarning)
        self.comm.heartbeat.connect(self.heartbeat)
        self.comm.inclinometerSensorWarning.connect(self.inclinometerSensorWarning)
        self.comm.interlockWarning.connect(self.interlockWarning)
        self.comm.powerWarning.connect(self.powerWarning)

        self.comm.accelerometerData.connect(self.accelerometerData)
        self.comm.forceActuatorData.connect(self.forceActuatorData)
        self.comm.gyroData.connect(self.gyroData)
        self.comm.hardpointActuatorData.connect(self.hardpointActuatorData)
        self.comm.imsData.connect(self.imsData)
        self.comm.inclinometerData.connect(self.inclinometerData)

        self.comm.Azimuth.connect(self.azimuth)
        self.comm.Elevation.connect(self.elevation)

    def accelerometerWarning(self, data):
        QTHelpers.setWarningLabel(self.accelerometerWarningLabel, data.anyWarning)

    @Slot(map)
    def airSupplyWarning(self, data):
        QTHelpers.setWarningLabel(self.airSupplyWarningLabel, data.anyWarning)

    @Slot(map)
    def appliedForces(self, data):
        self.faCommandedXLabel.setText("%0.3f" % (data.fx))
        self.faCommandedYLabel.setText("%0.3f" % (data.fy))
        self.faCommandedZLabel.setText("%0.3f" % (data.fz))
        self.faCommandedMxLabel.setText("%0.3f" % (data.mx))
        self.faCommandedMyLabel.setText("%0.3f" % (data.my))
        self.faCommandedMzLabel.setText("%0.3f" % (data.mz))
        self.faCommandedMagLabel.setText("%0.3f" % (data.forceMagnitude))

    @Slot(map)
    def cellLightWarning(self, data):
        QTHelpers.setWarningLabel(self.cellLightWarningLabel, data.anyWarning)

    @Slot(map)
    def displacementSensorWarning(self, data):
        QTHelpers.setWarningLabel(self.imsWarningLabel, data.anyWarning)

    @Slot(map)
    def detailedState(self, data):
        # summary state, mirror state, mode
        matrix = [
            ["---", "---", "---"],
            ["Disabled", "Parked", "Automatic"],
            ["Fault", "Parked", "Automatic"],
            ["Offline", "Unknown", "Unknown"],
            ["Standby", "Parked", "Automatic"],
            ["Enabled", "Parked", "Automatic"],
            ["Enabled", "Raising", "Automatic"],
            ["Enabled", "Active", "Automatic"],
            ["Enabled", "Lowering", "Automatic"],
            ["Enabled", "Parked", "Engineering"],
            ["Enabled", "Raising", "Engineering"],
            ["Enabled", "Active", "Engineering"],
            ["Enabled", "Lowering", "Engineering"],
            ["Fault", "Lowering", "Automatic"],
            ["Profile Hardpoint", "Parked", "Profile Hardpoint"],
        ]
        m = matrix[data.detailedState]
        self.summaryStateLabel.setText(m[0])
        self.mirrorStateLabel.setText(m[1])
        self.modeStateLabel.setText(m[2])

    @Slot(map)
    def forceActuatorWarning(self, data):
        QTHelpers.setWarningLabel(self.forceActuatorWarningLabel, data.anyWarning)

    @Slot(map)
    def gyroWarning(self, data):
        QTHelpers.setWarningLabel(self.gyroWarningLabel, data.anyWarning)

    @Slot(map)
    def hardpointActuatorWarning(self, data):
        QTHelpers.setWarningLabel(self.hardpointActuatorWarningLabel, data.anyWarning)

    @Slot(map)
    def hardpointMonitorWarning(self, data):
        QTHelpers.setWarningLabel(self.hardpointMonitorWarningLabel, data.anyWarning)

    @Slot(map)
    def heartbeat(self, data):
        self.heartbeatLabel.setText(datetime.now().strftime("%H:%M:%S.%f"))

    @Slot(map)
    def inclinometerSensorWarning(self, data):
        QTHelpers.setWarningLabel(self.inclinometerWarningLabel, data.anyWarning)

    @Slot(map)
    def interlockWarning(self, data):
        QTHelpers.setWarningLabel(self.interlockWarningLabel, data.anyWarning)

    @Slot(map)
    def powerWarning(self, data):
        QTHelpers.setWarningLabel(self.powerWarningLabel, data.anyWarning)

    @Slot(map)
    def accelerometerData(self, data):
        self.accelationXLabel.setText("%0.3f" % (data.angularAccelerationX))
        self.accelationYLabel.setText("%0.3f" % (data.angularAccelerationY))
        self.accelationZLabel.setText("%0.3f" % (data.angularAccelerationZ))

    @Slot(map)
    def forceActuatorData(self, data):
        self.faMeasuredXLabel.setText("%0.3f" % (data.fx))
        self.faMeasuredYLabel.setText("%0.3f" % (data.fy))
        self.faMeasuredZLabel.setText("%0.3f" % (data.fz))
        self.faMeasuredMxLabel.setText("%0.3f" % (data.mx))
        self.faMeasuredMyLabel.setText("%0.3f" % (data.my))
        self.faMeasuredMzLabel.setText("%0.3f" % (data.mz))
        self.faMeasuredMagLabel.setText("%0.3f" % (data.forceMagnitude))

    @Slot(map)
    def gyroData(self, data):
        self.velocityXLabel.setText("%0.3f" % (data.angularVelocityX))
        self.velocityYLabel.setText("%0.3f" % (data.angularVelocityY))
        self.velocityZLabel.setText("%0.3f" % (data.angularVelocityZ))

    @Slot(map)
    def hardpointActuatorData(self, data):
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

    @Slot(map)
    def imsData(self, data):
        self.imsPositionXLabel.setText("%0.3f" % (data.xPosition * 1000.0))
        self.imsPositionYLabel.setText("%0.3f" % (data.yPosition * 1000.0))
        self.imsPositionZLabel.setText("%0.3f" % (data.zPosition * 1000.0))
        self.imsPositionRxLabel.setText("%0.3f" % (data.xRotation * 1000.0))
        self.imsPositionRyLabel.setText("%0.3f" % (data.yRotation * 1000.0))
        self.imsPositionRzLabel.setText("%0.3f" % (data.zRotation * 1000.0))

    @Slot(map)
    def inclinometerData(self, data):
        self.inclinometerLabel.setText("%0.3f" % (data.inclinometerAngle))

    @Slot(map)
    def azimuth(self, data):
        self.tmaAzimuthLabel.setText("%0.3f" % (data.actualAngle))

    @Slot(map)
    def elevation(self, data):
        self.tmaElevationLabel.setText("%0.3f" % (data.actualAngle))
