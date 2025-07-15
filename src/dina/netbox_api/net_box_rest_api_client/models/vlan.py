import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_l2vpn_termination import BriefL2VPNTermination
    from ..models.brief_role import BriefRole
    from ..models.brief_site import BriefSite
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_vlan_group import BriefVLANGroup
    from ..models.nested_tag import NestedTag
    from ..models.nested_vlan import NestedVLAN
    from ..models.vlan_custom_fields import VLANCustomFields
    from ..models.vlan_qinq_role_type_0 import VLANQinqRoleType0
    from ..models.vlan_status import VLANStatus


T = TypeVar("T", bound="VLAN")


@_attrs_define
class VLAN:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        vid (int): Numeric VLAN ID (1-4094)
        name (str):
        l2vpn_termination (Union['BriefL2VPNTermination', None]):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        prefix_count (int):
        site (Union['BriefSite', None, Unset]):
        group (Union['BriefVLANGroup', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        status (Union[Unset, VLANStatus]):
        role (Union['BriefRole', None, Unset]):
        description (Union[Unset, str]):
        qinq_role (Union['VLANQinqRoleType0', None, Unset]):
        qinq_svlan (Union['NestedVLAN', None, Unset]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VLANCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    vid: int
    name: str
    l2vpn_termination: Union["BriefL2VPNTermination", None]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    prefix_count: int
    site: Union["BriefSite", None, Unset] = UNSET
    group: Union["BriefVLANGroup", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    status: Union[Unset, "VLANStatus"] = UNSET
    role: Union["BriefRole", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    qinq_role: Union["VLANQinqRoleType0", None, Unset] = UNSET
    qinq_svlan: Union["NestedVLAN", None, Unset] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VLANCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_role import BriefRole
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan_group import BriefVLANGroup
        from ..models.nested_vlan import NestedVLAN
        from ..models.vlan_qinq_role_type_0 import VLANQinqRoleType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        vid = self.vid

        name = self.name

        l2vpn_termination: Union[None, dict[str, Any]]
        if isinstance(self.l2vpn_termination, BriefL2VPNTermination):
            l2vpn_termination = self.l2vpn_termination.to_dict()
        else:
            l2vpn_termination = self.l2vpn_termination

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

        prefix_count = self.prefix_count

        site: Union[None, Unset, dict[str, Any]]
        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, BriefSite):
            site = self.site.to_dict()
        else:
            site = self.site

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefVLANGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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

        description = self.description

        qinq_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.qinq_role, Unset):
            qinq_role = UNSET
        elif isinstance(self.qinq_role, VLANQinqRoleType0):
            qinq_role = self.qinq_role.to_dict()
        else:
            qinq_role = self.qinq_role

        qinq_svlan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
        elif isinstance(self.qinq_svlan, NestedVLAN):
            qinq_svlan = self.qinq_svlan.to_dict()
        else:
            qinq_svlan = self.qinq_svlan

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
                "vid": vid,
                "name": name,
                "l2vpn_termination": l2vpn_termination,
                "created": created,
                "last_updated": last_updated,
                "prefix_count": prefix_count,
            }
        )
        if site is not UNSET:
            field_dict["site"] = site
        if group is not UNSET:
            field_dict["group"] = group
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if qinq_role is not UNSET:
            field_dict["qinq_role"] = qinq_role
        if qinq_svlan is not UNSET:
            field_dict["qinq_svlan"] = qinq_svlan
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_role import BriefRole
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan_group import BriefVLANGroup
        from ..models.nested_tag import NestedTag
        from ..models.nested_vlan import NestedVLAN
        from ..models.vlan_custom_fields import VLANCustomFields
        from ..models.vlan_qinq_role_type_0 import VLANQinqRoleType0
        from ..models.vlan_status import VLANStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        vid = d.pop("vid")

        name = d.pop("name")

        def _parse_l2vpn_termination(data: object) -> Union["BriefL2VPNTermination", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                l2vpn_termination_type_1 = BriefL2VPNTermination.from_dict(data)

                return l2vpn_termination_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefL2VPNTermination", None], data)

        l2vpn_termination = _parse_l2vpn_termination(d.pop("l2vpn_termination"))

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

        prefix_count = d.pop("prefix_count")

        def _parse_site(data: object) -> Union["BriefSite", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSite.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSite", None, Unset], data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_group(data: object) -> Union["BriefVLANGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefVLANGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, VLANStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VLANStatus.from_dict(_status)

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

        description = d.pop("description", UNSET)

        def _parse_qinq_role(data: object) -> Union["VLANQinqRoleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qinq_role_type_0 = VLANQinqRoleType0.from_dict(data)

                return qinq_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union["VLANQinqRoleType0", None, Unset], data)

        qinq_role = _parse_qinq_role(d.pop("qinq_role", UNSET))

        def _parse_qinq_svlan(data: object) -> Union["NestedVLAN", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qinq_svlan_type_1 = NestedVLAN.from_dict(data)

                return qinq_svlan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedVLAN", None, Unset], data)

        qinq_svlan = _parse_qinq_svlan(d.pop("qinq_svlan", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VLANCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VLANCustomFields.from_dict(_custom_fields)

        vlan = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            vid=vid,
            name=name,
            l2vpn_termination=l2vpn_termination,
            created=created,
            last_updated=last_updated,
            prefix_count=prefix_count,
            site=site,
            group=group,
            tenant=tenant,
            status=status,
            role=role,
            description=description,
            qinq_role=qinq_role,
            qinq_svlan=qinq_svlan,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        vlan.additional_properties = d
        return vlan

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
