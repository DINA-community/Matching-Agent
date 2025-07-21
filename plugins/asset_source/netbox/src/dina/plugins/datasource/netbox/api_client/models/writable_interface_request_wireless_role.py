from enum import Enum


class WritableInterfaceRequestWirelessRole(str, Enum):
    AP = "ap"
    STATION = "station"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
