from enum import Enum


class VirtualDeviceContextStatusLabel(str, Enum):
    ACTIVE = "Active"
    OFFLINE = "Offline"
    PLANNED = "Planned"

    def __str__(self) -> str:
        return str(self.value)
