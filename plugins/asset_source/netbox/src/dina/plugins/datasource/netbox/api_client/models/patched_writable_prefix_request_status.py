from enum import Enum


class PatchedWritablePrefixRequestStatus(str, Enum):
    ACTIVE = "active"
    CONTAINER = "container"
    DEPRECATED = "deprecated"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
