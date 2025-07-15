from enum import Enum


class TunnelEncapsulationValue(str, Enum):
    GRE = "gre"
    IPSEC_TRANSPORT = "ipsec-transport"
    IPSEC_TUNNEL = "ipsec-tunnel"
    IP_IP = "ip-ip"
    L2TP = "l2tp"
    OPENVPN = "openvpn"
    PPTP = "pptp"
    WIREGUARD = "wireguard"

    def __str__(self) -> str:
        return str(self.value)
