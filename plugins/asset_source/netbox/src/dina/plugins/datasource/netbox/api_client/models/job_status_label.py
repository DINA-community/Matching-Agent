from enum import Enum


class JobStatusLabel(str, Enum):
    COMPLETED = "Completed"
    ERRORED = "Errored"
    FAILED = "Failed"
    PENDING = "Pending"
    RUNNING = "Running"
    SCHEDULED = "Scheduled"

    def __str__(self) -> str:
        return str(self.value)
