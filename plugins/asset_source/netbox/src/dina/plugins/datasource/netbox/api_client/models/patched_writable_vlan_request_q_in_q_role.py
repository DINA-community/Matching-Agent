from enum import Enum


class PatchedWritableVLANRequestQInQRole(str, Enum):
    CVLAN = "cvlan"
    SVLAN = "svlan"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
