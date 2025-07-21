from enum import Enum


class WirelessLinkStatusValue(str, Enum):
    CONNECTED = "connected"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
