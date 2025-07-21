from enum import Enum


class CoreObjectChangesListAction(str, Enum):
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
