from enum import Enum


class ModuleTypeAirflowType0Label(str, Enum):
    FRONT_TO_REAR = "Front to rear"
    LEFT_TO_RIGHT = "Left to right"
    PASSIVE = "Passive"
    REAR_TO_FRONT = "Rear to front"
    RIGHT_TO_LEFT = "Right to left"
    SIDE_TO_REAR = "Side to rear"

    def __str__(self) -> str:
        return str(self.value)
