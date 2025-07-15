from enum import Enum


class PowerFeedRequestPhase(str, Enum):
    SINGLE_PHASE = "single-phase"
    THREE_PHASE = "three-phase"

    def __str__(self) -> str:
        return str(self.value)
