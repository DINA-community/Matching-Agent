from enum import Enum


class SchemaRetrieveLang(str, Enum):
    CS = "cs"
    DA = "da"
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"
    JA = "ja"
    NL = "nl"
    PL = "pl"
    PT = "pt"
    RU = "ru"
    TR = "tr"
    UK = "uk"
    ZH = "zh"

    def __str__(self) -> str:
        return str(self.value)
