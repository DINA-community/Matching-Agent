from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MappingRequest")


@_attrs_define
class MappingRequest:
    """REST API Model Serializer for Mapping.

    Attributes:
        type_ (str):
        name (str):
        data (Union[Unset, Any]):
    """

    type_: str
    name: str
    data: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        type_ = (None, str(self.type_).encode(), "text/plain")

        name = (None, str(self.name).encode(), "text/plain")

        data = (
            self.data
            if isinstance(self.data, Unset)
            else (None, str(self.data).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        data = d.pop("data", UNSET)

        mapping_request = cls(
            type_=type_,
            name=name,
            data=data,
        )

        mapping_request.additional_properties = d
        return mapping_request

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
