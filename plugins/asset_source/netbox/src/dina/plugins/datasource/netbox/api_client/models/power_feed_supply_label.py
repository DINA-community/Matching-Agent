from enum import Enum


class PowerFeedSupplyLabel(str, Enum):
    AC = "AC"
    DC = "DC"

    def __str__(self) -> str:
        return str(self.value)
