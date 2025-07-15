from enum import Enum


class JobStatusValue(str, Enum):
    COMPLETED = "completed"
    ERRORED = "errored"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
