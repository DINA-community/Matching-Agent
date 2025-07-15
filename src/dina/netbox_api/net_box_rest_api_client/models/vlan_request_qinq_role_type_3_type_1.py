from enum import Enum


class VLANRequestQinqRoleType3Type1(str, Enum):
    CVLAN = "cvlan"
    SVLAN = "svlan"

    def __str__(self) -> str:
        return str(self.value)
