from enum import Enum


class RackTypeWidthLabel(str, Enum):
    VALUE_0 = "10 inches"
    VALUE_1 = "19 inches"
    VALUE_2 = "21 inches"
    VALUE_3 = "23 inches"

    def __str__(self) -> str:
        return str(self.value)
