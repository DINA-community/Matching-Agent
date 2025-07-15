from enum import Enum


class CustomFieldUiVisibleValue(str, Enum):
    ALWAYS = "always"
    HIDDEN = "hidden"
    IF_SET = "if-set"

    def __str__(self) -> str:
        return str(self.value)
