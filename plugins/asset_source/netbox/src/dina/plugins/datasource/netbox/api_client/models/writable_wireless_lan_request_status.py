from enum import Enum


class WritableWirelessLANRequestStatus(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DISABLED = "disabled"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
