from enum import Enum


class ExtrasCustomFieldsListUiEditable(str, Enum):
    HIDDEN = "hidden"
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
