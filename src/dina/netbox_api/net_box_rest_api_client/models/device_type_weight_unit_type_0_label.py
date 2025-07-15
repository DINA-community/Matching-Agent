from enum import Enum


class DeviceTypeWeightUnitType0Label(str, Enum):
    GRAMS = "Grams"
    KILOGRAMS = "Kilograms"
    OUNCES = "Ounces"
    POUNDS = "Pounds"

    def __str__(self) -> str:
        return str(self.value)
