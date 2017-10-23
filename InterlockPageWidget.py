
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import InterlockSystemFlags
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout

class InterlockPageWidget(QWidget):
    def __init__(self, mtm1m3):
        QWidget.__init__(self)
        self.mtm1m3 = mtm1m3
        self.layout = QVBoxLayout()
        self.dataLayout = QGridLayout()
        self.warningLayout = QGridLayout()

        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.warningLayout)
        self.setLayout(self.layout)
        
        self.anyWarningLabel = QLabel("UNKNOWN")
        self.auxPowerNetworksOffLabel = QLabel("UNKNOWN")
        self.thermalEquipmentOffLabel = QLabel("UNKNOWN")
        self.airSupplyOffLabel = QLabel("UNKNOWN")
        self.tmaMotionStopLabel = QLabel("UNKNOWN")
        self.gisHeartbeatLostLabel = QLabel("UNKNOWN")
        self.cabinetDoorOpenLabel = QLabel("UNKNOWN")
        self.heartbeatLabel = QLabel("UNKNOWN")

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
        
        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("Controller to Interlock Heartbeat"), row, col)
        self.dataLayout.addWidget(self.heartbeatLabel, row, col + 1)
        
        self.mtm1m3.subscribeEvent_interlockWarning(self.processEventInterlockWarning)
        self.mtm1m3.subscribeEvent_interlockStatus(self.processEventInterlockStatus)

    def processEventInterlockWarning(self, data):
        data = data[-1]
        QTHelpers.setWarningLabel(self.anyWarningLabel, data.anyWarning)
        QTHelpers.setWarningLabel(self.auxPowerNetworksOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.AuxPowerNetworksOff))
        QTHelpers.setWarningLabel(self.thermalEquipmentOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.ThermalEquipmentOff))
        QTHelpers.setWarningLabel(self.airSupplyOffLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.AirSupplyOff))
        QTHelpers.setWarningLabel(self.tmaMotionStopLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.TMAMotionStop))
        QTHelpers.setWarningLabel(self.gisHeartbeatLostLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.GISHeartbeatLost))
        QTHelpers.setWarningLabel(self.cabinetDoorOpenLabel, BitHelper.get(data.interlockSystemFlags, InterlockSystemFlags.CabinetDoorOpen))

    def processEventInterlockStatus(self, data):
        data = data[-1]
        QTHelpers.setBoolLabelHighLow(self.heartbeatLabel, data.heartbeatCommandedState)