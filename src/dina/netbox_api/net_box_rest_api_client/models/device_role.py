import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_config_template import BriefConfigTemplate
    from ..models.device_role_custom_fields import DeviceRoleCustomFields
    from ..models.nested_device_role import NestedDeviceRole
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="DeviceRole")


@_attrs_define
class DeviceRole:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        field_depth (int):
        color (Union[Unset, str]):
        vm_role (Union[Unset, bool]): Virtual machines may be assigned to this role
        config_template (Union['BriefConfigTemplate', None, Unset]):
        parent (Union['NestedDeviceRole', None, Unset]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, DeviceRoleCustomFields]):
        device_count (Union[Unset, int]):
        virtualmachine_count (Union[Unset, int]):
        comments (Union[Unset, str]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_depth: int
    color: Union[Unset, str] = UNSET
    vm_role: Union[Unset, bool] = UNSET
    config_template: Union["BriefConfigTemplate", None, Unset] = UNSET
    parent: Union["NestedDeviceRole", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "DeviceRoleCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    virtualmachine_count: Union[Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.nested_device_role import NestedDeviceRole

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        slug = self.slug

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

        field_depth = self.field_depth

        color = self.color

        vm_role = self.vm_role

        config_template: Union[None, Unset, dict[str, Any]]
        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, BriefConfigTemplate):
            config_template = self.config_template.to_dict()
        else:
            config_template = self.config_template

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedDeviceRole):
            parent = self.parent.to_dict()
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

        device_count = self.device_count

        virtualmachine_count = self.virtualmachine_count

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
                "_depth": field_depth,
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
        if device_count is not UNSET:
            field_dict["device_count"] = device_count
        if virtualmachine_count is not UNSET:
            field_dict["virtualmachine_count"] = virtualmachine_count
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.device_role_custom_fields import DeviceRoleCustomFields
        from ..models.nested_device_role import NestedDeviceRole
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

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

        field_depth = d.pop("_depth")

        color = d.pop("color", UNSET)

        vm_role = d.pop("vm_role", UNSET)

        def _parse_config_template(data: object) -> Union["BriefConfigTemplate", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_template_type_1 = BriefConfigTemplate.from_dict(data)

                return config_template_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefConfigTemplate", None, Unset], data)

        config_template = _parse_config_template(d.pop("config_template", UNSET))

        def _parse_parent(data: object) -> Union["NestedDeviceRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedDeviceRole.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDeviceRole", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, DeviceRoleCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DeviceRoleCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        virtualmachine_count = d.pop("virtualmachine_count", UNSET)

        comments = d.pop("comments", UNSET)

        device_role = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            created=created,
            last_updated=last_updated,
            field_depth=field_depth,
            color=color,
            vm_role=vm_role,
            config_template=config_template,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
            virtualmachine_count=virtualmachine_count,
            comments=comments,
        )

        device_role.additional_properties = d
        return device_role

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
