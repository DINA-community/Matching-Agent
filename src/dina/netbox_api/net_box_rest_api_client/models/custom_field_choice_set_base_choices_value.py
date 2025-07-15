from enum import Enum


class CustomFieldChoiceSetBaseChoicesValue(str, Enum):
    IATA = "IATA"
    ISO_3166 = "ISO_3166"
    UN_LOCODE = "UN_LOCODE"

    def __str__(self) -> str:
        return str(self.value)
