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
            but.clicked.connect(lambda: _positionChanged(index, change))
            return but

        style = QApplication.instance().style()

        def addArrows(col, indexOffset, change):
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowUp), "X+", 0 + indexOffset, change
                ),
                1,
                col + 2,
            )
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowDown),
                    "X-",
                    0 + indexOffset,
                    -change,
                ),
                3,
                col + 2,
            )
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowLeft),
                    "Y-",
                    1 + indexOffset,
                    -change,
                ),
                2,
                col + 1,
            )
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowRight),
                    "Y+",
                    1 + indexOffset,
                    change,
                ),
                2,
                col + 3,
            )
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowUp), "Z+", 2 + indexOffset, change
                ),
                1,
                col + 4,
            )
            layout.addWidget(
                positionButton(
                    style.standardIcon(QStyle.SP_ArrowDown),
                    "Z-",
                    2 + indexOffset,
                    -change,
                ),
                3,
                col + 4,
            )

        addArrows(0, 0, 0.001)
        addArrows(5, 3, 0.00024)

        self.setLayout(layout)
