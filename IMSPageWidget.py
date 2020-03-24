
import QTHelpers
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout)
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB
from pyqtgraph import mkPen

class IMSPageWidget(QWidget):
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

        self.rawPositiveXAxialLabel = QLabel("UNKNOWN")
        self.rawPositiveXTangentLabel = QLabel("UNKNOWN")
        self.rawNegativeYAxialLabel = QLabel("UNKNOWN")
        self.rawNegativeYTangentLabel = QLabel("UNKNOWN")
        self.rawNegativeXAxialLabel = QLabel("UNKNOWN")
        self.rawNegativeXTangentLabel = QLabel("UNKNOWN")
        self.rawPositiveYAxialLabel = QLabel("UNKNOWN")
        self.rawPositiveYTangentLabel = QLabel("UNKNOWN")
        self.xPositionLabel = QLabel("UNKNOWN")
        self.yPositionLabel = QLabel("UNKNOWN")
        self.zPositionLabel = QLabel("UNKNOWN")
        self.xRotationLabel = QLabel("UNKNOWN")
        self.yRotationLabel = QLabel("UNKNOWN")
        self.zRotationLabel = QLabel("UNKNOWN")
       
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.sensorReportsInvalidCommandLabel = QLabel("UNKNOWN")
        self.sensorReportsCommunicationTimeoutErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsDataLengthErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsNumberOfParametersErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsParameterErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsCommunicationErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsIDNumberErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsExpansionLineErrorLabel = QLabel("UNKNOWN")
        self.sensorReportsWriteControlErrorLabel = QLabel("UNKNOWN")
        self.responseTimeoutLabel = QLabel("UNKNOWN")
        self.invalidLengthLabel = QLabel("UNKNOWN")
        self.invalidResponseLabel = QLabel("UNKNOWN")
        self.unknownCommandLabel = QLabel("UNKNOWN")
        self.unknownProblemLabel = QLabel("UNKNOWN")

        self.rawPlot = pg.PlotWidget()
        self.rawPlot.plotItem.addLegend()
        self.rawPlot.plotItem.setTitle("Displacement")
        self.rawPlot.plotItem.setLabel(axis = 'left', text = "Displacement (m)")
        self.rawPlot.plotItem.setLabel(axis = 'bottom', text = "Age (s)")
        self.rawPositiveXAxialCurve = self.rawPlot.plot(name = '+X Axial', pen = 'r') 
        self.rawPositiveXTangentCurve = self.rawPlot.plot(name = '+X Tangent', pen = 'g')
        self.rawNegativeYAxialCurve = self.rawPlot.plot(name = '-Y Axial', pen = 'b')
        self.rawNegativeYTangentCurve = self.rawPlot.plot(name = '-Y Tangent', pen = 'w')
        self.rawNegativeXAxialCurve = self.rawPlot.plot(name = '-X Axial', pen = 'y')
        self.rawNegativeXTangentCurve = self.rawPlot.plot(name = '-X Tangent', pen = 'c')
        self.rawPositiveYAxialCurve = self.rawPlot.plot(name = '+Y Axial', pen = 'm')
        self.rawPositiveYTangentCurve = self.rawPlot.plot(name = '+Y Tangent', pen = mkPen("FFA500"))
        self.posPlot = pg.PlotWidget()
        self.posPlot.plotItem.addLegend()
        self.posPlot.plotItem.setTitle("Position / Rotation")
        self.posPlot.plotItem.setLabel(axis = 'left', text = 'Displacement (m)')
        self.posPlot.plotItem.setLabel(axis = 'bottom', text = 'Age (s)')
        self.posPlot.plotItem.setLabel(axis = 'right', text = 'Rotation (rad)')
        self.xPositionCurve = self.posPlot.plot(name = 'X Position', pen = 'r')
        self.yPositionCurve = self.posPlot.plot(name = 'Y Position', pen = 'g')
        self.zPositionCurve = self.posPlot.plot(name = 'Z Position', pen = 'b')
        self.xRotationCurve = self.posPlot.plot(name = 'X Rotation', pen = 'w')
        self.yRotationCurve = self.posPlot.plot(name = 'Y Rotation', pen = 'y')
        self.zRotationCurve = self.posPlot.plot(name = 'Z Rotation', pen = 'c')

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("X"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Position (mm)"), row, col)
        self.dataLayout.addWidget(self.xPositionLabel, row, col + 1)
        self.dataLayout.addWidget(self.yPositionLabel, row, col + 2)
        self.dataLayout.addWidget(self.zPositionLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Rotation (rad)"), row, col)
        self.dataLayout.addWidget(self.xRotationLabel, row, col + 1)
        self.dataLayout.addWidget(self.yRotationLabel, row, col + 2)
        self.dataLayout.addWidget(self.zRotationLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("+X"), row, col + 1)
        self.dataLayout.addWidget(QLabel("-Y"), row, col + 2)
        self.dataLayout.addWidget(QLabel("-X"), row, col + 3)
        self.dataLayout.addWidget(QLabel("+Y"), row, col + 4)
        row += 1
        self.dataLayout.addWidget(QLabel("Axial (mm)"), row, col)
        self.dataLayout.addWidget(self.rawPositiveXAxialLabel, row, col + 1)
        self.dataLayout.addWidget(self.rawNegativeYAxialLabel, row, col + 2)
        self.dataLayout.addWidget(self.rawNegativeXAxialLabel, row, col + 3)
        self.dataLayout.addWidget(self.rawPositiveYAxialLabel, row, col + 4)
        row += 1
        self.dataLayout.addWidget(QLabel("Tangent (mm)"), row, col)
        self.dataLayout.addWidget(self.rawPositiveXTangentLabel, row, col + 1)
        self.dataLayout.addWidget(self.rawNegativeYTangentLabel, row, col + 2)
        self.dataLayout.addWidget(self.rawNegativeXTangentLabel, row, col + 3)
        self.dataLayout.addWidget(self.rawPositiveYTangentLabel, row, col + 4)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Invalid Command"), row, col)
        self.warningLayout.addWidget(self.sensorReportsInvalidCommandLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Communication Timeout"), row, col)
        self.warningLayout.addWidget(self.sensorReportsCommunicationTimeoutErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Data Length Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsDataLengthErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Parameter Count Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsNumberOfParametersErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Parameter Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsParameterErrorLabel, row, col + 1)
        
        row = 1
        col = 2
        self.warningLayout.addWidget(QLabel("Sensor Communication Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsCommunicationErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor ID Number Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsIDNumberErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Expansion Line Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsExpansionLineErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Write Control Error"), row, col)
        self.warningLayout.addWidget(self.sensorReportsWriteControlErrorLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Response Timeout"), row, col)
        self.warningLayout.addWidget(self.responseTimeoutLabel, row, col + 1)
        
        row = 1
        col = 4
        self.warningLayout.addWidget(QLabel("Invalid Length"), row, col)
        self.warningLayout.addWidget(self.invalidLengthLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Invalid Response"), row, col)
        self.warningLayout.addWidget(self.invalidResponseLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Unknown Command"), row, col)
        self.warningLayout.addWidget(self.unknownCommandLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Unknown Problem"), row, col)
        self.warningLayout.addWidget(self.unknownProblemLabel, row, col + 1)

        self.plotLayout.addWidget(self.posPlot)        
        self.plotLayout.addWidget(self.rawPlot)

        self.dataEventDisplacementSensorWarning = DataCache()
        self.rawPositiveXAxialCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawPositiveXTangentCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawNegativeYAxialCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawNegativeYTangentCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawNegativeXAxialCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawNegativeXTangentCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawPositiveYAxialCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.rawPositiveYTangentCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.xPositionCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.yPositionCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.zPositionCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.xRotationCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.yRotationCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.zRotationCurveData = DataCache(np.array(np.zeros(self.maxPlotSize)))
        self.dataTelemetryIMSData = DataCache()

        self.MTM1M3.subscribeEvent_displacementSensorWarning(self.processEventDisplacementSensorWarning)
        self.MTM1M3.subscribeTelemetry_imsData(self.processTelemetryIMSData)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventDisplacementSensorWarning.hasBeenUpdated():
            data = self.dataEventDisplacementSensorWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            #TODO QTHelpers.setWarningLabel(self.sensorReportsInvalidCommandLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsInvalidCommand))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsCommunicationTimeoutErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationTimeoutError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsDataLengthErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsDataLengthError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsNumberOfParametersErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsNumberOfParametersError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsParameterErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsCommunicationErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsIDNumberErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsIDNumberError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsExpansionLineErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsExpansionLineError))
            #TODO QTHelpers.setWarningLabel(self.sensorReportsWriteControlErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsWriteControlError))
            #TODO QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.ResponseTimeout))
            #TODO QTHelpers.setWarningLabel(self.invalidLengthLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.InvalidLength))
            #TODO QTHelpers.setWarningLabel(self.invalidResponseLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.InvalidResponse))
            #TODO QTHelpers.setWarningLabel(self.unknownCommandLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.UnknownCommand))
            #TODO QTHelpers.setWarningLabel(self.unknownProblemLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.UnknownProblem))

        if self.rawPositiveXAxialCurveData.hasBeenUpdated():
            data = self.rawPositiveXAxialCurveData.get()
            self.rawPositiveXAxialCurve.setData(data)

        if self.rawPositiveXTangentCurveData.hasBeenUpdated():
            data = self.rawPositiveXTangentCurveData.get()
            self.rawPositiveXTangentCurve.setData(data)

        if self.rawNegativeYAxialCurveData.hasBeenUpdated():
            data = self.rawNegativeYAxialCurveData.get()
            self.rawNegativeYAxialCurve.setData(data)

        if self.rawNegativeYTangentCurveData.hasBeenUpdated():
            data = self.rawNegativeYTangentCurveData.get()
            self.rawNegativeYTangentCurve.setData(data)

        if self.rawNegativeXAxialCurveData.hasBeenUpdated():
            data = self.rawNegativeXAxialCurveData.get()
            self.rawNegativeXAxialCurve.setData(data)

        if self.rawNegativeXTangentCurveData.hasBeenUpdated():
            data = self.rawNegativeXTangentCurveData.get()
            self.rawNegativeXTangentCurve.setData(data)

        if self.rawPositiveYAxialCurveData.hasBeenUpdated():
            data = self.rawPositiveYAxialCurveData.get()
            self.rawPositiveYAxialCurve.setData(data)

        if self.rawPositiveYTangentCurveData.hasBeenUpdated():
            data = self.rawPositiveYTangentCurveData.get()
            self.rawPositiveYTangentCurve.setData(data)

        if self.xPositionCurveData.hasBeenUpdated():
            data = self.xPositionCurveData.get()
            self.xPositionCurve.setData(data)

        if self.yPositionCurveData.hasBeenUpdated():
            data = self.yPositionCurveData.get()
            self.yPositionCurve.setData(data)

        if self.zPositionCurveData.hasBeenUpdated():
            data = self.zPositionCurveData.get()
            self.zPositionCurve.setData(data)

        if self.xRotationCurveData.hasBeenUpdated():
            data = self.xRotationCurveData.get()
            self.xRotationCurve.setData(data)

        if self.yRotationCurveData.hasBeenUpdated():
            data = self.yRotationCurveData.get()
            self.yRotationCurve.setData(data)

        if self.zRotationCurveData.hasBeenUpdated():
            data = self.zRotationCurveData.get()
            self.zRotationCurve.setData(data)

        if self.dataTelemetryIMSData.hasBeenUpdated():
            data = self.dataTelemetryIMSData.get()
            self.rawPositiveXAxialLabel.setText("%0.3f" % (data.rawSensorData[0]))
            self.rawPositiveXTangentLabel.setText("%0.3f" % (data.rawSensorData[1]))
            self.rawNegativeYAxialLabel.setText("%0.3f" % (data.rawSensorData[2]))
            self.rawNegativeYTangentLabel.setText("%0.3f" % (data.rawSensorData[3]))
            self.rawNegativeXAxialLabel.setText("%0.3f" % (data.rawSensorData[4]))
            self.rawNegativeXTangentLabel.setText("%0.3f" % (data.rawSensorData[5]))
            self.rawPositiveYAxialLabel.setText("%0.3f" % (data.rawSensorData[6]))
            self.rawPositiveYTangentLabel.setText("%0.3f" % (data.rawSensorData[7]))
            self.xPositionLabel.setText("%0.3f" % (data.xPosition * 1000.0))
            self.yPositionLabel.setText("%0.3f" % (data.yPosition * 1000.0))
            self.zPositionLabel.setText("%0.3f" % (data.zPosition * 1000.0))
            self.xRotationLabel.setText("%0.3f" % (data.xRotation))
            self.yRotationLabel.setText("%0.3f" % (data.yRotation))
            self.zRotationLabel.setText("%0.3f" % (data.zRotation))

    def processEventDisplacementSensorWarning(self, data):
        self.dataEventDisplacementSensorWarning.set(data[-1])        

    def processTelemetryIMSData(self, data):
        self.rawPositiveXAxialCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawPositiveXAxialCurveData.get(), [x.rawSensorData[0] for x in data], self.maxPlotSize))
        self.rawPositiveXTangentCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawPositiveXTangentCurveData.get(), [x.rawSensorData[1] for x in data], self.maxPlotSize))
        self.rawNegativeYAxialCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawNegativeYAxialCurveData.get(), [x.rawSensorData[2] for x in data], self.maxPlotSize))
        self.rawNegativeYTangentCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawNegativeYTangentCurveData.get(), [x.rawSensorData[3] for x in data], self.maxPlotSize))
        self.rawNegativeXAxialCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawNegativeXAxialCurveData.get(), [x.rawSensorData[4] for x in data], self.maxPlotSize))
        self.rawNegativeXTangentCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawNegativeXTangentCurveData.get(), [x.rawSensorData[5] for x in data], self.maxPlotSize))
        self.rawPositiveYAxialCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawPositiveYAxialCurveData.get(), [x.rawSensorData[6] for x in data], self.maxPlotSize))
        self.rawPositiveYTangentCurveData.set(QTHelpers.appendAndResizeCurveData(self.rawPositiveYTangentCurveData.get(), [x.rawSensorData[7] for x in data], self.maxPlotSize))
        self.xPositionCurveData.set(QTHelpers.appendAndResizeCurveData(self.xPositionCurveData.get(), [x.xPosition for x in data], self.maxPlotSize))
        self.yPositionCurveData.set(QTHelpers.appendAndResizeCurveData(self.yPositionCurveData.get(), [x.yPosition for x in data], self.maxPlotSize))
        self.zPositionCurveData.set(QTHelpers.appendAndResizeCurveData(self.zPositionCurveData.get(), [x.zPosition for x in data], self.maxPlotSize))
        self.xRotationCurveData.set(QTHelpers.appendAndResizeCurveData(self.xRotationCurveData.get(), [x.xRotation for x in data], self.maxPlotSize))
        self.yRotationCurveData.set(QTHelpers.appendAndResizeCurveData(self.yRotationCurveData.get(), [x.yRotation for x in data], self.maxPlotSize))
        self.zRotationCurveData.set(QTHelpers.appendAndResizeCurveData(self.zRotationCurveData.get(), [x.zRotation for x in data], self.maxPlotSize))
        self.dataTelemetryIMSData.set(data[-1])
