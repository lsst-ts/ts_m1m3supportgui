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


class AbstractChart(QtCharts.QChart):
    def __init__(self, parent=None, wFlags=Qt.WindowFlags()):
        super().__init__(parent, wFlags)

    def findSerie(self, name):
        """
        Returns serie with given name.

        Parameters
        ----------
        name : `str`
            Serie name.

        Returns
        -------
        serie : `QAbstractSerie`
            Serie with given name. None if no serie exists.
        """
        for s in self.series():
            if s.name() == name:
                return s
        return None

    def remove(self, name):
        """Removes serie with given name."""
        s = self.findSerie(name)
        if s is None:
            return
        self.removeSeries(s)

    def clearData(self):
        """Removes all data from the chart."""
        self.removeAllSeries()
        for a in self.axes(Qt.Vertical):
            self.removeAxis(a)


class TimeChart(AbstractChart):
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
        self.addAxis(self.timeAxis, Qt.AlignBottom)

        self.nextUpdate = 0
        self.updateInterval = updateInterval

    def findAxis(self, titleText, axisType=Qt.Vertical):
        for a in self.axes(axisType):
            if a.titleText() == axis:
                return a
        return None

    def _addSerie(self, axis, serie):
        s = QtCharts.QLineSeries()
        s.setName(serie)
        # s.setUseOpenGL(True)
        points = []
        a = self.findAxis(axis)
        if a is None:
            a = QtCharts.QValueAxis()
            a.setTickCount(10)
            a.setTitleText(axis)
            self.addAxis(
                a, Qt.AlignRight if len(self.axes(Qt.Vertical)) % 2 else Qt.AlignLeft
            )
        s.attachAxis(self.timeAxis)
        s.attachAxis(a)
        return s

    def append(self, timestamp, series, update=False):
        """Add data to a serie. Creates axis and serie if needed. Shrink if more than expected elements are stored.

        Parameters
        ----------
        timestamp : `float`
            Values timestamp.
        series : [(`str`, `str`, data)]
            Axis name, serie name and data. Serie name will be shown as data label.
        update : `boolean`, optional
            If true, updates plot. Otherwise, store points for future update
            call and update plot if updateInterval passed since the last
            completed update."""

        y_ranges = {}
        t_range = None

        # check for auto-update
        if update is False:
            now = time.time()
            if now > self.nextUpdate:
                update = True
                self.nextUpdate = now + self.updateInterval

        forceUpdate = False

        for d in series:
            axis, serie, data = d
            serie = self.findSerie(f"{serie} {axis}")
            if serie is None:
                serie = self._addSerie(axis, serie)
                forceUpdate = True

            points = serie.points()
            a = serie.attachedAxes()[0]

            points.append(QPointF(timestamp * 1000.0, data))
            if len(points) > self.maxItems:
                points = points[-self.maxItems :]

            if update is False and forceUpdate is False:
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

            serie.replace(points)

            if forceUpdate:
                a.applyNiceNumbers()
                self.addSeries(serie)

        if update is False and forceUpdate is False:
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
        self.setRubberBand(QtCharts.QChartView.HorizontalRubberBand)
