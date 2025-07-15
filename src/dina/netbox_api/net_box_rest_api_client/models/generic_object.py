from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenericObject")


@_attrs_define
class GenericObject:
    """Minimal representation of some generic object identified by ContentType and PK.

    Attributes:
        object_type (str):
        object_id (int):
        object_ (Any):
    """

    object_type: str
    object_id: int
    object_: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        object_id = self.object_id

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        object_ = d.pop("object")

        generic_object = cls(
            object_type=object_type,
            object_id=object_id,
            object_=object_,
        )

        generic_object.additional_properties = d
        return generic_object

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
