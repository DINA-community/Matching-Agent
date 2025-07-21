from enum import Enum


class PowerOutletStatusLabel(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    FAULTY = "Faulty"

    def __str__(self) -> str:
        return str(self.value)
