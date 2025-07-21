from enum import Enum


class IPAddressStatusLabel(str, Enum):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DHCP = "DHCP"
    RESERVED = "Reserved"
    SLAAC = "SLAAC"

    def __str__(self) -> str:
        return str(self.value)
