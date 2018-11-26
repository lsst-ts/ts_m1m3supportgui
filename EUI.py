#!/usr/bin/python3
# -'''- coding: utf-8 -'''-

import sys
import time

from MTM1M3Remote import MTM1M3Remote

from ApplicationControlWidget import ApplicationControlWidget
from ApplicationStatusWidget import ApplicationStatusWidget
from ApplicationPaginationWidget import ApplicationPaginationWidget

from ActuatorOverviewPageWidget import ActuatorOverviewPageWidget
from AirPageWidget import AirPageWidget
from CellLightPageWidget import CellLightPageWidget
from DCAccelerometerPageWidget import DCAccelerometerPageWidget
from ForceActuatorGraphPageWidget import ForceActuatorGraphPageWidget
from ForceActuatorValuePageWidget import ForceActuatorValuePageWidget
from ForceBalanceSystemPageWidget import ForceBalanceSystemPageWidget
from GyroPageWidget import GyroPageWidget
from IMSPageWidget import IMSPageWidget
from InclinometerPageWidget import InclinometerPageWidget
from InterlockPageWidget import InterlockPageWidget
from OverviewPageWidget import OverviewPageWidget
from PIDPageWidget import PIDPageWidget
from PowerPageWidget import PowerPageWidget

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import (QApplication, QVBoxLayout, QDialog, QHBoxLayout, QLabel)
from PySide2.QtGui import QFont

class EUI(QDialog):
    def __init__(self, MTM1M3, parent=None):
        super(EUI, self).__init__(parent)
        self.MTM1M3 = MTM1M3
        self.layout = QVBoxLayout()
        self.topLayerLayout = QHBoxLayout()
        
        self.applicationControlLayout = QVBoxLayout()
        self.applicationControl = ApplicationControlWidget(MTM1M3)
        self.applicationControl.setFixedSize(256, 175)
        self.applicationControlLayout.addWidget(QLabel("Application Control"))
        self.applicationControlLayout.addWidget(self.applicationControl)
        self.topLayerLayout.addLayout(self.applicationControlLayout)

        self.applicationStatusLayout = QVBoxLayout()
        self.applicationStatus = ApplicationStatusWidget(MTM1M3)
        self.applicationStatus.setFixedHeight(175)
        self.applicationStatusLayout.addWidget(QLabel("Application Status"))
        self.applicationStatusLayout.addWidget(self.applicationStatus)
        self.topLayerLayout.addLayout(self.applicationStatusLayout)
        
        self.middleLayerLayout = QHBoxLayout()
        self.applicationPagination = ApplicationPaginationWidget(MTM1M3)
        self.applicationPagination.setPageListWidth(238)
        self.applicationPagination.addPage("Overview", OverviewPageWidget(MTM1M3))
        self.applicationPagination.addPage("Actuator Overview", ActuatorOverviewPageWidget(MTM1M3))
        self.applicationPagination.addPage("DC Accelerometers", DCAccelerometerPageWidget(MTM1M3))
        self.applicationPagination.addPage("Gyro", GyroPageWidget(MTM1M3))
        self.applicationPagination.addPage("IMS", IMSPageWidget(MTM1M3))
        self.applicationPagination.addPage("Inclinometer", InclinometerPageWidget(MTM1M3))
        self.applicationPagination.addPage("Interlock", InterlockPageWidget(MTM1M3))
        self.applicationPagination.addPage("Lights", CellLightPageWidget(MTM1M3))
        self.applicationPagination.addPage("Air", AirPageWidget(MTM1M3))
        self.applicationPagination.addPage("Power", PowerPageWidget(MTM1M3))
        self.applicationPagination.addPage("PID", PIDPageWidget(MTM1M3))
        self.applicationPagination.addPage("Force Balance System", ForceBalanceSystemPageWidget(MTM1M3))
        self.applicationPagination.addPage("Force Actuator Graph", ForceActuatorGraphPageWidget(MTM1M3))
        self.applicationPagination.addPage("Force Actuator Value", ForceActuatorValuePageWidget(MTM1M3))
        self.middleLayerLayout.addWidget(self.applicationPagination)
        self.bottomLayerLayout = QHBoxLayout()
        self.layout.addLayout(self.topLayerLayout)
        self.layout.addLayout(self.middleLayerLayout)
        self.layout.addLayout(self.bottomLayerLayout)
        self.setLayout(self.layout)
        self.setFixedSize(1900, 1000)
        font = self.font()
        font.setStyleHint(QFont.Courier)
        font.setPointSize(13)
        self.setFont(font)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create EUI
    MTM1M3 = MTM1M3Remote()
    eui = EUI(MTM1M3)
    eui.show()
    # Create MTM1M3 Telemetry & Event Loop
    telemetryEventLoopTimer = QTimer()
    telemetryEventLoopTimer.timeout.connect(MTM1M3.runSubscriberChecks)
    telemetryEventLoopTimer.start(500)
    # Run the main Qt loop
    app.exec_()
    # Clean up MTM1M3 Telemetry & Event Loop
    telemetryEventLoopTimer.stop()
    # Close application
    sys.exit()