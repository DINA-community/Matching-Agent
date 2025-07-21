from enum import Enum


class BriefJobStatusLabel(str, Enum):
    COMPLETED = "Completed"
    ERRORED = "Errored"
    FAILED = "Failed"
    PENDING = "Pending"
    RUNNING = "Running"
    SCHEDULED = "Scheduled"

    def __str__(self) -> str:
        return str(self.value)
