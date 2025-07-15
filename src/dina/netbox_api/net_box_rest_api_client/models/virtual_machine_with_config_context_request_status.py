from enum import Enum


class VirtualMachineWithConfigContextRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    FAILED = "failed"
    OFFLINE = "offline"
    PAUSED = "paused"
    PLANNED = "planned"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
