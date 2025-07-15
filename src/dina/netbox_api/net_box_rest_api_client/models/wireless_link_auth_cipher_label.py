from enum import Enum


class WirelessLinkAuthCipherLabel(str, Enum):
    AES = "AES"
    AUTO = "Auto"
    TKIP = "TKIP"

    def __str__(self) -> str:
        return str(self.value)
