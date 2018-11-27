
import QTHelpers
from DataCache import DataCache
from BitHelper import BitHelper
from MTM1M3Enumerations import InclinometerSensorFlags
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class InclinometerPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.plotLayout = QHBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)
        
        self.maxPlotSize = 50 * 30 # 50Hz * 30s
        
        self.angleLabel = QLabel("UNKNOWN")
        
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.sensorReportsIllegalFunctionLabel = QLabel("UNKNOWN")
        self.sensorReportsIllegalDataAddressLabel = QLabel("UNKNOWN")
        self.responseTimeoutLabel = QLabel("UNKNOWN")
        self.invalidCRCLabel = QLabel("UNKNOWN")
        self.invalidLengthLabel = QLabel("UNKNOWN")
        self.unknownAddressLabel = QLabel("UNKNOWN")
        self.unknownFunctionLabel = QLabel("UNKNOWN")
        self.unknownProblemLabel = QLabel("UNKNOWN")
        
        self.plot = pg.PlotWidget()
        self.plot.plotItem.addLegend()
        self.plot.plotItem.setTitle("Inclination")
        self.plot.plotItem.setLabel(axis = 'left', text = 'Inclinometer Angle (deg)')
        self.plot.plotItem.setLabel(axis = 'bottom', text = "Age (s)")
        self.inclinometerAngleCurve = self.plot.plot(name = 'Angle', pen = 'r') 

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Angle (deg)"), row, col)
        self.dataLayout.addWidget(self.angleLabel, row, col + 1)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Illegal Function"), row, col)
        self.warningLayout.addWidget(self.sensorReportsIllegalFunctionLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Illegal Address"), row, col)
        self.warningLayout.addWidget(self.sensorReportsIllegalDataAddressLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Reponse Timeout"), row, col)
        self.warningLayout.addWidget(self.responseTimeoutLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Invalid CRC"), row, col)
        self.warningLayout.addWidget(self.invalidCRCLabel, row, col + 1)
        
        row = 1
        col = 2
        self.warningLayout.addWidget(QLabel("Invalid Length"), row, col)
        self.warningLayout.addWidget(self.invalidLengthLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Unknown Address"), row, col)
        self.warningLayout.addWidget(self.unknownAddressLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Unknown Function"), row, col)
        self.warningLayout.addWidget(self.unknownFunctionLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Unknown Problem"), row, col)
        self.warningLayout.addWidget(self.unknownProblemLabel, row, col + 1)
        
        self.plotLayout.addWidget(self.plot)

        self.dataEventInclinometerSensorWarning = DataCache()
        self.inclinometerAngleCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.dataTelemetryInclinometerData = DataCache()
        
        self.MTM1M3.subscribeEvent_inclinometerSensorWarning(self.processEventInclinometerSensorWarning)
        self.MTM1M3.subscribeTelemetry_inclinometerData(self.processTelemetryInclinometerData)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventInclinometerSensorWarning.hasBeenUpdated():
            data = self.dataEventInclinometerSensorWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            QTHelpers.setWarningLabel(self.sensorReportsIllegalFunctionLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.SensorReportsIllegalFunction))
            QTHelpers.setWarningLabel(self.sensorReportsIllegalDataAddressLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.SensorReportsIllegalDataAddress))
            QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.ResponseTimeout))
            QTHelpers.setWarningLabel(self.invalidCRCLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.InvalidCRC))
            QTHelpers.setWarningLabel(self.invalidLengthLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.InvalidLength))
            QTHelpers.setWarningLabel(self.unknownAddressLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownAddress))
            QTHelpers.setWarningLabel(self.unknownFunctionLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownFunction))
            QTHelpers.setWarningLabel(self.unknownProblemLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownProblem))

        if self.inclinometerAngleCurveData.hasBeenUpdated():
            data = self.inclinometerAngleCurveData.get()
            self.inclinometerAngleCurve.setData(data)

        if self.dataTelemetryInclinometerData.hasBeenUpdated():
            data = self.dataTelemetryInclinometerData.get()
            self.angleLabel.setText("%0.3f" % (data.inclinometerAngle))

    def processEventInclinometerSensorWarning(self, data):
        self.dataEventInclinometerSensorWarning.set(data[-1])

    def processTelemetryInclinometerData(self, data):
        self.inclinometerAngleCurveData.set(QTHelpers.appendAndResizeCurveData(self.inclinometerAngleCurveData.get(), [x.inclinometerAngle for x in data], self.maxPlotSize))
        self.dataTelemetryInclinometerData.set(data[-1])