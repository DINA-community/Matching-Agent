from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prefix_request_status import PrefixRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_role_request import BriefRoleRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_vlan_request import BriefVLANRequest
    from ..models.brief_vrf_request import BriefVRFRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.prefix_request_custom_fields import PrefixRequestCustomFields


T = TypeVar("T", bound="PrefixRequest")


@_attrs_define
class PrefixRequest:
    """Adds support for custom fields and tags.

    Attributes:
        prefix (str):
        vrf (Union['BriefVRFRequest', None, Unset, int]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        vlan (Union['BriefVLANRequest', None, Unset, int]):
        status (Union[Unset, PrefixRequestStatus]): * `container` - Container
            * `active` - Active
            * `reserved` - Reserved
            * `deprecated` - Deprecated
        role (Union['BriefRoleRequest', None, Unset, int]):
        is_pool (Union[Unset, bool]): All IP addresses within this prefix are considered usable
        mark_utilized (Union[Unset, bool]): Treat as fully utilized
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PrefixRequestCustomFields]):
    """

    prefix: str
    vrf: Union["BriefVRFRequest", None, Unset, int] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    vlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    status: Union[Unset, PrefixRequestStatus] = UNSET
    role: Union["BriefRoleRequest", None, Unset, int] = UNSET
    is_pool: Union[Unset, bool] = UNSET
    mark_utilized: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PrefixRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vrf_request import BriefVRFRequest

        prefix = self.prefix

        vrf: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRFRequest):
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

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        vlan: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vlan, Unset):
            vlan = UNSET
        elif isinstance(self.vlan, BriefVLANRequest):
            vlan = self.vlan.to_dict()
        else:
            vlan = self.vlan

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
                "prefix": prefix,
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
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.prefix_request_custom_fields import PrefixRequestCustomFields

        d = dict(src_dict)
        prefix = d.pop("prefix")

        def _parse_vrf(data: object) -> Union["BriefVRFRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrf_type_1_type_1 = BriefVRFRequest.from_dict(data)

                return vrf_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVRFRequest", None, Unset, int], data)

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

        def _parse_vlan(data: object) -> Union["BriefVLANRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vlan_type_1_type_1 = BriefVLANRequest.from_dict(data)

                return vlan_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANRequest", None, Unset, int], data)

        vlan = _parse_vlan(d.pop("vlan", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PrefixRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PrefixRequestStatus(_status)

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

        is_pool = d.pop("is_pool", UNSET)

        mark_utilized = d.pop("mark_utilized", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PrefixRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PrefixRequestCustomFields.from_dict(_custom_fields)

        prefix_request = cls(
            prefix=prefix,
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

        prefix_request.additional_properties = d
        return prefix_request

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
