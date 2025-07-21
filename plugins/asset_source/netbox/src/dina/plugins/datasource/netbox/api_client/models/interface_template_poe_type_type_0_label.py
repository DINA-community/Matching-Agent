from enum import Enum


class InterfaceTemplatePoeTypeType0Label(str, Enum):
    PASSIVE_24V_2_PAIR = "Passive 24V (2-pair)"
    PASSIVE_24V_4_PAIR = "Passive 24V (4-pair)"
    PASSIVE_48V_2_PAIR = "Passive 48V (2-pair)"
    PASSIVE_48V_4_PAIR = "Passive 48V (4-pair)"
    VALUE_0 = "802.3af (Type 1)"
    VALUE_1 = "802.3at (Type 2)"
    VALUE_2 = "802.3bt (Type 3)"
    VALUE_3 = "802.3bt (Type 4)"

    def __str__(self) -> str:
        return str(self.value)
