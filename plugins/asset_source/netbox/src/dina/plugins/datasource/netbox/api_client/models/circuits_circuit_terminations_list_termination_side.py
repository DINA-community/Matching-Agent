from enum import Enum


class CircuitsCircuitTerminationsListTerminationSide(str, Enum):
    A = "A"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
