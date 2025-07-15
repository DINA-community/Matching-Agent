from enum import Enum


class PowerOutletTemplateRequestFeedLegType1(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
