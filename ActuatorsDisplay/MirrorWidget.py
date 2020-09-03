from PySide2.QtWidgets import QWidget, QHBoxLayout

from . import MirrorView, Gauge


class MirrorWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.mirrorView = MirrorView()
        self.gauge = Gauge()

        layout = QHBoxLayout()
        layout.addWidget(self.mirrorView)
        layout.addWidget(self.gauge)

        self.setLayout(layout)

    def setRange(self, min, max):
        self.mirrorView.setRange(min, max)
        self.gauge.setRange(min, max)
