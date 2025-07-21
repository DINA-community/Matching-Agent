from enum import Enum


class CustomFieldTypeLabel(str, Enum):
    BOOLEAN_TRUEFALSE = "Boolean (true/false)"
    DATE = "Date"
    DATE_TIME = "Date & time"
    DECIMAL = "Decimal"
    INTEGER = "Integer"
    JSON = "JSON"
    MULTIPLE_OBJECTS = "Multiple objects"
    MULTIPLE_SELECTION = "Multiple selection"
    OBJECT = "Object"
    SELECTION = "Selection"
    TEXT = "Text"
    TEXT_LONG = "Text (long)"
    URL = "URL"

    def __str__(self) -> str:
        return str(self.value)
