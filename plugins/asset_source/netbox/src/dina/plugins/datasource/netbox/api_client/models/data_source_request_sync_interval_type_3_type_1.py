from enum import IntEnum


class DataSourceRequestSyncIntervalType3Type1(IntEnum):
    VALUE_1 = 1
    VALUE_60 = 60
    VALUE_720 = 720
    VALUE_1440 = 1440
    VALUE_10080 = 10080
    VALUE_43200 = 43200

    def __str__(self) -> str:
        return str(self.value)
