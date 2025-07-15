from enum import Enum


class IPAddressRoleLabel(str, Enum):
    ANYCAST = "Anycast"
    CARP = "CARP"
    GLBP = "GLBP"
    HSRP = "HSRP"
    LOOPBACK = "Loopback"
    SECONDARY = "Secondary"
    VIP = "VIP"
    VRRP = "VRRP"

    def __str__(self) -> str:
        return str(self.value)
