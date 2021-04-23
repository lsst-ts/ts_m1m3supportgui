import QTHelpers
from FATABLE import *
from ForceActuatorWidget import ForceActuatorWidget
from ActuatorsDisplay import MirrorWidget, ForceActuator


class ForceActuatorGraphPageWidget(ForceActuatorWidget):
    """
    Draw distribution of force actuators, and selected value. Intercept events callbacks to trigger updates.
    """

    def __init__(self, m1m3):
        self.mirrorWidget = MirrorWidget()
        super().__init__(m1m3, self.mirrorWidget)

        self.mirrorWidget.mirrorView.selectionChanged.connect(
            self.updateSelectedActuator
        )

    def updateValues(self, data):
        warningData = self.m1m3.remote.evt_forceActuatorWarning.get()
        points = []

        if data is None:
            values = None
        else:
            values = self.fieldGetter(data)

        self.mirrorWidget.mirrorView.clear()

        def getWarning(index):
            return (
                ForceActuator.STATE_WARNING
                if warningData.minorFault[index] or warningData.majorFault[index]
                else ForceActuator.STATE_ACTIVE
            )

        for row in FATABLE:
            id = row[FATABLE_ID]
            index = row[self.fieldDataIndex]
            if values is None or index is None:
                state = ForceActuator.STATE_INACTIVE
            elif warningData is not None:
                state = getWarning(row[FATABLE_INDEX])
            else:
                state = ForceActuator.STATE_ACTIVE

            self.mirrorWidget.mirrorView.addForceActuator(
                id,
                row[FATABLE_XPOSITION] * 1000,
                row[FATABLE_YPOSITION] * 1000,
                row[FATABLE_ORIENTATION],
                None if (values is None or index is None) else values[index],
                index,
                state,
            )

        if values is None:
            self.mirrorWidget.setRange(0, 0)
            return

        self.mirrorWidget.setRange(min(values), max(values))

        if self.mirrorWidget.mirrorView.selected is not None:
            if self.mirrorWidget.mirrorView.selected.dataIndex is not None:
                self.selectedActuatorValueLabel.setText(
                    str(values[self.mirrorWidget.mirrorView.selected.dataIndex])
                )
            if warningData is not None:
                QTHelpers.setWarningLabel(
                    self.selectedActuatorWarningLabel,
                    getWarning(self.mirrorWidgets.mirrorView.selected.id),
                )
