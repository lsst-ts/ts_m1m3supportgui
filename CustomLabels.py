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

__all__ = ["UnitLabel", "Force", "Mm", "WarningLabel", "Arcsec"]


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
    """

    def __init__(self, fmt="d", unit=None, convert=None):
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

    def __copy__(self):
        return UnitLabel(self.fmt, self.unit, self.convert)

    def setValue(self, value):
        """Sets value. Transformation and formatting is done according to unit, convert and fmt constructor arguments.

        Parameters
        ----------
        value : `float`
            Current (=to be displayed) variable value.
        """
        self.setText(f"{(value * self.scale):{self.fmt}}{self.unit_name}")


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

    def __init__(self, fmt=".04f"):
        super().__init__(fmt, u.meter, u.mm)


class Arcsec(UnitLabel):
    """Display radians as arcseconds.

    Parameters
    ----------
    fmt : `str`, optional
        Float formatting. Defaults to .02f.
    """

    def __init__(self, fmt="0.02f"):
        super().__init__(fmt, u.rad, u.arcsec)


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
