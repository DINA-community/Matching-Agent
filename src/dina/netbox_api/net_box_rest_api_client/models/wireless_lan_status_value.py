from enum import Enum


class WirelessLANStatusValue(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DISABLED = "disabled"
    RESERVED = "reserved"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
