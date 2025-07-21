from enum import Enum


class IPSecProfileModeLabel(str, Enum):
    AH = "AH"
    ESP = "ESP"

    def __str__(self) -> str:
        return str(self.value)
