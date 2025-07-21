from enum import Enum


class WritableVirtualCircuitTerminationRequestRole(str, Enum):
    HUB = "hub"
    PEER = "peer"
    SPOKE = "spoke"

    def __str__(self) -> str:
        return str(self.value)
