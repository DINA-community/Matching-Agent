from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tunnel_request_encapsulation import TunnelRequestEncapsulation
from ..models.tunnel_request_status import TunnelRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_sec_profile_request import BriefIPSecProfileRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_tunnel_group_request import BriefTunnelGroupRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.tunnel_request_custom_fields import TunnelRequestCustomFields


T = TypeVar("T", bound="TunnelRequest")


@_attrs_define
class TunnelRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        status (TunnelRequestStatus): * `planned` - Planned
            * `active` - Active
            * `disabled` - Disabled
        encapsulation (TunnelRequestEncapsulation): * `ipsec-transport` - IPsec - Transport
            * `ipsec-tunnel` - IPsec - Tunnel
            * `ip-ip` - IP-in-IP
            * `gre` - GRE
            * `wireguard` - WireGuard
            * `openvpn` - OpenVPN
            * `l2tp` - L2TP
            * `pptp` - PPTP
        group (Union['BriefTunnelGroupRequest', None, Unset, int]):
        ipsec_profile (Union['BriefIPSecProfileRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        tunnel_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, TunnelRequestCustomFields]):
    """

    name: str
    status: TunnelRequestStatus
    encapsulation: TunnelRequestEncapsulation
    group: Union["BriefTunnelGroupRequest", None, Unset, int] = UNSET
    ipsec_profile: Union["BriefIPSecProfileRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    tunnel_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "TunnelRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ip_sec_profile_request import BriefIPSecProfileRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_tunnel_group_request import BriefTunnelGroupRequest

        name = self.name

        status = self.status.value

        encapsulation = self.encapsulation.value

        group: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefTunnelGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        ipsec_profile: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.ipsec_profile, Unset):
            ipsec_profile = UNSET
        elif isinstance(self.ipsec_profile, BriefIPSecProfileRequest):
            ipsec_profile = self.ipsec_profile.to_dict()
        else:
            ipsec_profile = self.ipsec_profile

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
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
                "name": name,
                "status": status,
                "encapsulation": encapsulation,
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
        from ..models.brief_ip_sec_profile_request import BriefIPSecProfileRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_tunnel_group_request import BriefTunnelGroupRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.tunnel_request_custom_fields import TunnelRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        status = TunnelRequestStatus(d.pop("status"))

        encapsulation = TunnelRequestEncapsulation(d.pop("encapsulation"))

        def _parse_group(
            data: object,
        ) -> Union["BriefTunnelGroupRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1_type_1 = BriefTunnelGroupRequest.from_dict(data)

                return group_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTunnelGroupRequest", None, Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_ipsec_profile(
            data: object,
        ) -> Union["BriefIPSecProfileRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ipsec_profile_type_1_type_1 = BriefIPSecProfileRequest.from_dict(data)

                return ipsec_profile_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPSecProfileRequest", None, Unset, int], data)

        ipsec_profile = _parse_ipsec_profile(d.pop("ipsec_profile", UNSET))

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
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, TunnelRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TunnelRequestCustomFields.from_dict(_custom_fields)

        tunnel_request = cls(
            name=name,
            status=status,
            encapsulation=encapsulation,
            group=group,
            ipsec_profile=ipsec_profile,
            tenant=tenant,
            tunnel_id=tunnel_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        tunnel_request.additional_properties = d
        return tunnel_request

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
