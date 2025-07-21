from enum import Enum


class VLANRequestStatus(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
