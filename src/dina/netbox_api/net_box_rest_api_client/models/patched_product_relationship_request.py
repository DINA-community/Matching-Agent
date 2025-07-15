from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_product_relationship_request_category import PatchedProductRelationshipRequestCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProductRelationshipRequest")


@_attrs_define
class PatchedProductRelationshipRequest:
    """REST API Model Serializer for ProductRelationship.

    Attributes:
        source_type (Union[Unset, str]):
        source_id (Union[Unset, int]):
        category (Union[Unset, PatchedProductRelationshipRequestCategory]): * `1` - default_component_of
            * `2` - external_component_of
            * `3` - installed_on
            * `4` - installed_with
            * `5` - optional_component_of
        destination_type (Union[Unset, str]):
        destination_id (Union[Unset, int]):
    """

    source_type: Union[Unset, str] = UNSET
    source_id: Union[Unset, int] = UNSET
    category: Union[Unset, PatchedProductRelationshipRequestCategory] = UNSET
    destination_type: Union[Unset, str] = UNSET
    destination_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        source_id = self.source_id

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        destination_type = self.destination_type

        destination_id = self.destination_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if category is not UNSET:
            field_dict["category"] = category
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if destination_id is not UNSET:
            field_dict["destination_id"] = destination_id

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        source_type = (
            self.source_type
            if isinstance(self.source_type, Unset)
            else (None, str(self.source_type).encode(), "text/plain")
        )

        source_id = (
            self.source_id if isinstance(self.source_id, Unset) else (None, str(self.source_id).encode(), "text/plain")
        )

        category: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.category, Unset):
            category = (None, str(self.category.value).encode(), "text/plain")

        destination_type = (
            self.destination_type
            if isinstance(self.destination_type, Unset)
            else (None, str(self.destination_type).encode(), "text/plain")
        )

        destination_id = (
            self.destination_id
            if isinstance(self.destination_id, Unset)
            else (None, str(self.destination_id).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if category is not UNSET:
            field_dict["category"] = category
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if destination_id is not UNSET:
            field_dict["destination_id"] = destination_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_type = d.pop("source_type", UNSET)

        source_id = d.pop("source_id", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PatchedProductRelationshipRequestCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PatchedProductRelationshipRequestCategory(_category)

        destination_type = d.pop("destination_type", UNSET)

        destination_id = d.pop("destination_id", UNSET)

        patched_product_relationship_request = cls(
            source_type=source_type,
            source_id=source_id,
            category=category,
            destination_type=destination_type,
            destination_id=destination_id,
        )

        patched_product_relationship_request.additional_properties = d
        return patched_product_relationship_request

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
