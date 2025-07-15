from enum import Enum


class WirelessLANAuthCipherLabel(str, Enum):
    AES = "AES"
    AUTO = "Auto"
    TKIP = "TKIP"

    def __str__(self) -> str:
        return str(self.value)
