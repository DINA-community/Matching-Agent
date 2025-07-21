from enum import Enum


class DeviceStatusValue(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    FAILED = "failed"
    INVENTORY = "inventory"
    OFFLINE = "offline"
    PLANNED = "planned"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
