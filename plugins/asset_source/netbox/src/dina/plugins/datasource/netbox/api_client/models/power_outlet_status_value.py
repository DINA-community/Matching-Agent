from enum import Enum


class PowerOutletStatusValue(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    FAULTY = "faulty"

    def __str__(self) -> str:
        return str(self.value)
