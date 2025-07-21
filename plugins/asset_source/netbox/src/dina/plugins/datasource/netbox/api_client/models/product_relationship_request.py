from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_relationship_request_category import (
    ProductRelationshipRequestCategory,
)

T = TypeVar("T", bound="ProductRelationshipRequest")


@_attrs_define
class ProductRelationshipRequest:
    """REST API Model Serializer for ProductRelationship.

    Attributes:
        source_type (str):
        source_id (int):
        category (ProductRelationshipRequestCategory): * `1` - default_component_of
            * `2` - external_component_of
            * `3` - installed_on
            * `4` - installed_with
            * `5` - optional_component_of
        destination_type (str):
        destination_id (int):
    """

    source_type: str
    source_id: int
    category: ProductRelationshipRequestCategory
    destination_type: str
    destination_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        source_id = self.source_id

        category = self.category.value

        destination_type = self.destination_type

        destination_id = self.destination_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
                "source_id": source_id,
                "category": category,
                "destination_type": destination_type,
                "destination_id": destination_id,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        source_type = (None, str(self.source_type).encode(), "text/plain")

        source_id = (None, str(self.source_id).encode(), "text/plain")

        category = (None, str(self.category.value).encode(), "text/plain")

        destination_type = (None, str(self.destination_type).encode(), "text/plain")

        destination_id = (None, str(self.destination_id).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "source_type": source_type,
                "source_id": source_id,
                "category": category,
                "destination_type": destination_type,
                "destination_id": destination_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_type = d.pop("source_type")

        source_id = d.pop("source_id")

        category = ProductRelationshipRequestCategory(d.pop("category"))

        destination_type = d.pop("destination_type")

        destination_id = d.pop("destination_id")

        product_relationship_request = cls(
            source_type=source_type,
            source_id=source_id,
            category=category,
            destination_type=destination_type,
            destination_id=destination_id,
        )

        product_relationship_request.additional_properties = d
        return product_relationship_request

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
