from enum import Enum


class RackRequestAirflow(str, Enum):
    FRONT_TO_REAR = "front-to-rear"
    REAR_TO_FRONT = "rear-to-front"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
