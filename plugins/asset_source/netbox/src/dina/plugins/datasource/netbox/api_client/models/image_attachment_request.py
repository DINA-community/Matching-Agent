from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="ImageAttachmentRequest")


@_attrs_define
class ImageAttachmentRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_type (str):
            object_id (int):
            image (File):
            name (Union[Unset, str]):
    """

    object_type: str
    object_id: int
    image: File
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        object_id = self.object_id

        image = self.image.to_tuple()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "image": image,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_type = (None, str(self.object_type).encode(), "text/plain")

        object_id = (None, str(self.object_id).encode(), "text/plain")

        image = self.image.to_tuple()

        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "image": image,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        image = File(payload=BytesIO(d.pop("image")))

        name = d.pop("name", UNSET)

        image_attachment_request = cls(
            object_type=object_type,
            object_id=object_id,
            image=image,
            name=name,
        )

        image_attachment_request.additional_properties = d
        return image_attachment_request

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
