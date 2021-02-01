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

__all__ = ["UnitLabel", "Force", "Mm", "WarningLabel"]


class UnitLabel(QLabel):
    def __init__(self, fmt="d", unit=None, convert=None):
        super().__init__()
        self.fmt = fmt
        self.unit = unit
        self.convert = convert

    def __copy__(self):
        return UnitLabel(self.fmt, self.unit, self.convert)

    def setValue(self, value):
        if self.convert is not None:
            self.setText(f"{((value * self.unit).to(self.convert)):{self.fmt}}")
        elif self.unit is not None:
            self.setText(f"{(value * self.unit):{self.fmt}}")
        else:
            self.setText(f"{value:{self.fmt}}")


class Force(UnitLabel):
    def __init__(self, fmt=".02f"):
        super().__init__(fmt, u.N)


class Mm(UnitLabel):
    def __init__(self, fmt=".04f"):
        super().__init__(fmt, u.meter, u.mm)


class WarningLabel(ValueFormat):
    def __init__(self):
        super().__init__("b")
