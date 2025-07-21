from enum import Enum


class WritableInterfaceRequestPoeTypeType1(str, Enum):
    PASSIVE_24V_2PAIR = "passive-24v-2pair"
    PASSIVE_24V_4PAIR = "passive-24v-4pair"
    PASSIVE_48V_2PAIR = "passive-48v-2pair"
    PASSIVE_48V_4PAIR = "passive-48v-4pair"
    TYPE1_IEEE802_3AF = "type1-ieee802.3af"
    TYPE2_IEEE802_3AT = "type2-ieee802.3at"
    TYPE3_IEEE802_3BT = "type3-ieee802.3bt"
    TYPE4_IEEE802_3BT = "type4-ieee802.3bt"
    VALUE_8 = ""

    def __str__(self) -> str:
        return str(self.value)
