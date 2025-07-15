from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PatchedImageAttachmentRequest")


@_attrs_define
class PatchedImageAttachmentRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_type (Union[Unset, str]):
            object_id (Union[Unset, int]):
            name (Union[Unset, str]):
            image (Union[Unset, File]):
    """

    object_type: Union[Unset, str] = UNSET
    object_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    image: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        object_id = self.object_id

        name = self.name

        image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_type = (
            self.object_type
            if isinstance(self.object_type, Unset)
            else (None, str(self.object_type).encode(), "text/plain")
        )

        object_id = (
            self.object_id if isinstance(self.object_id, Unset) else (None, str(self.object_id).encode(), "text/plain")
        )

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        image: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_tuple()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("object_type", UNSET)

        object_id = d.pop("object_id", UNSET)

        name = d.pop("name", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, File]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = File(payload=BytesIO(_image))

        patched_image_attachment_request = cls(
            object_type=object_type,
            object_id=object_id,
            name=name,
            image=image,
        )

        patched_image_attachment_request.additional_properties = d
        return patched_image_attachment_request

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
