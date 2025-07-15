from enum import Enum


class WritableVLANRequestStatus(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
