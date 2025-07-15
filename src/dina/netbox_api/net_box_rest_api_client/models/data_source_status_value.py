from enum import Enum


class DataSourceStatusValue(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    NEW = "new"
    QUEUED = "queued"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
