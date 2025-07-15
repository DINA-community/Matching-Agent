from enum import Enum


class RackStatusValue(str, Enum):
    ACTIVE = "active"
    AVAILABLE = "available"
    DEPRECATED = "deprecated"
    PLANNED = "planned"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
