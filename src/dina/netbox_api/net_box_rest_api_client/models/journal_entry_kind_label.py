from enum import Enum


class JournalEntryKindLabel(str, Enum):
    DANGER = "Danger"
    INFO = "Info"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
