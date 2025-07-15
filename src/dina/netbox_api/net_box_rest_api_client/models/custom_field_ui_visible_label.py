from enum import Enum


class CustomFieldUiVisibleLabel(str, Enum):
    ALWAYS = "Always"
    HIDDEN = "Hidden"
    IF_SET = "If set"

    def __str__(self) -> str:
        return str(self.value)
