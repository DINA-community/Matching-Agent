from enum import Enum


class CircuitsCircuitTerminationsListCableEnd(str, Enum):
    A = "A"
    B = "B"

    def __str__(self) -> str:
        return str(self.value)
