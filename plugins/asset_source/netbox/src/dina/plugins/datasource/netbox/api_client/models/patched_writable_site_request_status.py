from enum import Enum


class PatchedWritableSiteRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"
    RETIRED = "retired"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)
