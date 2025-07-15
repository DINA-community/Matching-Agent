from enum import Enum


class PatchedWritableRackTypeRequestOuterUnitType3Type1(str, Enum):
    IN = "in"
    MM = "mm"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
