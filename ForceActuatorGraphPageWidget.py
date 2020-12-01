import QTHelpers
import copy
from FATABLE import *
from TopicData import Topics
from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QListWidget,
)
from ActuatorsDisplay import MirrorWidget, Actuator
from TimeDeltaLabel import TimeDeltaLabel


class ForceActuatorGraphPageWidget(QWidget):
    """
    Draw distribution of force actuators, and selected value. Intercept events callbacks to trigger updates.
    """

    def __init__(self, comm):
        super().__init__()
        self.comm = comm
        self.pageActive = False

        self.fieldDataIndex = None

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
        self.lastUpdatedLabel = TimeDeltaLabel()

        self.topicList = QListWidget()
        self.topicList.setFixedWidth(256)
        self.topicList.currentItemChanged.connect(self.selectedTopicChanged)
        self.topics = Topics(comm)
        for topic in self.topics.topics:
            self.topicList.addItem(topic.name)
        self.fieldList = QListWidget()
        self.fieldList.setFixedWidth(256)
        self.fieldList.currentItemChanged.connect(self.selectedFieldChanged)

        self.mirrorWidget = MirrorWidget()
        self.mirrorWidget.mirrorView.selectionChanged.connect(
            self.updateSelectedActuator
        )
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
        if not (active):
            self.topics.changeTopic(None, None)

    def selectedTopicChanged(self, current, previous):
        topicIndex = self.topicList.currentRow()
        if topicIndex < 0:
            self.setUnknown()
            return

        self.fieldList.clear()
        for field in self.topics.topics[topicIndex].fields:
            self.fieldList.addItem(field[0])

        fieldIndex = self.topics.topics[topicIndex].selectedField
        if fieldIndex < 0:
            self.setUnknown()
            return

        self.fieldList.setCurrentRow(fieldIndex)
        self.changePlot(topicIndex, fieldIndex)

    def selectedFieldChanged(self, current, previous):
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            self.setUnknown()
            return
        self.changePlot(topicIndex, fieldIndex)
        self.topics.topics[topicIndex].selectedField = fieldIndex

    def setUnknown(self):
        self.lastUpdatedLabel.setUnknown()

    def changePlot(self, topicIndex, fieldIndex):
        """
        Redraw actuators with values.
        """
        topic = self.topics.topics[topicIndex]
        field = topic.fields[fieldIndex]
        self.fieldGetter = field[1]
        self.fieldDataIndex = field[2]()
        try:
            data = topic.data.get()
            if data is None:
                self.setUnknown()
                return

            self.updateData(data)
            self.topics.changeTopic(topicIndex, self.dataCallback)
        except RuntimeError as err:
            print(err)
            pass

    def dataCallback(self, data):
        self.updateData(data)
        if self.topics.lastCallBack is not None:
            self.topics.lastCallBack(data)

    def updateData(self, data):
        warningData = self.comm.MTM1M3.evt_forceActuatorWarning.get()
        points = []
        values = self.fieldGetter(data)

        self.mirrorWidget.mirrorView.clear()

        for row in FATABLE:
            id = row[FATABLE_ID]
            index = row[self.fieldDataIndex]
            if index is None:
                state = Actuator.STATE_INACTIVE
            elif warningData is not None:
                state = (
                    Actuator.STATE_WARNING
                    if warningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
                    else Actuator.STATE_ACTIVE
                )
            else:
                state = Actuator.STATE_ACTIVE

            self.mirrorWidget.mirrorView.addActuator(
                id,
                row[FATABLE_XPOSITION] * 1000,
                row[FATABLE_YPOSITION] * 1000,
                None if index is None else values[index],
                index,
                state,
            )
        self.mirrorWidget.setRange(min(values), max(values))
        self.mirrorWidget.mirrorView.resetTransform()
        self.mirrorWidget.mirrorView.scale(*self.mirrorWidget.mirrorView.scaleHints())

        if (
            self.mirrorWidget.mirrorView.selected is not None
            and self.mirrorWidget.mirrorView.selected.dataIndex is not None
        ):
            self.selectedActuatorValueLabel.setText(
                str(values[self.mirrorWidget.mirrorView.selected.dataIndex])
            )
        self.lastUpdatedLabel.setTime(data.timestamp)

    def updateSelectedActuator(self, s):
        if s is None:
            self.selectedActuatorIdLabel.setText("not selected")
            self.selectedActuatorValueLabel.setText("")
            self.selectedActuatorWarningLabel.setText("")
            return

        self.selectedActuatorIdLabel.setText(str(s.id))
        self.selectedActuatorValueLabel.setText(str(s.data))
        QTHelpers.setWarningLabel(self.selectedActuatorWarningLabel, s.warning)
