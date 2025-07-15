from enum import Enum


class ConsolePortTemplateTypeLabel(str, Enum):
    DB_25 = "DB-25"
    DE_9 = "DE-9"
    MINI_DIN_8 = "Mini-DIN 8"
    OTHER = "Other"
    RJ_11 = "RJ-11"
    RJ_12 = "RJ-12"
    RJ_45 = "RJ-45"
    USB_MICRO_A = "USB Micro A"
    USB_MICRO_AB = "USB Micro AB"
    USB_MICRO_B = "USB Micro B"
    USB_MINI_A = "USB Mini A"
    USB_MINI_B = "USB Mini B"
    USB_TYPE_A = "USB Type A"
    USB_TYPE_B = "USB Type B"
    USB_TYPE_C = "USB Type C"

    def __str__(self) -> str:
        return str(self.value)
