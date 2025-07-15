from enum import Enum


class PatchedWritableWirelessLANRequestAuthenticationCipher(str, Enum):
    AES = "aes"
    AUTO = "auto"
    TKIP = "tkip"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
