from enum import Enum


class PatchedWritableL2VPNRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
