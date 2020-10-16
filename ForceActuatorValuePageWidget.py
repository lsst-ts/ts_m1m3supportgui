from BitHelper import BitHelper
from FATABLE import *
from TopicData import Topics
from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QHBoxLayout,
    QListWidget,
)
from PySide2.QtCore import Slot


class ForceActuatorValuePageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm

        self.fieldDataIndex = None

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
        self.topicList.currentItemChanged.connect(self.selectedTopicChanged)
        self.topics = Topics(comm)
        for topic in self.topics.topics:
            self.topicList.addItem(topic.name)
        self.fieldList = QListWidget()
        self.fieldList.setFixedWidth(256)
        self.fieldList.currentItemChanged.connect(self.selectedFieldChanged)

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
        for i in range(9):
            self.dataLayout.addWidget(self.forceActuatorLabels[i], row, col + 2 + i)

        row += 1
        self.dataLayout.addWidget(QLabel("110"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(self.forceActuatorLabels[9 + i], row, col + 1 + i)

        row += 1
        self.dataLayout.addWidget(QLabel("120"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[19 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("130"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[29 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("140"), row, col)
        for i in range(4):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[39 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("200"), row, col)
        for i in range(3):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[43 + i], row, col + 8 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("210"), row, col)
        for i in range(9):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[46 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("220"), row, col)
        for i in range(9):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[55 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("230"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[64 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("240"), row, col)
        for i in range(4):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[74 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("300"), row, col)
        for i in range(9):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[78 + i], row, col + 2 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("310"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[87 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("320"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[97 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("330"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[107 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("340"), row, col)
        for i in range(4):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[117 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel(" "), row, col)
        row += 1
        self.dataLayout.addWidget(QLabel("400"), row, col)
        for i in range(3):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[121 + i], row, col + 8 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("410"), row, col)
        for i in range(9):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[124 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("420"), row, col)
        for i in range(9):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[133 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("430"), row, col)
        for i in range(10):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[142 + i], row, col + 1 + i
            )

        row += 1
        self.dataLayout.addWidget(QLabel("440"), row, col)
        for i in range(4):
            self.dataLayout.addWidget(
                self.forceActuatorLabels[152 + i], row, col + 1 + i
            )

        row = 0
        col = 0
        self.detailsLayout.addWidget(QLabel("Last Updated"), row, col)
        self.detailsLayout.addWidget(self.lastUpdatedLabel, row, col + 1)

        self.filterLayout.addWidget(self.topicList)
        self.topicList.setCurrentRow(0)
        self.filterLayout.addWidget(self.fieldList)

    def setPageActive(self, active):
        self.pageActive = active

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
        self.lastUpdatedLabel.setText("UNKNOWN")
        for label in self.forceActuatorLabels:
            label.setText("UNKNOWN")

    def changePlot(self, topicIndex, fieldIndex):
        topic = self.topics.topics[topicIndex]
        field = topic.fields[fieldIndex]
        self.fieldGetter = field[1]
        self.fieldDataIndex = field[2]()
        data = topic.data.get()
        if data is None:
            self.setUnknown()
            return

        self.updateData(data)
        self.topics.changeTopic(topicIndex, self.dataCallback)

    def dataCallback(self, data):
        self.updateData(data)
        if self.topics.lastCallBack is not None:
            self.topics.lastCallBack(data)

    def updateData(self, data):
        # warningData = self.dataEventForceActuatorWarning.get()
        i = -1
        for row in FATABLE:
            i += 1
            index = row[self.fieldDataIndex]
            # warning = False
            # if self.actuatorWarningData is not None:
            #    warning = self.actuatorWarningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
            if index != -1 and data is not None:
                self.forceActuatorLabels[i].setText(
                    "%0.1f" % self.fieldGetter(data)[index]
                )
            elif index != -1:
                self.forceActuatorLabels[i].setText("UNKNOWN")
            else:
                self.forceActuatorLabels[i].setText("")
