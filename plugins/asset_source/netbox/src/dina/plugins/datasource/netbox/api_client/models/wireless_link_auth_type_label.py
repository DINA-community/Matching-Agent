from enum import Enum


class WirelessLinkAuthTypeLabel(str, Enum):
    OPEN = "Open"
    WEP = "WEP"
    WPA_ENTERPRISE = "WPA Enterprise"
    WPA_PERSONAL_PSK = "WPA Personal (PSK)"

    def __str__(self) -> str:
        return str(self.value)
