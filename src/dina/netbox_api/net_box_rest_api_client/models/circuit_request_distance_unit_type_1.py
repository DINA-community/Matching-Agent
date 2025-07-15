from enum import Enum


class CircuitRequestDistanceUnitType1(str, Enum):
    FT = "ft"
    KM = "km"
    M = "m"
    MI = "mi"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
