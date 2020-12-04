from FATABLE import *
from ForceActuator import ForceActuator
from ActuatorsDisplay import MirrorWidget, Actuator


class ForceActuatorGraphPageWidget(ForceActuator):
    """
    Draw distribution of force actuators, and selected value. Intercept events callbacks to trigger updates.
    """

    def __init__(self, comm):
        self.mirrorWidget = MirrorWidget()
        super().__init__(comm, self.mirrorWidget)

        self.mirrorWidget.mirrorView.selectionChanged.connect(
            self.updateSelectedActuator
        )

    def updateData(self, data):
        super().updateData(data)

        warningData = self.comm.MTM1M3.evt_forceActuatorWarning.get()
        points = []
        values = self.fieldGetter(data)

        self.mirrorWidget.mirrorView.clear()

        for row in FATABLE:
            id = row[FATABLE_ID]
            index = row[self.fieldDataIndex]
            if index is None:
                state = Actuator.STATE_INACTIVE
            elif warningData is not None:
                state = (
                    Actuator.STATE_WARNING
                    if warningData.forceActuatorFlags[row[FATABLE_INDEX]] != 0
                    else Actuator.STATE_ACTIVE
                )
            else:
                state = Actuator.STATE_ACTIVE

            self.mirrorWidget.mirrorView.addActuator(
                id,
                row[FATABLE_XPOSITION] * 1000,
                row[FATABLE_YPOSITION] * 1000,
                None if index is None else values[index],
                index,
                state,
            )
        self.mirrorWidget.setRange(min(values), max(values))
        self.mirrorWidget.mirrorView.resetTransform()
        self.mirrorWidget.mirrorView.scale(*self.mirrorWidget.mirrorView.scaleHints())

        if (
            self.mirrorWidget.mirrorView.selected is not None
            and self.mirrorWidget.mirrorView.selected.dataIndex is not None
        ):
            self.selectedActuatorValueLabel.setText(
                str(values[self.mirrorWidget.mirrorView.selected.dataIndex])
            )
