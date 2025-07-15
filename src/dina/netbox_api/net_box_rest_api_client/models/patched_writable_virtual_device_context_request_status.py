from enum import Enum


class PatchedWritableVirtualDeviceContextRequestStatus(str, Enum):
    ACTIVE = "active"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
