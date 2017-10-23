#!/usr/bin/python
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
from GyroPageWidget import GyroPageWidget
from IMSPageWidget import IMSPageWidget
from InclinometerPageWidget import InclinometerPageWidget
from InterlockPageWidget import InterlockPageWidget
from OverviewPageWidget import OverviewPageWidget
from PIDPageWidget import PIDPageWidget
from PowerPageWidget import PowerPageWidget

from PySide2.QtCore import QThread, QTimer
from PySide2.QtWidgets import (QApplication, QVBoxLayout, QDialog, QHBoxLayout)

class MTM1M3EUI(QDialog):
    def __init__(self, mtm1m3, parent=None):
        super(MTM1M3EUI, self).__init__(parent)
        self.mtm1m3 = mtm1m3
        self.layout = QVBoxLayout()
        self.topLayerLayout = QHBoxLayout()
        self.applicationControl = ApplicationControlWidget(mtm1m3)
        self.topLayerLayout.addWidget(self.applicationControl)
        self.applicationStatus = ApplicationStatusWidget(mtm1m3)
        self.topLayerLayout.addWidget(self.applicationStatus)
        self.middleLayerLayout = QHBoxLayout()
        self.applicationPagination = ApplicationPaginationWidget(mtm1m3)
        self.applicationPagination.addPage("Overview", OverviewPageWidget(mtm1m3))
        self.applicationPagination.addPage("Actuator Overview", ActuatorOverviewPageWidget(mtm1m3))
        self.applicationPagination.addPage("DC Accelerometers", DCAccelerometerPageWidget(mtm1m3))
        self.applicationPagination.addPage("Gyro", GyroPageWidget(mtm1m3))
        self.applicationPagination.addPage("IMS", IMSPageWidget(mtm1m3))
        self.applicationPagination.addPage("Inclinometer", InclinometerPageWidget(mtm1m3))
        self.applicationPagination.addPage("Interlock", InterlockPageWidget(mtm1m3))
        self.applicationPagination.addPage("Lights", CellLightPageWidget(mtm1m3))
        self.applicationPagination.addPage("Air", AirPageWidget(mtm1m3))
        self.applicationPagination.addPage("Power", PowerPageWidget(mtm1m3))
        self.applicationPagination.addPage("PID", PIDPageWidget(mtm1m3))
        self.middleLayerLayout.addWidget(self.applicationPagination)
        self.bottomLayerLayout = QHBoxLayout()
        self.layout.addLayout(self.topLayerLayout)
        self.layout.addLayout(self.middleLayerLayout)
        self.layout.addLayout(self.bottomLayerLayout)
        self.setLayout(self.layout)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create EUI
    mtm1m3 = MTM1M3Remote()
    eui = MTM1M3EUI(mtm1m3)
    eui.show()
    # Create MTM1M3 Telemetry & Event Loop
    telemetryEventLoopTimer = QTimer()
    telemetryEventLoopTimer.timeout.connect(mtm1m3.runSubscriberChecks)
    telemetryEventLoopTimer.start(500)
    # Run the main Qt loop
    app.exec_()
    # Clean up MTM1M3 Telemetry & Event Loop
    telemetryEventLoopTimer.stop()
    # Close application
    sys.exit()