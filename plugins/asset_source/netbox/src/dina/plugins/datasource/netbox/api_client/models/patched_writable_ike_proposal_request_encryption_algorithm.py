from enum import Enum


class PatchedWritableIKEProposalRequestEncryptionAlgorithm(str, Enum):
    AES_128_CBC = "aes-128-cbc"
    AES_128_GCM = "aes-128-gcm"
    AES_192_CBC = "aes-192-cbc"
    AES_192_GCM = "aes-192-gcm"
    AES_256_CBC = "aes-256-cbc"
    AES_256_GCM = "aes-256-gcm"
    DES_CBC = "des-cbc"
    VALUE_6 = "3des-cbc"

    def __str__(self) -> str:
        return str(self.value)
