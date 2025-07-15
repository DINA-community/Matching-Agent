from enum import Enum


class NotificationEvent(str, Enum):
    JOB_COMPLETED = "job_completed"
    JOB_ERRORED = "job_errored"
    JOB_FAILED = "job_failed"
    JOB_STARTED = "job_started"
    OBJECT_CREATED = "object_created"
    OBJECT_DELETED = "object_deleted"
    OBJECT_UPDATED = "object_updated"

    def __str__(self) -> str:
        return str(self.value)
