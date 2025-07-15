from enum import Enum


class WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1(str, Enum):
    IATA = "IATA"
    ISO_3166 = "ISO_3166"
    UN_LOCODE = "UN_LOCODE"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
