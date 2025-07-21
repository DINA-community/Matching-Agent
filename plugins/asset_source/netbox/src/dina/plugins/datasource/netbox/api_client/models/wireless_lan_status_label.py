from enum import Enum


class WirelessLANStatusLabel(str, Enum):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"
    RESERVED = "Reserved"

    def __str__(self) -> str:
        return str(self.value)
