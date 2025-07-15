from enum import Enum


class RackOuterUnitType0Label(str, Enum):
    INCHES = "Inches"
    MILLIMETERS = "Millimeters"

    def __str__(self) -> str:
        return str(self.value)
