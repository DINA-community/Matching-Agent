from enum import Enum


class VirtualMachineWithConfigContextStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    FAILED = "Failed"
    OFFLINE = "Offline"
    PAUSED = "Paused"
    PLANNED = "Planned"
    STAGED = "Staged"

    def __str__(self) -> str:
        return str(self.value)
