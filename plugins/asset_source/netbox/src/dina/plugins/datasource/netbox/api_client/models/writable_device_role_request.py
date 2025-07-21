import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_config_template_request import BriefConfigTemplateRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_device_role_request_custom_fields import (
        WritableDeviceRoleRequestCustomFields,
    )


T = TypeVar("T", bound="WritableDeviceRoleRequest")


@_attrs_define
class WritableDeviceRoleRequest:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        name (str):
        slug (str):
        color (Union[Unset, str]):
        vm_role (Union[Unset, bool]): Virtual machines may be assigned to this role
        config_template (Union['BriefConfigTemplateRequest', None, Unset, int]):
        parent (Union[None, Unset, int]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableDeviceRoleRequestCustomFields]):
        comments (Union[Unset, str]):
    """

    name: str
    slug: str
    color: Union[Unset, str] = UNSET
    vm_role: Union[Unset, bool] = UNSET
    config_template: Union["BriefConfigTemplateRequest", None, Unset, int] = UNSET
    parent: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableDeviceRoleRequestCustomFields"] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_config_template_request import BriefConfigTemplateRequest

        name = self.name

        slug = self.slug

        color = self.color

        vm_role = self.vm_role

        config_template: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, BriefConfigTemplateRequest):
            config_template = self.config_template.to_dict()
        else:
            config_template = self.config_template

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

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

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if vm_role is not UNSET:
            field_dict["vm_role"] = vm_role
        if config_template is not UNSET:
            field_dict["config_template"] = config_template
        if parent is not UNSET:
            field_dict["parent"] = parent
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        color = (
            self.color
            if isinstance(self.color, Unset)
            else (None, str(self.color).encode(), "text/plain")
        )

        vm_role = (
            self.vm_role
            if isinstance(self.vm_role, Unset)
            else (None, str(self.vm_role).encode(), "text/plain")
        )

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

        parent: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, int):
            parent = (None, str(self.parent).encode(), "text/plain")
        else:
            parent = (None, str(self.parent).encode(), "text/plain")

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

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if vm_role is not UNSET:
            field_dict["vm_role"] = vm_role
        if config_template is not UNSET:
            field_dict["config_template"] = config_template
        if parent is not UNSET:
            field_dict["parent"] = parent
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_device_role_request_custom_fields import (
            WritableDeviceRoleRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        color = d.pop("color", UNSET)

        vm_role = d.pop("vm_role", UNSET)

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

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableDeviceRoleRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableDeviceRoleRequestCustomFields.from_dict(
                _custom_fields
            )

        comments = d.pop("comments", UNSET)

        writable_device_role_request = cls(
            name=name,
            slug=slug,
            color=color,
            vm_role=vm_role,
            config_template=config_template,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            comments=comments,
        )

        writable_device_role_request.additional_properties = d
        return writable_device_role_request

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
