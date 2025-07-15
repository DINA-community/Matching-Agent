from enum import Enum


class VirtualizationVirtualMachinesRenderConfigCreateFormat(str, Enum):
    JSON = "json"
    TXT = "txt"

    def __str__(self) -> str:
        return str(self.value)
