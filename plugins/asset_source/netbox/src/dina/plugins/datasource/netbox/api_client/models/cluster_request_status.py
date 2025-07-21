from enum import Enum


class ClusterRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    OFFLINE = "offline"
    PLANNED = "planned"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)
