from enum import Enum


class PatchedWritableRackRequestFormFactorType2Type1(str, Enum):
    VALUE_0 = "2-post-frame"
    VALUE_1 = "4-post-frame"
    VALUE_2 = "4-post-cabinet"
    VALUE_7 = ""
    WALL_CABINET = "wall-cabinet"
    WALL_CABINET_VERTICAL = "wall-cabinet-vertical"
    WALL_FRAME = "wall-frame"
    WALL_FRAME_VERTICAL = "wall-frame-vertical"

    def __str__(self) -> str:
        return str(self.value)
