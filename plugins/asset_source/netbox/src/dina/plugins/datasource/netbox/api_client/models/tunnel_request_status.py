from enum import Enum


class TunnelRequestStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
