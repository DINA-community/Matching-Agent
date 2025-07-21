from enum import Enum


class SiteRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"
    RETIRED = "retired"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)
