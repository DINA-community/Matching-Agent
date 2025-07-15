from enum import Enum


class CircuitsCircuitGroupAssignmentsListPriority(str, Enum):
    INACTIVE = "inactive"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TERTIARY = "tertiary"

    def __str__(self) -> str:
        return str(self.value)
