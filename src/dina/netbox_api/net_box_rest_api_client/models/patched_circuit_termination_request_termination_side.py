from enum import Enum


class PatchedCircuitTerminationRequestTerminationSide(str, Enum):
    A = "A"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
