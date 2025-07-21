from enum import Enum


class BriefL2VPNTypeValue(str, Enum):
    EPL = "epl"
    EP_LAN = "ep-lan"
    EP_TREE = "ep-tree"
    EVPL = "evpl"
    EVPN_VPWS = "evpn-vpws"
    EVP_LAN = "evp-lan"
    EVP_TREE = "evp-tree"
    MPLS_EVPN = "mpls-evpn"
    PBB_EVPN = "pbb-evpn"
    SPB = "spb"
    VPLS = "vpls"
    VPWS = "vpws"
    VXLAN = "vxlan"
    VXLAN_EVPN = "vxlan-evpn"

    def __str__(self) -> str:
        return str(self.value)
