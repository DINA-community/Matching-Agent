from enum import Enum


class InterfaceTemplatePoeModeType0Label(str, Enum):
    PD = "PD"
    PSE = "PSE"

    def __str__(self) -> str:
        return str(self.value)
