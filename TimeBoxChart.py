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

__all__ = ["TimeBoxChart"]

from PySide2.QtCore import Qt, QDateTime, QPointF, Slot
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
import time
import numpy as np

from TimeChart import AbstractChart
import VMSUnit


class TimeBoxChart(AbstractChart):
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
        self.coefficient = 1
        self.unit = VMSUnit.units[0]

    @Slot(str)
    def unitChanged(self, unit):
        delta = VMSUnit.deltas(self.unit, unit)
        for s in self.series():
            for b in s.boxSets():
                for i in range(5):
                    b.setValue(i, b.at(i) * delta)
        self.coefficient = VMSUnit.coefficients(unit)
        self.unit = unit

    def append(self, serie, timestamp, data):
        """Add data to a serie. Creates serie if needed. Shrink if
        more than expected elements are stored.

        Parameters
        ----------
        serie : `QBoxPlotSeries`
            Serie name.
        timestamp : `float`
            Values timestamp.
        data : [float]
            Serie data."""

        if serie.count() > self.maxItems - 1:
            for r in range(serie.count() - self.maxItems + 1):
                serie.remove(serie.boxSets()[0])

        quantiles = np.quantile(data, [0, 0.25, 0.5, 0.75, 1]) * self.coefficient
        boxSet = QtCharts.QBoxSet(
            *quantiles,
            f"{time.localtime(timestamp).tm_sec:02d}.{int((timestamp - np.floor(timestamp)) * 1000)}",
        )

        serie.append(boxSet)

        d_min = d_max = 0
        for s in self.series():
            bs = s.boxSets()
            if len(bs) > 0:
                d_min = min(
                    d_min, min([b.at(QtCharts.QBoxSet.LowerExtreme) for b in bs])
                )
                d_max = max(
                    d_max, max([b.at(QtCharts.QBoxSet.UpperExtreme) for b in bs])
                )

        self.createDefaultAxes()
        r = abs(d_max - d_min)
        self.axes(Qt.Vertical)[0].setRange(d_min - 0.02 * r, d_max + r * 0.02)
