from enum import Enum


class PatchedWritableInterfaceTemplateRequestWirelessRole(str, Enum):
    AP = "ap"
    STATION = "station"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
