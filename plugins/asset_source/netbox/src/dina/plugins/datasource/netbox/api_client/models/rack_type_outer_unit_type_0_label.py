from enum import Enum


class RackTypeOuterUnitType0Label(str, Enum):
    INCHES = "Inches"
    MILLIMETERS = "Millimeters"

    def __str__(self) -> str:
        return str(self.value)
