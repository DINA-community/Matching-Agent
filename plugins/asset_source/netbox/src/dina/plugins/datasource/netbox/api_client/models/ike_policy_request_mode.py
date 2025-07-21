from enum import Enum


class IKEPolicyRequestMode(str, Enum):
    AGGRESSIVE = "aggressive"
    MAIN = "main"

    def __str__(self) -> str:
        return str(self.value)
