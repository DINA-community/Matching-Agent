from enum import Enum


class IKEProposalAuthenticationMethodLabel(str, Enum):
    CERTIFICATES = "Certificates"
    DSA_SIGNATURES = "DSA signatures"
    PRE_SHARED_KEYS = "Pre-shared keys"
    RSA_SIGNATURES = "RSA signatures"

    def __str__(self) -> str:
        return str(self.value)
