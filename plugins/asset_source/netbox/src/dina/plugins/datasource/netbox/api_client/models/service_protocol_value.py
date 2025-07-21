from enum import Enum


class ServiceProtocolValue(str, Enum):
    SCTP = "sctp"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
