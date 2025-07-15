from enum import Enum


class PatchedWritableDeviceWithConfigContextRequestRackFace(str, Enum):
    FRONT = "front"
    REAR = "rear"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
