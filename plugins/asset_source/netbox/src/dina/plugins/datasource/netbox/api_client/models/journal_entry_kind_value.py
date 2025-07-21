from enum import Enum


class JournalEntryKindValue(str, Enum):
    DANGER = "danger"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
