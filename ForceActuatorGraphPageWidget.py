import QTHelpers
import TimeChart
from BitHelper import BitHelper
from FATABLE import *
from TopicData import Topics
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QListWidget
from ActuatorsDisplay import MirrorWidget, Actuator
from lsst.ts.salobj import current_tai

class ForceActuatorGraphPageWidget(QWidget):
    """
    Draw distribution of force actuators, and selected value. Intercept events callbacks to trigger updates.
    """
    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.pageActive = False

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
        self.topics = Topics(comm)
        for topic in self.topics.topics:
            self.topicList.addItem(topic.name)
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

    def setPageActive(self, active):
        self.pageActive = active
        if active:
            self.updatePlot()

    def selectedTopicChanged(self):
        topicIndex = self.topicList.currentRow()
        if topicIndex < 0:
            return
        self.ignoreFieldChange = True
        self.fieldList.clear()
        for field in self.topics.topics[topicIndex].fields:
            self.fieldList.addItem(field[0])
        self.fieldList.setCurrentRow(self.topics.topics[topicIndex].selectedField) 

    def selectedFieldChanged(self):
        if self.ignoreFieldChange:
            self.ignoreFieldChange = False
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            return
        self.topics.topics[topicIndex].selectedField = fieldIndex
        self.updatePlot()

    def updatePlot(self):
        """
        Redraw actuators with values.
        """
        if not self.pageActive:
            return

        self.mirrorWidget.mirrorView.clear()

        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        topic = self.topics.topics[topicIndex]
        field = topic.fields[fieldIndex]
        fieldGetter = field[1]
        fieldDataIndex = field[2]()
        topicData = topic.data.get()
        if topicData is None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        data = fieldGetter(topicData)
        warningData = self.comm.MTM1M3.evt_forceActuatorWarning.get()
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

            self.mirrorWidget.mirrorView.addActuator(id, row[FATABLE_XPOSITION] * 1000, row[FATABLE_YPOSITION] * 1000, data[index], state)
            #else:
            #    try:
            #        self.mirrorWidget.mirrorView.updateActuator(id, data[index], state)
            #    except KeyError:
            #        # for the case when list is empty..we need to scale then..
            #        self.mirrorWidget.mirrorView.addActuator(id, row[FATABLE_XPOSITION] * 1000, row[FATABLE_YPOSITION] * 1000, data[index], state)
            #        redraw = True
        self.mirrorWidget.setRange(min(data), max(data))
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
        topic = self.topics.topics[topicIndex]
        topicData = topic.data.get()
        if topicData is None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            return
        self.lastUpdatedLabel.setText("%0.1fs" % (current_tai() - topic.data.timestamp))
