from enum import Enum


class DataSourceRequestTypeType1(str, Enum):
    AMAZON_S3 = "amazon-s3"
    GIT = "git"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
