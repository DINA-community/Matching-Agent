from enum import Enum


class InterfaceDuplexType0Label(str, Enum):
    AUTO = "Auto"
    FULL = "Full"
    HALF = "Half"

    def __str__(self) -> str:
        return str(self.value)
