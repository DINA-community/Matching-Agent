from enum import Enum


class InventoryItemStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    FAILED = "Failed"
    OFFLINE = "Offline"
    PLANNED = "Planned"
    STAGED = "Staged"

    def __str__(self) -> str:
        return str(self.value)
