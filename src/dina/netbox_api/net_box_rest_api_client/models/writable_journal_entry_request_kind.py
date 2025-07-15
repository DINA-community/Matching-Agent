from enum import Enum


class WritableJournalEntryRequestKind(str, Enum):
    DANGER = "danger"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
