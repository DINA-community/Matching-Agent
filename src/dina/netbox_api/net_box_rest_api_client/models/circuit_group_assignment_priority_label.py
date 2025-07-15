from enum import Enum


class CircuitGroupAssignmentPriorityLabel(str, Enum):
    INACTIVE = "Inactive"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    TERTIARY = "Tertiary"

    def __str__(self) -> str:
        return str(self.value)
