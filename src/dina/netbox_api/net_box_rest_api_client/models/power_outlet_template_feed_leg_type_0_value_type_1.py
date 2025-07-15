from enum import Enum


class PowerOutletTemplateFeedLegType0ValueType1(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
