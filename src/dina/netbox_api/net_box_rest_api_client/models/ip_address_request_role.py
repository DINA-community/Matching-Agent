from enum import Enum


class IPAddressRequestRole(str, Enum):
    ANYCAST = "anycast"
    CARP = "carp"
    GLBP = "glbp"
    HSRP = "hsrp"
    LOOPBACK = "loopback"
    SECONDARY = "secondary"
    VALUE_8 = ""
    VIP = "vip"
    VRRP = "vrrp"

    def __str__(self) -> str:
        return str(self.value)
