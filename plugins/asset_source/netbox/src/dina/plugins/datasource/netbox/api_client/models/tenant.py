import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_group import BriefTenantGroup
    from ..models.nested_tag import NestedTag
    from ..models.tenant_custom_fields import TenantCustomFields


T = TypeVar("T", bound="Tenant")


@_attrs_define
class Tenant:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        circuit_count (int):
        ipaddress_count (int):
        prefix_count (int):
        rack_count (int):
        site_count (int):
        vlan_count (int):
        vrf_count (int):
        cluster_count (int):
        group (Union['BriefTenantGroup', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, TenantCustomFields]):
        device_count (Union[Unset, int]):
        virtualmachine_count (Union[Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    circuit_count: int
    ipaddress_count: int
    prefix_count: int
    rack_count: int
    site_count: int
    vlan_count: int
    vrf_count: int
    cluster_count: int
    group: Union["BriefTenantGroup", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "TenantCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    virtualmachine_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_group import BriefTenantGroup

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

        circuit_count = self.circuit_count

        ipaddress_count = self.ipaddress_count

        prefix_count = self.prefix_count

        rack_count = self.rack_count

        site_count = self.site_count

        vlan_count = self.vlan_count

        vrf_count = self.vrf_count

        cluster_count = self.cluster_count

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefTenantGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        description = self.description

        comments = self.comments

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
                "circuit_count": circuit_count,
                "ipaddress_count": ipaddress_count,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
                "cluster_count": cluster_count,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if device_count is not UNSET:
            field_dict["device_count"] = device_count
        if virtualmachine_count is not UNSET:
            field_dict["virtualmachine_count"] = virtualmachine_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant_group import BriefTenantGroup
        from ..models.nested_tag import NestedTag
        from ..models.tenant_custom_fields import TenantCustomFields

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

        circuit_count = d.pop("circuit_count")

        ipaddress_count = d.pop("ipaddress_count")

        prefix_count = d.pop("prefix_count")

        rack_count = d.pop("rack_count")

        site_count = d.pop("site_count")

        vlan_count = d.pop("vlan_count")

        vrf_count = d.pop("vrf_count")

        cluster_count = d.pop("cluster_count")

        def _parse_group(data: object) -> Union["BriefTenantGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefTenantGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenantGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, TenantCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TenantCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        virtualmachine_count = d.pop("virtualmachine_count", UNSET)

        tenant = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            created=created,
            last_updated=last_updated,
            circuit_count=circuit_count,
            ipaddress_count=ipaddress_count,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            cluster_count=cluster_count,
            group=group,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
            virtualmachine_count=virtualmachine_count,
        )

        tenant.additional_properties = d
        return tenant

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
