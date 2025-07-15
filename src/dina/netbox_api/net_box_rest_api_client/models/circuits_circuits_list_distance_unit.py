from enum import Enum


class CircuitsCircuitsListDistanceUnit(str, Enum):
    FT = "ft"
    KM = "km"
    M = "m"
    MI = "mi"

    def __str__(self) -> str:
        return str(self.value)
