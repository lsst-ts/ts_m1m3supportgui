
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import ForceActuatorZIndexMap
from FATABLE import *
from TopicData import TopicData
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QListWidget
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class ForceActuatorValuePageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QHBoxLayout()
        self.dataLayout = QGridLayout()
        self.selectionLayout = QVBoxLayout()
        self.detailsLayout = QGridLayout()
        self.filterLayout = QHBoxLayout()
        self.layout.addLayout(self.dataLayout)
        self.layout.addLayout(self.selectionLayout)
        self.selectionLayout.addLayout(self.detailsLayout)
        self.selectionLayout.addWidget(QLabel("Filter Data"))
        self.selectionLayout.addLayout(self.filterLayout)
        self.setLayout(self.layout)

        self.forceActuatorLabels = []
        for i in range(156):
            self.forceActuatorLabels.append(QLabel("UNKNOWN"))

        self.lastUpdatedLabel = QLabel("UNKNOWN")

        self.topicList = QListWidget()
        self.topicList.setFixedWidth(256)
        self.topicList.itemSelectionChanged.connect(self.selectedTopicChanged)
        self.topics = [
            TopicData("Applied Aberration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Applied Acceleration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Active Optic Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Applied Azimuth Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Balance Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Cylinder Forces", [["Primary Cylinder Forces", lambda x: [i / 1000.0 for i in x.primaryCylinderForces], lambda: FATABLE_ZINDEX], ["Secondary Cylinder Forces", lambda x: [i / 1000.0 for i in x.secondaryCylinderForces], lambda: FATABLE_SINDEX]]),
            TopicData("Applied Elevation Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Offset Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Static Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Thermal Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Applied Velocity Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Aberration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Rejected Acceleration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Active Optic Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Rejected Azimuth Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Balance Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Cylinder Forces", [["Primary Cylinder Forces", lambda x: [i / 1000.0 for i in x.primaryCylinderForces], lambda: FATABLE_ZINDEX], ["Secondary Cylinder Forces", lambda x: [i / 1000.0 for i in x.secondaryCylinderForces], lambda: FATABLE_SINDEX]]),
            TopicData("Rejected Elevation Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Offset Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Static Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Thermal Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Rejected Velocity Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Force Actuator Backup Calibration Info", [["Primary Coefficient", lambda x: x.primaryCoefficient, lambda: FATABLE_ZINDEX], ["Primary Offset", lambda x: x.primaryOffset, lambda: FATABLE_ZINDEX], ["Primary Sensitivity", lambda x: x.primarySensitivity, lambda: FATABLE_ZINDEX], ["Secondary Coefficient", lambda x: x.secondaryCoefficient, lambda: FATABLE_SINDEX], ["Secondary Offset", lambda x: x.secondaryOffset, lambda: FATABLE_SINDEX], ["Secondary Sensitivity", lambda x: x.secondarySensitivity, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator ILC Info", [["Subnet", lambda x: x.modbusSubnet, lambda: FATABLE_ZINDEX], ["Address", lambda x: x.modbusAddress, lambda: FATABLE_ZINDEX], ["ILC Status", lambda x: x.ilcStatus, lambda: FATABLE_ZINDEX], ["Mezzanine Status", lambda x: x.mezzanineStatus, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Id Info", [["X Data Reference Id", lambda x: x.xDataReferenceId, lambda: FATABLE_XINDEX], ["Y Data Reference Id", lambda x: x.yDataReferenceId, lambda: FATABLE_YINDEX], ["Z Data Reference Id", lambda x: x.zDataReferenceId, lambda: FATABLE_ZINDEX], ["S Data Reference Id", lambda x: x.sDataReferenceId, lambda: FATABLE_SINDEX], ["ILC Unique Id", lambda x: x.ilcUniqueId, lambda: FATABLE_ZINDEX], ["Mezzanine Unique Id", lambda x: x.xDataReferenceId, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Main Calibration Info", [["Primary Coefficient", lambda x: x.primaryCoefficient, lambda: FATABLE_ZINDEX], ["Primary Offset", lambda x: x.primaryOffset, lambda: FATABLE_ZINDEX], ["Primary Sensitivity", lambda x: x.primarySensitivity, lambda: FATABLE_ZINDEX], ["Secondary Coefficient", lambda x: x.secondaryCoefficient, lambda: FATABLE_SINDEX], ["Secondary Offset", lambda x: x.secondaryOffset, lambda: FATABLE_SINDEX], ["Secondary Sensitivity", lambda x: x.secondarySensitivity, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator Mezzanine Calibration Info", [["Primary Cylinder Gain", lambda x: x.primaryCylinderFain, lambda: FATABLE_ZINDEX], ["Secondary Cylinder Gain", lambda x: x.secondaryCylinderGain, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator Position Info", [["Actuator Type", lambda x: x.actuatorType, lambda: FATABLE_ZINDEX], ["Actuator Orientation", lambda x: x.actuatorOrientation, lambda: FATABLE_ZINDEX], ["X Position", lambda x: x.xPosition, lambda: FATABLE_ZINDEX], ["Y Position", lambda x: x.yPosition, lambda: FATABLE_ZINDEX], ["Z Position", lambda x: x.zPosition, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator State", [["ILC State", lambda x: x.ilcState, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Warning", [["Force Actuator Flags", lambda x: x.forceActuatorFlags, lambda: FATABLE_ZINDEX]]),
        ]
        for topic in self.topics:
            self.topicList.addItem(topic.Topic)
        self.fieldList = QListWidget()
        self.fieldList.setFixedWidth(256)
        self.fieldList.itemSelectionChanged.connect(self.selectedFieldChanged)

        row = 0
        col = 0
        self.dataLayout.addWidget(QLabel("0"), row, col + 1)
        self.dataLayout.addWidget(QLabel("1"), row, col + 2)
        self.dataLayout.addWidget(QLabel("2"), row, col + 3)
        self.dataLayout.addWidget(QLabel("3"), row, col + 4)
        self.dataLayout.addWidget(QLabel("4"), row, col + 5)
        self.dataLayout.addWidget(QLabel("5"), row, col + 6)
        self.dataLayout.addWidget(QLabel("6"), row, col + 7)
        self.dataLayout.addWidget(QLabel("7"), row, col + 8)
        self.dataLayout.addWidget(QLabel("8"), row, col + 9)
        self.dataLayout.addWidget(QLabel("9"), row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("100"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA101], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA102], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA103], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA104], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA105], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA106], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA107], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA108], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA109], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("110"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA110], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA111], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA112], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA113], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA114], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA115], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA116], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA117], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA118], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA119], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("120"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA120], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA121], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA122], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA123], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA124], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA125], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA126], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA127], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA128], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA129], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("130"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA130], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA131], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA132], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA133], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA134], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA135], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA136], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA137], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA138], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA139], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("140"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA140], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA141], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA142], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA143], row, col + 4)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("200"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA207], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA208], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA209], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("210"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA210], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA211], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA212], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA214], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA215], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA216], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA217], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA218], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA219], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("220"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA220], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA221], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA222], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA223], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA224], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA225], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA227], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA228], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA229], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("230"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA230], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA231], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA232], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA233], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA234], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA235], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA236], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA237], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA238], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA239], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("240"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA240], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA241], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA242], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA243], row, col + 4)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("300"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA301], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA302], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA303], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA304], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA305], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA306], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA307], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA308], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA309], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("310"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA310], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA311], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA312], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA313], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA314], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA315], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA316], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA317], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA318], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA319], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("320"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA320], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA321], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA322], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA323], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA324], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA325], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA326], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA327], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA328], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA329], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("330"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA330], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA331], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA332], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA333], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA334], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA335], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA336], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA337], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA338], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA339], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("340"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA340], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA341], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA342], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA343], row, col + 4)
        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("400"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA407], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA408], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA409], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("410"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA410], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA411], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA412], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA414], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA415], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA416], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA417], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA418], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA419], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("420"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA420], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA421], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA422], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA423], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA424], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA425], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA427], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA428], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA429], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("430"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA430], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA431], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA432], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA433], row, col + 4)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA434], row, col + 5)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA435], row, col + 6)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA436], row, col + 7)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA437], row, col + 8)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA438], row, col + 9)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA439], row, col + 10)
        row += 1
        self.dataLayout.addWidget(QLabel("440"), row, col)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA440], row, col + 1)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA441], row, col + 2)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA442], row, col + 3)
        self.dataLayout.addWidget(self.forceActuatorLabels[ForceActuatorZIndexMap.FA443], row, col + 4)

        row = 0
        col = 0
        self.detailsLayout.addWidget(QLabel("Last Updated"), row, col)
        self.detailsLayout.addWidget(self.lastUpdatedLabel, row, col + 1)

        self.filterLayout.addWidget(self.topicList)
        self.topicList.setCurrentRow(0)
        self.filterLayout.addWidget(self.fieldList)

        self.MTM1M3.subscribeEvent_appliedAberrationForces(self.processEventAppliedAberrationForces)
        self.MTM1M3.subscribeEvent_appliedAccelerationForces(self.processEventAppliedAccelerationForces)
        self.MTM1M3.subscribeEvent_appliedActiveOpticForces(self.processEventAppliedActiveOpticForces)
        self.MTM1M3.subscribeEvent_appliedAzimuthForces(self.processEventAppliedAzimuthForces)
        self.MTM1M3.subscribeEvent_appliedBalanceForces(self.processEventAppliedBalanceForces)
        self.MTM1M3.subscribeEvent_appliedCylinderForces(self.processEventAppliedCylinderForces)
        self.MTM1M3.subscribeEvent_appliedElevationForces(self.processEventAppliedElevationForces)
        self.MTM1M3.subscribeEvent_appliedForces(self.processEventAppliedForces)
        self.MTM1M3.subscribeEvent_appliedOffsetForces(self.processEventAppliedOffsetForces)
        self.MTM1M3.subscribeEvent_appliedStaticForces(self.processEventAppliedStaticForces)
        self.MTM1M3.subscribeEvent_appliedThermalForces(self.processEventAppliedThermalForces)
        self.MTM1M3.subscribeEvent_appliedVelocityForces(self.processEventAppliedVelocityForces)

        self.MTM1M3.subscribeEvent_forceActuatorBackupCalibrationInfo(self.processEventForceActuatorBackupCalibrationInfo)
        self.MTM1M3.subscribeEvent_forceActuatorIdInfo(self.processEventForceActuatorIdInfo)
        self.MTM1M3.subscribeEvent_forceActuatorILCInfo(self.processEventForceActuatorILCInfo)
        self.MTM1M3.subscribeEvent_forceActuatorMainCalibrationInfo(self.processEventForceActuatorMainCalibrationInfo)
        self.MTM1M3.subscribeEvent_forceActuatorMezzanineCalibrationInfo(self.processEventForceActuatorMezzanineCalibrationInfo)
        self.MTM1M3.subscribeEvent_forceActuatorPositionInfo(self.processEventForceActuatorPositionInfo)
        self.MTM1M3.subscribeEvent_forceActuatorState(self.processEventForceActuatorState)
        self.MTM1M3.subscribeEvent_forceActuatorWarning(self.processEventForceActuatorWarning)

        self.MTM1M3.subscribeEvent_rejectedAberrationForces(self.processEventRejectedAberrationForces)
        self.MTM1M3.subscribeEvent_rejectedAccelerationForces(self.processEventRejectedAccelerationForces)
        self.MTM1M3.subscribeEvent_rejectedActiveOpticForces(self.processEventRejectedActiveOpticForces)
        self.MTM1M3.subscribeEvent_rejectedAzimuthForces(self.processEventRejectedAzimuthForces)
        self.MTM1M3.subscribeEvent_rejectedBalanceForces(self.processEventRejectedBalanceForces)
        self.MTM1M3.subscribeEvent_rejectedCylinderForces(self.processEventRejectedCylinderForces)
        self.MTM1M3.subscribeEvent_rejectedElevationForces(self.processEventRejectedElevationForces)
        self.MTM1M3.subscribeEvent_rejectedForces(self.processEventRejectedForces)
        self.MTM1M3.subscribeEvent_rejectedOffsetForces(self.processEventRejectedOffsetForces)
        self.MTM1M3.subscribeEvent_rejectedStaticForces(self.processEventRejectedStaticForces)
        self.MTM1M3.subscribeEvent_rejectedThermalForces(self.processEventRejectedThermalForces)
        self.MTM1M3.subscribeEvent_rejectedVelocityForces(self.processEventRejectedVelocityForces)
    
    def processEventAppliedAberrationForces(self, data):
        self.updateTopicData('Applied Aberration Forces', data[-1])

    def processEventAppliedAccelerationForces(self, data):
        self.updateTopicData('Applied Acceleration Forces', data[-1])

    def processEventAppliedActiveOpticForces(self, data):
        self.updateTopicData('Applied Active Optic Forces', data[-1])
    
    def processEventAppliedAzimuthForces(self, data):
        self.updateTopicData('Applied Azimuth Forces', data[-1])

    def processEventAppliedBalanceForces(self, data):
        self.updateTopicData('Applied Balance Forces', data[-1])

    def processEventAppliedCylinderForces(self, data):
        self.updateTopicData('Applied Cylinder Forces', data[-1])

    def processEventAppliedElevationForces(self, data):
        self.updateTopicData('Applied Elevation Forces', data[-1])

    def processEventAppliedForces(self, data):
        self.updateTopicData('Applied Forces', data[-1])

    def processEventAppliedOffsetForces(self, data):
        self.updateTopicData('Applied Offset Forces', data[-1])

    def processEventAppliedStaticForces(self, data):
        self.updateTopicData('Applied Static Forces', data[-1])

    def processEventAppliedThermalForces(self, data):
        self.updateTopicData('Applied Thermal Forces', data[-1])

    def processEventAppliedVelocityForces(self, data):
        self.updateTopicData('Applied Velocity Forces', data[-1])

    def processEventForceActuatorBackupCalibrationInfo(self, data):
        self.updateTopicData('Force Actuator Backup Calibration Info', data[-1])

    def processEventForceActuatorILCInfo(self, data):
        self.updateTopicData('Force Actuator ILC Info', data[-1])

    def processEventForceActuatorIdInfo(self, data):
        self.updateTopicData('Force Actuator Id Info', data[-1])

    def processEventForceActuatorMainCalibrationInfo(self, data):
        self.updateTopicData('Force Actuator Main Calibration Info', data[-1])
    
    def processEventForceActuatorMezzanineCalibrationInfo(self, data):
        self.updateTopicData('Force Actuator Mezzanine Calibration Info', data[-1])

    def processEventForceActuatorPositionInfo(self, data):
        self.updateTopicData('Force Actuator Position Info', data[-1])

    def processEventForceActuatorState(self, data):
        self.updateTopicData('Force Actuator State', data[-1])

    def processEventForceActuatorWarning(self, data):
        self.actuatorWarningData = data[-1]
        self.updateTopicData('Force Actuator Warning', self.actuatorWarningData)

    def processEventRejectedAberrationForces(self, data):
        self.updateTopicData('Rejected Aberration Forces', data[-1])

    def processEventRejectedAccelerationForces(self, data):
        self.updateTopicData('Rejected Acceleration Forces', data[-1])

    def processEventRejectedActiveOpticForces(self, data):
        self.updateTopicData('Rejected Active Optic Forces', data[-1])
    
    def processEventRejectedAzimuthForces(self, data):
        self.updateTopicData('Rejected Azimuth Forces', data[-1])

    def processEventRejectedBalanceForces(self, data):
        self.updateTopicData('Rejected Balance Forces', data[-1])

    def processEventRejectedCylinderForces(self, data):
        self.updateTopicData('Rejected Cylinder Forces', data[-1])

    def processEventRejectedElevationForces(self, data):
        self.updateTopicData('Rejected Elevation Forces', data[-1])

    def processEventRejectedForces(self, data):
        self.updateTopicData('Rejected Forces', data[-1])

    def processEventRejectedOffsetForces(self, data):
        self.updateTopicData('Rejected Offset Forces', data[-1])

    def processEventRejectedStaticForces(self, data):
        self.updateTopicData('Rejected Static Forces', data[-1])

    def processEventRejectedThermalForces(self, data):
        self.updateTopicData('Rejected Thermal Forces', data[-1])

    def processEventRejectedVelocityForces(self, data):
        self.updateTopicData('Rejected Velocity Forces', data[-1])

    def updateTopicData(self, topicName, data):
        for topic in self.topics:
            if topic.Topic == topicName:
                topic.Data = data
                topic.LastUpdated = self.MTM1M3.getTimestamp()
        if self.isCurrentTopic(topicName):
            self.updatePlot()

    def isCurrentTopic(self, topic):
        if len(self.topicList.selectedItems()) == 0:
            return False
        return self.topicList.selectedItems()[0].text() == topic

    def selectedTopicChanged(self):
        if self.topicList.currentRow() < 0:
            return
        self.ignoreFieldChange = True
        self.fieldList.clear()
        newTopicIndex = self.topicList.currentRow()
        for field in self.topics[newTopicIndex].Fields:
            self.fieldList.addItem(field[0])
        self.fieldList.setCurrentRow(self.topics[newTopicIndex].SelectedField) 

    def selectedFieldChanged(self):
        if self.ignoreFieldChange:
            self.ignoreFieldChange = False
            return
        if self.topicList.currentRow() < 0 or self.fieldList.currentRow() < 0:
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        self.topics[topicIndex].SelectedField = fieldIndex
        self.updatePlot()

    def updatePlot(self):
        if len(self.topicList.selectedIndexes()) == 0 or len(self.fieldList.selectedIndexes()) == 0:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        topic = self.topics[topicIndex]
        field = topic.Fields[fieldIndex]
        fieldGetter = field[1]
        fieldDataIndex = field[2]()
        data = None
        if topic.Data is not None:
            data = fieldGetter(topic.Data)
        else:
            self.lastUpdatedLabel.setText("UNKNOWN")
        i = -1
        for row in FATABLE:
            i += 1
            dataIndex = row[fieldDataIndex]
            #warning = False
            #if self.actuatorWarningData is not None:
            #    warning = self.actuatorWarningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
            if dataIndex != -1 and data is not None:
                self.forceActuatorLabels[i].setText("%0.1f" % data[dataIndex])
            elif dataIndex != -1:
                self.forceActuatorLabels[i].setText("UNKNOWN")
            else:
                self.forceActuatorLabels[i].setText("")
        lastUpdated = self.MTM1M3.getTimestamp() - topic.LastUpdated
        self.lastUpdatedLabel.setText("%0.1fs" % lastUpdated)