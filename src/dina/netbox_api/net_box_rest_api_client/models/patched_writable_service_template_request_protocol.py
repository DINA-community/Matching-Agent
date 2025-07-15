from enum import Enum


class PatchedWritableServiceTemplateRequestProtocol(str, Enum):
    SCTP = "sctp"
    TCP = "tcp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
