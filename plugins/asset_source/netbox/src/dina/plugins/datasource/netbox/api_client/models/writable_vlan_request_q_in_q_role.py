from enum import Enum


class WritableVLANRequestQInQRole(str, Enum):
    CVLAN = "cvlan"
    SVLAN = "svlan"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
