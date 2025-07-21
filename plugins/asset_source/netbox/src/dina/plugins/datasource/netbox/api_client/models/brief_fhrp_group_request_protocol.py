from enum import Enum


class BriefFHRPGroupRequestProtocol(str, Enum):
    CARP = "carp"
    CLUSTERXL = "clusterxl"
    GLBP = "glbp"
    HSRP = "hsrp"
    OTHER = "other"
    VRRP2 = "vrrp2"
    VRRP3 = "vrrp3"

    def __str__(self) -> str:
        return str(self.value)
