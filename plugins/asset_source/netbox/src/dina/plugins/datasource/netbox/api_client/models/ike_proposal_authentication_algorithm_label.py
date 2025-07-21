from enum import Enum


class IKEProposalAuthenticationAlgorithmLabel(str, Enum):
    MD5_HMAC = "MD5 HMAC"
    SHA_1_HMAC = "SHA-1 HMAC"
    SHA_256_HMAC = "SHA-256 HMAC"
    SHA_384_HMAC = "SHA-384 HMAC"
    SHA_512_HMAC = "SHA-512 HMAC"

    def __str__(self) -> str:
        return str(self.value)
