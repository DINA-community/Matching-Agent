import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_vlan_request_q_in_q_role import WritableVLANRequestQInQRole
from ..models.writable_vlan_request_status import WritableVLANRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_role_request import BriefRoleRequest
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_vlan_group_request import BriefVLANGroupRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_vlan_request_custom_fields import WritableVLANRequestCustomFields


T = TypeVar("T", bound="WritableVLANRequest")


@_attrs_define
class WritableVLANRequest:
    """Adds support for custom fields and tags.

    Attributes:
        vid (int): Numeric VLAN ID (1-4094)
        name (str):
        site (Union['BriefSiteRequest', None, Unset, int]):
        group (Union['BriefVLANGroupRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        status (Union[Unset, WritableVLANRequestStatus]): Operational status of this VLAN

            * `active` - Active
            * `reserved` - Reserved
            * `deprecated` - Deprecated
        role (Union['BriefRoleRequest', None, Unset, int]):
        description (Union[Unset, str]):
        qinq_role (Union[None, Unset, WritableVLANRequestQInQRole]): Customer/service VLAN designation (for Q-in-Q/IEEE
            802.1ad)

            * `svlan` - Service
            * `cvlan` - Customer
        qinq_svlan (Union[None, Unset, int]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableVLANRequestCustomFields]):
    """

    vid: int
    name: str
    site: Union["BriefSiteRequest", None, Unset, int] = UNSET
    group: Union["BriefVLANGroupRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    status: Union[Unset, WritableVLANRequestStatus] = UNSET
    role: Union["BriefRoleRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    qinq_role: Union[None, Unset, WritableVLANRequestQInQRole] = UNSET
    qinq_svlan: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableVLANRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vlan_group_request import BriefVLANGroupRequest

        vid = self.vid

        name = self.name

        site: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        group: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefVLANGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        description = self.description

        qinq_role: Union[None, Unset, str]
        if isinstance(self.qinq_role, Unset):
            qinq_role = UNSET
        elif isinstance(self.qinq_role, WritableVLANRequestQInQRole):
            qinq_role = self.qinq_role.value
        elif isinstance(self.qinq_role, WritableVLANRequestQInQRole):
            qinq_role = self.qinq_role.value
        elif isinstance(self.qinq_role, WritableVLANRequestQInQRole):
            qinq_role = self.qinq_role.value
        else:
            qinq_role = self.qinq_role

        qinq_svlan: Union[None, Unset, int]
        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
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
                "vid": vid,
                "name": name,
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

    def to_multipart(self) -> dict[str, Any]:
        vid = (None, str(self.vid).encode(), "text/plain")

        name = (None, str(self.name).encode(), "text/plain")

        site: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, int):
            site = (None, str(self.site).encode(), "text/plain")
        elif isinstance(self.site, None):
            site = (None, str(self.site).encode(), "text/plain")
        elif isinstance(self.site, BriefSiteRequest):
            site = (None, json.dumps(self.site.to_dict()).encode(), "application/json")
        else:
            site = (None, str(self.site).encode(), "text/plain")

        group: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, int):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, None):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, BriefVLANGroupRequest):
            group = (None, json.dumps(self.group.to_dict()).encode(), "application/json")
        else:
            group = (None, str(self.group).encode(), "text/plain")

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (None, json.dumps(self.tenant.to_dict()).encode(), "application/json")
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, int):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, None):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, BriefRoleRequest):
            role = (None, json.dumps(self.role.to_dict()).encode(), "application/json")
        else:
            role = (None, str(self.role).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        qinq_role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.qinq_role, Unset):
            qinq_role = UNSET
        elif isinstance(self.qinq_role, None):
            qinq_role = (None, str(self.qinq_role).encode(), "text/plain")
        elif isinstance(self.qinq_role, WritableVLANRequestQInQRole):
            qinq_role = (None, str(self.qinq_role.value).encode(), "text/plain")
        elif isinstance(self.qinq_role, None):
            qinq_role = (None, str(self.qinq_role).encode(), "text/plain")
        elif isinstance(self.qinq_role, WritableVLANRequestQInQRole):
            qinq_role = (None, str(self.qinq_role.value).encode(), "text/plain")
        elif isinstance(self.qinq_role, None):
            qinq_role = (None, str(self.qinq_role).encode(), "text/plain")
        else:
            qinq_role = (None, str(self.qinq_role.value).encode(), "text/plain")

        qinq_svlan: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
        elif isinstance(self.qinq_svlan, int):
            qinq_svlan = (None, str(self.qinq_svlan).encode(), "text/plain")
        else:
            qinq_svlan = (None, str(self.qinq_svlan).encode(), "text/plain")

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
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
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "vid": vid,
                "name": name,
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
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vlan_group_request import BriefVLANGroupRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_vlan_request_custom_fields import WritableVLANRequestCustomFields

        d = dict(src_dict)
        vid = d.pop("vid")

        name = d.pop("name")

        def _parse_site(data: object) -> Union["BriefSiteRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", None, Unset, int], data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_group(data: object) -> Union["BriefVLANGroupRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1_type_1 = BriefVLANGroupRequest.from_dict(data)

                return group_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANGroupRequest", None, Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_tenant(data: object) -> Union["BriefTenantRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1_type_1 = BriefTenantRequest.from_dict(data)

                return tenant_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenantRequest", None, Unset, int], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableVLANRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableVLANRequestStatus(_status)

        def _parse_role(data: object) -> Union["BriefRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        description = d.pop("description", UNSET)

        def _parse_qinq_role(data: object) -> Union[None, Unset, WritableVLANRequestQInQRole]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                qinq_role_type_1 = WritableVLANRequestQInQRole(data)

                return qinq_role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                qinq_role_type_2_type_1 = WritableVLANRequestQInQRole(data)

                return qinq_role_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                qinq_role_type_3_type_1 = WritableVLANRequestQInQRole(data)

                return qinq_role_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WritableVLANRequestQInQRole], data)

        qinq_role = _parse_qinq_role(d.pop("qinq_role", UNSET))

        def _parse_qinq_svlan(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        qinq_svlan = _parse_qinq_svlan(d.pop("qinq_svlan", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableVLANRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableVLANRequestCustomFields.from_dict(_custom_fields)

        writable_vlan_request = cls(
            vid=vid,
            name=name,
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

        writable_vlan_request.additional_properties = d
        return writable_vlan_request

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
