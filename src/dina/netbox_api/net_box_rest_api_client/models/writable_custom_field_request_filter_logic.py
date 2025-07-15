from enum import Enum


class WritableCustomFieldRequestFilterLogic(str, Enum):
    DISABLED = "disabled"
    EXACT = "exact"
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
