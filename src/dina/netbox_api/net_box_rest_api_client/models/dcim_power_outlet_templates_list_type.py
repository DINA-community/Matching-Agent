from enum import Enum


class DcimPowerOutletTemplatesListType(str, Enum):
    CALIFORNIA_STYLE = "California Style"
    DC = "DC"
    IEC_60309 = "IEC 60309"
    IEC_60320 = "IEC 60320"
    IEC_60906_1 = "IEC 60906-1"
    ITAINTERNATIONAL = "ITA/International"
    MOLEX = "Molex"
    NEMA_LOCKING = "NEMA (Locking)"
    NEMA_NON_LOCKING = "NEMA (Non-locking)"
    OTHER = "Other"
    PROPRIETARY = "Proprietary"
    USB = "USB"

    def __str__(self) -> str:
        return str(self.value)
