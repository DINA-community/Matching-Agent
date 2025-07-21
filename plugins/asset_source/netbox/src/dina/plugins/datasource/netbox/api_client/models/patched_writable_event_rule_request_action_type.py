from enum import Enum


class PatchedWritableEventRuleRequestActionType(str, Enum):
    NOTIFICATION = "notification"
    SCRIPT = "script"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
