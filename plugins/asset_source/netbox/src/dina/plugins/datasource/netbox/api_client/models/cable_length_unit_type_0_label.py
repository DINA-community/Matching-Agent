from enum import Enum


class CableLengthUnitType0Label(str, Enum):
    CENTIMETERS = "Centimeters"
    FEET = "Feet"
    INCHES = "Inches"
    KILOMETERS = "Kilometers"
    METERS = "Meters"
    MILES = "Miles"

    def __str__(self) -> str:
        return str(self.value)
