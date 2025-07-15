from enum import Enum


class DcimModuleTypesListWeightUnit(str, Enum):
    G = "g"
    KG = "kg"
    LB = "lb"
    OZ = "oz"

    def __str__(self) -> str:
        return str(self.value)
