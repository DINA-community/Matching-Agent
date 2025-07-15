from enum import Enum


class DataSourceTypeLabel(str, Enum):
    AMAZON_S3 = "Amazon S3"
    GIT = "Git"
    LOCAL = "Local"
    VALUE_0 = "---------"

    def __str__(self) -> str:
        return str(self.value)
