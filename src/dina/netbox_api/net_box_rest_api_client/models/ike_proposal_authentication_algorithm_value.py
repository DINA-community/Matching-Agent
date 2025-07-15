from enum import Enum


class IKEProposalAuthenticationAlgorithmValue(str, Enum):
    HMAC_MD5 = "hmac-md5"
    HMAC_SHA1 = "hmac-sha1"
    HMAC_SHA256 = "hmac-sha256"
    HMAC_SHA384 = "hmac-sha384"
    HMAC_SHA512 = "hmac-sha512"

    def __str__(self) -> str:
        return str(self.value)
