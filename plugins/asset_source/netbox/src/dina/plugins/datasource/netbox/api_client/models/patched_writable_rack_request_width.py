from enum import IntEnum


class PatchedWritableRackRequestWidth(IntEnum):
    VALUE_10 = 10
    VALUE_19 = 19
    VALUE_21 = 21
    VALUE_23 = 23

    def __str__(self) -> str:
        return str(self.value)
