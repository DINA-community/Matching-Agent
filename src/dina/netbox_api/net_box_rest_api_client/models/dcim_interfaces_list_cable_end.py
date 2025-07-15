from enum import Enum


class DcimInterfacesListCableEnd(str, Enum):
    A = "A"
    B = "B"

    def __str__(self) -> str:
        return str(self.value)
