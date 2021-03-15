# This file is part of M1M3 SS GUI.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org). See the COPYRIGHT file at the top - level directory
# of this distribution for details of code ownership.
#
# This program is free software : you can redistribute it and / or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtCore import Slot, QRect, QTimer
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar, QSizePolicy
from PySide2.QtGui import QPainter, QColor, QPalette, QBrush
import astropy.units as u
from datetime import datetime

__all__ = [
    "UnitLabel",
    "Force",
    "Moment",
    "Mm",
    "Arcsec",
    "ArcsecWarning",
    "MmWarning",
    "WarningLabel",
    "Heartbeat",
]


class UnitLabel(QLabel):
    """Qt Label that can display and convert Astropy units.

    Parameters
    ----------
    fmt : `str`, optional
        Format string. See Python formatting function for details. Defaults to
        'd' for decimal number.
    unit : `astropy.units`, optional
        Variable unit. Default is None - no unit
    convert : `astropy.units`, optional
        Convert values to this unit. Default is None - no unit. If provided, unit must be provided as well.
    is_warn_func : `func`, optional
        Function evaluated on each value. If true is returned, value is assumed to be in warning range and will be color coded (displayed in yellow text). Default is None - no color coded warning value.
    is_err_func : `func`, optional
        Function evaluated on each value. If true is returned, value is assumed to be in warning range and will be color coded (displayed in yellow text). Default is None - no color coded error value.
    """

    def __init__(
        self, fmt="d", unit=None, convert=None, is_warn_func=None, is_err_func=None
    ):
        super().__init__("---")
        self.fmt = fmt
        if convert is not None:
            if unit is None:
                raise RuntimeError("Cannot specify conversion without input units!")
            self.scale = unit.to(convert)
            self.unit_name = " " + convert.to_string()
        elif unit is not None:
            self.scale = 1
            self.unit_name = " " + unit.to_string()
        else:
            self.scale = 1
            self.unit_name = ""
        self.unit = unit
        self.convert = convert
        self.is_warn_func = is_warn_func
        self.is_err_func = is_err_func

    def __copy__(self):
        return UnitLabel(
            self.fmt, self.unit, self.convert, self.is_warn_func, self.is_err_func
        )

    def setValue(self, value):
        """Sets value. Transformation and formatting is done according to unit, convert and fmt constructor arguments.

        Parameters
        ----------
        value : `float`
            Current (=to be displayed) variable value.
        """
        text = f"{(value * self.scale):{self.fmt}}{self.unit_name}"
        if self.is_err_func is not None and self.is_err_func(value):
            self.setText("<font color='red'>" + text + "</font>")
        elif self.is_warn_func is not None and self.is_warn_func(value):
            self.setText("<font color='yellow'>" + text + "</font>")
        else:
            self.setText(text)


class Force(UnitLabel):
    """Displays force in N (Newtons).

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .02f.
    """

    def __init__(self, fmt=".02f"):
        super().__init__(fmt, u.N)


class Moment(UnitLabel):
    """Displays moment in N*m (Newtons meters).

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .02f.
    """

    def __init__(self, fmt=".02f"):
        super().__init__(fmt, u.N * u.m)


class Mm(UnitLabel):
    """Display meters as mm (millimeters).

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .04f.
    """

    def __init__(self, fmt=".04f", is_warn_func=None, is_err_func=None):
        super().__init__(fmt, u.meter, u.mm, is_warn_func, is_err_func)


class MmWarning(Mm):
    """Display meters as mm (millimeters). Shows values above threshold as
    error / fault.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .04f.
    warning_threshold : `float`, optional
        If abs(value) is above the threshold, display value as warning (yellow
        text). Defaults to 4 microns, half allowed deviation.
    error_threshold : `float`, optional
        If abs(value) is above the threshold, display value as error (red
        text). Defaults to 8 microns, full sensor error budget.
    """

    def __init__(
        self,
        fmt=".04f",
        warning_threshold=4 * u.um.to(u.meter),
        error_threshold=8 * u.um.to(u.meter),
    ):
        super().__init__(
            fmt,
            lambda v: abs(v) > warning_threshold,
            lambda v: abs(v) > error_threshold,
        )


