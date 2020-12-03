from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedLayout,
    QListWidget,
)


class ApplicationPaginationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.listLayout = QVBoxLayout()
        self.pageLayout = QStackedLayout()
        self.layout.addLayout(self.listLayout)
        self.layout.addLayout(self.pageLayout)
        self.setLayout(self.layout)

        self.pageList = QListWidget()
        self.pageList.currentRowChanged.connect(self.changePage)
        self.listLayout.addWidget(self.pageList)

    def setPageListWidth(self, width):
        self.pageList.setFixedWidth(width)

    def addPage(self, text, widget):
        widget.setPageActive(False)
        self.pageList.addItem(text)
        self.pageLayout.addWidget(widget)
        if self.pageLayout.count() == 1:
            self.pageList.setCurrentRow(0)

    def changePage(self, row):
        if row < 0:
            return
        current = self.pageLayout.currentWidget()
        if current is not None:
            current.setPageActive(False)
        newActive = self.pageLayout.widget(row)
        self.pageLayout.setCurrentWidget(newActive)
        newActive.setPageActive(True)
