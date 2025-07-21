from enum import Enum


class ConsoleServerPortSpeedType0Label(str, Enum):
    VALUE_0 = "1200 bps"
    VALUE_1 = "2400 bps"
    VALUE_2 = "4800 bps"
    VALUE_3 = "9600 bps"
    VALUE_4 = "19.2 kbps"
    VALUE_5 = "38.4 kbps"
    VALUE_6 = "57.6 kbps"
    VALUE_7 = "115.2 kbps"

    def __str__(self) -> str:
        return str(self.value)
