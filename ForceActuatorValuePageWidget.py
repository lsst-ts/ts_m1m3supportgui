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
from lsst.ts.salobj import current_tai


class ForceActuatorValuePageWidget(QWidget):
    def __init__(self, comm):
        super().__init__()
        self.comm = comm

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
        self.topics = Topics(comm)
        for topic in self.topics.topics:
            self.topicList.addItem(topic.name)
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
        if not self.pageActive:
            return
        topicIndex = self.topicList.currentRow()
        fieldIndex = self.fieldList.currentRow()
        if topicIndex < 0 or fieldIndex < 0:
            self.lastUpdatedLabel.setText("UNKNOWN")
            for label in self.forceActuatorLabels:
                label.setText("UNKNOWN")
            return
        topic = self.topics.topics[topicIndex]
        field = topic.fields[fieldIndex]
        fieldGetter = field[1]
        fieldDataIndex = field[2]()
        topicData = topic.data.get()
        if topicData is None:
            self.lastUpdatedLabel.setText("UNKNOWN")
            for label in self.forceActuatorLabels:
                label.setText("UNKNOWN")
            return
        data = fieldGetter(topicData)
        # warningData = self.dataEventForceActuatorWarning.get()
        i = -1
        for row in FATABLE:
            i += 1
            dataIndex = row[fieldDataIndex]
            # warning = False
            # if self.actuatorWarningData is not None:
            #    warning = self.actuatorWarningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
            if dataIndex != -1 and data is not None:
                self.forceActuatorLabels[i].setText("%0.1f" % data[dataIndex])
            elif dataIndex != -1:
                self.forceActuatorLabels[i].setText("UNKNOWN")
            else:
                self.forceActuatorLabels[i].setText("")

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
        self.lastUpdatedLabel.setText(
            "%0.1fs" % current_tai() - topic.data.get().timestamp
        )
