from enum import Enum


class IKEProposalAuthenticationMethodValue(str, Enum):
    CERTIFICATES = "certificates"
    DSA_SIGNATURES = "dsa-signatures"
    PRESHARED_KEYS = "preshared-keys"
    RSA_SIGNATURES = "rsa-signatures"

    def __str__(self) -> str:
        return str(self.value)
