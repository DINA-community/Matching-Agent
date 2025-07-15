from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_relationship_category import ProductRelationshipCategory

T = TypeVar("T", bound="ProductRelationship")


@_attrs_define
class ProductRelationship:
    """REST API Model Serializer for ProductRelationship.

    Attributes:
        id (int):
        source_type (str):
        source_id (int):
        source (Any):
        category (ProductRelationshipCategory): * `1` - default_component_of
            * `2` - external_component_of
            * `3` - installed_on
            * `4` - installed_with
            * `5` - optional_component_of
        destination_type (str):
        destination_id (int):
        destination (Any):
    """

    id: int
    source_type: str
    source_id: int
    source: Any
    category: ProductRelationshipCategory
    destination_type: str
    destination_id: int
    destination: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def method1(self):
        print ("HALLO productrelationship")

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source_type = self.source_type

        source_id = self.source_id

        source = self.source

        category = self.category.value

        destination_type = self.destination_type

        destination_id = self.destination_id

        destination = self.destination

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source_type": source_type,
                "source_id": source_id,
                "source": source,
                "category": category,
                "destination_type": destination_type,
                "destination_id": destination_id,
                "destination": destination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        source_type = d.pop("source_type")

        source_id = d.pop("source_id")

        source = d.pop("source")

        category = ProductRelationshipCategory(d.pop("category"))

        destination_type = d.pop("destination_type")

        destination_id = d.pop("destination_id")

        destination = d.pop("destination")

        product_relationship = cls(
            id=id,
            source_type=source_type,
            source_id=source_id,
            source=source,
            category=category,
            destination_type=destination_type,
            destination_id=destination_id,
            destination=destination,
        )

        product_relationship.additional_properties = d
        return product_relationship

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
