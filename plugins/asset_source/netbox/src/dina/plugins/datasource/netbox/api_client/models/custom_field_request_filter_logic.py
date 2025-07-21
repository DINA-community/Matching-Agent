from enum import Enum


class CustomFieldRequestFilterLogic(str, Enum):
    DISABLED = "disabled"
    EXACT = "exact"
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
