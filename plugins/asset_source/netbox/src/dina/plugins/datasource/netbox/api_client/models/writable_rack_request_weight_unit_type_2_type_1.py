from enum import Enum


class WritableRackRequestWeightUnitType2Type1(str, Enum):
    G = "g"
    KG = "kg"
    LB = "lb"
    OZ = "oz"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
