from enum import Enum


class IPAddressStatusValue(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    DHCP = "dhcp"
    RESERVED = "reserved"
    SLAAC = "slaac"

    def __str__(self) -> str:
        return str(self.value)
