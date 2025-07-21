from enum import Enum


class WritableCableRequestLengthUnitType2Type1(str, Enum):
    CM = "cm"
    FT = "ft"
    IN = "in"
    KM = "km"
    M = "m"
    MI = "mi"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
