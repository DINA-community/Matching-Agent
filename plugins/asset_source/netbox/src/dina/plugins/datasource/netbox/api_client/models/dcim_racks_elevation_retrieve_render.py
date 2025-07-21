from enum import Enum


class DcimRacksElevationRetrieveRender(str, Enum):
    JSON = "json"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
