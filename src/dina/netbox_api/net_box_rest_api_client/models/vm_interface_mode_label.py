from enum import Enum


class VMInterfaceModeLabel(str, Enum):
    ACCESS = "Access"
    Q_IN_Q_802_1AD = "Q-in-Q (802.1ad)"
    TAGGED = "Tagged"
    TAGGED_ALL = "Tagged (All)"

    def __str__(self) -> str:
        return str(self.value)
