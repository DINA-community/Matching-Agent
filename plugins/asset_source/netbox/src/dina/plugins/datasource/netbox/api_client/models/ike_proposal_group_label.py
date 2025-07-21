from enum import Enum


class IKEProposalGroupLabel(str, Enum):
    GROUP_1 = "Group 1"
    GROUP_14 = "Group 14"
    GROUP_15 = "Group 15"
    GROUP_16 = "Group 16"
    GROUP_17 = "Group 17"
    GROUP_18 = "Group 18"
    GROUP_19 = "Group 19"
    GROUP_2 = "Group 2"
    GROUP_20 = "Group 20"
    GROUP_21 = "Group 21"
    GROUP_22 = "Group 22"
    GROUP_23 = "Group 23"
    GROUP_24 = "Group 24"
    GROUP_25 = "Group 25"
    GROUP_26 = "Group 26"
    GROUP_27 = "Group 27"
    GROUP_28 = "Group 28"
    GROUP_29 = "Group 29"
    GROUP_30 = "Group 30"
    GROUP_31 = "Group 31"
    GROUP_32 = "Group 32"
    GROUP_33 = "Group 33"
    GROUP_34 = "Group 34"
    GROUP_5 = "Group 5"

    def __str__(self) -> str:
        return str(self.value)
