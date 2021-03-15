# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https: //www.lsst.org).
# See the COPYRIGHT file at the top - level directory of this distribution
# for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.If not, see < https:  // www.gnu.org/licenses/>.

from PySide2.QtCore import Qt, QDateTime, QPointF
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
import time
import numpy as np


__all__ = ["TimeBoxChart", "TimeChartView"]


class TimeBoxChart(QtCharts.QChart):
    """Class with time axis and value(s). Keeps last n/dt items. Holds axis
    titles and series, and handle axis auto scaling. Plots multiple values
    passed in append method as box charts with upper/lower extremes and
    quantiles and median value marked.

    Data to the graph shall be added with the append method. The class does the
    rest, creates axis/series and autoscale them as needed.

    Parameters
    ----------

    maxItems : `int`, optional
        Number of items to keep in graph. When series grows above the specified
        number of points, oldest points are removed. Defaults to 50 * 30 = 50Hz * 30s.
    """

    def __init__(self, maxItems=10):
        super().__init__()
        self.maxItems = maxItems

        self._storedSeries = {}

    def _findSerie(self, axis, serie):
        """
        Returns serie with given name.
        """
        return self._storedSeries[axis][serie]

    def _addSerie(self, axis, serie):
        s = QtCharts.QBoxPlotSeries()
        s.setName(serie)
        try:
            self._storedSeries[axis][serie] = s
        except KeyError:
            self._storedSeries[axis] = {serie: s}
        return s

    def append(self, timestamp, series):
        """Add data to a serie. Creates axis and serie if needed. Shrink if
        more than expected elements are stored.

        Parameters
        ----------
        timestamp : `float`
            Values timestamp.
        series : [(`str`, `str`, data)]
            Axis name, serie name and data. Serie name will be shown as data
            label. Data is an array of one box values."""

        for d in series:
            axis, serie, data = d
            try:
                s = self._findSerie(axis, serie)
            except KeyError:
                s = self._addSerie(axis, serie)
                self.addSeries(s)

            if s.count() > self.maxItems - 1:
                for r in range(s.count() - self.maxItems + 1):
                    s.remove(s.boxSets()[0])

            quantiles = np.quantile(data, [0, 0.25, 0.5, 0.75, 1])
            boxSet = QtCharts.QBoxSet(
                *quantiles,
                f"{time.localtime(timestamp).tm_sec:02d}.{int((timestamp - np.floor(timestamp)) * 1000)}",
            )

            s.append(boxSet)

        self.createDefaultAxes()
        self.axes(Qt.Vertical)[0].setRange(-0.01, 0.01)

    def clearData(self):
        """Removes all data from the chart."""
        self._storedSeries = {}
        super().removeAllSeries()
        for a in self.axes(Qt.Vertical):
            self.removeAxis(a)
