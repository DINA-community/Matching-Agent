import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_sec_profile import BriefIPSecProfile
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_tunnel_group import BriefTunnelGroup
    from ..models.nested_tag import NestedTag
    from ..models.tunnel_custom_fields import TunnelCustomFields
    from ..models.tunnel_encapsulation import TunnelEncapsulation
    from ..models.tunnel_status import TunnelStatus


T = TypeVar("T", bound="Tunnel")


@_attrs_define
class Tunnel:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        status (TunnelStatus):
        encapsulation (TunnelEncapsulation):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        terminations_count (int):
        group (Union['BriefTunnelGroup', None, Unset]):
        ipsec_profile (Union['BriefIPSecProfile', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        tunnel_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, TunnelCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    status: "TunnelStatus"
    encapsulation: "TunnelEncapsulation"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    terminations_count: int
    group: Union["BriefTunnelGroup", None, Unset] = UNSET
    ipsec_profile: Union["BriefIPSecProfile", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    tunnel_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "TunnelCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ip_sec_profile import BriefIPSecProfile
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_tunnel_group import BriefTunnelGroup

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        status = self.status.to_dict()

        encapsulation = self.encapsulation.to_dict()

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

        terminations_count = self.terminations_count

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefTunnelGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        ipsec_profile: Union[None, Unset, dict[str, Any]]
        if isinstance(self.ipsec_profile, Unset):
            ipsec_profile = UNSET
        elif isinstance(self.ipsec_profile, BriefIPSecProfile):
            ipsec_profile = self.ipsec_profile.to_dict()
        else:
            ipsec_profile = self.ipsec_profile

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        tunnel_id: Union[None, Unset, int]
        if isinstance(self.tunnel_id, Unset):
            tunnel_id = UNSET
        else:
            tunnel_id = self.tunnel_id

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
                "name": name,
                "status": status,
                "encapsulation": encapsulation,
                "created": created,
                "last_updated": last_updated,
                "terminations_count": terminations_count,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if ipsec_profile is not UNSET:
            field_dict["ipsec_profile"] = ipsec_profile
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tunnel_id is not UNSET:
            field_dict["tunnel_id"] = tunnel_id
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
        from ..models.brief_ip_sec_profile import BriefIPSecProfile
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_tunnel_group import BriefTunnelGroup
        from ..models.nested_tag import NestedTag
        from ..models.tunnel_custom_fields import TunnelCustomFields
        from ..models.tunnel_encapsulation import TunnelEncapsulation
        from ..models.tunnel_status import TunnelStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        status = TunnelStatus.from_dict(d.pop("status"))

        encapsulation = TunnelEncapsulation.from_dict(d.pop("encapsulation"))

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

        terminations_count = d.pop("terminations_count")

        def _parse_group(data: object) -> Union["BriefTunnelGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefTunnelGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTunnelGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_ipsec_profile(data: object) -> Union["BriefIPSecProfile", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ipsec_profile_type_1 = BriefIPSecProfile.from_dict(data)

                return ipsec_profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPSecProfile", None, Unset], data)

        ipsec_profile = _parse_ipsec_profile(d.pop("ipsec_profile", UNSET))

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

        def _parse_tunnel_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tunnel_id = _parse_tunnel_id(d.pop("tunnel_id", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, TunnelCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TunnelCustomFields.from_dict(_custom_fields)

        tunnel = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            status=status,
            encapsulation=encapsulation,
            created=created,
            last_updated=last_updated,
            terminations_count=terminations_count,
            group=group,
            ipsec_profile=ipsec_profile,
            tenant=tenant,
            tunnel_id=tunnel_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        tunnel.additional_properties = d
        return tunnel

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
