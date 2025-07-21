from enum import Enum


class WirelessLinkStatusLabel(str, Enum):
    CONNECTED = "Connected"
    DECOMMISSIONING = "Decommissioning"
    PLANNED = "Planned"

    def __str__(self) -> str:
        return str(self.value)
