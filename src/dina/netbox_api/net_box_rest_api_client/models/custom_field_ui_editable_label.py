from enum import Enum


class CustomFieldUiEditableLabel(str, Enum):
    HIDDEN = "Hidden"
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
