from enum import Enum


class PatchedCustomLinkRequestButtonClass(str, Enum):
    BLACK = "black"
    BLUE = "blue"
    CYAN = "cyan"
    DEFAULT = "default"
    GHOST_DARK = "ghost-dark"
    GRAY = "gray"
    GREEN = "green"
    INDIGO = "indigo"
    ORANGE = "orange"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    TEAL = "teal"
    WHITE = "white"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
