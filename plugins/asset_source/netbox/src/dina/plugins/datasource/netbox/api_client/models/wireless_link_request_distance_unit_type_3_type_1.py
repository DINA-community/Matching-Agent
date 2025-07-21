from enum import Enum


class WirelessLinkRequestDistanceUnitType3Type1(str, Enum):
    FT = "ft"
    KM = "km"
    M = "m"
    MI = "mi"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
