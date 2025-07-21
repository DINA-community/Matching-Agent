from enum import Enum


class WritableCustomFieldRequestUiEditable(str, Enum):
    HIDDEN = "hidden"
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
