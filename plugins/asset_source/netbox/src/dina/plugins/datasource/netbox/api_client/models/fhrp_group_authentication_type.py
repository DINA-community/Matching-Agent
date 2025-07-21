from enum import Enum


class FHRPGroupAuthenticationType(str, Enum):
    MD5 = "md5"
    PLAINTEXT = "plaintext"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
