from enum import Enum


class IKEPolicyVersionLabel(str, Enum):
    IKEV1 = "IKEv1"
    IKEV2 = "IKEv2"

    def __str__(self) -> str:
        return str(self.value)
