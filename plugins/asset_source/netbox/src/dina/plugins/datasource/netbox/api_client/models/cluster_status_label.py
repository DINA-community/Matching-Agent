from enum import Enum


class ClusterStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    OFFLINE = "Offline"
    PLANNED = "Planned"
    STAGING = "Staging"

    def __str__(self) -> str:
        return str(self.value)
