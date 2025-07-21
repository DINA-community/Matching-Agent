from enum import Enum


class WritableInterfaceRequestDuplexType3Type1(str, Enum):
    AUTO = "auto"
    FULL = "full"
    HALF = "half"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
