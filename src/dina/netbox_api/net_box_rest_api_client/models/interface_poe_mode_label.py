from enum import Enum


class InterfacePoeModeLabel(str, Enum):
    PD = "PD"
    PSE = "PSE"

    def __str__(self) -> str:
        return str(self.value)
