from enum import Enum


class RackUnitFaceValue(str, Enum):
    FRONT = "front"
    REAR = "rear"

    def __str__(self) -> str:
        return str(self.value)
