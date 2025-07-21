from enum import Enum


class WritableTunnelRequestStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
