from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_address_request_role import IPAddressRequestRole
from ..models.ip_address_request_status import IPAddressRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_vrf_request import BriefVRFRequest
    from ..models.ip_address_request_custom_fields import IPAddressRequestCustomFields
    from ..models.nested_ip_address_request import NestedIPAddressRequest
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IPAddressRequest")


@_attrs_define
class IPAddressRequest:
    """Adds support for custom fields and tags.

    Attributes:
        address (str):
        vrf (Union['BriefVRFRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        status (Union[Unset, IPAddressRequestStatus]): * `active` - Active
            * `reserved` - Reserved
            * `deprecated` - Deprecated
            * `dhcp` - DHCP
            * `slaac` - SLAAC
        role (Union[Unset, IPAddressRequestRole]): * `loopback` - Loopback
            * `secondary` - Secondary
            * `anycast` - Anycast
            * `vip` - VIP
            * `vrrp` - VRRP
            * `hsrp` - HSRP
            * `glbp` - GLBP
            * `carp` - CARP
        assigned_object_type (Union[None, Unset, str]):
        assigned_object_id (Union[None, Unset, int]):
        nat_inside (Union['NestedIPAddressRequest', None, Unset]):
        dns_name (Union[Unset, str]): Hostname or FQDN (not case-sensitive)
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IPAddressRequestCustomFields]):
    """

    address: str
    vrf: Union["BriefVRFRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    status: Union[Unset, IPAddressRequestStatus] = UNSET
    role: Union[Unset, IPAddressRequestRole] = UNSET
    assigned_object_type: Union[None, Unset, str] = UNSET
    assigned_object_id: Union[None, Unset, int] = UNSET
    nat_inside: Union["NestedIPAddressRequest", None, Unset] = UNSET
    dns_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IPAddressRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.nested_ip_address_request import NestedIPAddressRequest

        address = self.address

        vrf: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRFRequest):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

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

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        assigned_object_type: Union[None, Unset, str]
        if isinstance(self.assigned_object_type, Unset):
            assigned_object_type = UNSET
        else:
            assigned_object_type = self.assigned_object_type

        assigned_object_id: Union[None, Unset, int]
        if isinstance(self.assigned_object_id, Unset):
            assigned_object_id = UNSET
        else:
            assigned_object_id = self.assigned_object_id

        nat_inside: Union[None, Unset, dict[str, Any]]
        if isinstance(self.nat_inside, Unset):
            nat_inside = UNSET
        elif isinstance(self.nat_inside, NestedIPAddressRequest):
            nat_inside = self.nat_inside.to_dict()
        else:
            nat_inside = self.nat_inside

        dns_name = self.dns_name

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
                "address": address,
            }
        )
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if assigned_object_type is not UNSET:
            field_dict["assigned_object_type"] = assigned_object_type
        if assigned_object_id is not UNSET:
            field_dict["assigned_object_id"] = assigned_object_id
        if nat_inside is not UNSET:
            field_dict["nat_inside"] = nat_inside
        if dns_name is not UNSET:
            field_dict["dns_name"] = dns_name
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
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.ip_address_request_custom_fields import (
            IPAddressRequestCustomFields,
        )
        from ..models.nested_ip_address_request import NestedIPAddressRequest
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        address = d.pop("address")

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

        def _parse_tenant(
            data: object,
        ) -> Union["BriefTenantRequest", None, Unset, int]:
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
        status: Union[Unset, IPAddressRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IPAddressRequestStatus(_status)

        _role = d.pop("role", UNSET)
        role: Union[Unset, IPAddressRequestRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = IPAddressRequestRole(_role)

        def _parse_assigned_object_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assigned_object_type = _parse_assigned_object_type(
            d.pop("assigned_object_type", UNSET)
        )

        def _parse_assigned_object_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assigned_object_id = _parse_assigned_object_id(
            d.pop("assigned_object_id", UNSET)
        )

        def _parse_nat_inside(
            data: object,
        ) -> Union["NestedIPAddressRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nat_inside_type_1 = NestedIPAddressRequest.from_dict(data)

                return nat_inside_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedIPAddressRequest", None, Unset], data)

        nat_inside = _parse_nat_inside(d.pop("nat_inside", UNSET))

        dns_name = d.pop("dns_name", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IPAddressRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPAddressRequestCustomFields.from_dict(_custom_fields)

        ip_address_request = cls(
            address=address,
            vrf=vrf,
            tenant=tenant,
            status=status,
            role=role,
            assigned_object_type=assigned_object_type,
            assigned_object_id=assigned_object_id,
            nat_inside=nat_inside,
            dns_name=dns_name,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ip_address_request.additional_properties = d
        return ip_address_request

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
