from enum import Enum


class DcimConsoleServerPortTemplatesListType(str, Enum):
    OTHER = "Other"
    SERIAL = "Serial"
    USB = "USB"

    def __str__(self) -> str:
        return str(self.value)
