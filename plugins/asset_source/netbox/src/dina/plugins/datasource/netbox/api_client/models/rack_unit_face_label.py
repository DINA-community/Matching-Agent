from enum import Enum


class RackUnitFaceLabel(str, Enum):
    FRONT = "Front"
    REAR = "Rear"

    def __str__(self) -> str:
        return str(self.value)
