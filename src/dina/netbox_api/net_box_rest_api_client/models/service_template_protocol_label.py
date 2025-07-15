from enum import Enum


class ServiceTemplateProtocolLabel(str, Enum):
    SCTP = "SCTP"
    TCP = "TCP"
    UDP = "UDP"

    def __str__(self) -> str:
        return str(self.value)
