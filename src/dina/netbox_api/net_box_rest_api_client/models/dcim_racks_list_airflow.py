from enum import Enum


class DcimRacksListAirflow(str, Enum):
    FRONT_TO_REAR = "front-to-rear"
    REAR_TO_FRONT = "rear-to-front"

    def __str__(self) -> str:
        return str(self.value)
