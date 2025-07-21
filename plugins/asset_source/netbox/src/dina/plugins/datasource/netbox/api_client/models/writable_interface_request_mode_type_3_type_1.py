from enum import Enum


class WritableInterfaceRequestModeType3Type1(str, Enum):
    ACCESS = "access"
    Q_IN_Q = "q-in-q"
    TAGGED = "tagged"
    TAGGED_ALL = "tagged-all"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
