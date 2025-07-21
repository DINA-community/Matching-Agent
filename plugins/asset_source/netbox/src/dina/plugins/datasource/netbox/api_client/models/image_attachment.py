import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageAttachment")


@_attrs_define
class ImageAttachment:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display (str):
            object_type (str):
            object_id (int):
            parent (Any):
            image (str):
            image_height (int):
            image_width (int):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            name (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    object_type: str
    object_id: int
    parent: Any
    image: str
    image_height: int
    image_width: int
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        object_type = self.object_type

        object_id = self.object_id

        parent = self.parent

        image = self.image

        image_height = self.image_height

        image_width = self.image_width

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "object_type": object_type,
                "object_id": object_id,
                "parent": parent,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        parent = d.pop("parent")

        image = d.pop("image")

        image_height = d.pop("image_height")

        image_width = d.pop("image_width")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

        name = d.pop("name", UNSET)

        image_attachment = cls(
            id=id,
            url=url,
            display=display,
            object_type=object_type,
            object_id=object_id,
            parent=parent,
            image=image,
            image_height=image_height,
            image_width=image_width,
            created=created,
            last_updated=last_updated,
            name=name,
        )

        image_attachment.additional_properties = d
        return image_attachment

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
