from enum import Enum


class PatchedWritableInterfaceTemplateRequestPoeModeType1(str, Enum):
    PD = "pd"
    PSE = "pse"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
