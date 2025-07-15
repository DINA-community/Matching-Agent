from enum import Enum


class CustomFieldChoiceSetBaseChoicesLabel(str, Enum):
    IATA_AIRPORT_CODES = "IATA (Airport codes)"
    ISO_3166_COUNTRY_CODES = "ISO 3166 (Country codes)"
    UNLOCODE_LOCATION_CODES = "UN/LOCODE (Location codes)"

    def __str__(self) -> str:
        return str(self.value)
