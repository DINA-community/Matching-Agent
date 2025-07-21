from enum import Enum


class PowerFeedRequestStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
