from enum import Enum


class IKEPolicyModeValue(str, Enum):
    AGGRESSIVE = "aggressive"
    MAIN = "main"

    def __str__(self) -> str:
        return str(self.value)
