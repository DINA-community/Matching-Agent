from enum import Enum


class RackStatusLabel(str, Enum):
    ACTIVE = "Active"
    AVAILABLE = "Available"
    DEPRECATED = "Deprecated"
    PLANNED = "Planned"
    RESERVED = "Reserved"

    def __str__(self) -> str:
        return str(self.value)
