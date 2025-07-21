from enum import Enum


class WritableVirtualCircuitRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONED = "decommissioned"
    DEPROVISIONING = "deprovisioning"
    OFFLINE = "offline"
    PLANNED = "planned"
    PROVISIONING = "provisioning"

    def __str__(self) -> str:
        return str(self.value)
