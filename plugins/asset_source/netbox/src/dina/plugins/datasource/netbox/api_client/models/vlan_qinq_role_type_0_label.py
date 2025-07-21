from enum import Enum


class VLANQinqRoleType0Label(str, Enum):
    CUSTOMER = "Customer"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
