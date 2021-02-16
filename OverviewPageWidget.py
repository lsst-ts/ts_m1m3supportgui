import QTHelpers
from datetime import datetime
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QGridLayout
from PySide2.QtCore import Slot

from CustomLabels import *


class OverviewPageWidget(QWidget):
    POSITIONS = [
        "xPosition",
        "yPosition",
        "zPosition",
        "xRotation",
        "yRotation",
        "zRotation",
    ]

    FORCES = ["fx", "fy", "fz", "mx", "my", "mz", "forceMagnitude"]

    def __init__(self, comm):
        super().__init__()

        self.layout = QHBoxLayout()
        dataLayout = QGridLayout()
        self.layout.addLayout(dataLayout)
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

        def createForces():
            return {
                "fx": Force(),
                "fy": Force(),
                "fz": Force(),
                "mx": Force(),
                "my": Force(),
                "mz": Force(),
                "forceMagnitude": Force(),
            }

        def addDataRow(variables, row, col=1):
            for k, v in variables.items():
                dataLayout.addWidget(v, row, col)
                col += 1

        self.faCommanded = createForces()
        self.faMeasured = createForces()

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
        dataLayout.addWidget(QLabel("Summary State"), row, col)
        dataLayout.addWidget(self.summaryStateLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Mirror State"), row, col)
        dataLayout.addWidget(self.mirrorStateLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Mode State"), row, col)
        dataLayout.addWidget(self.modeStateLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Warnings"), row, col)
        row += 1
        dataLayout.addWidget(QLabel("Interlocks"), row, col)
        dataLayout.addWidget(self.interlockWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Power"), row, col)
        dataLayout.addWidget(self.powerWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Force Actuators"), row, col)
        dataLayout.addWidget(self.forceActuatorWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Hardpoint Actuators"), row, col)
        dataLayout.addWidget(self.hardpointActuatorWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Hardpoint Monitors"), row, col)
        dataLayout.addWidget(self.hardpointMonitorWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Inclinometer"), row, col)
        dataLayout.addWidget(self.inclinometerWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Accelerometer"), row, col)
        dataLayout.addWidget(self.accelerometerWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Gyro"), row, col)
        dataLayout.addWidget(self.gyroWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Air Supply"), row, col)
        dataLayout.addWidget(self.airSupplyWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("IMS"), row, col)
        dataLayout.addWidget(self.imsWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Cell Light"), row, col)
        dataLayout.addWidget(self.cellLightWarningLabel, row, col + 1)
        row += 1
        dataLayout.addWidget(QLabel("Heartbeat"), row, col)
        dataLayout.addWidget(self.heartbeatLabel, row, col + 1)

        row = 0
        col = 2
        dataLayout.addWidget(QLabel("<b>Forces</b>"), row, col)
        dataLayout.addWidget(QLabel("<b>X</b>"), row, col + 1)
        dataLayout.addWidget(QLabel("<b>Y</b>"), row, col + 2)
        dataLayout.addWidget(QLabel("<b>Z</b>"), row, col + 3)
        dataLayout.addWidget(QLabel("<b>Mx</b>"), row, col + 4)
        dataLayout.addWidget(QLabel("<b>My</b>"), row, col + 5)
        dataLayout.addWidget(QLabel("<b>Mz</b>"), row, col + 6)
        dataLayout.addWidget(QLabel("<b>Mag</b>"), row, col + 7)

        row += 1
        dataLayout.addWidget(QLabel("<b>Commanded</b>"), row, col)
        addDataRow(self.faCommanded, row, col + 1)
        row += 1

        dataLayout.addWidget(QLabel("<b>Measured</b>"), row, col)
        addDataRow(self.faMeasured, row, col + 1)

        row += 1
        dataLayout.addWidget(QLabel("Hardpoints"), row, col)
        dataLayout.addWidget(self.hpMeasuredXLabel, row, col + 1)
        dataLayout.addWidget(self.hpMeasuredYLabel, row, col + 2)
        dataLayout.addWidget(self.hpMeasuredZLabel, row, col + 3)
        dataLayout.addWidget(self.hpMeasuredMxLabel, row, col + 4)
        dataLayout.addWidget(self.hpMeasuredMyLabel, row, col + 5)
        dataLayout.addWidget(self.hpMeasuredMzLabel, row, col + 6)
        dataLayout.addWidget(self.hpMeasuredMagLabel, row, col + 7)
        row += 1
        dataLayout.addWidget(QLabel("Mirror Position"), row, col)
        dataLayout.addWidget(QLabel("X (mm)"), row, col + 1)
        dataLayout.addWidget(QLabel("Y (mm)"), row, col + 2)
        dataLayout.addWidget(QLabel("Z (mm)"), row, col + 3)
        dataLayout.addWidget(QLabel("Rx (mrad)"), row, col + 4)
        dataLayout.addWidget(QLabel("Ry (mrad)"), row, col + 5)
        dataLayout.addWidget(QLabel("Rz (mrad)"), row, col + 6)
        row += 1
        dataLayout.addWidget(QLabel("Hardpoints"), row, col)
        dataLayout.addWidget(self.hpPositionXLabel, row, col + 1)
        dataLayout.addWidget(self.hpPositionYLabel, row, col + 2)
        dataLayout.addWidget(self.hpPositionZLabel, row, col + 3)
        dataLayout.addWidget(self.hpPositionRxLabel, row, col + 4)
        dataLayout.addWidget(self.hpPositionRyLabel, row, col + 5)
        dataLayout.addWidget(self.hpPositionRzLabel, row, col + 6)
        row += 1
        dataLayout.addWidget(QLabel("IMS"), row, col)
        dataLayout.addWidget(self.imsPositionXLabel, row, col + 1)
        dataLayout.addWidget(self.imsPositionYLabel, row, col + 2)
        dataLayout.addWidget(self.imsPositionZLabel, row, col + 3)
        dataLayout.addWidget(self.imsPositionRxLabel, row, col + 4)
        dataLayout.addWidget(self.imsPositionRyLabel, row, col + 5)
        dataLayout.addWidget(self.imsPositionRzLabel, row, col + 6)
        row += 1
        dataLayout.addWidget(QLabel("Angular Acceleration"), row, col)
        dataLayout.addWidget(QLabel("X (?)"), row, col + 1)
        dataLayout.addWidget(QLabel("Y (?)"), row, col + 2)
        dataLayout.addWidget(QLabel("Z (?)"), row, col + 3)
        row += 1
        dataLayout.addWidget(self.accelationXLabel, row, col + 1)
        dataLayout.addWidget(self.accelationYLabel, row, col + 2)
        dataLayout.addWidget(self.accelationZLabel, row, col + 3)
        row += 1
        dataLayout.addWidget(QLabel("Angular Velocity"), row, col)
        dataLayout.addWidget(QLabel("X (?)"), row, col + 1)
        dataLayout.addWidget(QLabel("Y (?)"), row, col + 2)
        dataLayout.addWidget(QLabel("Z (?)"), row, col + 3)
        row += 1
        dataLayout.addWidget(self.velocityXLabel, row, col + 1)
        dataLayout.addWidget(self.velocityYLabel, row, col + 2)
        dataLayout.addWidget(self.velocityZLabel, row, col + 3)
        row += 1
        dataLayout.addWidget(QLabel("Air Supply"), row, col)
        dataLayout.addWidget(QLabel("Commanded"), row, col + 1)
        dataLayout.addWidget(QLabel("Valve State"), row, col + 2)
        row += 1
        dataLayout.addWidget(self.airCommandLabel, row, col + 1)
        dataLayout.addWidget(self.airValveLabel, row, col + 2)
        row += 1
        dataLayout.addWidget(QLabel("M1M3"), row, col + 1)
        dataLayout.addWidget(QLabel("TMA"), row, col + 2)
        row += 1
        dataLayout.addWidget(QLabel("Azimuth (deg)"), row, col)
        dataLayout.addWidget(QLabel("-"), row, col + 1)
        dataLayout.addWidget(self.tmaAzimuthLabel, row, col + 2)
        row += 1
        dataLayout.addWidget(QLabel("Elevation (deg)"), row, col)
        dataLayout.addWidget(self.inclinometerLabel, row, col + 1)
        dataLayout.addWidget(self.tmaElevationLabel, row, col + 2)

        comm.accelerometerWarning.connect(self.accelerometerWarning)
        comm.airSupplyWarning.connect(self.airSupplyWarning)
        comm.appliedForces.connect(self.appliedForces)
        comm.cellLightWarning.connect(self.cellLightWarning)
        comm.detailedState.connect(self.detailedState)
        comm.displacementSensorWarning.connect(self.displacementSensorWarning)
        comm.forceActuatorWarning.connect(self.forceActuatorWarning)
        comm.gyroWarning.connect(self.gyroWarning)
        comm.hardpointActuatorWarning.connect(self.hardpointActuatorWarning)
        comm.hardpointMonitorWarning.connect(self.hardpointMonitorWarning)
        comm.heartbeat.connect(self.heartbeat)
        comm.inclinometerSensorWarning.connect(self.inclinometerSensorWarning)
        comm.interlockWarning.connect(self.interlockWarning)
        comm.powerWarning.connect(self.powerWarning)

        comm.accelerometerData.connect(self.accelerometerData)
        comm.forceActuatorData.connect(self.forceActuatorData)
        comm.gyroData.connect(self.gyroData)
        comm.hardpointActuatorData.connect(self.hardpointActuatorData)
        comm.imsData.connect(self.imsData)
        comm.inclinometerData.connect(self.inclinometerData)

        comm.azimuth.connect(self.azimuth)
        comm.elevation.connect(self.elevation)

    def accelerometerWarning(self, data):
        QTHelpers.setWarningLabel(self.accelerometerWarningLabel, data.anyWarning)

    @Slot(map)
    def airSupplyWarning(self, data):
        QTHelpers.setWarningLabel(self.airSupplyWarningLabel, data.anyWarning)

    def _setValues(self, variables, data):
        for k, v in variables.items():
            v.setValue(getattr(data, k))

    @Slot(map)
    def appliedForces(self, data):
        self._setValues(self.faCommanded, data)

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
        self._setValues(self.faMeasured, data)

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
