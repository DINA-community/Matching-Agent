from enum import Enum


class CircuitTerminationTerminationSide(str, Enum):
    A = "A"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
