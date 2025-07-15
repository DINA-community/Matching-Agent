from enum import Enum


class DcimCableTerminationsListEnd(str, Enum):
    A = "A"
    B = "B"

    def __str__(self) -> str:
        return str(self.value)
