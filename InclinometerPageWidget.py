import QTHelpers
import TimeChart
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide2.QtCore import Slot


class InclinometerPageWidget(QWidget):
    def __init__(self, m1m3):
        super().__init__()
        self.m1m3 = m1m3

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)

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

        self.chart = TimeChart.TimeChart()
        self.chart_view = TimeChart.TimeChartView(self.chart)

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
        self.warningLayout.addWidget(
            self.sensorReportsIllegalFunctionLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("Sensor Illegal Address"), row, col)
        self.warningLayout.addWidget(
            self.sensorReportsIllegalDataAddressLabel, row, col + 1
        )
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

        self.layout.addWidget(self.chart_view)

        self.setLayout(self.layout)

        self.m1m3.inclinometerSensorWarning.connect(self.inclinometerSensorWarning)
        self.m1m3.inclinometerData.connect(self.inclinometerData)

    @Slot(bool)
    def inclinometerSensorWarning(self, anyWarning):
        QTHelpers.setWarningLabel(self.anyWarningLabel, anyWarning)
        # TODO QTHelpers.setWarningLabel(self.sensorReportsIllegalFunctionLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.SensorReportsIllegalFunction))
        # TODO QTHelpers.setWarningLabel(self.sensorReportsIllegalDataAddressLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.SensorReportsIllegalDataAddress))
        # TODO QTHelpers.setWarningLabel(self.responseTimeoutLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.ResponseTimeout))
        # TODO QTHelpers.setWarningLabel(self.invalidCRCLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.InvalidCRC))
        # TODO QTHelpers.setWarningLabel(self.invalidLengthLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.InvalidLength))
        # TODO QTHelpers.setWarningLabel(self.unknownAddressLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownAddress))
        # TODO QTHelpers.setWarningLabel(self.unknownFunctionLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownFunction))
        # TODO QTHelpers.setWarningLabel(self.unknownProblemLabel, BitHelper.get(data.inclinometerSensorFlags, InclinometerSensorFlags.UnknownProblem))

    @Slot(map)
    def inclinometerData(self, data):
        self.angleLabel.setText("%0.3f" % (data.inclinometerAngle))

        self.chart.append(
            data.timestamp,
            [("Angle (deg)", "Inclinometer Angle", data.inclinometerAngle)],
        )
