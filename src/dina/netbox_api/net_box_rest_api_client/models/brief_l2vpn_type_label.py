from enum import Enum


class BriefL2VPNTypeLabel(str, Enum):
    EPL = "EPL"
    ETHERNET_PRIVATE_LAN = "Ethernet Private LAN"
    ETHERNET_PRIVATE_TREE = "Ethernet Private Tree"
    ETHERNET_VIRTUAL_PRIVATE_LAN = "Ethernet Virtual Private LAN"
    ETHERNET_VIRTUAL_PRIVATE_TREE = "Ethernet Virtual Private Tree"
    EVPL = "EVPL"
    EVPN_VPWS = "EVPN VPWS"
    MPLS_EVPN = "MPLS EVPN"
    PBB_EVPN = "PBB EVPN"
    SPB = "SPB"
    VPLS = "VPLS"
    VPWS = "VPWS"
    VXLAN = "VXLAN"
    VXLAN_EVPN = "VXLAN-EVPN"

    def __str__(self) -> str:
        return str(self.value)
