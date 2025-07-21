from enum import Enum


class WritableVirtualDeviceContextRequestStatus(str, Enum):
    ACTIVE = "active"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
