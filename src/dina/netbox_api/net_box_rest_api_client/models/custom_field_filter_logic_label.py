from enum import Enum


class CustomFieldFilterLogicLabel(str, Enum):
    DISABLED = "Disabled"
    EXACT = "Exact"
    LOOSE = "Loose"

    def __str__(self) -> str:
        return str(self.value)
