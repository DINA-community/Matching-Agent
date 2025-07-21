from enum import Enum


class InterfaceTemplateRfRoleType0ValueType1(str, Enum):
    AP = "ap"
    STATION = "station"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
