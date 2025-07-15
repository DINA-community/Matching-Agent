from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_tag import BriefTag


T = TypeVar("T", bound="TaggedItem")


@_attrs_define
class TaggedItem:
    """
    Attributes:
        id (int):
        url (str):
        display (str):
        object_type (str):
        object_id (int):
        object_ (Any):
        tag (BriefTag): Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated
            instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)
    """

    id: int
    url: str
    display: str
    object_type: str
    object_id: int
    object_: Any
    tag: "BriefTag"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        object_type = self.object_type

        object_id = self.object_id

        object_ = self.object_

        tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "object_type": object_type,
                "object_id": object_id,
                "object": object_,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tag import BriefTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        object_ = d.pop("object")

        tag = BriefTag.from_dict(d.pop("tag"))

        tagged_item = cls(
            id=id,
            url=url,
            display=display,
            object_type=object_type,
            object_id=object_id,
            object_=object_,
            tag=tag,
        )

        tagged_item.additional_properties = d
        return tagged_item

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
