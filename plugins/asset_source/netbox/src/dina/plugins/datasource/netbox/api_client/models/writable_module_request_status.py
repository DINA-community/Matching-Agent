from enum import Enum


class WritableModuleRequestStatus(str, Enum):
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    FAILED = "failed"
    OFFLINE = "offline"
    PLANNED = "planned"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
