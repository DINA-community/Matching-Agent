from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.nested_module_bay import NestedModuleBay


T = TypeVar("T", bound="BriefModule")


@_attrs_define
class BriefModule:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        module_bay (NestedModuleBay): Represents an object related through a ForeignKey field. On write, it accepts a
            primary key (PK) value or a
            dictionary of attributes which can be used to uniquely identify the related object. This class should be
            subclassed to return a full representation of the related object on read.
    """

    id: int
    url: str
    display: str
    device: "BriefDevice"
    module_bay: "NestedModuleBay"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        device = self.device.to_dict()

        module_bay = self.module_bay.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "device": device,
                "module_bay": module_bay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device import BriefDevice
        from ..models.nested_module_bay import NestedModuleBay

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        module_bay = NestedModuleBay.from_dict(d.pop("module_bay"))

        brief_module = cls(
            id=id,
            url=url,
            display=display,
            device=device,
            module_bay=module_bay,
        )

        brief_module.additional_properties = d
        return brief_module

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
