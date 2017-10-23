
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import AccelerometerFlags, AccelerometerIndexMap
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class DCAccelerometerPageWidget(QWidget):
    def __init__(self, mtm1m3):
        QWidget.__init__(self)
        self.mtm1m3 = mtm1m3
        self.layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        
        self.maxPlotSize = 50 * 30 # 50Hz * 30s

        self.plot = pg.PlotWidget()
        self.plot.plotItem.setTitle("Angular Acceleration")
        self.plot.plotItem.setLabel(axis = 'left', text = "Angular Acceleration (rad/s^2)")
        self.plot.plotItem.setLabel(axis = 'bottom', text = "Age (s)")
        self.layout.addLayout(self.gridLayout)
        self.layout.addWidget(self.plot)
        self.setLayout(self.layout)
        
        self.plot.plotItem.addLegend()
        self.angularAccelerationXCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.angularAccelerationYCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.angularAccelerationZCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.angularAccelerationXCurve = self.plot.plot(name = 'X', pen = 'r')
        self.angularAccelerationYCurve = self.plot.plot(name = 'Y', pen = 'g')
        self.angularAccelerationZCurve = self.plot.plot(name = 'Z', pen = 'b')
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.responseTimeoutLabel = QLabel("UNKNOWN")
        self.rawAccelerometer1XLabel = QLabel("UNKNOWN")
        self.rawAccelerometer1YLabel = QLabel("UNKNOWN")
        self.rawAccelerometer2XLabel = QLabel("UNKNOWN")
        self.rawAccelerometer2YLabel = QLabel("UNKNOWN")
        self.rawAccelerometer3XLabel = QLabel("UNKNOWN")
        self.rawAccelerometer3YLabel = QLabel("UNKNOWN")
        self.rawAccelerometer4XLabel = QLabel("UNKNOWN")
        self.rawAccelerometer4YLabel = QLabel("UNKNOWN")
        self.accelerometer1XLabel = QLabel("UNKNOWN")
        self.accelerometer1YLabel = QLabel("UNKNOWN")
        self.accelerometer2XLabel = QLabel("UNKNOWN")
        self.accelerometer2YLabel = QLabel("UNKNOWN")
        self.accelerometer3XLabel = QLabel("UNKNOWN")
        self.accelerometer3YLabel = QLabel("UNKNOWN")
        self.accelerometer4XLabel = QLabel("UNKNOWN")
        self.accelerometer4YLabel = QLabel("UNKNOWN")
        self.angularAccelerationXLabel = QLabel("UNKNOWN")
        self.angularAccelerationYLabel = QLabel("UNKNOWN")
        self.angularAccelerationZLabel = QLabel("UNKNOWN")

        row = 0
        col = 0
        self.gridLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.gridLayout.addWidget(self.anyWarningLabel, row, col + 1)
        self.gridLayout.addWidget(QLabel("Response Timeout"), row + 1, col)
        self.gridLayout.addWidget(self.responseTimeoutLabel, row + 1, col + 1)

        row = 0
        col = 2
        self.gridLayout.addWidget(QLabel("1X"), row, col + 1)
        self.gridLayout.addWidget(QLabel("1Y"), row, col + 2)
        self.gridLayout.addWidget(QLabel("2X"), row, col + 3)
        self.gridLayout.addWidget(QLabel("2Y"), row, col + 4)
        self.gridLayout.addWidget(QLabel("3X"), row, col + 5)
        self.gridLayout.addWidget(QLabel("3Y"), row, col + 6)
        self.gridLayout.addWidget(QLabel("4X"), row, col + 7)
        self.gridLayout.addWidget(QLabel("4Y"), row, col + 8)
        self.gridLayout.addWidget(QLabel("Raw (V)"), row + 1, col)
        self.gridLayout.addWidget(self.rawAccelerometer1XLabel, row + 1, col + 1)
        self.gridLayout.addWidget(self.rawAccelerometer1YLabel, row + 1, col + 2)
        self.gridLayout.addWidget(self.rawAccelerometer2XLabel, row + 1, col + 3)
        self.gridLayout.addWidget(self.rawAccelerometer2YLabel, row + 1, col + 4)
        self.gridLayout.addWidget(self.rawAccelerometer3XLabel, row + 1, col + 5)
        self.gridLayout.addWidget(self.rawAccelerometer3YLabel, row + 1, col + 6)
        self.gridLayout.addWidget(self.rawAccelerometer4XLabel, row + 1, col + 7)
        self.gridLayout.addWidget(self.rawAccelerometer4YLabel, row + 1, col + 8)
        self.gridLayout.addWidget(QLabel("Acceleration (m/s^2)"), row + 2, col)
        self.gridLayout.addWidget(self.accelerometer1XLabel, row + 2, col + 1)
        self.gridLayout.addWidget(self.accelerometer1YLabel, row + 2, col + 2)
        self.gridLayout.addWidget(self.accelerometer2XLabel, row + 2, col + 3)
        self.gridLayout.addWidget(self.accelerometer2YLabel, row + 2, col + 4)
        self.gridLayout.addWidget(self.accelerometer3XLabel, row + 2, col + 5)
        self.gridLayout.addWidget(self.accelerometer3YLabel, row + 2, col + 6)
        self.gridLayout.addWidget(self.accelerometer4XLabel, row + 2, col + 7)
        self.gridLayout.addWidget(self.accelerometer4YLabel, row + 2, col + 8)
        self.gridLayout.addWidget(QLabel("X"), row + 3, col + 1)
        self.gridLayout.addWidget(QLabel("Y"), row + 3, col + 2)
        self.gridLayout.addWidget(QLabel("Z"), row + 3, col + 3)
        self.gridLayout.addWidget(QLabel("Angular Acceleration (rad/s^2)"), row + 4, col)
        self.gridLayout.addWidget(self.angularAccelerationXLabel, row + 4, col + 1)
        self.gridLayout.addWidget(self.angularAccelerationYLabel, row + 4, col + 2)
        self.gridLayout.addWidget(self.angularAccelerationZLabel, row + 4, col + 3)

        self.mtm1m3.subscribeEvent_accelerometerWarning(self.processEventAccelerometerWarning)
        self.mtm1m3.subscribeTelemetry_accelerometerData(self.processTelemetryAccelerometerData)

    def processEventAccelerometerWarning(self, data):
        data = data[-1]
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.accelerometerFlags, AccelerometerFlags.ResponseTimeout))

    def processTelemetryAccelerometerData(self, data):
        self.angularAccelerationXCurveData = QTHelpers.appendAndResizeCurveData(self.angularAccelerationXCurveData, [x.angularAccelerationX for x in data], self.maxPlotSize)
        self.angularAccelerationYCurveData = QTHelpers.appendAndResizeCurveData(self.angularAccelerationYCurveData, [x.angularAccelerationY for x in data], self.maxPlotSize)
        self.angularAccelerationZCurveData = QTHelpers.appendAndResizeCurveData(self.angularAccelerationZCurveData, [x.angularAccelerationZ for x in data], self.maxPlotSize)
        self.angularAccelerationXCurve.setData(self.angularAccelerationXCurveData)
        self.angularAccelerationYCurve.setData(self.angularAccelerationYCurveData)
        self.angularAccelerationZCurve.setData(self.angularAccelerationZCurveData)

        data = data[-1]
        self.rawAccelerometer1XLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer1X]))
        self.rawAccelerometer1YLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer1Y]))
        self.rawAccelerometer2XLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer2X]))
        self.rawAccelerometer2YLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer2Y]))
        self.rawAccelerometer3XLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer3X]))
        self.rawAccelerometer3YLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer3Y]))
        self.rawAccelerometer4XLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer4X]))
        self.rawAccelerometer4YLabel.setText("%0.3f" % (data.rawAccelerometers[AccelerometerIndexMap.Accelerometer4Y]))
        self.accelerometer1XLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer1X]))
        self.accelerometer1YLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer1Y]))
        self.accelerometer2XLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer2X]))
        self.accelerometer2YLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer2Y]))
        self.accelerometer3XLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer3X]))
        self.accelerometer3YLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer3Y]))
        self.accelerometer4XLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer4X]))
        self.accelerometer4YLabel.setText("%0.3f" % (data.accelerometers[AccelerometerIndexMap.Accelerometer4Y]))
        self.angularAccelerationXLabel.setText("%0.3f" % (data.angularAccelerationX))
        self.angularAccelerationYLabel.setText("%0.3f" % (data.angularAccelerationY))
        self.angularAccelerationZLabel.setText("%0.3f" % (data.angularAccelerationZ))
