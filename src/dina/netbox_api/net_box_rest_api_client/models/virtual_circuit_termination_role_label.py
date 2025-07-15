from enum import Enum


class VirtualCircuitTerminationRoleLabel(str, Enum):
    HUB = "Hub"
    PEER = "Peer"
    SPOKE = "Spoke"

    def __str__(self) -> str:
        return str(self.value)
