import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.vlan_group_custom_fields import VLANGroupCustomFields


T = TypeVar("T", bound="VLANGroup")


@_attrs_define
class VLANGroup:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        slug (str):
        scope (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        vlan_count (int):
        utilization (str):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        vid_ranges (Union[Unset, list[list[list[int]]]]):
        tenant (Union['BriefTenant', None, Unset]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VLANGroupCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    scope: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    vlan_count: int
    utilization: str
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    vid_ranges: Union[Unset, list[list[list[int]]]] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VLANGroupCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        slug = self.slug

        scope = self.scope

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

        vlan_count = self.vlan_count

        utilization = self.utilization

        scope_type: Union[None, Unset, str]
        if isinstance(self.scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = self.scope_type

        scope_id: Union[None, Unset, int]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        vid_ranges: Union[Unset, list[list[list[int]]]] = UNSET
        if not isinstance(self.vid_ranges, Unset):
            vid_ranges = []
            for vid_ranges_item_data in self.vid_ranges:
                vid_ranges_item = []
                for componentsschemas_integer_range_item_data in vid_ranges_item_data:
                    componentsschemas_integer_range_item = componentsschemas_integer_range_item_data

                    vid_ranges_item.append(componentsschemas_integer_range_item)

                vid_ranges.append(vid_ranges_item)

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "slug": slug,
                "scope": scope,
                "created": created,
                "last_updated": last_updated,
                "vlan_count": vlan_count,
                "utilization": utilization,
            }
        )
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if vid_ranges is not UNSET:
            field_dict["vid_ranges"] = vid_ranges
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.vlan_group_custom_fields import VLANGroupCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

        scope = d.pop("scope")

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

        vlan_count = d.pop("vlan_count")

        utilization = d.pop("utilization")

        def _parse_scope_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_type = _parse_scope_type(d.pop("scope_type", UNSET))

        def _parse_scope_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scope_id = _parse_scope_id(d.pop("scope_id", UNSET))

        vid_ranges = []
        _vid_ranges = d.pop("vid_ranges", UNSET)
        for vid_ranges_item_data in _vid_ranges or []:
            vid_ranges_item = []
            _vid_ranges_item = vid_ranges_item_data
            for componentsschemas_integer_range_item_data in _vid_ranges_item:
                componentsschemas_integer_range_item = cast(list[int], componentsschemas_integer_range_item_data)

                vid_ranges_item.append(componentsschemas_integer_range_item)

            vid_ranges.append(vid_ranges_item)

        def _parse_tenant(data: object) -> Union["BriefTenant", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1 = BriefTenant.from_dict(data)

                return tenant_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenant", None, Unset], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VLANGroupCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VLANGroupCustomFields.from_dict(_custom_fields)

        vlan_group = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            scope=scope,
            created=created,
            last_updated=last_updated,
            vlan_count=vlan_count,
            utilization=utilization,
            scope_type=scope_type,
            scope_id=scope_id,
            vid_ranges=vid_ranges,
            tenant=tenant,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        vlan_group.additional_properties = d
        return vlan_group

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
