from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_device_request import NestedDeviceRequest


T = TypeVar("T", bound="BriefVirtualChassisRequest")


@_attrs_define
class BriefVirtualChassisRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        master (Union['NestedDeviceRequest', None, Unset]):
        description (Union[Unset, str]):
    """

    name: str
    master: Union["NestedDeviceRequest", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_device_request import NestedDeviceRequest

        name = self.name

        master: Union[None, Unset, dict[str, Any]]
        if isinstance(self.master, Unset):
            master = UNSET
        elif isinstance(self.master, NestedDeviceRequest):
            master = self.master.to_dict()
        else:
            master = self.master

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if master is not UNSET:
            field_dict["master"] = master
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_device_request import NestedDeviceRequest

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_master(data: object) -> Union["NestedDeviceRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                master_type_1 = NestedDeviceRequest.from_dict(data)

                return master_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDeviceRequest", None, Unset], data)

        master = _parse_master(d.pop("master", UNSET))

        description = d.pop("description", UNSET)

        brief_virtual_chassis_request = cls(
            name=name,
            master=master,
            description=description,
        )

        brief_virtual_chassis_request.additional_properties = d
        return brief_virtual_chassis_request

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
