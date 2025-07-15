from enum import Enum


class PrefixStatusLabel(str, Enum):
    ACTIVE = "Active"
    CONTAINER = "Container"
    DEPRECATED = "Deprecated"
    RESERVED = "Reserved"

    def __str__(self) -> str:
        return str(self.value)
