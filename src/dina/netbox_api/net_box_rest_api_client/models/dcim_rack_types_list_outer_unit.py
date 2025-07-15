from enum import Enum


class DcimRackTypesListOuterUnit(str, Enum):
    IN = "in"
    MM = "mm"

    def __str__(self) -> str:
        return str(self.value)
