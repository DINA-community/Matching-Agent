from enum import Enum


class DcimCablesListLengthUnit(str, Enum):
    CM = "cm"
    FT = "ft"
    IN = "in"
    KM = "km"
    M = "m"
    MI = "mi"

    def __str__(self) -> str:
        return str(self.value)
