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
        number of points, oldest points are removed. Defaults to 50 * 30 = 50Hz * 30s.
    updateInterval: `float`, optional
        Interval for chart redraws responding to append call. Defaults to 0.1 second.
    """

    def __init__(self, maxItems=50 * 30, updateInterval=0.1):
        super().__init__()
        self.maxItems = maxItems
        self.timeAxis = QtCharts.QDateTimeAxis()
        self.timeAxis.setReverse(True)
        self.timeAxis.setTickCount(5)
        self.timeAxis.setTitleText("Time (UTC)")
        self.timeAxis.setFormat("h:mm:ss.zzz")
        self.nextUpdate = 0
        self.updateInterval = updateInterval

        self._storedSeries = {}

    def _findSerie(self, axis, serie):
        """
        Returns serie with given name.
        """
        return (
            self._storedSeries[axis][0],
            self._storedSeries[axis][1][serie][0],
            self._storedSeries[axis][1][serie][1],
        )

    def _addSerie(self, axis, serie):
        s = QtCharts.QLineSeries()
        s.setName(serie)
        # s.setUseOpenGL(True)
        points = []
        try:
            self._storedSeries[axis][1][serie] = [s, points]
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
            self._storedSeries[axis] = (a, {serie: [s, points]})
        return a, s, points

    def append(self, timestamp, series, update=False):
        """Add data to a serie. Creates axis and serie if needed. Shrink if more than expected elements are stored.

        Parameters
        ----------
        timestamp : `float`
            Values timestamp.
        series : [(`str`, `str`, data)]
            Axis name, serie name and data. Serie name will be shown as data label.
        update : `boolean`
            If true, updates plot. Otherwise, store points for future update
            call and update plot if updateInterval passed since the last
            completed update."""

        y_ranges = {}
        t_range = None

        # check for auto-update
        if update == False:
            now = time.time()
            if now > self.nextUpdate:
                update = True
                self.nextUpdate = now + self.updateInterval

        forceUpdate = False

        for d in series:
            axis, serie, data = d
            try:
                a, s, points = self._findSerie(axis, serie)
            except KeyError:
                a, s, points = self._addSerie(axis, serie)
                forceUpdate = True

            points.append(QPointF(timestamp * 1000.0, data))
            if len(points) > self.maxItems:
                points = points[-self.maxItems :]

            if update == False and forceUpdate == False:
                continue

            values = [p.y() for p in points]
            y_range = [min(values), max(values)]
            if y_range[0] == y_range[1]:
                clip = 1.5
            else:
                clip = (y_range[1] - y_range[0]) * 0.05
            y_range = [y_range[0] - clip, y_range[1] + clip]

            try:
                y_ranges[a] = [
                    min(y_range[0], y_ranges[a][0]),
                    max(y_range[1], y_ranges[a][1]),
                ]
            except KeyError:
                y_ranges[a] = y_range

            if t_range is None:
                t_values = [p.x() for p in points]
                t_range = [min(t_values), max(t_values)]
                self.timeAxis.setRange(
                    *(map(lambda i: QDateTime().fromMSecsSinceEpoch(i), t_range))
                )

            s.replace(points)

            if forceUpdate:
                a.applyNiceNumbers()
                self.addSeries(s)
                s.attachAxis(self.timeAxis)
                s.attachAxis(a)

        if update == False and forceUpdate == False:
            return

        for a, y_range in y_ranges.items():
            a.setRange(*y_range)

    def clearData(self):
        """Removes all data from the chart."""
        self._storedSeries = {}
        super().removeAllSeries()
        for a in self.axes(Qt.Vertical):
            self.removeAxis(a)


class TimeChartView(QtCharts.QChartView):
    """Time chart view. Add handling of mouse move events."""

    def __init__(self, chart):
        super().__init__(chart)
        self.setRenderHint(QPainter.Antialiasing)
