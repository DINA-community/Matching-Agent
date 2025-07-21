from enum import Enum


class VLANStatusLabel(str, Enum):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    RESERVED = "Reserved"

    def __str__(self) -> str:
        return str(self.value)
