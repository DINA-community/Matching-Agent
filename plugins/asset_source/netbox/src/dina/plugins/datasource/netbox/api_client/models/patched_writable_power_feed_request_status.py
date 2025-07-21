from enum import Enum


class PatchedWritablePowerFeedRequestStatus(str, Enum):
    ACTIVE = "active"
    FAILED = "failed"
    OFFLINE = "offline"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
