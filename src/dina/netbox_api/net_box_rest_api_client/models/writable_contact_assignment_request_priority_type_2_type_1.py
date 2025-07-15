from enum import Enum


class WritableContactAssignmentRequestPriorityType2Type1(str, Enum):
    INACTIVE = "inactive"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TERTIARY = "tertiary"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
