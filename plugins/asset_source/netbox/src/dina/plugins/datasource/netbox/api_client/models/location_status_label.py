from enum import Enum


class LocationStatusLabel(str, Enum):
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    PLANNED = "Planned"
    RETIRED = "Retired"
    STAGING = "Staging"

    def __str__(self) -> str:
        return str(self.value)
