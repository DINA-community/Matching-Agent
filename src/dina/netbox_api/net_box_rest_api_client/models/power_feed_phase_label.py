from enum import Enum


class PowerFeedPhaseLabel(str, Enum):
    SINGLE_PHASE = "Single phase"
    THREE_PHASE = "Three-phase"

    def __str__(self) -> str:
        return str(self.value)
