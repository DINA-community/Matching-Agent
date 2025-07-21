import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_config_template_request import BriefConfigTemplateRequest
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_platform_request_custom_fields import (
        PatchedPlatformRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedPlatformRequest")


@_attrs_define
class PatchedPlatformRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
        manufacturer (Union['BriefManufacturerRequest', None, Unset, int]):
        config_template (Union['BriefConfigTemplateRequest', None, Unset, int]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedPlatformRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    manufacturer: Union["BriefManufacturerRequest", None, Unset, int] = UNSET
    config_template: Union["BriefConfigTemplateRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedPlatformRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        name = self.name

        slug = self.slug

        manufacturer: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        config_template: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, BriefConfigTemplateRequest):
            config_template = self.config_template.to_dict()
        else:
            config_template = self.config_template

        description = self.description

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if config_template is not UNSET:
            field_dict["config_template"] = config_template
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        slug = (
            self.slug
            if isinstance(self.slug, Unset)
            else (None, str(self.slug).encode(), "text/plain")
        )

        manufacturer: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, int):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        elif isinstance(self.manufacturer, None):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        elif isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = (
                None,
                json.dumps(self.manufacturer.to_dict()).encode(),
                "application/json",
            )
        else:
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")

        config_template: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, int):
            config_template = (None, str(self.config_template).encode(), "text/plain")
        elif isinstance(self.config_template, None):
            config_template = (None, str(self.config_template).encode(), "text/plain")
        elif isinstance(self.config_template, BriefConfigTemplateRequest):
            config_template = (
                None,
                json.dumps(self.config_template.to_dict()).encode(),
                "application/json",
            )
        else:
            config_template = (None, str(self.config_template).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if config_template is not UNSET:
            field_dict["config_template"] = config_template
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_platform_request_custom_fields import (
            PatchedPlatformRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_manufacturer(
            data: object,
        ) -> Union["BriefManufacturerRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1_type_1 = BriefManufacturerRequest.from_dict(data)

                return manufacturer_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturerRequest", None, Unset, int], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_config_template(
            data: object,
        ) -> Union["BriefConfigTemplateRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_template_type_1_type_1 = BriefConfigTemplateRequest.from_dict(
                    data
                )

                return config_template_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefConfigTemplateRequest", None, Unset, int], data)

        config_template = _parse_config_template(d.pop("config_template", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedPlatformRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedPlatformRequestCustomFields.from_dict(_custom_fields)

        patched_platform_request = cls(
            name=name,
            slug=slug,
            manufacturer=manufacturer,
            config_template=config_template,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_platform_request.additional_properties = d
        return patched_platform_request

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
