from enum import Enum


class DeviceTypeRequestSubdeviceRoleType1(str, Enum):
    CHILD = "child"
    PARENT = "parent"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
