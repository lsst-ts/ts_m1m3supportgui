import QTHelpers
import TimeChart
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot


class GyroPageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.maxPlotSize = 50 * 30  # 50Hz * 30s

        self.velocityXLabel = QLabel("UNKNOWN")
        self.velocityYLabel = QLabel("UNKNOWN")
        self.velocityZLabel = QLabel("UNKNOWN")
        self.sequenceNumberLabel = QLabel("UNKNOWN")
        self.temperatureLabel = QLabel("UNKNOWN")

        self.anyWarningLabel = QLabel("UNKNOWN")
        self.gyroXStatusWarningLabel = QLabel("UNKNOWN")
        self.gyroYStatusWarningLabel = QLabel("UNKNOWN")
        self.gyroZStatusWarningLabel = QLabel("UNKNOWN")
        self.sequenceNumberWarningLabel = QLabel("UNKNOWN")
        self.crcMismatchWarningLabel = QLabel("UNKNOWN")
        self.invalidLengthWarningLabel = QLabel("UNKNOWN")
        self.invalidHeaderWarningLabel = QLabel("UNKNOWN")
        self.incompleteFrameWarningLabel = QLabel("UNKNOWN")
        self.gyroXSLDWarningLabel = QLabel("UNKNOWN")
        self.gyroXMODDACWarningLabel = QLabel("UNKNOWN")
        self.gyroXPhaseWarningLabel = QLabel("UNKNOWN")
        self.gyroXFlashWarningLabel = QLabel("UNKNOWN")
        self.gyroYSLDWarningLabel = QLabel("UNKNOWN")
        self.gyroYMODDACWarningLabel = QLabel("UNKNOWN")
        self.gyroYPhaseWarningLabel = QLabel("UNKNOWN")
        self.gyroYFlashWarningLabel = QLabel("UNKNOWN")
        self.gyroZSLDWarningLabel = QLabel("UNKNOWN")
        self.gyroZMODDACWarningLabel = QLabel("UNKNOWN")
        self.gyroZPhaseWarningLabel = QLabel("UNKNOWN")
        self.gyroZFlashWarningLabel = QLabel("UNKNOWN")
        self.gyroXSLDTemperatureStatusWarningLabel = QLabel("UNKNOWN")
        self.gyroYSLDTemperatureStatusWarningLabel = QLabel("UNKNOWN")
        self.gyroZSLDTemperatureStatusWarningLabel = QLabel("UNKNOWN")
        self.gcbTemperatureStatusWarningLabel = QLabel("UNKNOWN")
        self.temperatureStatusWarningLabel = QLabel("UNKNOWN")
        self.gcbDSPSPIFlashStatusWarningLabel = QLabel("UNKNOWN")
        self.gcbFPGASPIFlashStatusWarningLabel = QLabel("UNKNOWN")
        self.dspSPIFlashWarningLabel = QLabel("UNKNOWN")
        self.fpgaSPIFlashStatusWarningLabel = QLabel("UNKNOWN")
        self.gcb1_2VStatusWarningLabel = QLabel("UNKNOWN")
        self.gcb3_3VStatusWarningLabel = QLabel("UNKNOWN")
        self.gcb5VStatusWarningLabel = QLabel("UNKNOWN")
        self.v1_2StatusWarningLabel = QLabel("UNKNOWN")
        self.v3_3StatusWarningLabel = QLabel("UNKNOWN")
        self.v5StatusWarningLabel = QLabel("UNKNOWN")
        self.gcbFPGAStatusWarningLabel = QLabel("UNKNOWN")
        self.fpgaStatusWarningLabel = QLabel("UNKNOWN")
        self.hiSpeedSPORTStatusWarningLabel = QLabel("UNKNOWN")
        self.auxSPORTStatusWarningLabel = QLabel("UNKNOWN")
        self.sufficientSoftwareResourcesWarningLabel = QLabel("UNKNOWN")
        self.gyroEOVoltsPositiveWarningLabel = QLabel("UNKNOWN")
        self.gyroEOVoltsNegativeWarningLabel = QLabel("UNKNOWN")
        self.gyroXVoltsWarningLabel = QLabel("UNKNOWN")
        self.gyroYVoltsWarningLabel = QLabel("UNKNOWN")
        self.gyroZVoltsWarningLabel = QLabel("UNKNOWN")
        self.gcbADCCommsWarningLabel = QLabel("UNKNOWN")
        self.mSYNCExternalTimingWarningLabel = QLabel("UNKNOWN")

        self.chart = TimeChart.TimeChart()
        self.chart_view = TimeChart.TimeChartView(self.chart)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("X"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Y"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Z"), row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel("Angular Velocity (rad/s)"), row, col)
        self.dataLayout.addWidget(self.velocityXLabel, row, col + 1)
        self.dataLayout.addWidget(self.velocityYLabel, row, col + 2)
        self.dataLayout.addWidget(self.velocityZLabel, row, col + 3)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("Sequence Number"), row, col)
        self.dataLayout.addWidget(self.sequenceNumberLabel, row, col + 1)
        row += 1
        self.dataLayout.addWidget(QLabel("Temperature (C)"), row, col)
        self.dataLayout.addWidget(self.temperatureLabel, row, col + 1)

        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X Status"), row, col)
        self.warningLayout.addWidget(self.gyroXStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X SLD"), row, col)
        self.warningLayout.addWidget(self.gyroXSLDWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X MOD DAC"), row, col)
        self.warningLayout.addWidget(self.gyroXMODDACWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X Phase"), row, col)
        self.warningLayout.addWidget(self.gyroXPhaseWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X Flash"), row, col)
        self.warningLayout.addWidget(self.gyroXFlashWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("X SLD Temperature"), row, col)
        self.warningLayout.addWidget(
            self.gyroXSLDTemperatureStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("X Volts"), row, col)
        self.warningLayout.addWidget(self.gyroXVoltsWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Hi-Speed SPORT"), row, col)
        self.warningLayout.addWidget(self.hiSpeedSPORTStatusWarningLabel, row, col + 1)

        row = 1
        col = 2
        self.warningLayout.addWidget(QLabel("Y Status"), row, col)
        self.warningLayout.addWidget(self.gyroYStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Y SLD"), row, col)
        self.warningLayout.addWidget(self.gyroYSLDWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Y MOD DAC"), row, col)
        self.warningLayout.addWidget(self.gyroYMODDACWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Y Phase"), row, col)
        self.warningLayout.addWidget(self.gyroYPhaseWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Y Flash"), row, col)
        self.warningLayout.addWidget(self.gyroYFlashWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Y SLD Temperature"), row, col)
        self.warningLayout.addWidget(
            self.gyroYSLDTemperatureStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("Y Volts"), row, col)
        self.warningLayout.addWidget(self.gyroYVoltsWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Aux SPORT"), row, col)
        self.warningLayout.addWidget(self.auxSPORTStatusWarningLabel, row, col + 1)

        row = 1
        col = 4
        self.warningLayout.addWidget(QLabel("Z Status"), row, col)
        self.warningLayout.addWidget(self.gyroZStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Z SLD"), row, col)
        self.warningLayout.addWidget(self.gyroZSLDWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Z MOD DAC"), row, col)
        self.warningLayout.addWidget(self.gyroZMODDACWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Z Phase"), row, col)
        self.warningLayout.addWidget(self.gyroZPhaseWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Z Flash"), row, col)
        self.warningLayout.addWidget(self.gyroZFlashWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Z SLD Temperature"), row, col)
        self.warningLayout.addWidget(
            self.gyroZSLDTemperatureStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("Z Volts"), row, col)
        self.warningLayout.addWidget(self.gyroZVoltsWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Sufficient Resources"), row, col)
        self.warningLayout.addWidget(
            self.sufficientSoftwareResourcesWarningLabel, row, col + 1
        )

        row = 1
        col = 6
        self.warningLayout.addWidget(QLabel("GCB 1.2v"), row, col)
        self.warningLayout.addWidget(self.gcb1_2VStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GCB 3.3v"), row, col)
        self.warningLayout.addWidget(self.gcb3_3VStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GCB 5v"), row, col)
        self.warningLayout.addWidget(self.gcb5VStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("1.2v"), row, col)
        self.warningLayout.addWidget(self.v1_2StatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("3.3v"), row, col)
        self.warningLayout.addWidget(self.v3_3StatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("5v"), row, col)
        self.warningLayout.addWidget(self.v5StatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("EO Volts Positive"), row, col)
        self.warningLayout.addWidget(self.gyroEOVoltsPositiveWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("EO Volts Negative"), row, col)
        self.warningLayout.addWidget(self.gyroEOVoltsNegativeWarningLabel, row, col + 1)

        row = 1
        col = 8
        self.warningLayout.addWidget(QLabel("Sequence Number"), row, col)
        self.warningLayout.addWidget(self.sequenceNumberWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("CRC Mismatch"), row, col)
        self.warningLayout.addWidget(self.crcMismatchWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Invalid Length"), row, col)
        self.warningLayout.addWidget(self.invalidLengthWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Invalid Header"), row, col)
        self.warningLayout.addWidget(self.invalidHeaderWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Incomplete Frame"), row, col)
        self.warningLayout.addWidget(self.incompleteFrameWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("M SYNC External Timing"), row, col)
        self.warningLayout.addWidget(self.mSYNCExternalTimingWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GCB FPGA"), row, col)
        self.warningLayout.addWidget(self.gcbFPGAStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("FPGA"), row, col)
        self.warningLayout.addWidget(self.fpgaStatusWarningLabel, row, col + 1)

        row = 1
        col = 10
        self.warningLayout.addWidget(QLabel("GCB DSP SPI Flash"), row, col)
        self.warningLayout.addWidget(
            self.gcbDSPSPIFlashStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("GCB FPGA SPI Flash"), row, col)
        self.warningLayout.addWidget(
            self.gcbFPGASPIFlashStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("DSP SPI Flash"), row, col)
        self.warningLayout.addWidget(self.dspSPIFlashWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("FPGA SPI Flash"), row, col)
        self.warningLayout.addWidget(self.fpgaSPIFlashStatusWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GCB ADC Comms"), row, col)
        self.warningLayout.addWidget(self.gcbADCCommsWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GCB Temperature"), row, col)
        self.warningLayout.addWidget(
            self.gcbTemperatureStatusWarningLabel, row, col + 1
        )
        row += 1
        self.warningLayout.addWidget(QLabel("Temperature"), row, col)
        self.warningLayout.addWidget(self.temperatureStatusWarningLabel, row, col + 1)

        self.plotLayout.addWidget(self.chart_view)

        self.comm.gyroWarning.connect(self.gyroWarning)
        self.comm.gyroData.connect(self.gyroData)

    @Slot(bool)
    def gyroWarning(self, anyWarning):
        QTHelpers.setWarningLabel(self.anyWarningLabel, anyWarning)
        # TODO QTHelpers.setWarningLabel(self.gyroXStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.sequenceNumberWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.SequenceNumberWarning))
        # TODO QTHelpers.setWarningLabel(self.crcMismatchWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.CRCMismatchWarning))
        # TODO QTHelpers.setWarningLabel(self.invalidLengthWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.InvalidLengthWarning))
        # TODO QTHelpers.setWarningLabel(self.invalidHeaderWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.InvalidHeaderWarning))
        # TODO QTHelpers.setWarningLabel(self.incompleteFrameWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.IncompleteFrameWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXSLDWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXSLDWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXMODDACWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXMODDACWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXPhaseWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXPhaseWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXFlashWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXFlashWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYSLDWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYSLDWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYMODDACWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYMODDACWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYPhaseWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYPhaseWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYFlashWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYFlashWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZSLDWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZSLDWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZMODDACWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZMODDACWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZPhaseWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZPhaseWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZFlashWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZFlashWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXSLDTemperatureStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXSLDTemperatureStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYSLDTemperatureStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYSLDTemperatureStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZSLDTemperatureStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZSLDTemperatureStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcbTemperatureStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCBTemperatureStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.temperatureStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.TemperatureStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcbDSPSPIFlashStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCBDSPSPIFlashStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcbFPGASPIFlashStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCBFPGASPIFlashStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.dspSPIFlashWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.DSPSPIFlashStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.fpgaSPIFlashStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.FPGASPIFlashStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcb1_2VStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCB1_2VStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcb3_3VStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCB3_3VStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcb5VStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCB5VStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.v1_2StatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.V1_2StatusWarning))
        # TODO QTHelpers.setWarningLabel(self.v3_3StatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.V3_3StatusWarning))
        # TODO QTHelpers.setWarningLabel(self.v5StatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.V5StatusWarning))
        # TODO QTHelpers.setWarningLabel(self.gcbFPGAStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCBFPGAStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.fpgaStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.FPGAStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.hiSpeedSPORTStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.HiSpeedSPORTStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.auxSPORTStatusWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.AuxSPORTStatusWarning))
        # TODO QTHelpers.setWarningLabel(self.sufficientSoftwareResourcesWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.SufficientSoftwareResourcesWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroEOVoltsPositiveWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroEOVoltsPositiveWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroEOVoltsNegativeWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroEOVoltsNegativeWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroXVoltsWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroXVoltsWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroYVoltsWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroYVoltsWarning))
        # TODO QTHelpers.setWarningLabel(self.gyroZVoltsWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GyroZVoltsWarning))
        # TODO QTHelpers.setWarningLabel(self.gcbADCCommsWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.GCBADCCommsWarning))
        # TODO QTHelpers.setWarningLabel(self.mSYNCExternalTimingWarningLabel, BitHelper.get(data.gyroSensorFlags, GyroSensorFlags.MSYNCExternalTimingWarning))

    @Slot(map)
    def gyroData(self, data):
        self.velocityXLabel.setText("%0.3f" % (data.angularVelocityX))
        self.velocityYLabel.setText("%0.3f" % (data.angularVelocityY))
        self.velocityZLabel.setText("%0.3f" % (data.angularVelocityZ))
        self.sequenceNumberLabel.setText("%0.3f" % (data.sequenceNumber))
        self.temperatureLabel.setText("%0.3f" % (data.temperature))

        self.chart.append(
            data.timestamp,
            [
                ("Angular Velocity (rad/s)", "X", data.angularVelocityX,),
                ("Angular Velocity (rad/s)", "Y", data.angularVelocityY),
                ("Angular Velocity (rad/s)", "Z", data.angularVelocityZ),
            ],
        )