class Arcsec(UnitLabel):
    """Display degrees as arcseconds.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .02f.
    """

    def __init__(self, fmt="0.02f", is_warn_func=None, is_err_func=None):
        super().__init__(fmt, u.deg, u.arcsec, is_warn_func, is_err_func)


class ArcsecWarning(Arcsec):
    """Display degrees as arcseconds. Shows values above threshold as error /
    fault.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to 0.02f.
    warning_threshold : `float`, optional
        If abs(value) is above the threshold, display value as warning (yellow
        text). Defaults to 0.73 arcsecond, half of the allowed measurement error.

    error_threshold : `float`, optional
        If abs(value) is above the threshold, display value as error (red
        text).  Defaults to 1.45 arcseconds, full measurement error budget.
    """

    def __init__(
        self,
        fmt="0.02f",
        warning_threshold=0.73 * u.arcsec.to(u.deg),
        error_threshold=1.45 * u.arcsec.to(u.deg),
    ):
        super().__init__(
            fmt,
            lambda v: abs(v) > warning_threshold,
            lambda v: abs(v) > error_threshold,
        )


class WarningLabel(QLabel):
    """Displays on/off warnings"""

    def __init__(self):
        super().__init__()

    def __copy__(self):
        return WarningLabel()

    def setValue(self, value):
        """Sets formatted value. Color codes On (red)/Off (green).

        Parameters
        ----------
        value : `bool`
            Current (=to be displayed) variable value. True means warning/error is raised.
        """
        if value:
            self.setText(f"<font color='red'>On</font>")
        else:
            self.setText(f"<font color='green'>Off</font>")


class Heartbeat(QWidget):
    """Display heartbeat"""

    def __init__(self):
        super().__init__()

        self.hbIndicator = QProgressBar()
        self.hbIndicator.setRange(0, 2)
        self.hbIndicator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.timestamp = QLabel("- waiting -")

        layout = QVBoxLayout()
        layout.addWidget(self.hbIndicator)
        layout.addWidget(self.timestamp)
        self.setLayout(layout)

        self._timeoutTimer = None
        self._initTimer(3000)

    def _initTimer(self, timeout=2001):
        if self._timeoutTimer is not None:
            self._timeoutTimer.stop()

        self._timeoutTimer = QTimer(self)
        self._timeoutTimer.setSingleShot(True)
        self._timeoutTimer.timeout.connect(self.timeouted)
        self._timeoutTimer.start(timeout)

    @Slot()
    def timeouted(self):
        self.hbIndicator.setFormat("")
        self.hbIndicator.setValue(0)
        self.hbIndicator.setInvertedAppearance(False)
        self.timestamp.setText("<font color='red'>- timeouted -</font>")

    @Slot(map)
    def heartbeat(self, data):
        v = data.private_seqNum % 3
        if v == 0 or v == 1:
            self.hbIndicator.setValue(1)
            self.hbIndicator.setInvertedAppearance(v == 1)
        else:
            self.hbIndicator.setValue(2)

        self.hbIndicator.setFormat(f"{data.private_seqNum % int(1e12):012d}")
        diff = data.private_rcvStamp - data.private_sndStamp
        if abs(diff) > 0.5:
            self.timestamp.setText(
                datetime.fromtimestamp(data.private_sndStamp).strftime(
                    f"<font color='red'>%H:%M:%S ({diff:0.1f})</font>"
                )
            )
        else:
            self.timestamp.setText(
                datetime.fromtimestamp(data.private_sndStamp).strftime(
                    "<font color='green'>%H:%M:%S.%f</font>"
                )
            )

        self._initTimer(2001)
