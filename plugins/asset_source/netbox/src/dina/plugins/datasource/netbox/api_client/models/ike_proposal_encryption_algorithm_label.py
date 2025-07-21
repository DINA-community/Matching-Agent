from enum import Enum


class IKEProposalEncryptionAlgorithmLabel(str, Enum):
    DES = "DES"
    VALUE_0 = "128-bit AES (CBC)"
    VALUE_1 = "128-bit AES (GCM)"
    VALUE_2 = "192-bit AES (CBC)"
    VALUE_3 = "192-bit AES (GCM)"
    VALUE_4 = "256-bit AES (CBC)"
    VALUE_5 = "256-bit AES (GCM)"
    VALUE_6 = "3DES"

    def __str__(self) -> str:
        return str(self.value)
