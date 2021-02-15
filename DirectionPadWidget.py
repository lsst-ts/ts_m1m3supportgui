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

from PySide2.QtWidgets import QWidget, QGridLayout, QPushButton, QStyle, QApplication
from PySide2.QtCore import Signal

__all__ = ["DirectionPadWidget"]


class DirectionPadWidget(QWidget):
    """Widget displaying direction pad - allows to move and rotate XYZ"""

    """Called when position is changed."""
    positionChanged = Signal(list)

    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        self.position = [0.0] * 6

        def _positionChanged(index, change):
            self.position[index] += change
            self.positionChanged.emit(self.position)

        def positionButton(icon, text, index, change):
            but = QPushButton(icon, text)
            but.clicked.connect(_positionChanged(index, change))
            return but

        self.x_plus = positionButton(
            QApplication.instance().style().standardIcon(QStyle.SP_ArrowUp),
            "X+",
            0,
            0.001,
        )
        self.x_minus = positionButton(
            QApplication.instance().style().standardIcon(QStyle.SP_ArrowDown),
            "X-",
            0,
            -0.001,
        )
        self.y_plus = positionButton(
            QApplication.instance().style().standardIcon(QStyle.SP_ArrowRight),
            "Y+",
            1,
            0.001,
        )
        self.y_minus = positionButton(
            QApplication.instance().style().standardIcon(QStyle.SP_ArrowLeft),
            "Y-",
            1,
            -0.001,
        )

        layout.addWidget(self.x_plus, 1, 2)
        layout.addWidget(self.x_minus, 3, 2)
        layout.addWidget(self.y_plus, 2, 3)
        layout.addWidget(self.y_minus, 2, 1)

        self.setLayout(layout)
