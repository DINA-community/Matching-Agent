from enum import Enum


class PowerFeedStatusLabel(str, Enum):
    ACTIVE = "Active"
    FAILED = "Failed"
    OFFLINE = "Offline"
    PLANNED = "Planned"

    def __str__(self) -> str:
        return str(self.value)
