from enum import Enum


class PatchedWritableInterfaceRequestWirelessRole(str, Enum):
    AP = "ap"
    STATION = "station"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
