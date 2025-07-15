import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_role import BriefRole
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_vlan import BriefVLAN
    from ..models.brief_vrf import BriefVRF
    from ..models.nested_tag import NestedTag
    from ..models.prefix_custom_fields import PrefixCustomFields
    from ..models.prefix_family import PrefixFamily
    from ..models.prefix_status import PrefixStatus


T = TypeVar("T", bound="Prefix")


@_attrs_define
class Prefix:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        family (PrefixFamily):
        prefix (str):
        scope (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        children (int):
        field_depth (int):
        vrf (Union['BriefVRF', None, Unset]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        tenant (Union['BriefTenant', None, Unset]):
        vlan (Union['BriefVLAN', None, Unset]):
        status (Union[Unset, PrefixStatus]):
        role (Union['BriefRole', None, Unset]):
        is_pool (Union[Unset, bool]): All IP addresses within this prefix are considered usable
        mark_utilized (Union[Unset, bool]): Treat as fully utilized
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, PrefixCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    family: "PrefixFamily"
    prefix: str
    scope: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    children: int
    field_depth: int
    vrf: Union["BriefVRF", None, Unset] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    vlan: Union["BriefVLAN", None, Unset] = UNSET
    status: Union[Unset, "PrefixStatus"] = UNSET
    role: Union["BriefRole", None, Unset] = UNSET
    is_pool: Union[Unset, bool] = UNSET
    mark_utilized: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "PrefixCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_role import BriefRole
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vrf import BriefVRF

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        family = self.family.to_dict()

        prefix = self.prefix

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

        children = self.children

        field_depth = self.field_depth

        vrf: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRF):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

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

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        vlan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vlan, Unset):
            vlan = UNSET
        elif isinstance(self.vlan, BriefVLAN):
            vlan = self.vlan.to_dict()
        else:
            vlan = self.vlan

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefRole):
            role = self.role.to_dict()
        else:
            role = self.role

        is_pool = self.is_pool

        mark_utilized = self.mark_utilized

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "family": family,
                "prefix": prefix,
                "scope": scope,
                "created": created,
                "last_updated": last_updated,
                "children": children,
                "_depth": field_depth,
            }
        )
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if is_pool is not UNSET:
            field_dict["is_pool"] = is_pool
        if mark_utilized is not UNSET:
            field_dict["mark_utilized"] = mark_utilized
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_role import BriefRole
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vrf import BriefVRF
        from ..models.nested_tag import NestedTag
        from ..models.prefix_custom_fields import PrefixCustomFields
        from ..models.prefix_family import PrefixFamily
        from ..models.prefix_status import PrefixStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        family = PrefixFamily.from_dict(d.pop("family"))

        prefix = d.pop("prefix")

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

        children = d.pop("children")

        field_depth = d.pop("_depth")

        def _parse_vrf(data: object) -> Union["BriefVRF", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrf_type_1 = BriefVRF.from_dict(data)

                return vrf_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVRF", None, Unset], data)

        vrf = _parse_vrf(d.pop("vrf", UNSET))

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

        def _parse_vlan(data: object) -> Union["BriefVLAN", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vlan_type_1 = BriefVLAN.from_dict(data)

                return vlan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLAN", None, Unset], data)

        vlan = _parse_vlan(d.pop("vlan", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PrefixStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PrefixStatus.from_dict(_status)

        def _parse_role(data: object) -> Union["BriefRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefRole.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRole", None, Unset], data)

        role = _parse_role(d.pop("role", UNSET))

        is_pool = d.pop("is_pool", UNSET)

        mark_utilized = d.pop("mark_utilized", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PrefixCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PrefixCustomFields.from_dict(_custom_fields)

        prefix = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            family=family,
            prefix=prefix,
            scope=scope,
            created=created,
            last_updated=last_updated,
            children=children,
            field_depth=field_depth,
            vrf=vrf,
            scope_type=scope_type,
            scope_id=scope_id,
            tenant=tenant,
            vlan=vlan,
            status=status,
            role=role,
            is_pool=is_pool,
            mark_utilized=mark_utilized,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        prefix.additional_properties = d
        return prefix

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
