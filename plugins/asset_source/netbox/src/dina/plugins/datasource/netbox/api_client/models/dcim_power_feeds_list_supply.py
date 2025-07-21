from enum import Enum


class DcimPowerFeedsListSupply(str, Enum):
    AC = "ac"
    DC = "dc"

    def __str__(self) -> str:
        return str(self.value)
