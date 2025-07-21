from enum import Enum


class WritableCableRequestTypeType2Type1(str, Enum):
    AOC = "aoc"
    CAT3 = "cat3"
    CAT5 = "cat5"
    CAT5E = "cat5e"
    CAT6 = "cat6"
    CAT6A = "cat6a"
    CAT7 = "cat7"
    CAT7A = "cat7a"
    CAT8 = "cat8"
    COAXIAL = "coaxial"
    DAC_ACTIVE = "dac-active"
    DAC_PASSIVE = "dac-passive"
    MMF = "mmf"
    MMF_OM1 = "mmf-om1"
    MMF_OM2 = "mmf-om2"
    MMF_OM3 = "mmf-om3"
    MMF_OM4 = "mmf-om4"
    MMF_OM5 = "mmf-om5"
    MRJ21_TRUNK = "mrj21-trunk"
    POWER = "power"
    SMF = "smf"
    SMF_OS1 = "smf-os1"
    SMF_OS2 = "smf-os2"
    USB = "usb"
    VALUE_24 = ""

    def __str__(self) -> str:
        return str(self.value)
