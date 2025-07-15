from enum import IntEnum


class IPAddressFamilyValue(IntEnum):
    VALUE_4 = 4
    VALUE_6 = 6

    def __str__(self) -> str:
        return str(self.value)
