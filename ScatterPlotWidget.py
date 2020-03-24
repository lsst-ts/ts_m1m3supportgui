
import QTHelpers
from BitHelper import BitHelper
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from pyqtgraph.Qt import QtGui, QtCore, QT_LIB

class ScatterPlotWidget(QWidget):
    def __init__(self, pointSize, minValue, maxValue):
        QWidget.__init__(self)
        self.pointSize = pointSize
        self.minValue = minValue
        self.maxValue = maxValue

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.plot = pg.PlotWidget()
        self.scatterItem = pg.ScatterPlotItem(pxMode=False)
        self.plot.addItem(self.scatterItem)
        self.points = []
        self.values = []

        self.layout.addWidget(self.plot)

    def setPointSize(self, pointSize):
        self.pointSize = pointSize

    def setZScale(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def setPoints(self, points):
        self.values = points

    def setXScale(self, minValue, maxValue):
        self.plot.setRange(xRange = (minValue, maxValue))

    def setYScale(self, minValue, maxValue):
        self.plot.setRange(yRange = (minValue, maxValue))

    def setClicked(self, action):
        self.scatterItem.sigClicked.connect(action)

    def refreshPlot(self):
        self.points = []
        for point in self.values:
            penColor = 'k'
            penWidth = 1
            if point[5]:
                penColor = 'r'
                penWidth = 4
            if point[3]:
                penColor = 'w'
                penWidth = 4
            if point[4]:
                self.points.append({
                    'pos': (point[0], point[1]),
                    'size': self.pointSize,
                    'pen': {'color': penColor, 'width': penWidth},
                    'brush': QTHelpers.getGradientColor(self.minValue, self.maxValue, point[2])})
            else:
                self.points.append({
                    'pos': (point[0], point[1]),
                    'size': self.pointSize,
                    'pen': {'color': penColor, 'width': penWidth},
                    'brush': 'k'})
        self.scatterItem.clear()
        self.scatterItem.addPoints(self.points)
