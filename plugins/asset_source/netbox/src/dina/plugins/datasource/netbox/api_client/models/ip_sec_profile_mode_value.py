from enum import Enum


class IPSecProfileModeValue(str, Enum):
    AH = "ah"
    ESP = "esp"

    def __str__(self) -> str:
        return str(self.value)
