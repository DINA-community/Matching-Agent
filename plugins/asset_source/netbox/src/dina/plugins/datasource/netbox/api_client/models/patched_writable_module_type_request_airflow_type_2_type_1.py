from enum import Enum


class PatchedWritableModuleTypeRequestAirflowType2Type1(str, Enum):
    FRONT_TO_REAR = "front-to-rear"
    LEFT_TO_RIGHT = "left-to-right"
    PASSIVE = "passive"
    REAR_TO_FRONT = "rear-to-front"
    RIGHT_TO_LEFT = "right-to-left"
    SIDE_TO_REAR = "side-to-rear"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
