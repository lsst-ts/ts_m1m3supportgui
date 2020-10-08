# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import Qt, QDateTime
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts

__all__ = ["TimeChart", "TimeChartView"]


class TimeChart(QtCharts.QChart):
    """Class with time axis and value(s). Keeps last n/dt items. Holds axis
    titles and series, and handle axis auto scaling.

    Data to the graph shall be added with the append method. The class does the
    rest, creates axis/series and autoscale them as needed.

    Parameters
    ----------

    maxItems : `int`, optional
        Number of items to keep in graph. When series grows above the specified
        number of points, oldest points are removed. Defaults to 50 * 30 = 50Hz * 30s
    redrawAfter : `int`, optional
        Redraw axis after adding this number of points.
    """

    def __init__(self, maxItems=50*30, redrawAfter = 50):
        super().__init__()
        self.maxItems = maxItems
        self.timeAxis = QtCharts.QDateTimeAxis()
        self.timeAxis.setReverse(True)
        self.timeAxis.setTickCount(10)
        self.timeAxis.setTitleText("Time (UTC)")
        self.timeAxis.setFormat("h:mm:ss.zzz")

        self._storedSeries = {}
        self._redrawAfter = redrawAfter
        self._appendCount = 0

    def _findSerie(self, axis, serie):
        """
        Returns serie with given name.
        """
        return self._storedSeries[axis][0], self._storedSeries[axis][1][serie]

    def _addSerie(self, axis, serie):
        s = QtCharts.QLineSeries()
        s.setName(serie)
        try:
            self._storedSeries[axis][1][serie] = s
            a = self._storedSeries[axis][0]
        except KeyError:
            a = QtCharts.QValueAxis()
            a.setTickCount(10)
            a.setTitleText(axis)
            self.addAxis(
                a, Qt.AlignRight if len(self._storedSeries) % 2 else Qt.AlignLeft
            )
            if len(self._storedSeries) == 0:
                self.addAxis(self.timeAxis, Qt.AlignBottom)
            self._storedSeries[axis] = (a, {serie: s})
        return a, s

    def autoRange(self, axis, yClip=0.05):
        a = self._storedSeries[axis][0]
        t_range = [None] * 2
        y_range = [None] * 2
        for s in self._storedSeries[axis][1].values():
            points = s.pointsVector()
            if len(points) == 0:
                continue

            if t_range[0] is None:
                t_range = [points[0].x()] * 2
                y_range = [points[0].y()] * 2
                points = points[1:]

            for p in points:
                x = p.x()
                t_range = [min(x, t_range[0]), max(x, t_range[1])]
                y = p.y()
                y_range = [min(y, y_range[0]), max(y, y_range[1])]

        self.timeAxis.setRange(
            *(map(lambda i: QDateTime().fromMSecsSinceEpoch(i), t_range))
        )

        if y_range[0] == y_range[1]:
            clip = 1.5
        else:
            clip = (y_range[1] - y_range[0]) * yClip
        y_range = [y_range[0] - clip, y_range[1] + clip]
        a.setRange(*y_range)

    def append(self, axis, serie, data, forceUpdate=False):
        """Add data to a serie. Creates axis and serie if needed.

        Parameters
        ----------
        axis : `str`
            Asis label. This will be visible on right/left graph side
        serie : `str`
            Serie name. Will be shown as data label.
        data : matrix
            Float matrix 2xn. First element is timestamp, second is the value.
        forceUpdate : `bool`
            Force graph redraw.
        """

        self._appendCount += len(data)

        if self._appendCount >= self._redrawAfter:
            self._appendCount = 0
            forceUpdate = True

        try:
            a, s = self._findSerie(axis, serie)
            if forceUpdate:
                s.detachAxis(self.timeAxis)
                s.detachAxis(a)
                self.removeSeries(s)
        except KeyError:
            a, s = self._addSerie(axis, serie)
            forceUpdate = True

        for (i, d) in data:
            s.append(i * 1000.0, d)

        if s.count() > self.maxItems:
            s.removePoints(0, s.count() - self.maxItems)

        if forceUpdate:
            self.autoRange(axis)
            a.applyNiceNumbers()
            self.addSeries(s)

            s.attachAxis(self.timeAxis)
            s.attachAxis(a)

class TimeChartView(QtCharts.QChartView):
    """Time chart view. Add handling of mouse move events.
    """

    def __init__(self, chart):
        super().__init__(chart)
        self.setRenderHint(QPainter.Antialiasing)
