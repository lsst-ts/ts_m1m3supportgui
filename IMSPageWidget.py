
import QTHelpers
import TimeChart
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout)

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

        self.rawChart = TimeChart.TimeChart()
        self.rawChartView = TimeChart.TimeChartView(self.rawChart)

        self.posChart = TimeChart.TimeChart()
        self.posChartView = TimeChart.TimeChartView(self.posChart)
        
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

        self.plotLayout.addWidget(self.posChartView)
        self.plotLayout.addWidget(self.rawChartView)

        self.dataEventDisplacementSensorWarning = DataCache()
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
        self.rawChart.append('Displacement (mm)', '+X Axial', [(x.timestamp, x.rawSensorData[0] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '+X Tangent', [(x.timestamp, x.rawSensorData[1] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-Y Axial', [(x.timestamp, x.rawSensorData[2] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-Y Tangent', [(x.timestamp, x.rawSensorData[3] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-X Axial', [(x.timestamp, x.rawSensorData[4] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-X Tangent', [(x.timestamp, x.rawSensorData[5] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-Y Axial', [(x.timestamp, x.rawSensorData[6] / 1000) for x in data])
        self.rawChart.append('Displacement (mm)', '-Y Tangent', [(x.timestamp, x.rawSensorData[7] / 1000) for x in data])
 
        self.posChart.append('Position (m)', 'X', [(x.timestamp, x.xPosition) for x in data])

        self.posChart.append('Position (m)', 'Y', [(x.timestamp, x.yPosition) for x in data])
        self.posChart.append('Position (m)', 'Z', [(x.timestamp, x.zPosition) for x in data])
        self.posChart.append('Rotation (rad)', 'X', [(x.timestamp, x.xRotation) for x in data])
        self.posChart.append('Rotation (rad)', 'Y', [(x.timestamp, x.yRotation) for x in data])
        self.posChart.append('Rotation (rad)', 'Z', [(x.timestamp, x.zRotation) for x in data])
        self.dataTelemetryIMSData.set(data[-1])
