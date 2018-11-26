
import QTHelpers
from BitHelper import BitHelper
from MTM1M3Enumerations import HardpointIndexMap, ForceActuatorFlags
from FATABLE import *
from TopicData import TopicData
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB
from ScatterPlotWidget import ScatterPlotWidget

class ForceActuatorGraphPageWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QHBoxLayout()
        self.plotLayout = QVBoxLayout()
        self.selectionLayout = QVBoxLayout()
        self.detailsLayout = QGridLayout()
        self.filterLayout = QHBoxLayout()
        self.layout.addLayout(self.plotLayout)
        self.layout.addLayout(self.selectionLayout)
        self.selectionLayout.addLayout(self.detailsLayout)
        self.selectionLayout.addWidget(QLabel("Filter Data"))
        self.selectionLayout.addLayout(self.filterLayout)
        self.setLayout(self.layout)

        self.selectedActuatorZIndex = -1
        self.ignoreFieldChange = False
        self.actuatorWarningData = None

        self.plot = ScatterPlotWidget(0.4, 0, 1800)
        self.plot.setFixedSize(750, 750)
        self.plot.setXScale(-4.5, 4.5)
        self.plot.setYScale(-4.5, 4.5)
        self.plot.setClicked(self.plotPointClicked)

        self.selectedActuatorIdLabel = QLabel("")
        self.selectedActuatorValueLabel = QLabel("")
        self.selectedActuatorWarningLabel = QLabel("")
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
            TopicData("Force Actuator Warning", [["Force Actuator Flags", lambda x: x.forceActuatorFlags, lambda: FATABLE_ZINDEX]]),#, ["ILC Major Fault", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX], ["Broadcast Counter Mismatch", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX]]),
        ]
        for topic in self.topics:
            self.topicList.addItem(topic.Topic)
        self.fieldList = QListWidget()
        self.fieldList.setFixedWidth(256)
        self.fieldList.itemSelectionChanged.connect(self.selectedFieldChanged)

        self.plotLayout.addWidget(self.plot)

        row = 0
        col = 0
        self.detailsLayout.addWidget(QLabel("Selected Actuator Details"), row, col)
        row += 1
        self.detailsLayout.addWidget(QLabel("Actuator Id"), row, col)
        self.detailsLayout.addWidget(self.selectedActuatorIdLabel, row, col + 1)
        row += 1
        self.detailsLayout.addWidget(QLabel("Actuator Value"), row, col)
        self.detailsLayout.addWidget(self.selectedActuatorValueLabel, row, col + 1)
        row += 1
        self.detailsLayout.addWidget(QLabel("Actuator Warning"), row, col)
        self.detailsLayout.addWidget(self.selectedActuatorWarningLabel, row, col + 1)
        row += 1
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

    def plotPointClicked(self, plot, points):
        for p in points:
            p.setPen('w', width = 4)
            x = p.pos().x()
            y = p.pos().y()
            for row in FATABLE:
                actX = row[FATABLE_XPOSITION]
                actY = row[FATABLE_YPOSITION]
                if x == actX and y == actY:
                    self.selectedActuatorZIndex = row[FATABLE_INDEX]
                    self.updateSelectedActuator()
                    break

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
        if topic.Data == None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        data = fieldGetter(topic.Data)
        points = []
        self.plot.setZScale(min(data), max(data))
        for row in FATABLE:
            index = row[fieldDataIndex]
            warning = False
            if self.actuatorWarningData is not None:
                warning = self.actuatorWarningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
            if index != -1:
                points.append([row[FATABLE_XPOSITION], row[FATABLE_YPOSITION], data[index], row[FATABLE_INDEX] == self.selectedActuatorZIndex, True, warning])
            elif row[FATABLE_INDEX] == self.selectedActuatorZIndex:
                points.append([row[FATABLE_XPOSITION], row[FATABLE_YPOSITION], 0, row[FATABLE_INDEX] == self.selectedActuatorZIndex, False, warning])
        self.plot.setPoints(points)
        self.plot.refreshPlot()
        self.updateSelectedActuator()
        lastUpdated = self.MTM1M3.getTimestamp() - topic.LastUpdated
        self.lastUpdatedLabel.setText("%0.1fs" % lastUpdated)

    def updateSelectedActuator(self):
        if self.selectedActuatorZIndex == -1:
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        topic = self.topics[topicIndex]
        field = topic.Fields[fieldIndex]
        fieldGetter = field[1]
        fieldDataIndex = field[2]()
        if topic.Data == None:
            return
        data = fieldGetter(topic.Data)
        self.selectedActuatorIdLabel.setText("%d" % FATABLE[self.selectedActuatorZIndex][FATABLE_ID])
        dataIndex = FATABLE[self.selectedActuatorZIndex][fieldDataIndex]
        if dataIndex == -1:
            self.selectedActuatorValueLabel.setText("NA")
        else:
            self.selectedActuatorValueLabel.setText("%0.1f" % data[dataIndex])
        warning = False
        if self.actuatorWarningData is not None:
            warning = self.actuatorWarningData.forceActuatorFlags[self.selectedActuatorZIndex] != 0
        QTHelpers.setWarningLabel(self.selectedActuatorWarningLabel, warning)
