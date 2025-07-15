from enum import Enum


class WritableWirelessLinkRequestStatus(str, Enum):
    CONNECTED = "connected"
    DECOMMISSIONING = "decommissioning"
    PLANNED = "planned"

    def __str__(self) -> str:
        return str(self.value)
