from enum import Enum


class CircuitDistanceUnitType0Label(str, Enum):
    FEET = "Feet"
    KILOMETERS = "Kilometers"
    METERS = "Meters"
    MILES = "Miles"

    def __str__(self) -> str:
        return str(self.value)
