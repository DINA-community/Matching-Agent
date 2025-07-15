from enum import Enum


class TunnelEncapsulationLabel(str, Enum):
    GRE = "GRE"
    IPSEC_TRANSPORT = "IPsec - Transport"
    IPSEC_TUNNEL = "IPsec - Tunnel"
    IP_IN_IP = "IP-in-IP"
    L2TP = "L2TP"
    OPENVPN = "OpenVPN"
    PPTP = "PPTP"
    WIREGUARD = "WireGuard"

    def __str__(self) -> str:
        return str(self.value)
