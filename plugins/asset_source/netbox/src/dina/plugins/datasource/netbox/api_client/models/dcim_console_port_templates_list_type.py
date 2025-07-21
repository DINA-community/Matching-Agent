from enum import Enum


class DcimConsolePortTemplatesListType(str, Enum):
    OTHER = "Other"
    SERIAL = "Serial"
    USB = "USB"

    def __str__(self) -> str:
        return str(self.value)
