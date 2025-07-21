from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hash_ import Hash
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="FileHash")


@_attrs_define
class FileHash:
    """REST API Model Serializer for FileHash.

    Attributes:
        id (int):
        algorithm (str):
        value (str):
        hash_ (Hash): REST API Model Serializer for Hash.
        tags (Union[Unset, list['NestedTag']]):
    """

    id: int
    algorithm: str
    value: str
    hash_: "Hash"
    tags: Union[Unset, list["NestedTag"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        algorithm = self.algorithm

        value = self.value

        hash_ = self.hash_.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "algorithm": algorithm,
                "value": value,
                "hash": hash_,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hash_ import Hash
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        algorithm = d.pop("algorithm")

        value = d.pop("value")

        hash_ = Hash.from_dict(d.pop("hash"))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        file_hash = cls(
            id=id,
            algorithm=algorithm,
            value=value,
            hash_=hash_,
            tags=tags,
        )

        file_hash.additional_properties = d
        return file_hash

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
