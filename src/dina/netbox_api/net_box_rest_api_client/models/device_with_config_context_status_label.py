from enum import Enum


class DeviceWithConfigContextStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    FAILED = "Failed"
    INVENTORY = "Inventory"
    OFFLINE = "Offline"
    PLANNED = "Planned"
    STAGED = "Staged"

    def __str__(self) -> str:
        return str(self.value)
