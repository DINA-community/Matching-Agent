from enum import Enum


class WritablePowerOutletRequestStatus(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    FAULTY = "faulty"

    def __str__(self) -> str:
        return str(self.value)
