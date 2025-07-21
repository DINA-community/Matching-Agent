from enum import Enum


class WritablePowerFeedRequestStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
