from enum import Enum


class TunnelTerminationRoleLabel(str, Enum):
    HUB = "Hub"
    PEER = "Peer"
    SPOKE = "Spoke"

    def __str__(self) -> str:
        return str(self.value)
