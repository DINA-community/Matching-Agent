from enum import Enum


class WritableCustomFieldRequestType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    DECIMAL = "decimal"
    INTEGER = "integer"
    JSON = "json"
    LONGTEXT = "longtext"
    MULTIOBJECT = "multiobject"
    MULTISELECT = "multiselect"
    OBJECT = "object"
    SELECT = "select"
    TEXT = "text"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
