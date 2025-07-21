from enum import Enum


class DeviceWithConfigContextAirflowLabel(str, Enum):
    BOTTOM_TO_TOP = "Bottom to top"
    FRONT_TO_REAR = "Front to rear"
    LEFT_TO_RIGHT = "Left to right"
    MIXED = "Mixed"
    PASSIVE = "Passive"
    REAR_TO_FRONT = "Rear to front"
    REAR_TO_SIDE = "Rear to side"
    RIGHT_TO_LEFT = "Right to left"
    SIDE_TO_REAR = "Side to rear"
    TOP_TO_BOTTOM = "Top to bottom"

    def __str__(self) -> str:
        return str(self.value)
