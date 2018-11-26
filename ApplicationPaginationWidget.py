
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QListWidget

class ApplicationPaginationWidget(QWidget):
    def __init__(self, MTM1M3):
        QWidget.__init__(self)
        self.MTM1M3 = MTM1M3
        self.layout = QHBoxLayout()
        self.listLayout = QVBoxLayout()
        self.pageLayout = QStackedLayout()
        self.layout.addLayout(self.listLayout)
        self.layout.addLayout(self.pageLayout)
        self.setLayout(self.layout)

        self.pageList = QListWidget()
        self.pageList.itemSelectionChanged.connect(self.changePage)
        self.listLayout.addWidget(self.pageList)
        self.pages = []

    def setPageListWidth(self, width):
        self.pageList.setFixedWidth(width)

    def addPage(self, text, widget):
        self.pages.append([text, widget])
        self.pageList.addItem(text)
        self.pageLayout.addWidget(widget)

    def changePage(self):
        items = self.pageList.selectedItems()
        if len(items) > 0:
            text = items[0].text()
            for pages in self.pages:
                if pages[0] == text:
                    self.pageLayout.setCurrentWidget(pages[1])
                    #pageActive = getattr(pages[1], "setPageActive", None)
                    #if callable(pageActive):
                    #    pageActive(self.path.parent_op)