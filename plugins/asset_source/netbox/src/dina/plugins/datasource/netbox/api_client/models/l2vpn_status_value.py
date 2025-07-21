from enum import Enum


class L2VPNStatusValue(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
