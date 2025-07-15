from enum import Enum


class WritablePowerFeedRequestPhase(str, Enum):
    SINGLE_PHASE = "single-phase"
    THREE_PHASE = "three-phase"

    def __str__(self) -> str:
        return str(self.value)
