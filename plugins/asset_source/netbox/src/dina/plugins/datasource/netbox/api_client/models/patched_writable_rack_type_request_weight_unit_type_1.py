from enum import Enum


class PatchedWritableRackTypeRequestWeightUnitType1(str, Enum):
    G = "g"
    KG = "kg"
    LB = "lb"
    OZ = "oz"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
