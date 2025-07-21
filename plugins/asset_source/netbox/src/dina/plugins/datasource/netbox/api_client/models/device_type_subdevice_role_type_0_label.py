from enum import Enum


class DeviceTypeSubdeviceRoleType0Label(str, Enum):
    CHILD = "Child"
    PARENT = "Parent"

    def __str__(self) -> str:
        return str(self.value)
