from enum import Enum


class RackAirflowLabel(str, Enum):
    FRONT_TO_REAR = "Front to rear"
    REAR_TO_FRONT = "Rear to front"

    def __str__(self) -> str:
        return str(self.value)
