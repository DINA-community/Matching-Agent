from enum import Enum


class InterfaceTemplateRfRoleType0Label(str, Enum):
    ACCESS_POINT = "Access point"
    STATION = "Station"

    def __str__(self) -> str:
        return str(self.value)
