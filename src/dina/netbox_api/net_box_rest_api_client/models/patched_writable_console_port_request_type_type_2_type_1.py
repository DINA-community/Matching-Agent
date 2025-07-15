from enum import Enum


class PatchedWritableConsolePortRequestTypeType2Type1(str, Enum):
    DB_25 = "db-25"
    DE_9 = "de-9"
    MINI_DIN_8 = "mini-din-8"
    OTHER = "other"
    RJ_11 = "rj-11"
    RJ_12 = "rj-12"
    RJ_45 = "rj-45"
    USB_A = "usb-a"
    USB_B = "usb-b"
    USB_C = "usb-c"
    USB_MICRO_A = "usb-micro-a"
    USB_MICRO_AB = "usb-micro-ab"
    USB_MICRO_B = "usb-micro-b"
    USB_MINI_A = "usb-mini-a"
    USB_MINI_B = "usb-mini-b"
    VALUE_15 = ""

    def __str__(self) -> str:
        return str(self.value)
