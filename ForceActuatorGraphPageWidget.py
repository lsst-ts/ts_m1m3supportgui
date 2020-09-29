
import QTHelpers
import TimeChart
from DataCache import DataCache
from BitHelper import BitHelper
from FATABLE import *
from TopicData import TopicData
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget
from ActuatorsDisplay import MirrorWidget, Actuator

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

        self.ignoreFieldChange = False

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
            TopicData("Pre-clipped Aberration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Pre-clipped Acceleration Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Active Optic Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]]),
            TopicData("Pre-clipped Azimuth Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Balance Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Cylinder Forces", [["Primary Cylinder Forces", lambda x: [i / 1000.0 for i in x.primaryCylinderForces], lambda: FATABLE_ZINDEX], ["Secondary Cylinder Forces", lambda x: [i / 1000.0 for i in x.secondaryCylinderForces], lambda: FATABLE_SINDEX]]),
            TopicData("Pre-clipped Elevation Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Offset Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Static Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Thermal Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Pre-clipped Velocity Forces", [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX], ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX], ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX]]),
            TopicData("Force Actuator Backup Calibration Info", [["Primary Coefficient", lambda x: x.primaryCoefficient, lambda: FATABLE_ZINDEX], ["Primary Offset", lambda x: x.primaryOffset, lambda: FATABLE_ZINDEX], ["Primary Sensitivity", lambda x: x.primarySensitivity, lambda: FATABLE_ZINDEX], ["Secondary Coefficient", lambda x: x.secondaryCoefficient, lambda: FATABLE_SINDEX], ["Secondary Offset", lambda x: x.secondaryOffset, lambda: FATABLE_SINDEX], ["Secondary Sensitivity", lambda x: x.secondarySensitivity, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator ILC Info", [["Subnet", lambda x: x.modbusSubnet, lambda: FATABLE_ZINDEX], ["Address", lambda x: x.modbusAddress, lambda: FATABLE_ZINDEX], ["ILC Status", lambda x: x.ilcStatus, lambda: FATABLE_ZINDEX], ["Mezzanine Status", lambda x: x.mezzanineStatus, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Id Info", [["X Data Reference Id", lambda x: x.xDataReferenceId, lambda: FATABLE_XINDEX], ["Y Data Reference Id", lambda x: x.yDataReferenceId, lambda: FATABLE_YINDEX], ["Z Data Reference Id", lambda x: x.zDataReferenceId, lambda: FATABLE_ZINDEX], ["S Data Reference Id", lambda x: x.sDataReferenceId, lambda: FATABLE_SINDEX], ["ILC Unique Id", lambda x: x.ilcUniqueId, lambda: FATABLE_ZINDEX], ["Mezzanine Unique Id", lambda x: x.xDataReferenceId, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Main Calibration Info", [["Primary Coefficient", lambda x: x.primaryCoefficient, lambda: FATABLE_ZINDEX], ["Primary Offset", lambda x: x.primaryOffset, lambda: FATABLE_ZINDEX], ["Primary Sensitivity", lambda x: x.primarySensitivity, lambda: FATABLE_ZINDEX], ["Secondary Coefficient", lambda x: x.secondaryCoefficient, lambda: FATABLE_SINDEX], ["Secondary Offset", lambda x: x.secondaryOffset, lambda: FATABLE_SINDEX], ["Secondary Sensitivity", lambda x: x.secondarySensitivity, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator Mezzanine Calibration Info", [["Primary Cylinder Gain", lambda x: x.primaryCylinderGain, lambda: FATABLE_ZINDEX], ["Secondary Cylinder Gain", lambda x: x.secondaryCylinderGain, lambda: FATABLE_SINDEX]]),
            TopicData("Force Actuator Position Info", [["Actuator Type", lambda x: x.actuatorType, lambda: FATABLE_ZINDEX], ["Actuator Orientation", lambda x: x.actuatorOrientation, lambda: FATABLE_ZINDEX], ["X Position", lambda x: x.xPosition, lambda: FATABLE_ZINDEX], ["Y Position", lambda x: x.yPosition, lambda: FATABLE_ZINDEX], ["Z Position", lambda x: x.zPosition, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator State", [["ILC State", lambda x: x.ilcState, lambda: FATABLE_ZINDEX]]),
            TopicData("Force Actuator Warning", [["Force Actuator Flags", lambda x: x.forceActuatorFlags, lambda: FATABLE_ZINDEX]]),#, ["ILC Major Fault", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX], ["Broadcast Counter Mismatch", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX]]),
        ]
        for topic in self.topics:
            self.topicList.addItem(topic.Topic)
        self.fieldList = QListWidget()
        self.fieldList.setFixedWidth(256)
        self.fieldList.itemSelectionChanged.connect(self.selectedFieldChanged)

        self.mirrorWidget = MirrorWidget()
        self.mirrorWidget.mirrorView.selectionChanged.connect(self.updateSelectedActuator)
        self.plotLayout.addWidget(self.mirrorWidget)

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

        self.dataEventAppliedAberrationForces = DataCache()
        self.dataEventAppliedAccelerationForces = DataCache()
        self.dataEventAppliedActiveOpticForces = DataCache()
        self.dataEventAppliedAzimuthForces = DataCache()
        self.dataEventAppliedBalanceForces = DataCache()
        self.dataEventAppliedCylinderForces = DataCache()
        self.dataEventAppliedElevationForces = DataCache()
        self.dataEventAppliedForces = DataCache()
        self.dataEventAppliedOffsetForces = DataCache()
        self.dataEventAppliedStaticForces = DataCache()
        self.dataEventAppliedThermalForces = DataCache()
        self.dataEventAppliedVelocityForces = DataCache()
        self.dataEventForceActuatorInfo = DataCache()
        self.dataEventForceActuatorState = DataCache()
        self.dataEventForceActuatorWarning = DataCache()
        self.dataEventPreclippedAberrationForces = DataCache()
        self.dataEventPreclippedAccelerationForces = DataCache()
        self.dataEventPreclippedActiveOpticForces = DataCache()
        self.dataEventPreclippedAzimuthForces = DataCache()
        self.dataEventPreclippedBalanceForces = DataCache()
        self.dataEventPreclippedCylinderForces = DataCache()
        self.dataEventPreclippedElevationForces = DataCache()
        self.dataEventPreclippedForces = DataCache()
        self.dataEventPreclippedOffsetForces = DataCache()
        self.dataEventPreclippedStaticForces = DataCache()
        self.dataEventPreclippedThermalForces = DataCache()
        self.dataEventPreclippedVelocityForces = DataCache()

        self.setTopicData("Applied Aberration Forces", self.dataEventAppliedAberrationForces)
        self.setTopicData("Applied Acceleration Forces", self.dataEventAppliedAccelerationForces)
        self.setTopicData("Applied Active Optic Forces", self.dataEventAppliedActiveOpticForces)
        self.setTopicData("Applied Azimuth Forces", self.dataEventAppliedAzimuthForces)
        self.setTopicData("Applied Balance Forces", self.dataEventAppliedBalanceForces)
        self.setTopicData("Applied Cylinder Forces", self.dataEventAppliedCylinderForces)
        self.setTopicData("Applied Elevation Forces", self.dataEventAppliedElevationForces)
        self.setTopicData("Applied Forces", self.dataEventAppliedForces)
        self.setTopicData("Applied Offset Forces", self.dataEventAppliedOffsetForces)
        self.setTopicData("Applied Static Forces", self.dataEventAppliedStaticForces)
        self.setTopicData("Applied Thermal Forces", self.dataEventAppliedThermalForces)
        self.setTopicData("Applied Velocity Forces", self.dataEventAppliedVelocityForces)
        self.setTopicData("Force Actuator Info", self.dataEventForceActuatorInfo)
        self.setTopicData("Force Actuator State", self.dataEventForceActuatorState)
        self.setTopicData("Force Actuator Warning", self.dataEventForceActuatorWarning)
        self.setTopicData("Pre-clipped Aberration Forces", self.dataEventPreclippedAberrationForces)
        self.setTopicData("Pre-clipped Acceleration Forces", self.dataEventPreclippedAccelerationForces)
        self.setTopicData("Pre-clipped Active Optic Forces", self.dataEventPreclippedActiveOpticForces)
        self.setTopicData("Pre-clipped Azimuth Forces", self.dataEventPreclippedAzimuthForces)
        self.setTopicData("Pre-clipped Balance Forces", self.dataEventPreclippedBalanceForces)
        self.setTopicData("Pre-clipped Cylinder Forces", self.dataEventPreclippedCylinderForces)
        self.setTopicData("Pre-clipped Elevation Forces", self.dataEventPreclippedElevationForces)
        self.setTopicData("Pre-clipped Forces", self.dataEventPreclippedForces)
        self.setTopicData("Pre-clipped Offset Forces", self.dataEventPreclippedOffsetForces)
        self.setTopicData("Pre-clipped Static Forces", self.dataEventPreclippedStaticForces)
        self.setTopicData("Pre-clipped Thermal Forces", self.dataEventPreclippedThermalForces)
        self.setTopicData("Pre-clipped Velocity Forces", self.dataEventPreclippedVelocityForces)

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

        self.MTM1M3.subscribeEvent_forceActuatorInfo(self.processEventForceActuatorInfo)
        self.MTM1M3.subscribeEvent_forceActuatorState(self.processEventForceActuatorState)
        self.MTM1M3.subscribeEvent_forceActuatorWarning(self.processEventForceActuatorWarning)

        self.MTM1M3.subscribeEvent_preclippedAberrationForces(self.processEventPreclippedAberrationForces)
        self.MTM1M3.subscribeEvent_preclippedAccelerationForces(self.processEventPreclippedAccelerationForces)
        self.MTM1M3.subscribeEvent_preclippedActiveOpticForces(self.processEventPreclippedActiveOpticForces)
        self.MTM1M3.subscribeEvent_preclippedAzimuthForces(self.processEventPreclippedAzimuthForces)
        self.MTM1M3.subscribeEvent_preclippedBalanceForces(self.processEventPreclippedBalanceForces)
        self.MTM1M3.subscribeEvent_preclippedCylinderForces(self.processEventPreclippedCylinderForces)
        self.MTM1M3.subscribeEvent_preclippedElevationForces(self.processEventPreclippedElevationForces)
        self.MTM1M3.subscribeEvent_preclippedForces(self.processEventPreclippedForces)
        self.MTM1M3.subscribeEvent_preclippedOffsetForces(self.processEventPreclippedOffsetForces)
        self.MTM1M3.subscribeEvent_preclippedStaticForces(self.processEventPreclippedStaticForces)
        self.MTM1M3.subscribeEvent_preclippedThermalForces(self.processEventPreclippedThermalForces)
        self.MTM1M3.subscribeEvent_preclippedVelocityForces(self.processEventPreclippedVelocityForces)

    def setPageActive(self, active):
        self.pageActive = active
        if active:
            self.updatePlot(True)

    def updatePage(self):
        if not self.pageActive:
            return

        for i in range(len(self.topics)):
            if self.topicList.currentRow() == i:
                topic = self.topics[i]
                if topic.Data.hasBeenUpdated() or self.dataEventForceActuatorWarning.hasBeenUpdated():
                    self.updatePlot()
                self.updateLastUpdated()

    def processEventAppliedAberrationForces(self, data):
        self.dataEventAppliedAberrationForces.set(data[-1])

    def processEventAppliedAccelerationForces(self, data):
        self.dataEventAppliedAccelerationForces.set(data[-1])

    def processEventAppliedActiveOpticForces(self, data):
        self.dataEventAppliedActiveOpticForces.set(data[-1])
    
    def processEventAppliedAzimuthForces(self, data):
        self.dataEventAppliedAzimuthForces.set(data[-1])

    def processEventAppliedBalanceForces(self, data):
        self.dataEventAppliedBalanceForces.set(data[-1])

    def processEventAppliedCylinderForces(self, data):
        self.dataEventAppliedCylinderForces.set(data[-1])

    def processEventAppliedElevationForces(self, data):
        self.dataEventAppliedElevationForces.set(data[-1])

    def processEventAppliedForces(self, data):
        self.dataEventAppliedForces.set(data[-1])

    def processEventAppliedOffsetForces(self, data):
        self.dataEventAppliedOffsetForces.set(data[-1])

    def processEventAppliedStaticForces(self, data):
        self.dataEventAppliedStaticForces.set(data[-1])

    def processEventAppliedThermalForces(self, data):
        self.dataEventAppliedThermalForces.set(data[-1])

    def processEventAppliedVelocityForces(self, data):
        self.dataEventAppliedVelocityForces.set(data[-1])

    def processEventForceActuatorInfo(self, data):
        self.dataEventForceActuatorInfo.set(data[-1])

    def processEventForceActuatorState(self, data):
        self.dataEventForceActuatorState.set(data[-1])

    def processEventForceActuatorWarning(self, data):
        self.dataEventForceActuatorWarning.set(data[-1])

    def processEventPreclippedAberrationForces(self, data):
        self.dataEventPreclippedAberrationForces.set(data[-1])

    def processEventPreclippedAccelerationForces(self, data):
        self.dataEventPreclippedAccelerationForces.set(data[-1])

    def processEventPreclippedActiveOpticForces(self, data):
        self.dataEventPreclippedActiveOpticForces.set(data[-1])
    
    def processEventPreclippedAzimuthForces(self, data):
        self.dataEventPreclippedAzimuthForces.set(data[-1])

    def processEventPreclippedBalanceForces(self, data):
        self.dataEventPreclippedBalanceForces.set(data[-1])

    def processEventPreclippedCylinderForces(self, data):
        self.dataEventPreclippedCylinderForces.set(data[-1])

    def processEventPreclippedElevationForces(self, data):
        self.dataEventPreclippedElevationForces.set(data[-1])

    def processEventPreclippedForces(self, data):
        self.dataEventPreclippedForces.set(data[-1])

    def processEventPreclippedOffsetForces(self, data):
        self.dataEventPreclippedOffsetForces.set(data[-1])

    def processEventPreclippedStaticForces(self, data):
        self.dataEventPreclippedStaticForces.set(data[-1])

    def processEventPreclippedThermalForces(self, data):
        self.dataEventPreclippedThermalForces.set(data[-1])

    def processEventPreclippedVelocityForces(self, data):
        self.dataEventPreclippedVelocityForces.set(data[-1])

    def selectedTopicChanged(self):
        topicIndex = self.topicList.currentRow()
        if topicIndex < 0:
            return
        self.ignoreFieldChange = True
        self.fieldList.clear()
        for field in self.topics[topicIndex].Fields:
            self.fieldList.addItem(field[0])
        self.fieldList.setCurrentRow(self.topics[topicIndex].SelectedField) 

    def selectedFieldChanged(self):
        if self.ignoreFieldChange:
            self.ignoreFieldChange = False
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            return
        self.topics[topicIndex].SelectedField = fieldIndex
        self.updatePlot(True)

    def updatePlot(self, redraw = False):
        """Update plot. Redraw plot if new set is selected.

        Paramaters
        ----------

        redraw : `boolean`
             If true, actuator list is cleared and then constructed from available data. Forces plot redraw.
        """
        if not self.pageActive:
            return
        if redraw:
            self.mirrorWidget.mirrorView.clear()
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        topic = self.topics[topicIndex]
        field = topic.Fields[fieldIndex]
        fieldGetter = field[1]
        fieldDataIndex = field[2]()
        topicData = topic.Data.get()
        if topicData is None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        data = fieldGetter(topicData)
        warningData = self.dataEventForceActuatorWarning.get()
        points = []
        for row in FATABLE:
            id = row[FATABLE_ID]
            index = row[fieldDataIndex]
            if index < 0:
                state = Actuator.STATE_INACTIVE
            elif warningData is not None:
                state = Actuator.STATE_WARNING if warningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0 else Actuator.STATE_ACTIVE
            else:
                state = Actuator.STATE_ACTIVE
            if redraw:
                self.mirrorWidget.mirrorView.addActuator(id, row[FATABLE_XPOSITION] * 1000, row[FATABLE_YPOSITION] * 1000, data[index], state)
            else:
                try:
                    self.mirrorWidget.mirrorView.updateActuator(id, data[index], state)
                except KeyError:
                    # for the case when list is empty..we need to scale then..
                    self.mirrorWidget.mirrorView.addActuator(id, row[FATABLE_XPOSITION] * 1000, row[FATABLE_YPOSITION] * 1000, data[index], state)
                    redraw = True
        self.mirrorWidget.setRange(min(data), max(data))
        if redraw:
            self.mirrorWidget.mirrorView.resetTransform()
            self.mirrorWidget.mirrorView.scale(*self.mirrorWidget.mirrorView.scaleHints())

    def updateSelectedActuator(self, s):
        if s is None:
            self.selectedActuatorIdLabel.setText('not selected')
            self.selectedActuatorValueLabel.setText('')
            self.selectedActuatorWarningLabel.setText('')
            return

        self.selectedActuatorIdLabel.setText(str(s.id))
        self.selectedActuatorValueLabel.setText(str(s.data))
        QTHelpers.setWarningLabel(self.selectedActuatorWarningLabel, s.warning)

    def updateLastUpdated(self):
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        topic = self.topics[topicIndex]
        topicData = topic.Data.get()
        if topicData is None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        self.lastUpdatedLabel.setText("%0.1fs" % topic.Data.getTimeSinceLastUpdate())

    def setTopicData(self, topic, data):
        for i in self.topics:
            if i.Topic == topic:
                i.Data = data
                break
