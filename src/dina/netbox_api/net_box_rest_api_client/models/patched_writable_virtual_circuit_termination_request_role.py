from enum import Enum


class PatchedWritableVirtualCircuitTerminationRequestRole(str, Enum):
    HUB = "hub"
    PEER = "peer"
    SPOKE = "spoke"

    def __str__(self) -> str:
        return str(self.value)
