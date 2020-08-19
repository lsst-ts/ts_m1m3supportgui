import QTHelpers
import TimeChart
from DataCache import DataCache
from BitHelper import BitHelper
from PySide2.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, QSpacerItem)

class DCAccelerometerPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)
        
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

        self.anyWarningLabel = QLabel("UNKNOWN")
        self.responseTimeoutLabel = QLabel("UNKNOWN")

        self.chart = TimeChart.TimeChart(50 * 30) # 50Hz * 30s
        self.chart_view = TimeChart.TimeChartView(self.chart)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("X"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Angular Acceleration (rad/s<sup>2</sup>)"), row, col)
        self.dataLayout.addWidget(self.angularAccelerationXLabel, row, col + 1)
        self.dataLayout.addWidget(self.angularAccelerationYLabel, row, col + 2)
        self.dataLayout.addWidget(self.angularAccelerationZLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("1X"), row, col + 1)
        self.dataLayout.addWidget(QLabel("1Y"), row, col + 2)
        self.dataLayout.addWidget(QLabel("2X"), row, col + 3)
        self.dataLayout.addWidget(QLabel("2Y"), row, col + 4)
        self.dataLayout.addWidget(QLabel("3X"), row, col + 5)
        self.dataLayout.addWidget(QLabel("3Y"), row, col + 6)
        self.dataLayout.addWidget(QLabel("4X"), row, col + 7)
        self.dataLayout.addWidget(QLabel("4Y"), row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Raw (V)"), row, col)
        self.dataLayout.addWidget(self.rawAccelerometer1XLabel, row, col + 1)
        self.dataLayout.addWidget(self.rawAccelerometer1YLabel, row, col + 2)
        self.dataLayout.addWidget(self.rawAccelerometer2XLabel, row, col + 3)
        self.dataLayout.addWidget(self.rawAccelerometer2YLabel, row, col + 4)
        self.dataLayout.addWidget(self.rawAccelerometer3XLabel, row, col + 5)
        self.dataLayout.addWidget(self.rawAccelerometer3YLabel, row, col + 6)
        self.dataLayout.addWidget(self.rawAccelerometer4XLabel, row, col + 7)
        self.dataLayout.addWidget(self.rawAccelerometer4YLabel, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Acceleration (m/s<sup>2</sup>)"), row, col)
        self.dataLayout.addWidget(self.accelerometer1XLabel, row, col + 1)
        self.dataLayout.addWidget(self.accelerometer1YLabel, row, col + 2)
        self.dataLayout.addWidget(self.accelerometer2XLabel, row, col + 3)
        self.dataLayout.addWidget(self.accelerometer2YLabel, row, col + 4)
        self.dataLayout.addWidget(self.accelerometer3XLabel, row, col + 5)
        self.dataLayout.addWidget(self.accelerometer3YLabel, row, col + 6)
        self.dataLayout.addWidget(self.accelerometer4XLabel, row, col + 7)
        self.dataLayout.addWidget(self.accelerometer4YLabel, row, col + 8)
        
        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Response Timeout"), row, col)
        self.warningLayout.addWidget(self.responseTimeoutLabel, row, col + 1)

        self.plotLayout.addWidget(self.chart_view)

        self.dataEventAccelerometerWarning = DataCache()
        self.dataTelemetryAccelerometerData = DataCache()

        self.MTM1M3.subscribeEvent_accelerometerWarning(self.processEventAccelerometerWarning)
        self.MTM1M3.subscribeTelemetry_accelerometerData(self.processTelemetryAccelerometerData)

    def setPageActive(self, active):
        self.pageActive = active
        if self.pageActive:
            self.updatePage()

    def updatePage(self):
        if not self.pageActive:
            return 

        if self.dataEventAccelerometerWarning.hasBeenUpdated():
            data = self.dataEventAccelerometerWarning.get()
            QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            #TODO QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.accelerometerFlags, AccelerometerFlags.ResponseTimeout))

        if self.dataTelemetryAccelerometerData.hasBeenUpdated():
            data = self.dataTelemetryAccelerometerData.get()
            self.rawAccelerometer1XLabel.setText("%0.3f" % (data.rawAccelerometer[0]))
            self.rawAccelerometer1YLabel.setText("%0.3f" % (data.rawAccelerometer[1]))
            self.rawAccelerometer2XLabel.setText("%0.3f" % (data.rawAccelerometer[2]))
            self.rawAccelerometer2YLabel.setText("%0.3f" % (data.rawAccelerometer[3]))
            self.rawAccelerometer3XLabel.setText("%0.3f" % (data.rawAccelerometer[4]))
            self.rawAccelerometer3YLabel.setText("%0.3f" % (data.rawAccelerometer[5]))
            self.rawAccelerometer4XLabel.setText("%0.3f" % (data.rawAccelerometer[6]))
            self.rawAccelerometer4YLabel.setText("%0.3f" % (data.rawAccelerometer[7]))
            self.accelerometer1XLabel.setText("%0.3f" % (data.accelerometer[0]))
            self.accelerometer1YLabel.setText("%0.3f" % (data.accelerometer[1]))
            self.accelerometer2XLabel.setText("%0.3f" % (data.accelerometer[2]))
            self.accelerometer2YLabel.setText("%0.3f" % (data.accelerometer[3]))
            self.accelerometer3XLabel.setText("%0.3f" % (data.accelerometer[4]))
            self.accelerometer3YLabel.setText("%0.3f" % (data.accelerometer[5]))
            self.accelerometer4XLabel.setText("%0.3f" % (data.accelerometer[6]))
            self.accelerometer4YLabel.setText("%0.3f" % (data.accelerometer[7]))
            self.angularAccelerationXLabel.setText("%0.3f" % (data.angularAccelerationX))
            self.angularAccelerationYLabel.setText("%0.3f" % (data.angularAccelerationY))
            self.angularAccelerationZLabel.setText("%0.3f" % (data.angularAccelerationZ))
    
    def processEventAccelerometerWarning(self, data):
        self.dataEventAccelerometerWarning.set(data[-1])
        
    def processTelemetryAccelerometerData(self, data):
        self.chart.append('Angular Acceleration (rad/s<sup>2</sup>)','X', [(x.timestamp, x.angularAccelerationX) for x in data])
        self.chart.append('Angular Acceleration (rad/s<sup>2</sup>)','Y', [(x.timestamp, x.angularAccelerationY) for x in data])
        self.chart.append('Angular Acceleration (rad/s<sup>2</sup>)','Z', [(x.timestamp, x.angularAccelerationZ) for x in data])
        self.dataTelemetryAccelerometerData.set(data[-1])
