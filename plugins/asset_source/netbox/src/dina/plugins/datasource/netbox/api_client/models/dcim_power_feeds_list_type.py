from enum import Enum


class DcimPowerFeedsListType(str, Enum):
    PRIMARY = "primary"
    REDUNDANT = "redundant"

    def __str__(self) -> str:
        return str(self.value)
