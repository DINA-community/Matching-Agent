from enum import Enum


class ObjectChangeActionLabel(str, Enum):
    CREATED = "Created"
    DELETED = "Deleted"
    UPDATED = "Updated"

    def __str__(self) -> str:
        return str(self.value)
