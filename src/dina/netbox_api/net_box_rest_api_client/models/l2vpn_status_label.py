from enum import Enum


class L2VPNStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    PLANNED = "Planned"

    def __str__(self) -> str:
        return str(self.value)
