from enum import Enum


class PowerFeedTypeLabel(str, Enum):
    PRIMARY = "Primary"
    REDUNDANT = "Redundant"

    def __str__(self) -> str:
        return str(self.value)
