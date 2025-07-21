from enum import Enum


class DcimRacksListOuterUnit(str, Enum):
    IN = "in"
    MM = "mm"

    def __str__(self) -> str:
        return str(self.value)
