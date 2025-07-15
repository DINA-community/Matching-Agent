from enum import Enum


class WritableIKEPolicyRequestModeType3Type1(str, Enum):
    AGGRESSIVE = "aggressive"
    MAIN = "main"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
