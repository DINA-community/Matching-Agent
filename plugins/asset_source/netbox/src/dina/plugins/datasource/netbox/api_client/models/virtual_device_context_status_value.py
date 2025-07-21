from enum import Enum


class VirtualDeviceContextStatusValue(str, Enum):
    ACTIVE = "active"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
