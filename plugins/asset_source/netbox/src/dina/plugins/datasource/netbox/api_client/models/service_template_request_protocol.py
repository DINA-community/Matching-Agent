from enum import Enum


class ServiceTemplateRequestProtocol(str, Enum):
    SCTP = "sctp"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
