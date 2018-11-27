
import QTHelpers
from DataCache import DataCache
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class ActuatorOverviewPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.maxPlotSize = 50 * 30 # 50Hz * 30s

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
        self.aberrationMagLabel = QLabel("UNKNOWN")
        self.activeOpticZLabel = QLabel("UNKNOWN")
        self.activeOpticMxLabel = QLabel("UNKNOWN")
        self.activeOpticMyLabel = QLabel("UNKNOWN")
        self.activeOpticMagLabel = QLabel("UNKNOWN")
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

        self.plot = pg.PlotWidget()
        self.plot.plotItem.addLegend()
        self.plot.plotItem.setTitle("Total Force")
        self.plot.plotItem.setLabel(axis = 'left', text = 'Force (N)')
        self.plot.plotItem.setLabel(axis = 'bottom', text = 'Age (s)')
        self.appliedForcesMagnitudeCurve = self.plot.plot(name = 'Total Mag', pen = 'r')

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
        self.dataLayout.addWidget(self.aberrationMagLabel, row, col +7)
        row += 1
        self.dataLayout.addWidget(QLabel("Active Optic"), row, col)
        self.dataLayout.addWidget(QLabel("-"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-"), row, col + 2)
        self.dataLayout.addWidget(self.activeOpticZLabel, row, col + 3)
        self.dataLayout.addWidget(self.activeOpticMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.activeOpticMyLabel, row, col + 5)
        self.dataLayout.addWidget(QLabel("-"), row, col + 6)
        self.dataLayout.addWidget(self.activeOpticMagLabel, row, col + 7)
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

        self.plotLayout.addWidget(self.plot)

        self.dataEventAppliedAberrationForces = DataCache()
        self.dataEventAppliedAccelerationForces = DataCache()
        self.dataEventAppliedActiveOpticForces = DataCache()
        self.dataEventAppliedAzimuthForces = DataCache()
        self.dataEventAppliedBalanceForces = DataCache()
        self.dataEventAppliedCylinderForces = DataCache()
        self.dataEventAppliedElevationForces = DataCache()
        self.appliedForcesMagnitudeCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.dataEventAppliedForces = DataCache()
        self.dataEventAppliedOffsetForces = DataCache()
        self.dataEventAppliedStaticForces = DataCache()
        self.dataEventAppliedThermalForces = DataCache()
        self.dataEventAppliedVelocityForces = DataCache()

        self.MTM1M3.subscribeEvent_appliedAberrationForces(self.processEventAppliedAberrationForces)
        self.MTM1M3.subscribeEvent_appliedAccelerationForces(self.processEventAppliedAccelerationForces)
        self.MTM1M3.subscribeEvent_appliedActiveOpticForces(self.processEventAppliedActiveOpticForces)
        self.MTM1M3.subscribeEvent_appliedAzimuthForces(self.processEventAppliedAzimuthForces)
        self.MTM1M3.subscribeEvent_appliedBalanceForces(self.processEventAppliedBalanceForces)
        self.MTM1M3.subscribeEvent_appliedCylinderForces(self.processEventAppliedCylinderForces)
        self.MTM1M3.subscribeEvent_appliedElevationForces(self.processEventAppliedElevationForces)
        self.MTM1M3.subscribeEvent_appliedForces(self.processEventAppliedForces)
        self.MTM1M3.subscribeEvent_appliedOffsetForces(self.processEventAppliedOffsetForces)
        self.MTM1M3.subscribeEvent_appliedStaticForces(self.processEventAppliedStaticForces)
        self.MTM1M3.subscribeEvent_appliedThermalForces(self.processEventAppliedThermalForces)
        self.MTM1M3.subscribeEvent_appliedVelocityForces(self.processEventAppliedVelocityForces)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 
        
        if self.dataEventAppliedAberrationForces.hasBeenUpdated():
            data = self.dataEventAppliedAberrationForces.get()
            self.aberrationZLabel.setText("%0.1f" % data.fZ)
            self.aberrationMxLabel.setText("%0.1f" % data.mX)
            self.aberrationMyLabel.setText("%0.1f" % data.mY)
            self.aberrationMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedAccelerationForces.hasBeenUpdated():
            data = self.dataEventAppliedAccelerationForces.get()
            self.accelerationXLabel.setText("%0.1f" % data.fX)
            self.accelerationYLabel.setText("%0.1f" % data.fY)
            self.accelerationZLabel.setText("%0.1f" % data.fZ)
            self.accelerationMxLabel.setText("%0.1f" % data.mX)
            self.accelerationMyLabel.setText("%0.1f" % data.mY)
            self.accelerationMzLabel.setText("%0.1f" % data.mZ)
            self.accelerationMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedActiveOpticForces.hasBeenUpdated():
            data = self.dataEventAppliedActiveOpticForces.get()
            self.activeOpticZLabel.setText("%0.1f" % data.fZ)
            self.activeOpticMxLabel.setText("%0.1f" % data.mX)
            self.activeOpticMyLabel.setText("%0.1f" % data.mY)
            self.activeOpticMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedAzimuthForces.hasBeenUpdated():
            data = self.dataEventAppliedAzimuthForces.get()
            self.azimuthXLabel.setText("%0.1f" % data.fX)
            self.azimuthYLabel.setText("%0.1f" % data.fY)
            self.azimuthZLabel.setText("%0.1f" % data.fZ)
            self.azimuthMxLabel.setText("%0.1f" % data.mX)
            self.azimuthMyLabel.setText("%0.1f" % data.mY)
            self.azimuthMzLabel.setText("%0.1f" % data.mZ)
            self.azimuthMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedBalanceForces.hasBeenUpdated():
            data = self.dataEventAppliedBalanceForces.get()
            self.balanceXLabel.setText("%0.1f" % data.fX)
            self.balanceYLabel.setText("%0.1f" % data.fY)
            self.balanceZLabel.setText("%0.1f" % data.fZ)
            self.balanceMxLabel.setText("%0.1f" % data.mX)
            self.balanceMyLabel.setText("%0.1f" % data.mY)
            self.balanceMzLabel.setText("%0.1f" % data.mZ)
            self.balanceMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedCylinderForces.hasBeenUpdated():
            data = self.dataEventAppliedCylinderForces.get()

        if self.dataEventAppliedElevationForces.hasBeenUpdated():
            data = self.dataEventAppliedElevationForces.get()
            self.elevationXLabel.setText("%0.1f" % data.fX)
            self.elevationYLabel.setText("%0.1f" % data.fY)
            self.elevationZLabel.setText("%0.1f" % data.fZ)
            self.elevationMxLabel.setText("%0.1f" % data.mX)
            self.elevationMyLabel.setText("%0.1f" % data.mY)
            self.elevationMzLabel.setText("%0.1f" % data.mZ)
            self.elevationMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.appliedForcesMagnitudeCurveData.hasBeenUpdated():
            data = self.appliedForcesMagnitudeCurveData.get()
            self.appliedForcesMagnitudeCurve.setData(data)

        if self.dataEventAppliedForces.hasBeenUpdated():
            data = self.dataEventAppliedForces.get()
            self.totalCommandedXLabel.setText("%0.1f" % data.fX)
            self.totalCommandedYLabel.setText("%0.1f" % data.fY)
            self.totalCommandedZLabel.setText("%0.1f" % data.fZ)
            self.totalCommandedMxLabel.setText("%0.1f" % data.mX)
            self.totalCommandedMyLabel.setText("%0.1f" % data.mY)
            self.totalCommandedMzLabel.setText("%0.1f" % data.mZ)
            self.totalCommandedMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedOffsetForces.hasBeenUpdated():
            data = self.dataEventAppliedOffsetForces.get()
            self.offsetXLabel.setText("%0.1f" % data.fX)
            self.offsetYLabel.setText("%0.1f" % data.fY)
            self.offsetZLabel.setText("%0.1f" % data.fZ)
            self.offsetMxLabel.setText("%0.1f" % data.mX)
            self.offsetMyLabel.setText("%0.1f" % data.mY)
            self.offsetMzLabel.setText("%0.1f" % data.mZ)
            self.offsetMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedStaticForces.hasBeenUpdated():
            data = self.dataEventAppliedStaticForces.get()
            self.staticXLabel.setText("%0.1f" % data.fX)
            self.staticYLabel.setText("%0.1f" % data.fY)
            self.staticZLabel.setText("%0.1f" % data.fZ)
            self.staticMxLabel.setText("%0.1f" % data.mX)
            self.staticMyLabel.setText("%0.1f" % data.mY)
            self.staticMzLabel.setText("%0.1f" % data.mZ)
            self.staticMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedThermalForces.hasBeenUpdated():
            data = self.dataEventAppliedThermalForces.get()
            self.thermalXLabel.setText("%0.1f" % data.fX)
            self.thermalYLabel.setText("%0.1f" % data.fY)
            self.thermalZLabel.setText("%0.1f" % data.fZ)
            self.thermalMxLabel.setText("%0.1f" % data.mX)
            self.thermalMyLabel.setText("%0.1f" % data.mY)
            self.thermalMzLabel.setText("%0.1f" % data.mZ)
            self.thermalMagLabel.setText("%0.1f" % data.forceMagnitude)

        if self.dataEventAppliedVelocityForces.hasBeenUpdated():
            data = self.dataEventAppliedVelocityForces.get()
            self.velocityXLabel.setText("%0.1f" % data.fX)
            self.velocityYLabel.setText("%0.1f" % data.fY)
            self.velocityZLabel.setText("%0.1f" % data.fZ)
            self.velocityMxLabel.setText("%0.1f" % data.mX)
            self.velocityMyLabel.setText("%0.1f" % data.mY)
            self.velocityMzLabel.setText("%0.1f" % data.mZ)
            self.velocityMagLabel.setText("%0.1f" % data.forceMagnitude)

    def processEventAppliedAberrationForces(self, data):
        self.dataEventAppliedAberrationForces.set(data[-1])
        
    def processEventAppliedAccelerationForces(self, data):
        self.dataEventAppliedAccelerationForces.set(data[-1])

    def processEventAppliedActiveOpticForces(self, data):
        self.dataEventAppliedActiveOpticForces.set(data[-1])
        
    def processEventAppliedAzimuthForces(self, data):
        self.dataEventAppliedAzimuthForces.set(data[-1])
        
    def processEventAppliedBalanceForces(self, data):
        self.dataEventAppliedBalanceForces.set(data[-1])

    def processEventAppliedCylinderForces(self, data):
        self.dataEventAppliedCylinderForces.set(data[-1])

    def processEventAppliedElevationForces(self, data):
        self.dataEventAppliedElevationForces.set(data[-1])
        
    def processEventAppliedForces(self, data):
        self.appliedForcesMagnitudeCurveData.set(QTHelpers.appendAndResizeCurveData(self.appliedForcesMagnitudeCurveData.get(), [x.forceMagnitude for x in data], self.maxPlotSize))
        self.dataEventAppliedForces.set(data[-1])
        
    def processEventAppliedOffsetForces(self, data):
        self.dataEventAppliedOffsetForces.set(data[-1])
        
    def processEventAppliedStaticForces(self, data):
        self.dataEventAppliedStaticForces.set(data[-1])
        
    def processEventAppliedThermalForces(self, data):
        self.dataEventAppliedThermalForces.set(data[-1])
        
    def processEventAppliedVelocityForces(self, data):
        self.dataEventAppliedVelocityForces.set(data[-1])