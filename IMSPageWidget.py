
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import DisplacementSensorFlags
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
        self.posPlot = pg.PlotWidget()
        self.posPlot.plotItem.addLegend()
        self.posPlot.plotItem.setTitle("Position / Rotation")
        self.posPlot.plotItem.setLabel(axis = 'left', text = 'Displacement (m)')
        self.posPlot.plotItem.setLabel(axis = 'bottom', text = 'Age (s)')
        self.posPlot.plotItem.setLabel(axis = 'right', text = 'Rotation (rad)')
        self.rawPositiveXAxialCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawPositiveXTangentCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawNegativeYAxialCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawNegativeYTangentCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawNegativeXAxialCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawNegativeXTangentCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawPositiveYAxialCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawPositiveYTangentCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.rawPositiveXAxialCurve = self.rawPlot.plot(name = '+X Axial', pen = 'r') 
        self.rawPositiveXTangentCurve = self.rawPlot.plot(name = '+X Tangent', pen = 'g')
        self.rawNegativeYAxialCurve = self.rawPlot.plot(name = '-Y Axial', pen = 'b')
        self.rawNegativeYTangentCurve = self.rawPlot.plot(name = '-Y Tangent', pen = 'w')
        self.rawNegativeXAxialCurve = self.rawPlot.plot(name = '-X Axial', pen = 'y')
        self.rawNegativeXTangentCurve = self.rawPlot.plot(name = '-X Tangent', pen = 'c')
        self.rawPositiveYAxialCurve = self.rawPlot.plot(name = '+Y Axial', pen = 'm')
        self.rawPositiveYTangentCurve = self.rawPlot.plot(name = '+Y Tangent', pen = mkPen("FFA500"))
        self.xPositionCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.yPositionCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.zPositionCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.xRotationCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.yRotationCurveData = np.array([np.zeros(self.maxPlotSize)])
        self.zRotationCurveData = np.array([np.zeros(self.maxPlotSize)])
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
        #self.plotLayout.addWidget(self.rawPlot)

        self.MTM1M3.subscribeEvent_displacementSensorWarning(self.processEventDisplacementSensorWarning)
        self.MTM1M3.subscribeTelemetry_imsData(self.processTelemetryIMSData)

    def processEventDisplacementSensorWarning(self, data):
        data = data[-1]
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        QTHelpers.setWarningLabel(self.sensorReportsInvalidCommandLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsInvalidCommand))
        QTHelpers.setWarningLabel(self.sensorReportsCommunicationTimeoutErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationTimeoutError))
        QTHelpers.setWarningLabel(self.sensorReportsDataLengthErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsDataLengthError))
        QTHelpers.setWarningLabel(self.sensorReportsNumberOfParametersErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsNumberOfParametersError))
        QTHelpers.setWarningLabel(self.sensorReportsParameterErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationError))
        QTHelpers.setWarningLabel(self.sensorReportsCommunicationErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsCommunicationError))
        QTHelpers.setWarningLabel(self.sensorReportsIDNumberErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsIDNumberError))
        QTHelpers.setWarningLabel(self.sensorReportsExpansionLineErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsExpansionLineError))
        QTHelpers.setWarningLabel(self.sensorReportsWriteControlErrorLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.SensorReportsWriteControlError))
        QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.ResponseTimeout))
        QTHelpers.setWarningLabel(self.invalidLengthLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.InvalidLength))
        QTHelpers.setWarningLabel(self.invalidResponseLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.InvalidResponse))
        QTHelpers.setWarningLabel(self.unknownCommandLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.UnknownCommand))
        QTHelpers.setWarningLabel(self.unknownProblemLabel, BitHelper.get(data.displacementSensorFlags, DisplacementSensorFlags.UnknownProblem))

    def processTelemetryIMSData(self, data):
        self.rawPositiveXAxialCurveData = QTHelpers.appendAndResizeCurveData(self.rawPositiveXAxialCurveData, [x.rawSensorData[0] for x in data], self.maxPlotSize)
        self.rawPositiveXTangentCurveData = QTHelpers.appendAndResizeCurveData(self.rawPositiveXTangentCurveData, [x.rawSensorData[1] for x in data], self.maxPlotSize)
        self.rawNegativeYAxialCurveData = QTHelpers.appendAndResizeCurveData(self.rawNegativeYAxialCurveData, [x.rawSensorData[2] for x in data], self.maxPlotSize)
        self.rawNegativeYTangentCurveData = QTHelpers.appendAndResizeCurveData(self.rawNegativeYTangentCurveData, [x.rawSensorData[3] for x in data], self.maxPlotSize)
        self.rawNegativeXAxialCurveData = QTHelpers.appendAndResizeCurveData(self.rawNegativeXAxialCurveData, [x.rawSensorData[4] for x in data], self.maxPlotSize)
        self.rawNegativeXTangentCurveData = QTHelpers.appendAndResizeCurveData(self.rawNegativeXTangentCurveData, [x.rawSensorData[5] for x in data], self.maxPlotSize)
        self.rawPositiveYAxialCurveData = QTHelpers.appendAndResizeCurveData(self.rawPositiveYAxialCurveData, [x.rawSensorData[6] for x in data], self.maxPlotSize)
        self.rawPositiveYTangentCurveData = QTHelpers.appendAndResizeCurveData(self.rawPositiveYTangentCurveData, [x.rawSensorData[7] for x in data], self.maxPlotSize)
        self.rawPositiveXAxialCurve.setData(self.rawPositiveXAxialCurveData)
        self.rawPositiveXTangentCurve.setData(self.rawPositiveXTangentCurveData)
        self.rawNegativeYAxialCurve.setData(self.rawNegativeYAxialCurveData)
        self.rawNegativeYTangentCurve.setData(self.rawNegativeYTangentCurveData)
        self.rawNegativeXAxialCurve.setData(self.rawNegativeXAxialCurveData)
        self.rawNegativeXTangentCurve.setData(self.rawNegativeXTangentCurveData)
        self.rawPositiveYAxialCurve.setData(self.rawPositiveYAxialCurveData)
        self.rawPositiveYTangentCurve.setData(self.rawPositiveYTangentCurveData)
        self.xPositionCurveData = QTHelpers.appendAndResizeCurveData(self.xPositionCurveData, [x.xPosition for x in data], self.maxPlotSize)
        self.yPositionCurveData = QTHelpers.appendAndResizeCurveData(self.yPositionCurveData, [x.yPosition for x in data], self.maxPlotSize)
        self.zPositionCurveData = QTHelpers.appendAndResizeCurveData(self.zPositionCurveData, [x.zPosition for x in data], self.maxPlotSize)
        self.xRotationCurveData = QTHelpers.appendAndResizeCurveData(self.xRotationCurveData, [x.xRotation for x in data], self.maxPlotSize)
        self.yRotationCurveData = QTHelpers.appendAndResizeCurveData(self.yRotationCurveData, [x.yRotation for x in data], self.maxPlotSize)
        self.zRotationCurveData = QTHelpers.appendAndResizeCurveData(self.zRotationCurveData, [x.zRotation for x in data], self.maxPlotSize)
        self.xPositionCurve.setData(self.xPositionCurveData)
        self.yPositionCurve.setData(self.yPositionCurveData)
        self.zPositionCurve.setData(self.zPositionCurveData)
        self.xRotationCurve.setData(self.xRotationCurveData)
        self.yRotationCurve.setData(self.yRotationCurveData)
        self.zRotationCurve.setData(self.zRotationCurveData)
        
        data = data[-1]
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