from enum import Enum


class PatchedWritableDeviceWithConfigContextRequestAirflowType1(str, Enum):
    BOTTOM_TO_TOP = "bottom-to-top"
    FRONT_TO_REAR = "front-to-rear"
    LEFT_TO_RIGHT = "left-to-right"
    MIXED = "mixed"
    PASSIVE = "passive"
    REAR_TO_FRONT = "rear-to-front"
    REAR_TO_SIDE = "rear-to-side"
    RIGHT_TO_LEFT = "right-to-left"
    SIDE_TO_REAR = "side-to-rear"
    TOP_TO_BOTTOM = "top-to-bottom"
    VALUE_10 = ""

    def __str__(self) -> str:
        return str(self.value)
