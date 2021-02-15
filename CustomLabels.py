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

from PySide2.QtWidgets import QLabel
import astropy.units as u

__all__ = [
    "UnitLabel",
    "Force",
    "Mm",
    "Arcsec",
    "ArcsecWarning",
    "MmWarning",
    "WarningLabel",
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
        super().__init__()
        self.fmt = fmt
        if convert is not None and unit is not None:
            self.scale = (1 * unit).to(convert).value
            self.unit_name = " " + convert.name
        elif convert is not None and unit is None:
            raise RuntimeError("Cannot specify conversion without input units!")
        elif unit is not None:
            self.scale = 1
            self.unit_name = " " + unit.name
        else:
            self.scale = 1
            self.unit_name = ""
        self.unit = unit
        self.convert = convert
        self.is_warn_func = is_warn_func
        self.is_err_func = is_err_func

    def __copy__(self):
        return UnitLabel(self.fmt, self.unit, self.convert)

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
    warning_threshold : `float`
        If abs(value) is above the threshold, display value as warning (yellow text).
    error_threshold : `float`
        If abs(value) is above the threshold, display value as error (red text). 
    """

    def __init__(
        self,
        fmt=".04f",
        warning_threshold=(4 * u.um).to(u.meter).value,
        error_threshold=(8 * u.um).to(u.meter).value,
    ):
        super().__init__(
            fmt,
            lambda v: abs(v) > warning_threshold,
            lambda v: abs(v) > error_threshold,
        )


class Arcsec(UnitLabel):
    """Display radians as arcseconds.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .02f.
    """

    def __init__(self, fmt="0.02f", is_warn_func=None, is_err_func=None):
        super().__init__(fmt, u.rad, u.arcsec, is_warn_func, is_err_func)


class ArcsecWarning(Arcsec):
    """Display radians as arcseconds.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to 0.02f.
    warning_threshold : `float`
        If abs(value) is above the threshold, display value as warning (yellow text).
    error_threshold : `float`
        If abs(value) is above the threshold, display value as error (red text). 
    """

    def __init__(
        self,
        fmt="0.02f",
        warning_level=(0.73 * u.arcsec).to(u.rad).value,
        error_level=(1.45 * u.arcsec).to(u.rad).value,
    ):
        super().__init__(
            fmt, lambda v: abs(v) > warning_level, lambda v: abs(v) > error_level
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
