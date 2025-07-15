from enum import Enum


class EventRuleActionTypeLabel(str, Enum):
    NOTIFICATION = "Notification"
    SCRIPT = "Script"
    WEBHOOK = "Webhook"

    def __str__(self) -> str:
        return str(self.value)
