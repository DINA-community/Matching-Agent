from enum import Enum


class BriefCircuitGroupAssignmentSerializerPriorityLabel(str, Enum):
    INACTIVE = "Inactive"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    TERTIARY = "Tertiary"

    def __str__(self) -> str:
        return str(self.value)
