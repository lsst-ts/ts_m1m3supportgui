import TimeChart
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout)
from PySide2.QtCore import Slot

class ActuatorOverviewPageWidget(QWidget):
    def __init__(self, comm):
        QWidget.__init__(self)
        self.comm = comm
        self.pageActive = False

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.totalCommandedXLabel = QLabel("UNKNOWN")
        self.totalCommandedYLabel = QLabel("UNKNOWN")
        self.totalCommandedZLabel = QLabel("UNKNOWN")
        self.totalCommandedMxLabel = QLabel("UNKNOWN")
        self.totalCommandedMyLabel = QLabel("UNKNOWN")
        self.totalCommandedMzLabel = QLabel("UNKNOWN")
        self.totalCommandedMagLabel = QLabel("UNKNOWN")
        self.totalMeasuredXLabel = QLabel("UNKNOWN")
        self.totalMeasuredYLabel = QLabel("UNKNOWN")
        self.totalMeasuredZLabel = QLabel("UNKNOWN")
        self.totalMeasuredMxLabel = QLabel("UNKNOWN")
        self.totalMeasuredMyLabel = QLabel("UNKNOWN")
        self.totalMeasuredMzLabel = QLabel("UNKNOWN")
        self.totalMeasuredMagLabel = QLabel("UNKNOWN")
        self.totalErrorXLabel = QLabel("UNKNOWN")
        self.totalErrorYLabel = QLabel("UNKNOWN")
        self.totalErrorZLabel = QLabel("UNKNOWN")
        self.totalErrorMxLabel = QLabel("UNKNOWN")
        self.totalErrorMyLabel = QLabel("UNKNOWN")
        self.totalErrorMzLabel = QLabel("UNKNOWN")
        self.totalErrorMagLabel = QLabel("UNKNOWN")
        self.totalMirrorXLabel = QLabel("UNKNOWN")
        self.totalMirrorYLabel = QLabel("UNKNOWN")
        self.totalMirrorZLabel = QLabel("UNKNOWN")
        self.totalMirrorMxLabel = QLabel("UNKNOWN")
        self.totalMirrorMyLabel = QLabel("UNKNOWN")
        self.totalMirrorMzLabel = QLabel("UNKNOWN")
        self.totalMirrorMagLabel = QLabel("UNKNOWN")
        self.accelerationXLabel = QLabel("UNKNOWN")
        self.accelerationYLabel = QLabel("UNKNOWN")
        self.accelerationZLabel = QLabel("UNKNOWN")
        self.accelerationMxLabel = QLabel("UNKNOWN")
        self.accelerationMyLabel = QLabel("UNKNOWN")
        self.accelerationMzLabel = QLabel("UNKNOWN")
        self.accelerationMagLabel = QLabel("UNKNOWN")
        self.aberrationZLabel = QLabel("UNKNOWN")
        self.aberrationMxLabel = QLabel("UNKNOWN")
        self.aberrationMyLabel = QLabel("UNKNOWN")
        self.activeOpticZLabel = QLabel("UNKNOWN")
        self.activeOpticMxLabel = QLabel("UNKNOWN")
        self.activeOpticMyLabel = QLabel("UNKNOWN")
        self.azimuthXLabel = QLabel("UNKNOWN")
        self.azimuthYLabel = QLabel("UNKNOWN")
        self.azimuthZLabel = QLabel("UNKNOWN")
        self.azimuthMxLabel = QLabel("UNKNOWN")
        self.azimuthMyLabel = QLabel("UNKNOWN")
        self.azimuthMzLabel = QLabel("UNKNOWN")
        self.azimuthMagLabel = QLabel("UNKNOWN")
        self.balanceXLabel = QLabel("UNKNOWN")
        self.balanceYLabel = QLabel("UNKNOWN")
        self.balanceZLabel = QLabel("UNKNOWN")
        self.balanceMxLabel = QLabel("UNKNOWN")
        self.balanceMyLabel = QLabel("UNKNOWN")
        self.balanceMzLabel = QLabel("UNKNOWN")
        self.balanceMagLabel = QLabel("UNKNOWN")
        self.elevationXLabel = QLabel("UNKNOWN")
        self.elevationYLabel = QLabel("UNKNOWN")
        self.elevationZLabel = QLabel("UNKNOWN")
        self.elevationMxLabel = QLabel("UNKNOWN")
        self.elevationMyLabel = QLabel("UNKNOWN")
        self.elevationMzLabel = QLabel("UNKNOWN")
        self.elevationMagLabel = QLabel("UNKNOWN")
        self.offsetXLabel = QLabel("UNKNOWN")
        self.offsetYLabel = QLabel("UNKNOWN")
        self.offsetZLabel = QLabel("UNKNOWN")
        self.offsetMxLabel = QLabel("UNKNOWN")
        self.offsetMyLabel = QLabel("UNKNOWN")
        self.offsetMzLabel = QLabel("UNKNOWN")
        self.offsetMagLabel = QLabel("UNKNOWN")
        self.staticXLabel = QLabel("UNKNOWN")
        self.staticYLabel = QLabel("UNKNOWN")
        self.staticZLabel = QLabel("UNKNOWN")
        self.staticMxLabel = QLabel("UNKNOWN")
        self.staticMyLabel = QLabel("UNKNOWN")
        self.staticMzLabel = QLabel("UNKNOWN")
        self.staticMagLabel = QLabel("UNKNOWN")
        self.thermalXLabel = QLabel("UNKNOWN")
        self.thermalYLabel = QLabel("UNKNOWN")
        self.thermalZLabel = QLabel("UNKNOWN")
        self.thermalMxLabel = QLabel("UNKNOWN")
        self.thermalMyLabel = QLabel("UNKNOWN")
        self.thermalMzLabel = QLabel("UNKNOWN")
        self.thermalMagLabel = QLabel("UNKNOWN")
        self.velocityXLabel = QLabel("UNKNOWN")
        self.velocityYLabel = QLabel("UNKNOWN")
        self.velocityZLabel = QLabel("UNKNOWN")
        self.velocityMxLabel = QLabel("UNKNOWN")
        self.velocityMyLabel = QLabel("UNKNOWN")
        self.velocityMzLabel = QLabel("UNKNOWN")
        self.velocityMagLabel = QLabel("UNKNOWN")

        self.chart = TimeChart.TimeChart(50 * 30) # 50Hz * 30s
        self.chart_view = TimeChart.TimeChartView(self.chart)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Forces"), row, col)
        self.dataLayout.addWidget(QLabel("X (N)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y (N)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z (N)"), row, col + 3)
        self.dataLayout.addWidget(QLabel("Mx (Nm)"), row, col + 4)
        self.dataLayout.addWidget(QLabel("My (Nm)"), row, col + 5)
        self.dataLayout.addWidget(QLabel("Mz (Nm)"), row, col + 6)
        self.dataLayout.addWidget(QLabel("Magnitude (N)"), row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Total Commanded"), row, col)
        self.dataLayout.addWidget(self.totalCommandedXLabel, row, col + 1)
        self.dataLayout.addWidget(self.totalCommandedYLabel, row, col + 2)
        self.dataLayout.addWidget(self.totalCommandedZLabel, row, col + 3)
        self.dataLayout.addWidget(self.totalCommandedMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.totalCommandedMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.totalCommandedMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.totalCommandedMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Total Measured"), row, col)
        self.dataLayout.addWidget(self.totalMeasuredXLabel, row, col + 1)
        self.dataLayout.addWidget(self.totalMeasuredYLabel, row, col + 2)
        self.dataLayout.addWidget(self.totalMeasuredZLabel, row, col + 3)
        self.dataLayout.addWidget(self.totalMeasuredMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.totalMeasuredMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.totalMeasuredMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.totalMeasuredMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Total Error"), row, col)
        self.dataLayout.addWidget(self.totalErrorXLabel, row, col + 1)
        self.dataLayout.addWidget(self.totalErrorYLabel, row, col + 2)
        self.dataLayout.addWidget(self.totalErrorZLabel, row, col + 3)
        self.dataLayout.addWidget(self.totalErrorMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.totalErrorMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.totalErrorMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.totalErrorMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Total Mirror"), row, col)
        self.dataLayout.addWidget(self.totalMirrorXLabel, row, col + 1)
        self.dataLayout.addWidget(self.totalMirrorYLabel, row, col + 2)
        self.dataLayout.addWidget(self.totalMirrorZLabel, row, col + 3)
        self.dataLayout.addWidget(self.totalMirrorMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.totalMirrorMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.totalMirrorMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.totalMirrorMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Acceleration"), row, col)
        self.dataLayout.addWidget(self.accelerationXLabel, row, col + 1)
        self.dataLayout.addWidget(self.accelerationYLabel, row, col + 2)
        self.dataLayout.addWidget(self.accelerationZLabel, row, col + 3)
        self.dataLayout.addWidget(self.accelerationMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.accelerationMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.accelerationMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.accelerationMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Aberration"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-"), row, col + 2)
        self.dataLayout.addWidget(self.aberrationZLabel, row, col + 3)
        self.dataLayout.addWidget(self.aberrationMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.aberrationMyLabel, row, col + 5)
        self.dataLayout.addWidget(QLabel("-"), row, col + 6)
        row += 1
        self.dataLayout.addWidget(QLabel("Active Optic"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-"), row, col + 2)
        self.dataLayout.addWidget(self.activeOpticZLabel, row, col + 3)
        self.dataLayout.addWidget(self.activeOpticMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.activeOpticMyLabel, row, col + 5)
        self.dataLayout.addWidget(QLabel("-"), row, col + 6)
        row += 1
        self.dataLayout.addWidget(QLabel("Azimuth"), row, col)
        self.dataLayout.addWidget(self.azimuthXLabel, row, col + 1)
        self.dataLayout.addWidget(self.azimuthYLabel, row, col + 2)
        self.dataLayout.addWidget(self.azimuthZLabel, row, col + 3)
        self.dataLayout.addWidget(self.azimuthMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.azimuthMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.azimuthMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.azimuthMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Balance"), row, col)
        self.dataLayout.addWidget(self.balanceXLabel, row, col + 1)
        self.dataLayout.addWidget(self.balanceYLabel, row, col + 2)
        self.dataLayout.addWidget(self.balanceZLabel, row, col + 3)
        self.dataLayout.addWidget(self.balanceMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.balanceMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.balanceMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.balanceMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Elevation"), row, col)
        self.dataLayout.addWidget(self.elevationXLabel, row, col + 1)
        self.dataLayout.addWidget(self.elevationYLabel, row, col + 2)
        self.dataLayout.addWidget(self.elevationZLabel, row, col + 3)
        self.dataLayout.addWidget(self.elevationMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.elevationMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.elevationMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.elevationMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Offset"), row, col)
        self.dataLayout.addWidget(self.offsetXLabel, row, col + 1)
        self.dataLayout.addWidget(self.offsetYLabel, row, col + 2)
        self.dataLayout.addWidget(self.offsetZLabel, row, col + 3)
        self.dataLayout.addWidget(self.offsetMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.offsetMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.offsetMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.offsetMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Static"), row, col)
        self.dataLayout.addWidget(self.staticXLabel, row, col + 1)
        self.dataLayout.addWidget(self.staticYLabel, row, col + 2)
        self.dataLayout.addWidget(self.staticZLabel, row, col + 3)
        self.dataLayout.addWidget(self.staticMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.staticMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.staticMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.staticMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Thermal"), row, col)
        self.dataLayout.addWidget(self.thermalXLabel, row, col + 1)
        self.dataLayout.addWidget(self.thermalYLabel, row, col + 2)
        self.dataLayout.addWidget(self.thermalZLabel, row, col + 3)
        self.dataLayout.addWidget(self.thermalMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.thermalMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.thermalMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.thermalMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Velocity"), row, col)
        self.dataLayout.addWidget(self.velocityXLabel, row, col + 1)
        self.dataLayout.addWidget(self.velocityYLabel, row, col + 2)
        self.dataLayout.addWidget(self.velocityZLabel, row, col + 3)
        self.dataLayout.addWidget(self.velocityMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.velocityMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.velocityMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.velocityMagLabel, row, col + 7)

        self.plotLayout.addWidget(self.chart_view)

    def setPageActive(self, active):
        if self.pageActive == active:
            return

        if active:
            self.comm.appliedAberrationForces.connect(self.appliedAberrationForces)
            self.comm.appliedAccelerationForces.connect(self.appliedAccelerationForces)
            self.comm.appliedActiveOpticForces.connect(self.appliedActiveOpticForces)
            self.comm.appliedAzimuthForces.connect(self.appliedAzimuthForces)
            self.comm.appliedBalanceForces.connect(self.appliedBalanceForces)
            self.comm.appliedElevationForces.connect(self.appliedElevationForces)
            self.comm.appliedForces.connect(self.appliedForces)
            self.comm.appliedOffsetForces.connect(self.appliedOffsetForces)
            self.comm.appliedStaticForces.connect(self.appliedStaticForces)
            self.comm.appliedThermalForces.connect(self.appliedThermalForces)
            self.comm.appliedVelocityForces.connect(self.appliedVelocityForces)
        else:
            self.comm.appliedAberrationForces.disconnect(self.appliedAberrationForces)
            self.comm.appliedAccelerationForces.disconnect(self.appliedAccelerationForces)
            self.comm.appliedActiveOpticForces.disconnect(self.appliedActiveOpticForces)
            self.comm.appliedAzimuthForces.disconnect(self.appliedAzimuthForces)
            self.comm.appliedBalanceForces.disconnect(self.appliedBalanceForces)
            self.comm.appliedElevationForces.disconnect(self.appliedElevationForces)
            self.comm.appliedForces.disconnect(self.appliedForces)
            self.comm.appliedOffsetForces.disconnect(self.appliedOffsetForces)
            self.comm.appliedStaticForces.disconnect(self.appliedStaticForces)
            self.comm.appliedThermalForces.disconnect(self.appliedThermalForces)
            self.comm.appliedVelocityForces.disconnect(self.appliedVelocityForces)

        self.pageActive = active

    @Slot(map)
    def appliedAberrationForces(self, data):
        self.aberrationZLabel.setText("%0.1f" % data.fz)
        self.aberrationMxLabel.setText("%0.1f" % data.mx)
        self.aberrationMyLabel.setText("%0.1f" % data.my)

    @Slot(map)
    def appliedAccelerationForces(self, data):
        self.accelerationXLabel.setText("%0.1f" % data.fx)
        self.accelerationYLabel.setText("%0.1f" % data.fy)
        self.accelerationZLabel.setText("%0.1f" % data.fz)
        self.accelerationMxLabel.setText("%0.1f" % data.mx)
        self.accelerationMyLabel.setText("%0.1f" % data.my)
        self.accelerationMzLabel.setText("%0.1f" % data.mz)
        self.accelerationMagLabel.setText("%0.1f" % data.forceMagnitude)
    
    @Slot(map)
    def appliedActiveOpticForces(self, data):
        self.activeOpticZLabel.setText("%0.1f" % data.fz)
        self.activeOpticMxLabel.setText("%0.1f" % data.mx)
        self.activeOpticMyLabel.setText("%0.1f" % data.my)

    @Slot(map)
    def appliedAzimuthForces(self, data):
        self.azimuthXLabel.setText("%0.1f" % data.fx)
        self.azimuthYLabel.setText("%0.1f" % data.fy)
        self.azimuthZLabel.setText("%0.1f" % data.fz)
        self.azimuthMxLabel.setText("%0.1f" % data.mx)
        self.azimuthMyLabel.setText("%0.1f" % data.my)
        self.azimuthMzLabel.setText("%0.1f" % data.mz)
        self.azimuthMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedBalanceForces(self, data):
        self.balanceXLabel.setText("%0.1f" % data.fx)
        self.balanceYLabel.setText("%0.1f" % data.fy)
        self.balanceZLabel.setText("%0.1f" % data.fz)
        self.balanceMxLabel.setText("%0.1f" % data.mx)
        self.balanceMyLabel.setText("%0.1f" % data.my)
        self.balanceMzLabel.setText("%0.1f" % data.mz)
        self.balanceMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedElevationForces(self, data):
        self.elevationXLabel.setText("%0.1f" % data.fx)
        self.elevationYLabel.setText("%0.1f" % data.fy)
        self.elevationZLabel.setText("%0.1f" % data.fz)
        self.elevationMxLabel.setText("%0.1f" % data.mx)
        self.elevationMyLabel.setText("%0.1f" % data.my)
        self.elevationMzLabel.setText("%0.1f" % data.mz)
        self.elevationMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedForces(self, data):
        self.totalCommandedXLabel.setText("%0.1f" % data.fx)
        self.totalCommandedYLabel.setText("%0.1f" % data.fy)
        self.totalCommandedZLabel.setText("%0.1f" % data.fz)
        self.totalCommandedMxLabel.setText("%0.1f" % data.mx)
        self.totalCommandedMyLabel.setText("%0.1f" % data.my)
        self.totalCommandedMzLabel.setText("%0.1f" % data.mz)
        self.totalCommandedMagLabel.setText("%0.1f" % data.forceMagnitude)

        self.chart.append('Force (N)', 'Total Mag', [(data.timestamp, data.forceMagnitude)])

    @Slot(map)
    def appliedOffsetForces(self, data):
        self.offsetXLabel.setText("%0.1f" % data.fx)
        self.offsetYLabel.setText("%0.1f" % data.fy)
        self.offsetZLabel.setText("%0.1f" % data.fz)
        self.offsetMxLabel.setText("%0.1f" % data.mx)
        self.offsetMyLabel.setText("%0.1f" % data.my)
        self.offsetMzLabel.setText("%0.1f" % data.mz)
        self.offsetMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedStaticForces(self, data):
        self.staticXLabel.setText("%0.1f" % data.fx)
        self.staticYLabel.setText("%0.1f" % data.fy)
        self.staticZLabel.setText("%0.1f" % data.fz)
        self.staticMxLabel.setText("%0.1f" % data.mx)
        self.staticMyLabel.setText("%0.1f" % data.my)
        self.staticMzLabel.setText("%0.1f" % data.mz)
        self.staticMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedThermalForces(self, data):
        self.thermalXLabel.setText("%0.1f" % data.fx)
        self.thermalYLabel.setText("%0.1f" % data.fy)
        self.thermalZLabel.setText("%0.1f" % data.fz)
        self.thermalMxLabel.setText("%0.1f" % data.mx)
        self.thermalMyLabel.setText("%0.1f" % data.my)
        self.thermalMzLabel.setText("%0.1f" % data.mz)
        self.thermalMagLabel.setText("%0.1f" % data.forceMagnitude)

    @Slot(map)
    def appliedVelocityForces(self, data):
        self.velocityXLabel.setText("%0.1f" % data.fx)
        self.velocityYLabel.setText("%0.1f" % data.fy)
        self.velocityZLabel.setText("%0.1f" % data.fz)
        self.velocityMxLabel.setText("%0.1f" % data.mx)
        self.velocityMyLabel.setText("%0.1f" % data.my)
        self.velocityMzLabel.setText("%0.1f" % data.mz)
        self.velocityMagLabel.setText("%0.1f" % data.forceMagnitude)
