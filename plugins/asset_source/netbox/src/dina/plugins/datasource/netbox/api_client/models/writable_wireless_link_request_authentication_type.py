from enum import Enum


class WritableWirelessLinkRequestAuthenticationType(str, Enum):
    OPEN = "open"
    VALUE_4 = ""
    WEP = "wep"
    WPA_ENTERPRISE = "wpa-enterprise"
    WPA_PERSONAL = "wpa-personal"

    def __str__(self) -> str:
        return str(self.value)
