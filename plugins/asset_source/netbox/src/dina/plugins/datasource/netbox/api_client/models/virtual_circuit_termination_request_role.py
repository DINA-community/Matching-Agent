from enum import Enum


class VirtualCircuitTerminationRequestRole(str, Enum):
    HUB = "hub"
    PEER = "peer"
    SPOKE = "spoke"

    def __str__(self) -> str:
        return str(self.value)
