from enum import Enum


class ExtrasCustomFieldsListFilterLogic(str, Enum):
    DISABLED = "disabled"
    EXACT = "exact"
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
