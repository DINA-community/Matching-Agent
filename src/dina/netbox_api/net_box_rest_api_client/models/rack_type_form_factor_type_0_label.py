from enum import Enum


class RackTypeFormFactorType0Label(str, Enum):
    VALUE_0 = "2-post frame"
    VALUE_1 = "4-post frame"
    VALUE_2 = "4-post cabinet"
    WALL_MOUNTED_CABINET = "Wall-mounted cabinet"
    WALL_MOUNTED_CABINET_VERTICAL = "Wall-mounted cabinet (vertical)"
    WALL_MOUNTED_FRAME = "Wall-mounted frame"
    WALL_MOUNTED_FRAME_VERTICAL = "Wall-mounted frame (vertical)"

    def __str__(self) -> str:
        return str(self.value)
