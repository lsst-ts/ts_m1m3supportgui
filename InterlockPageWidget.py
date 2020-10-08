import QTHelpers
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot

class InterlockPageWidget(QWidget):
    def __init__(self, comm):
        QWidget.__init__(self)
        self.comm = comm
        self.pageActive = False

        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addWidget(QLabel(" "))
        self.layout.addLayout(self.warningLayout)
        self.setLayout(self.layout)
        self.setFixedHeight(250)
        
        self.heartbeatLabel = QLabel("UNKNOWN")
        
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.auxPowerNetworksOffLabel = QLabel("UNKNOWN")
        self.thermalEquipmentOffLabel = QLabel("UNKNOWN")
        self.airSupplyOffLabel = QLabel("UNKNOWN")
        self.tmaMotionStopLabel = QLabel("UNKNOWN")
        self.gisHeartbeatLostLabel = QLabel("UNKNOWN")
        self.cabinetDoorOpenLabel = QLabel("UNKNOWN")

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Controller to Interlock Heartbeat"), row, col)
        self.dataLayout.addWidget(self.heartbeatLabel, row, col + 1)
        
        row = 0
        col = 0
        self.warningLayout.addWidget(QLabel("Any Warnings"), row, col)
        self.warningLayout.addWidget(self.anyWarningLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("AUX Power Networks Off"), row, col)
        self.warningLayout.addWidget(self.auxPowerNetworksOffLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Thermal Equipment Off"), row, col)
        self.warningLayout.addWidget(self.thermalEquipmentOffLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Air Supply Off"), row, col)
        self.warningLayout.addWidget(self.airSupplyOffLabel, row, col + 1)
        
        row = 1
        col = 2
        self.warningLayout.addWidget(QLabel("TMA Motion Stop"), row, col)
        self.warningLayout.addWidget(self.tmaMotionStopLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("GIS Heartbeat Lost"), row, col)
        self.warningLayout.addWidget(self.gisHeartbeatLostLabel, row, col + 1)
        row += 1
        self.warningLayout.addWidget(QLabel("Cabinet Door Open"), row, col)
        self.warningLayout.addWidget(self.cabinetDoorOpenLabel, row, col + 1)

    def setPageActive(self, active):
        if self.pageActive == active:
            return

        if active:
            self.comm.interlockWarning.connect(self.interlockWarning)
            self.comm.interlockStatus.connect(self.interlockStatus)
        else:
            self.comm.interlockWarning.disconnect(self.interlockWarning)
            self.comm.interlockStatus.disconnect(self.interlockStatus)

        self.pageActive = active

    @Slot(map)
    def interlockWarning(self, data):
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
            #TODO QTHelpers.setWarningLabel(self.auxPowerNetworksOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.AuxPowerNetworksOff))
            #TODO QTHelpers.setWarningLabel(self.thermalEquipmentOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.ThermalEquipmentOff))
            #TODO QTHelpers.setWarningLabel(self.airSupplyOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.AirSupplyOff))
            #TODO QTHelpers.setWarningLabel(self.tmaMotionStopLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.TMAMotionStop))
            #TODO QTHelpers.setWarningLabel(self.gisHeartbeatLostLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.GISHeartbeatLost))
            #TODO QTHelpers.setWarningLabel(self.cabinetDoorOpenLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.CabinetDoorOpen))

    @Slot(map)
    def interlockStatus(self, data):
        QTHelpers.setBoolLabelHighLow(self.heartbeatLabel, data.heartbeatCommandedState)
