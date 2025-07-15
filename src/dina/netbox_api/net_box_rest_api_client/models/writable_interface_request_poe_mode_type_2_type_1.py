from enum import Enum


class WritableInterfaceRequestPoeModeType2Type1(str, Enum):
    PD = "pd"
    PSE = "pse"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
