from enum import Enum


class InterfacePoeModeValue(str, Enum):
    PD = "pd"
    PSE = "pse"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
