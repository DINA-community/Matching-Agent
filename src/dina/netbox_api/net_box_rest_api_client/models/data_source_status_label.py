from enum import Enum


class DataSourceStatusLabel(str, Enum):
    COMPLETED = "Completed"
    FAILED = "Failed"
    NEW = "New"
    QUEUED = "Queued"
    SYNCING = "Syncing"

    def __str__(self) -> str:
        return str(self.value)
