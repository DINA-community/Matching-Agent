from enum import Enum


class CircuitStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONED = "Decommissioned"
    DEPROVISIONING = "Deprovisioning"
    OFFLINE = "Offline"
    PLANNED = "Planned"
    PROVISIONING = "Provisioning"

    def __str__(self) -> str:
        return str(self.value)
