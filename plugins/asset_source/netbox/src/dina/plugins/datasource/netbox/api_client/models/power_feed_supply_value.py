from enum import Enum


class PowerFeedSupplyValue(str, Enum):
    AC = "ac"
    DC = "dc"

    def __str__(self) -> str:
        return str(self.value)
