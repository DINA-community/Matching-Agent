from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_software import BriefSoftware
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Hash")


@_attrs_define
class Hash:
    """REST API Model Serializer for Hash.

    Attributes:
        id (int):
        software (BriefSoftware): REST API Model Serializer for Software.
        filename (str):
        tags (Union[Unset, list['NestedTag']]):
    """

    id: int
    software: "BriefSoftware"
    filename: str
    tags: Union[Unset, list["NestedTag"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        software = self.software.to_dict()

        filename = self.filename

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
                "software": software,
                "filename": filename,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_software import BriefSoftware
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        software = BriefSoftware.from_dict(d.pop("software"))

        filename = d.pop("filename")

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        hash_ = cls(
            id=id,
            software=software,
            filename=filename,
            tags=tags,
        )

        hash_.additional_properties = d
        return hash_

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
