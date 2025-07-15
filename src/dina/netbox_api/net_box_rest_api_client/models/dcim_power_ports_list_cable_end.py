from enum import Enum


class DcimPowerPortsListCableEnd(str, Enum):
    A = "A"
    B = "B"

    def __str__(self) -> str:
        return str(self.value)
