import QTHelpers
import TimeChart
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot


class PIDPageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.pageActive = False

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.commandLayout = QVBoxLayout()
        self.plotLayout = QVBoxLayout()
        self.layout.addLayout(self.commandLayout)
        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.plotLayout)
        self.setLayout(self.layout)

        self.fxSetpointLabel = QLabel("UNKNOWN")
        self.fxMeasurementLabel = QLabel("UNKNOWN")
        self.fxErrorLabel = QLabel("UNKNOWN")
        self.fxErrorT1Label = QLabel("UNKNOWN")
        self.fxErrorT2Label = QLabel("UNKNOWN")
        self.fxControlLabel = QLabel("UNKNOWN")
        self.fxControlT1Label = QLabel("UNKNOWN")
        self.fxControlT2Label = QLabel("UNKNOWN")
        self.fySetpointLabel = QLabel("UNKNOWN")
        self.fyMeasurementLabel = QLabel("UNKNOWN")
        self.fyErrorLabel = QLabel("UNKNOWN")
        self.fyErrorT1Label = QLabel("UNKNOWN")
        self.fyErrorT2Label = QLabel("UNKNOWN")
        self.fyControlLabel = QLabel("UNKNOWN")
        self.fyControlT1Label = QLabel("UNKNOWN")
        self.fyControlT2Label = QLabel("UNKNOWN")
        self.fzSetpointLabel = QLabel("UNKNOWN")
        self.fzMeasurementLabel = QLabel("UNKNOWN")
        self.fzErrorLabel = QLabel("UNKNOWN")
        self.fzErrorT1Label = QLabel("UNKNOWN")
        self.fzErrorT2Label = QLabel("UNKNOWN")
        self.fzControlLabel = QLabel("UNKNOWN")
        self.fzControlT1Label = QLabel("UNKNOWN")
        self.fzControlT2Label = QLabel("UNKNOWN")
        self.mxSetpointLabel = QLabel("UNKNOWN")
        self.mxMeasurementLabel = QLabel("UNKNOWN")
        self.mxErrorLabel = QLabel("UNKNOWN")
        self.mxErrorT1Label = QLabel("UNKNOWN")
        self.mxErrorT2Label = QLabel("UNKNOWN")
        self.mxControlLabel = QLabel("UNKNOWN")
        self.mxControlT1Label = QLabel("UNKNOWN")
        self.mxControlT2Label = QLabel("UNKNOWN")
        self.mySetpointLabel = QLabel("UNKNOWN")
        self.myMeasurementLabel = QLabel("UNKNOWN")
        self.myErrorLabel = QLabel("UNKNOWN")
        self.myErrorT1Label = QLabel("UNKNOWN")
        self.myErrorT2Label = QLabel("UNKNOWN")
        self.myControlLabel = QLabel("UNKNOWN")
        self.myControlT1Label = QLabel("UNKNOWN")
        self.myControlT2Label = QLabel("UNKNOWN")
        self.mzSetpointLabel = QLabel("UNKNOWN")
        self.mzMeasurementLabel = QLabel("UNKNOWN")
        self.mzErrorLabel = QLabel("UNKNOWN")
        self.mzErrorT1Label = QLabel("UNKNOWN")
        self.mzErrorT2Label = QLabel("UNKNOWN")
        self.mzControlLabel = QLabel("UNKNOWN")
        self.mzControlT1Label = QLabel("UNKNOWN")
        self.mzControlT2Label = QLabel("UNKNOWN")
        self.fxTimestepLabel = QLabel("UNKNOWN")
        self.fxPLabel = QLabel("UNKNOWN")
        self.fxILabel = QLabel("UNKNOWN")
        self.fxDLabel = QLabel("UNKNOWN")
        self.fxNLabel = QLabel("UNKNOWN")
        self.fxCalculatedALabel = QLabel("UNKNOWN")
        self.fxCalculatedBLabel = QLabel("UNKNOWN")
        self.fxCalculatedCLabel = QLabel("UNKNOWN")
        self.fxCalculatedDLabel = QLabel("UNKNOWN")
        self.fxCalculatedELabel = QLabel("UNKNOWN")
        self.fyTimestepLabel = QLabel("UNKNOWN")
        self.fyPLabel = QLabel("UNKNOWN")
        self.fyILabel = QLabel("UNKNOWN")
        self.fyDLabel = QLabel("UNKNOWN")
        self.fyNLabel = QLabel("UNKNOWN")
        self.fyCalculatedALabel = QLabel("UNKNOWN")
        self.fyCalculatedBLabel = QLabel("UNKNOWN")
        self.fyCalculatedCLabel = QLabel("UNKNOWN")
        self.fyCalculatedDLabel = QLabel("UNKNOWN")
        self.fyCalculatedELabel = QLabel("UNKNOWN")
        self.fzTimestepLabel = QLabel("UNKNOWN")
        self.fzPLabel = QLabel("UNKNOWN")
        self.fzILabel = QLabel("UNKNOWN")
        self.fzDLabel = QLabel("UNKNOWN")
        self.fzNLabel = QLabel("UNKNOWN")
        self.fzCalculatedALabel = QLabel("UNKNOWN")
        self.fzCalculatedBLabel = QLabel("UNKNOWN")
        self.fzCalculatedCLabel = QLabel("UNKNOWN")
        self.fzCalculatedDLabel = QLabel("UNKNOWN")
        self.fzCalculatedELabel = QLabel("UNKNOWN")
        self.mxTimestepLabel = QLabel("UNKNOWN")
        self.mxPLabel = QLabel("UNKNOWN")
        self.mxILabel = QLabel("UNKNOWN")
        self.mxDLabel = QLabel("UNKNOWN")
        self.mxNLabel = QLabel("UNKNOWN")
        self.mxCalculatedALabel = QLabel("UNKNOWN")
        self.mxCalculatedBLabel = QLabel("UNKNOWN")
        self.mxCalculatedCLabel = QLabel("UNKNOWN")
        self.mxCalculatedDLabel = QLabel("UNKNOWN")
        self.mxCalculatedELabel = QLabel("UNKNOWN")
        self.myTimestepLabel = QLabel("UNKNOWN")
        self.myPLabel = QLabel("UNKNOWN")
        self.myILabel = QLabel("UNKNOWN")
        self.myDLabel = QLabel("UNKNOWN")
        self.myNLabel = QLabel("UNKNOWN")
        self.myCalculatedALabel = QLabel("UNKNOWN")
        self.myCalculatedBLabel = QLabel("UNKNOWN")
        self.myCalculatedCLabel = QLabel("UNKNOWN")
        self.myCalculatedDLabel = QLabel("UNKNOWN")
        self.myCalculatedELabel = QLabel("UNKNOWN")
        self.mzTimestepLabel = QLabel("UNKNOWN")
        self.mzPLabel = QLabel("UNKNOWN")
        self.mzILabel = QLabel("UNKNOWN")
        self.mzDLabel = QLabel("UNKNOWN")
        self.mzNLabel = QLabel("UNKNOWN")
        self.mzCalculatedALabel = QLabel("UNKNOWN")
        self.mzCalculatedBLabel = QLabel("UNKNOWN")
        self.mzCalculatedCLabel = QLabel("UNKNOWN")
        self.mzCalculatedDLabel = QLabel("UNKNOWN")
        self.mzCalculatedELabel = QLabel("UNKNOWN")

        self.chart = TimeChart.TimeChart()
        self.chartView = TimeChart.TimeChartView(self.chart)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Setpoint"), row, col + 1)
        self.dataLayout.addWidget(QLabel("Measurement"), row, col + 2)
        self.dataLayout.addWidget(QLabel("Error"), row, col + 3)
        self.dataLayout.addWidget(QLabel("ErrorT1"), row, col + 4)
        self.dataLayout.addWidget(QLabel("ErrorT2"), row, col + 5)
        self.dataLayout.addWidget(QLabel("Control"), row, col + 6)
        self.dataLayout.addWidget(QLabel("ControlT1"), row, col + 7)
        self.dataLayout.addWidget(QLabel("ControlT2"), row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Fx"), row, col)
        self.dataLayout.addWidget(self.fxSetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.fxMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.fxErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.fxErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.fxErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.fxControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.fxControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.fxControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Fy"), row, col)
        self.dataLayout.addWidget(self.fySetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.fyMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.fyErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.fyErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.fyErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.fyControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.fyControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.fyControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Fz"), row, col)
        self.dataLayout.addWidget(self.fzSetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.fzMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.fzErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.fzErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.fzErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.fzControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.fzControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.fzControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Mx"), row, col)
        self.dataLayout.addWidget(self.mxSetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.mxMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.mxErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.mxErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.mxErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.mxControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.mxControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.mxControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("My"), row, col)
        self.dataLayout.addWidget(self.mySetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.myMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.myErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.myErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.myErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.myControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.myControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.myControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel("Mz"), row, col)
        self.dataLayout.addWidget(self.mzSetpointLabel, row, col + 1)
        self.dataLayout.addWidget(self.mzMeasurementLabel, row, col + 2)
        self.dataLayout.addWidget(self.mzErrorLabel, row, col + 3)
        self.dataLayout.addWidget(self.mzErrorT1Label, row, col + 4)
        self.dataLayout.addWidget(self.mzErrorT2Label, row, col + 5)
        self.dataLayout.addWidget(self.mzControlLabel, row, col + 6)
        self.dataLayout.addWidget(self.mzControlT1Label, row, col + 7)
        self.dataLayout.addWidget(self.mzControlT2Label, row, col + 8)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("Timestep"), row, col + 1)
        self.dataLayout.addWidget(QLabel("P"), row, col + 2)
        self.dataLayout.addWidget(QLabel("I"), row, col + 3)
        self.dataLayout.addWidget(QLabel("D"), row, col + 4)
        self.dataLayout.addWidget(QLabel("N"), row, col + 5)
        self.dataLayout.addWidget(QLabel("CalculatedA"), row, col + 6)
        self.dataLayout.addWidget(QLabel("CalculatedB"), row, col + 7)
        self.dataLayout.addWidget(QLabel("CalculatedC"), row, col + 8)
        self.dataLayout.addWidget(QLabel("CalculatedD"), row, col + 9)
        self.dataLayout.addWidget(QLabel("CalculatedE"), row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("Fx"), row, col)
        self.dataLayout.addWidget(self.fxTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.fxPLabel, row, col + 2)
        self.dataLayout.addWidget(self.fxILabel, row, col + 3)
        self.dataLayout.addWidget(self.fxDLabel, row, col + 4)
        self.dataLayout.addWidget(self.fxNLabel, row, col + 5)
        self.dataLayout.addWidget(self.fxCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.fxCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.fxCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.fxCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.fxCalculatedELabel, row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("Fy"), row, col)
        self.dataLayout.addWidget(self.fyTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.fyPLabel, row, col + 2)
        self.dataLayout.addWidget(self.fyILabel, row, col + 3)
        self.dataLayout.addWidget(self.fyDLabel, row, col + 4)
        self.dataLayout.addWidget(self.fyNLabel, row, col + 5)
        self.dataLayout.addWidget(self.fyCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.fyCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.fyCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.fyCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.fyCalculatedELabel, row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("Fz"), row, col)
        self.dataLayout.addWidget(self.fzTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.fzPLabel, row, col + 2)
        self.dataLayout.addWidget(self.fzILabel, row, col + 3)
        self.dataLayout.addWidget(self.fzDLabel, row, col + 4)
        self.dataLayout.addWidget(self.fzNLabel, row, col + 5)
        self.dataLayout.addWidget(self.fzCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.fzCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.fzCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.fzCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.fzCalculatedELabel, row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("Mx"), row, col)
        self.dataLayout.addWidget(self.mxTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.mxPLabel, row, col + 2)
        self.dataLayout.addWidget(self.mxILabel, row, col + 3)
        self.dataLayout.addWidget(self.mxDLabel, row, col + 4)
        self.dataLayout.addWidget(self.mxNLabel, row, col + 5)
        self.dataLayout.addWidget(self.mxCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.mxCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.mxCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.mxCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.mxCalculatedELabel, row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("My"), row, col)
        self.dataLayout.addWidget(self.myTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.myPLabel, row, col + 2)
        self.dataLayout.addWidget(self.myILabel, row, col + 3)
        self.dataLayout.addWidget(self.myDLabel, row, col + 4)
        self.dataLayout.addWidget(self.myNLabel, row, col + 5)
        self.dataLayout.addWidget(self.myCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.myCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.myCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.myCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.myCalculatedELabel, row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("Mz"), row, col)
        self.dataLayout.addWidget(self.mzTimestepLabel, row, col + 1)
        self.dataLayout.addWidget(self.mzPLabel, row, col + 2)
        self.dataLayout.addWidget(self.mzILabel, row, col + 3)
        self.dataLayout.addWidget(self.mzDLabel, row, col + 4)
        self.dataLayout.addWidget(self.mzNLabel, row, col + 5)
        self.dataLayout.addWidget(self.mzCalculatedALabel, row, col + 6)
        self.dataLayout.addWidget(self.mzCalculatedBLabel, row, col + 7)
        self.dataLayout.addWidget(self.mzCalculatedCLabel, row, col + 8)
        self.dataLayout.addWidget(self.mzCalculatedDLabel, row, col + 9)
        self.dataLayout.addWidget(self.mzCalculatedELabel, row, col + 10)

        self.plotLayout.addWidget(self.chartView)

    def setPageActive(self, active):
        if self.pageActive == active:
            return

        if active:
            self.comm.pidInfo.connect(self.pidInfo)
            self.comm.pidData.connect(self.pidData)
        else:
            self.comm.pidInfo.disconnect(self.pidInfo)
            self.comm.pidData.disconnect(self.pidData)

        self.pageActive = active

    @Slot(map)
    def pidInfo(self, data):
        self.fxTimestepLabel.setText("%0.3f" % data.timestep[0])
        self.fxPLabel.setText("%0.3f" % data.p[0])
        self.fxILabel.setText("%0.3f" % data.i[0])
        self.fxDLabel.setText("%0.3f" % data.d[0])
        self.fxNLabel.setText("%0.3f" % data.n[0])
        self.fxCalculatedALabel.setText("%0.3f" % data.calculatedA[0])
        self.fxCalculatedBLabel.setText("%0.3f" % data.calculatedB[0])
        self.fxCalculatedCLabel.setText("%0.3f" % data.calculatedC[0])
        self.fxCalculatedDLabel.setText("%0.3f" % data.calculatedD[0])
        self.fxCalculatedELabel.setText("%0.3f" % data.calculatedE[0])

        self.fyTimestepLabel.setText("%0.3f" % data.timestep[1])
        self.fyPLabel.setText("%0.3f" % data.p[1])
        self.fyILabel.setText("%0.3f" % data.i[1])
        self.fyDLabel.setText("%0.3f" % data.d[1])
        self.fyNLabel.setText("%0.3f" % data.n[1])
        self.fyCalculatedALabel.setText("%0.3f" % data.calculatedA[1])
        self.fyCalculatedBLabel.setText("%0.3f" % data.calculatedB[1])
        self.fyCalculatedCLabel.setText("%0.3f" % data.calculatedC[1])
        self.fyCalculatedDLabel.setText("%0.3f" % data.calculatedD[1])
        self.fyCalculatedELabel.setText("%0.3f" % data.calculatedE[1])

        self.fzTimestepLabel.setText("%0.3f" % data.timestep[2])
        self.fzPLabel.setText("%0.3f" % data.p[2])
        self.fzILabel.setText("%0.3f" % data.i[2])
        self.fzDLabel.setText("%0.3f" % data.d[2])
        self.fzNLabel.setText("%0.3f" % data.n[2])
        self.fzCalculatedALabel.setText("%0.3f" % data.calculatedA[2])
        self.fzCalculatedBLabel.setText("%0.3f" % data.calculatedB[2])
        self.fzCalculatedCLabel.setText("%0.3f" % data.calculatedC[2])
        self.fzCalculatedDLabel.setText("%0.3f" % data.calculatedD[2])
        self.fzCalculatedELabel.setText("%0.3f" % data.calculatedE[2])

        self.mxTimestepLabel.setText("%0.3f" % data.timestep[3])
        self.mxPLabel.setText("%0.3f" % data.p[3])
        self.mxILabel.setText("%0.3f" % data.i[3])
        self.mxDLabel.setText("%0.3f" % data.d[3])
        self.mxNLabel.setText("%0.3f" % data.n[3])
        self.mxCalculatedALabel.setText("%0.3f" % data.calculatedA[3])
        self.mxCalculatedBLabel.setText("%0.3f" % data.calculatedB[3])
        self.mxCalculatedCLabel.setText("%0.3f" % data.calculatedC[3])
        self.mxCalculatedDLabel.setText("%0.3f" % data.calculatedD[3])
        self.mxCalculatedELabel.setText("%0.3f" % data.calculatedE[3])

        self.myTimestepLabel.setText("%0.3f" % data.timestep[4])
        self.myPLabel.setText("%0.3f" % data.p[4])
        self.myILabel.setText("%0.3f" % data.i[4])
        self.myDLabel.setText("%0.3f" % data.d[4])
        self.myNLabel.setText("%0.3f" % data.n[4])
        self.myCalculatedALabel.setText("%0.3f" % data.calculatedA[4])
        self.myCalculatedBLabel.setText("%0.3f" % data.calculatedB[4])
        self.myCalculatedCLabel.setText("%0.3f" % data.calculatedC[4])
        self.myCalculatedDLabel.setText("%0.3f" % data.calculatedD[4])
        self.myCalculatedELabel.setText("%0.3f" % data.calculatedE[4])

        self.mzTimestepLabel.setText("%0.3f" % data.timestep[5])
        self.mzPLabel.setText("%0.3f" % data.p[5])
        self.mzILabel.setText("%0.3f" % data.i[5])
        self.mzDLabel.setText("%0.3f" % data.d[5])
        self.mzNLabel.setText("%0.3f" % data.n[5])
        self.mzCalculatedALabel.setText("%0.3f" % data.calculatedA[5])
        self.mzCalculatedBLabel.setText("%0.3f" % data.calculatedB[5])
        self.mzCalculatedCLabel.setText("%0.3f" % data.calculatedC[5])
        self.mzCalculatedDLabel.setText("%0.3f" % data.calculatedD[5])
        self.mzCalculatedELabel.setText("%0.3f" % data.calculatedE[5])

    @Slot(map)
    def pidData(self, data):
        self.fxSetpointLabel.setText("%0.3f" % data.setpoint[0])
        self.fxMeasurementLabel.setText("%0.3f" % data.measurement[0])
        self.fxErrorLabel.setText("%0.3f" % data.error[0])
        self.fxErrorT1Label.setText("%0.3f" % data.errorT1[0])
        self.fxErrorT2Label.setText("%0.3f" % data.errorT2[0])
        self.fxControlLabel.setText("%0.3f" % data.control[0])
        self.fxControlT1Label.setText("%0.3f" % data.controlT1[0])
        self.fxControlT2Label.setText("%0.3f" % data.controlT2[0])
        self.fySetpointLabel.setText("%0.3f" % data.setpoint[1])
        self.fyMeasurementLabel.setText("%0.3f" % data.measurement[1])
        self.fyErrorLabel.setText("%0.3f" % data.error[1])
        self.fyErrorT1Label.setText("%0.3f" % data.errorT1[1])
        self.fyErrorT2Label.setText("%0.3f" % data.errorT2[1])
        self.fyControlLabel.setText("%0.3f" % data.control[1])
        self.fyControlT1Label.setText("%0.3f" % data.controlT1[1])
        self.fyControlT2Label.setText("%0.3f" % data.controlT2[1])
        self.fzSetpointLabel.setText("%0.3f" % data.setpoint[2])
        self.fzMeasurementLabel.setText("%0.3f" % data.measurement[2])
        self.fzErrorLabel.setText("%0.3f" % data.error[2])
        self.fzErrorT1Label.setText("%0.3f" % data.errorT1[2])
        self.fzErrorT2Label.setText("%0.3f" % data.errorT2[2])
        self.fzControlLabel.setText("%0.3f" % data.control[2])
        self.fzControlT1Label.setText("%0.3f" % data.controlT1[2])
        self.fzControlT2Label.setText("%0.3f" % data.controlT2[2])
        self.mxSetpointLabel.setText("%0.3f" % data.setpoint[3])
        self.mxMeasurementLabel.setText("%0.3f" % data.measurement[3])
        self.mxErrorLabel.setText("%0.3f" % data.error[3])
        self.mxErrorT1Label.setText("%0.3f" % data.errorT1[3])
        self.mxErrorT2Label.setText("%0.3f" % data.errorT2[3])
        self.mxControlLabel.setText("%0.3f" % data.control[3])
        self.mxControlT1Label.setText("%0.3f" % data.controlT1[3])
        self.mxControlT2Label.setText("%0.3f" % data.controlT2[3])
        self.mySetpointLabel.setText("%0.3f" % data.setpoint[4])
        self.myMeasurementLabel.setText("%0.3f" % data.measurement[4])
        self.myErrorLabel.setText("%0.3f" % data.error[4])
        self.myErrorT1Label.setText("%0.3f" % data.errorT1[4])
        self.myErrorT2Label.setText("%0.3f" % data.errorT2[4])
        self.myControlLabel.setText("%0.3f" % data.control[4])
        self.myControlT1Label.setText("%0.3f" % data.controlT1[4])
        self.myControlT2Label.setText("%0.3f" % data.controlT2[4])
        self.mzSetpointLabel.setText("%0.3f" % data.setpoint[5])
        self.mzMeasurementLabel.setText("%0.3f" % data.measurement[5])
        self.mzErrorLabel.setText("%0.3f" % data.error[5])
        self.mzErrorT1Label.setText("%0.3f" % data.errorT1[5])
        self.mzErrorT2Label.setText("%0.3f" % data.errorT2[5])
        self.mzControlLabel.setText("%0.3f" % data.control[5])
        self.mzControlT1Label.setText("%0.3f" % data.controlT1[5])
        self.mzControlT2Label.setText("%0.3f" % data.controlT2[5])

        self.chart.append(
            data.timestamp,
            [
                ("Command", "Fx", data.control[0]),
                self.chart.append("Command", "Fy", data.control[1]),
                self.chart.append("Command", "Fz", data.control[2]),
                self.chart.append("Command", "Mx", data.control[3]),
                self.chart.append("Command", "My", data.control[4]),
                self.chart.append("Command", "Mz", data.control[5]),
            ],
        )
