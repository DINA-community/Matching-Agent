from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.nested_module_bay_request import NestedModuleBayRequest


T = TypeVar("T", bound="BriefModuleRequest")


@_attrs_define
class BriefModuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', int]):
        module_bay (NestedModuleBayRequest): Represents an object related through a ForeignKey field. On write, it
            accepts a primary key (PK) value or a
            dictionary of attributes which can be used to uniquely identify the related object. This class should be
            subclassed to return a full representation of the related object on read.
    """

    device: Union["BriefDeviceRequest", int]
    module_bay: "NestedModuleBayRequest"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest

        device: Union[dict[str, Any], int]
        if isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        module_bay = self.module_bay.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device": device,
                "module_bay": module_bay,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.nested_module_bay_request import NestedModuleBayRequest

        d = dict(src_dict)

        def _parse_device(data: object) -> Union["BriefDeviceRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", int], data)

        device = _parse_device(d.pop("device"))

        module_bay = NestedModuleBayRequest.from_dict(d.pop("module_bay"))

        brief_module_request = cls(
            device=device,
            module_bay=module_bay,
        )

        brief_module_request.additional_properties = d
        return brief_module_request

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
