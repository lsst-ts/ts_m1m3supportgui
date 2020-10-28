from FATABLE import *

__all__ = ["Topics"]


class TopicData:
    def __init__(self, name, fields, data):
        self.name = name
        self.fields = fields
        self.selectedField = 0
        self.data = data


class Topics:
    """
    Class constructing list of all available topics.
    """

    def __init__(self, comm):
        self.lastIndex = None
        self.lastCallBack = None

        self.topics = [
            TopicData(
                "Applied Aberration Forces",
                [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_appliedAberrationForces,
            ),
            TopicData(
                "Applied Acceleration Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedAccelerationForces,
            ),
            TopicData(
                "Applied Active Optic Forces",
                [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_appliedActiveOpticForces,
            ),
            TopicData(
                "Applied Azimuth Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedAzimuthForces,
            ),
            TopicData(
                "Applied Balance Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedBalanceForces,
            ),
            TopicData(
                "Applied Cylinder Forces",
                [
                    [
                        "Primary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.primaryCylinderForces],
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.secondaryCylinderForces],
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_appliedCylinderForces,
            ),
            TopicData(
                "Applied Elevation Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedElevationForces,
            ),
            TopicData(
                "Applied Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedForces,
            ),
            TopicData(
                "Applied Offset Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedOffsetForces,
            ),
            TopicData(
                "Applied Static Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedStaticForces,
            ),
            TopicData(
                "Applied Thermal Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedThermalForces,
            ),
            TopicData(
                "Applied Velocity Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_appliedVelocityForces,
            ),
            TopicData(
                "Pre-clipped Aberration Forces",
                [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_preclippedAberrationForces,
            ),
            TopicData(
                "Pre-clipped Acceleration Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedAccelerationForces,
            ),
            TopicData(
                "Pre-clipped Active Optic Forces",
                [["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_preclippedActiveOpticForces,
            ),
            TopicData(
                "Pre-clipped Azimuth Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedAzimuthForces,
            ),
            TopicData(
                "Pre-clipped Balance Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedBalanceForces,
            ),
            TopicData(
                "Pre-clipped Cylinder Forces",
                [
                    [
                        "Primary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.primaryCylinderForces],
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.secondaryCylinderForces],
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_preclippedCylinderForces,
            ),
            TopicData(
                "Pre-clipped Elevation Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedElevationForces,
            ),
            TopicData(
                "Pre-clipped Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedForces,
            ),
            TopicData(
                "Pre-clipped Offset Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedOffsetForces,
            ),
            TopicData(
                "Pre-clipped Static Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedStaticForces,
            ),
            TopicData(
                "Pre-clipped Thermal Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedThermalForces,
            ),
            TopicData(
                "Pre-clipped Velocity Forces",
                [
                    ["Z Forces", lambda x: x.zForces, lambda: FATABLE_ZINDEX],
                    ["Y Forces", lambda x: x.yForces, lambda: FATABLE_YINDEX],
                    ["X Forces", lambda x: x.xForces, lambda: FATABLE_XINDEX],
                ],
                comm.MTM1M3.evt_preclippedVelocityForces,
            ),
            TopicData(
                "Measured forces",
                [
                    [
                        "Primary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.primaryCylinderForce],
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Cylinder Forces",
                        lambda x: [i / 1000.0 for i in x.secondaryCylinderForce],
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Z Forces",
                        lambda x: [i / 1000.0 for i in x.zForce],
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Y Forces",
                        lambda x: [i / 1000.0 for i in x.yForce],
                        lambda: FATABLE_YINDEX,
                    ],
                    [
                        "X Forces",
                        lambda x: [i / 1000.0 for i in x.xForce],
                        lambda: FATABLE_XINDEX,
                    ],
                ],
                comm.MTM1M3.tel_forceActuatorData,
            ),
            TopicData(
                "Force Actuator ILC Info",
                [
                    ["Subnet", lambda x: x.modbusSubnet, lambda: FATABLE_ZINDEX],
                    ["Address", lambda x: x.modbusAddress, lambda: FATABLE_ZINDEX],
                    ["Major Revision", lambda x: x.majorRevision],
                    ["Minor Revision", lambda x: x.minorRevision],
                    ["ADC Scan Rate", lambda x: x.adcScanRate, lambda: FATABLE_ZINDEX],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator Id Info",
                [
                    [
                        "X Data Reference Id",
                        lambda x: x.xDataReferenceId,
                        lambda: FATABLE_XINDEX,
                    ],
                    [
                        "Y Data Reference Id",
                        lambda x: x.yDataReferenceId,
                        lambda: FATABLE_YINDEX,
                    ],
                    [
                        "Z Data Reference Id",
                        lambda x: x.zDataReferenceId,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "S Data Reference Id",
                        lambda x: x.sDataReferenceId,
                        lambda: FATABLE_SINDEX,
                    ],
                    ["ILC Unique Id", lambda x: x.ilcUniqueId, lambda: FATABLE_ZINDEX],
                    [
                        "Mezzanine Unique Id",
                        lambda x: x.xDataReferenceId,
                        lambda: FATABLE_ZINDEX,
                    ],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator Main Calibration Info",
                [
                    [
                        "Primary Coefficient",
                        lambda x: x.mainPrimaryCylinderCoefficient,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Primary Offset",
                        lambda x: x.mainPrimaryCylinderLoadCellOffset,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Primary Sensitivity",
                        lambda x: x.mainPrimaryCylinderLoadCellSensitivity,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Coefficient",
                        lambda x: x.mainSecondaryCylinderCoefficient,
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Secondary Offset",
                        lambda x: x.mainSecondaryCylinderLoadCellOffset,
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Secondary Sensitivity",
                        lambda x: x.mainSecondaryLoadCellSensitivity,
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator Backup Calibration Info",
                [
                    [
                        "Primary Coefficient",
                        lambda x: x.backupPrimaryCylinderCoefficient,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Primary Offset",
                        lambda x: x.backupPrimaryCylinderLoadCellOffset,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Primary Sensitivity",
                        lambda x: x.backupPrimaryCylinderLoadCellSensitivity,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Coefficient",
                        lambda x: x.backupSecondaryCylinderCoefficient,
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Secondary Offset",
                        lambda x: x.backupSecondaryCylinderLoadCellOffset,
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Secondary Sensitivity",
                        lambda x: x.backupSecondaryLoadCellSensitivity,
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator Mezzanine Calibration Info",
                [
                    [
                        "Primary Cylinder Gain",
                        lambda x: x.mezzaninePrimaryCylinderGain,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Cylinder Gain",
                        lambda x: x.mezzanineSecondaryCylinderGain,
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator Position Info",
                [
                    ["Actuator Type", lambda x: x.actuatorType, lambda: FATABLE_ZINDEX],
                    [
                        "Actuator Orientation",
                        lambda x: x.actuatorOrientation,
                        lambda: FATABLE_ZINDEX,
                    ],
                    ["X Position", lambda x: x.xPosition, lambda: FATABLE_ZINDEX],
                    ["Y Position", lambda x: x.yPosition, lambda: FATABLE_ZINDEX],
                    ["Z Position", lambda x: x.zPosition, lambda: FATABLE_ZINDEX],
                ],
                comm.MTM1M3.evt_forceActuatorInfo,
            ),
            TopicData(
                "Force Actuator State",
                [["ILC State", lambda x: x.ilcState, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_forceActuatorState,
            ),
            TopicData(
                "Force Actuator Warning",
                [["Any Warning", lambda x: x.anyWarning, lambda: FATABLE_ZINDEX]],
                comm.MTM1M3.evt_forceActuatorWarning,
            ),  # , ["ILC Major Fault", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX], ["Broadcast Counter Mismatch", lambda x: [BitHelper.getBit(i, ForceActuatorFlags.ILCMajorFault) for i in x.forceActuatorFlags], lambda: FATABLE_ZINDEX]]),
            TopicData(
                "FA Bump Test",
                [
                    ["Primary Test", lambda x: x.primaryTest, lambda: FATABLE_ZINDEX],
                    [
                        "Secondary Test",
                        lambda x: x.secondaryTest,
                        lambda: FATABLE_SINDEX,
                    ],
                    [
                        "Primary Timestamps",
                        lambda x: x.primaryTestTimestamps,
                        lambda: FATABLE_ZINDEX,
                    ],
                    [
                        "Secondary Timestamps",
                        lambda x: x.secondaryTestTimestamps,
                        lambda: FATABLE_SINDEX,
                    ],
                ],
                comm.MTM1M3.evt_forceActuatorBumpTestStatus,
            ),
        ]

    def changeTopic(self, index, callback):
        if self.lastIndex is not None:
            self.topics[self.lastIndex].data.callback = self.lastCallBack

        self.lastIndex = index
        if index is None:
            self.lastCallBack = None
            return

        self.lastCallBack = self.topics[index].data.callback
        self.topics[index].data.callback = callback
