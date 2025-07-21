from enum import Enum


class PowerFeedRequestSupply(str, Enum):
    AC = "ac"
    DC = "dc"

    def __str__(self) -> str:
        return str(self.value)
