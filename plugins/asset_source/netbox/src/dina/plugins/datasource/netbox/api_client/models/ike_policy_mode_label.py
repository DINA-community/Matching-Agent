from enum import Enum


class IKEPolicyModeLabel(str, Enum):
    AGGRESSIVE = "Aggressive"
    MAIN = "Main"

    def __str__(self) -> str:
        return str(self.value)
