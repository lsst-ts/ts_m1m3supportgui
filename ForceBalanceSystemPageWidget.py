
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import HardpointIndexMap, ForceActuatorFlags
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class ForceBalanceSystemPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.commandLayout = QVBoxLayout()
        self.plotLayout = QHBoxLayout()
        self.layout.addLayout(self.commandLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.maxPlotSize = 50 * 30 # 50Hz * 30s
        
        self.enableHardpointCorrectionsButton = QPushButton("Enable Hardpoint Corrections")
        self.enableHardpointCorrectionsButton.clicked.connect(self.issueCommandEnableHardpointCorrections)
        self.enableHardpointCorrectionsButton.setFixedWidth(256)
        self.disableHardpointCorrectionsButton = QPushButton("Disable Hardpoint Corrections")
        self.disableHardpointCorrectionsButton.clicked.connect(self.issueCommandDisableHardpointCorrections)
        self.disableHardpointCorrectionsButton.setFixedWidth(256)

        self.hardpoint1ForceLabel = QLabel("0.0")
        self.hardpoint2ForceLabel = QLabel("0.0")
        self.hardpoint3ForceLabel = QLabel("0.0")
        self.hardpoint4ForceLabel = QLabel("0.0")
        self.hardpoint5ForceLabel = QLabel("0.0")
        self.hardpoint6ForceLabel = QLabel("0.0")
        self.hardpointMagForceLabel = QLabel("0.0")
        self.hardpointFxLabel = QLabel("0.0")
        self.hardpointFyLabel = QLabel("0.0")
        self.hardpointFzLabel = QLabel("0.0")
        self.hardpointMxLabel = QLabel("0.0")
        self.hardpointMyLabel = QLabel("0.0")
        self.hardpointMzLabel = QLabel("0.0")
        self.hardpointMagLabel = QLabel("0.0")
        self.balanceFxLabel = QLabel("0.0")
        self.balanceFyLabel = QLabel("0.0")
        self.balanceFzLabel = QLabel("0.0")
        self.balanceMxLabel = QLabel("0.0")
        self.balanceMyLabel = QLabel("0.0")
        self.balanceMzLabel = QLabel("0.0")
        self.balanceMagLabel = QLabel("0.0")
        self.totalFxLabel = QLabel("0.0")
        self.totalFyLabel = QLabel("0.0")
        self.totalFzLabel = QLabel("0.0")
        self.totalMxLabel = QLabel("0.0")
        self.totalMyLabel = QLabel("0.0")
        self.totalMzLabel = QLabel("0.0")
        self.totalMagLabel = QLabel("0.0")

        self.balanceForcesClippedLabel = QLabel("UNKNOWN")

        self.balancePlot = pg.PlotWidget()
        self.balancePlot.plotItem.addLegend()
        self.balancePlot.plotItem.setTitle("Balance Forces")
        self.balancePlot.plotItem.setLabel(axis = 'left', text = 'Force (N)')
        self.balancePlot.plotItem.setLabel(axis = 'bottom', text = 'Age (s)')
        self.balanceFxCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceFyCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceFzCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceMxCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceMyCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceMzCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.balanceFxCurve = self.balancePlot.plot(name = 'Fx', pen = 'r')
        self.balanceFyCurve = self.balancePlot.plot(name = 'Fy', pen = 'g')
        self.balanceFzCurve = self.balancePlot.plot(name = 'Fz', pen = 'b')
        self.balanceMxCurve = self.balancePlot.plot(name = 'Mx', pen = 'w')
        self.balanceMyCurve = self.balancePlot.plot(name = 'My', pen = 'y')
        self.balanceMzCurve = self.balancePlot.plot(name = 'Mz', pen = 'c')

        self.commandLayout.addWidget(self.enableHardpointCorrectionsButton)
        self.commandLayout.addWidget(self.disableHardpointCorrectionsButton)
        
        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Fx (N)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Fy (N)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Fz (N)"), row, col + 3)
        self.dataLayout.addWidget(QLabel("Mx (Nm)"), row, col + 4)
        self.dataLayout.addWidget(QLabel("My (Nm)"), row, col + 5)
        self.dataLayout.addWidget(QLabel("Mz (Nm)"), row, col + 6)
        self.dataLayout.addWidget(QLabel("Mag (N)"), row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Total"), row, col)
        self.dataLayout.addWidget(self.totalFxLabel, row, col + 1)
        self.dataLayout.addWidget(self.totalFyLabel, row, col + 2)
        self.dataLayout.addWidget(self.totalFzLabel, row, col + 3)
        self.dataLayout.addWidget(self.totalMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.totalMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.totalMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.totalMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Corrected"), row, col)
        self.dataLayout.addWidget(self.balanceFxLabel, row, col + 1)
        self.dataLayout.addWidget(self.balanceFyLabel, row, col + 2)
        self.dataLayout.addWidget(self.balanceFzLabel, row, col + 3)
        self.dataLayout.addWidget(self.balanceMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.balanceMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.balanceMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.balanceMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Remaining"), row, col)
        self.dataLayout.addWidget(self.hardpointFxLabel, row, col + 1)
        self.dataLayout.addWidget(self.hardpointFyLabel, row, col + 2)
        self.dataLayout.addWidget(self.hardpointFzLabel, row, col + 3)
        self.dataLayout.addWidget(self.hardpointMxLabel, row, col + 4)
        self.dataLayout.addWidget(self.hardpointMyLabel, row, col + 5)
        self.dataLayout.addWidget(self.hardpointMzLabel, row, col + 6)
        self.dataLayout.addWidget(self.hardpointMagLabel, row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("HP1 (N)"), row, col + 1)
        self.dataLayout.addWidget(QLabel("HP2 (N)"), row, col + 2)
        self.dataLayout.addWidget(QLabel("HP3 (N)"), row, col + 3)
        self.dataLayout.addWidget(QLabel("HP4 (N)"), row, col + 4)
        self.dataLayout.addWidget(QLabel("HP5 (N)"), row, col + 5)
        self.dataLayout.addWidget(QLabel("HP6 (N)"), row, col + 6)
        self.dataLayout.addWidget(QLabel("Mag (N)"), row, col + 7)
        row += 1
        self.dataLayout.addWidget(QLabel("Measured Force"), row, col)
        self.dataLayout.addWidget(self.hardpoint1ForceLabel, row, col + 1)
        self.dataLayout.addWidget(self.hardpoint2ForceLabel, row, col + 2)
        self.dataLayout.addWidget(self.hardpoint3ForceLabel, row, col + 3)
        self.dataLayout.addWidget(self.hardpoint4ForceLabel, row, col + 4)
        self.dataLayout.addWidget(self.hardpoint5ForceLabel, row, col + 5)
        self.dataLayout.addWidget(self.hardpoint6ForceLabel, row, col + 6)
        self.dataLayout.addWidget(self.hardpointMagForceLabel, row, col + 7)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Balance Forces Clipped"), row, col)
        self.warningLayout.addWidget(self.balanceForcesClippedLabel, row, col + 1)

        self.plotLayout.addWidget(self.balancePlot)

        self.MTM1M3.subscribeEvent_appliedBalanceForces(self.processEventAppliedBalanceForces)
        self.MTM1M3.subscribeEvent_forceActuatorWarning(self.processEventForceActuatorWarning)
        self.MTM1M3.subscribeTelemetry_hardpointActuatorData(self.processTelemetryHardpointActuatorData)

    def issueCommandEnableHardpointCorrections(self):
        self.MTM1M3.issueCommandThenWait_enableHardpointCorrections(False)

    def issueCommandDisableHardpointCorrections(self):
        self.MTM1M3.issueCommandThenWait_disableHardpointCorrections(False)

    def processEventAppliedBalanceForces(self, data):
        self.balanceFxCurveData = QTHelpers.appendAndResizeCurveData(self.balanceFxCurveData, [x.fX for x in data], self.maxPlotSize)
        self.balanceFyCurveData = QTHelpers.appendAndResizeCurveData(self.balanceFyCurveData, [x.fY for x in data], self.maxPlotSize)
        self.balanceFzCurveData = QTHelpers.appendAndResizeCurveData(self.balanceFzCurveData, [x.fZ for x in data], self.maxPlotSize)
        self.balanceMxCurveData = QTHelpers.appendAndResizeCurveData(self.balanceMxCurveData, [x.mX for x in data], self.maxPlotSize)
        self.balanceMyCurveData = QTHelpers.appendAndResizeCurveData(self.balanceMyCurveData, [x.mY for x in data], self.maxPlotSize)
        self.balanceMzCurveData = QTHelpers.appendAndResizeCurveData(self.balanceMzCurveData, [x.mZ for x in data], self.maxPlotSize)
        self.balanceFxCurve.setData(self.balanceFxCurveData)
        self.balanceFyCurve.setData(self.balanceFyCurveData)
        self.balanceFzCurve.setData(self.balanceFzCurveData)
        self.balanceMxCurve.setData(self.balanceMxCurveData)
        self.balanceMyCurve.setData(self.balanceMyCurveData)
        self.balanceMzCurve.setData(self.balanceMzCurveData)

        data = data[-1]
        self.balanceFxLabel.setText("%0.1f" % data.fX)
        self.balanceFyLabel.setText("%0.1f" % data.fY)
        self.balanceFzLabel.setText("%0.1f" % data.fZ)
        self.balanceMxLabel.setText("%0.1f" % data.mX)
        self.balanceMyLabel.setText("%0.1f" % data.mY)
        self.balanceMzLabel.setText("%0.1f" % data.mZ)
        self.balanceMagLabel.setText("%0.1f" % data.forceMagnitude)
        self.setTotalForces()

    def processEventForceActuatorWarning(self, data):
        data = data[-1]
        QTHelpers.setBoolLabelYesNo(self.balanceForcesClippedLabel, BitHelper.get(data.anyForceActuatorFlags, ForceActuatorFlags.ForceSetpointBalanceForceClipped))

    def processTelemetryHardpointActuatorData(self, data):
        data = data[-1]
        self.hardpoint1ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint1])
        self.hardpoint2ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint2])
        self.hardpoint3ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint3])
        self.hardpoint4ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint4])
        self.hardpoint5ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint5])
        self.hardpoint6ForceLabel.setText("%0.1f" % data.measuredForce[HardpointIndexMap.Hardpoint6])
        self.hardpointMagForceLabel.setText("%0.1f" % (sum(data.measuredForce)))
        self.hardpointFxLabel.setText("%0.1f" % data.fX)
        self.hardpointFyLabel.setText("%0.1f" % data.fY)
        self.hardpointFzLabel.setText("%0.1f" % data.fZ)
        self.hardpointMxLabel.setText("%0.1f" % data.mX)
        self.hardpointMyLabel.setText("%0.1f" % data.mY)
        self.hardpointMzLabel.setText("%0.1f" % data.mZ)
        self.hardpointMagLabel.setText("%0.1f" % data.forceMagnitude)
        self.setTotalForces()

    def setTotalForces(self):
        self.totalFxLabel.setText("%0.1f" % (float(self.balanceFxLabel.text()) + float(self.hardpointFxLabel.text())))
        self.totalFyLabel.setText("%0.1f" % (float(self.balanceFyLabel.text()) + float(self.hardpointFyLabel.text())))
        self.totalFzLabel.setText("%0.1f" % (float(self.balanceFzLabel.text()) + float(self.hardpointFzLabel.text())))
        self.totalMxLabel.setText("%0.1f" % (float(self.balanceMxLabel.text()) + float(self.hardpointMxLabel.text())))
        self.totalMyLabel.setText("%0.1f" % (float(self.balanceMyLabel.text()) + float(self.hardpointMyLabel.text())))
        self.totalMzLabel.setText("%0.1f" % (float(self.balanceMzLabel.text()) + float(self.hardpointMzLabel.text())))
        self.totalMagLabel.setText("%0.1f" % (float(self.balanceMagLabel.text()) + float(self.hardpointMagLabel.text())))