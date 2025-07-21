from enum import Enum


class WritablePowerFeedRequestSupply(str, Enum):
    AC = "ac"
    DC = "dc"

    def __str__(self) -> str:
        return str(self.value)
