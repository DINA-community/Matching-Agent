from enum import Enum


class TunnelStatusLabel(str, Enum):
    ACTIVE = "Active"
    DISABLED = "Disabled"
    PLANNED = "Planned"

    def __str__(self) -> str:
        return str(self.value)
