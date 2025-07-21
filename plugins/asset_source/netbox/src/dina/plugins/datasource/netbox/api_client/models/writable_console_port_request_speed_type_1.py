from enum import IntEnum


class WritableConsolePortRequestSpeedType1(IntEnum):
    VALUE_1200 = 1200
    VALUE_2400 = 2400
    VALUE_4800 = 4800
    VALUE_9600 = 9600
    VALUE_19200 = 19200
    VALUE_38400 = 38400
    VALUE_57600 = 57600
    VALUE_115200 = 115200

    def __str__(self) -> str:
        return str(self.value)
