from enum import Enum


class DeviceWithConfigContextFaceLabel(str, Enum):
    FRONT = "Front"
    REAR = "Rear"

    def __str__(self) -> str:
        return str(self.value)
