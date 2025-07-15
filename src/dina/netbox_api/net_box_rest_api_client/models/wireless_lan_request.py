from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wireless_lan_request_auth_cipher import WirelessLANRequestAuthCipher
from ..models.wireless_lan_request_auth_type import WirelessLANRequestAuthType
from ..models.wireless_lan_request_status import WirelessLANRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_vlan_request import BriefVLANRequest
    from ..models.brief_wireless_lan_group_request import BriefWirelessLANGroupRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.wireless_lan_request_custom_fields import WirelessLANRequestCustomFields


T = TypeVar("T", bound="WirelessLANRequest")


@_attrs_define
class WirelessLANRequest:
    """Adds support for custom fields and tags.

    Attributes:
        ssid (str):
        description (Union[Unset, str]):
        group (Union['BriefWirelessLANGroupRequest', None, Unset, int]):
        status (Union[Unset, WirelessLANRequestStatus]): * `active` - Active
            * `reserved` - Reserved
            * `disabled` - Disabled
            * `deprecated` - Deprecated
        vlan (Union['BriefVLANRequest', None, Unset, int]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        auth_type (Union[Unset, WirelessLANRequestAuthType]): * `open` - Open
            * `wep` - WEP
            * `wpa-personal` - WPA Personal (PSK)
            * `wpa-enterprise` - WPA Enterprise
        auth_cipher (Union[Unset, WirelessLANRequestAuthCipher]): * `auto` - Auto
            * `tkip` - TKIP
            * `aes` - AES
        auth_psk (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WirelessLANRequestCustomFields]):
    """

    ssid: str
    description: Union[Unset, str] = UNSET
    group: Union["BriefWirelessLANGroupRequest", None, Unset, int] = UNSET
    status: Union[Unset, WirelessLANRequestStatus] = UNSET
    vlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    auth_type: Union[Unset, WirelessLANRequestAuthType] = UNSET
    auth_cipher: Union[Unset, WirelessLANRequestAuthCipher] = UNSET
    auth_psk: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WirelessLANRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_wireless_lan_group_request import BriefWirelessLANGroupRequest

        ssid = self.ssid

        description = self.description

        group: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefWirelessLANGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        vlan: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vlan, Unset):
            vlan = UNSET
        elif isinstance(self.vlan, BriefVLANRequest):
            vlan = self.vlan.to_dict()
        else:
            vlan = self.vlan

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

        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        auth_cipher: Union[Unset, str] = UNSET
        if not isinstance(self.auth_cipher, Unset):
            auth_cipher = self.auth_cipher.value

        auth_psk = self.auth_psk

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
                "ssid": ssid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group is not UNSET:
            field_dict["group"] = group
        if status is not UNSET:
            field_dict["status"] = status
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if auth_cipher is not UNSET:
            field_dict["auth_cipher"] = auth_cipher
        if auth_psk is not UNSET:
            field_dict["auth_psk"] = auth_psk
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
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_wireless_lan_group_request import BriefWirelessLANGroupRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.wireless_lan_request_custom_fields import WirelessLANRequestCustomFields

        d = dict(src_dict)
        ssid = d.pop("ssid")

        description = d.pop("description", UNSET)

        def _parse_group(data: object) -> Union["BriefWirelessLANGroupRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1_type_1 = BriefWirelessLANGroupRequest.from_dict(data)

                return group_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefWirelessLANGroupRequest", None, Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WirelessLANRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WirelessLANRequestStatus(_status)

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

        _auth_type = d.pop("auth_type", UNSET)
        auth_type: Union[Unset, WirelessLANRequestAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = WirelessLANRequestAuthType(_auth_type)

        _auth_cipher = d.pop("auth_cipher", UNSET)
        auth_cipher: Union[Unset, WirelessLANRequestAuthCipher]
        if isinstance(_auth_cipher, Unset):
            auth_cipher = UNSET
        else:
            auth_cipher = WirelessLANRequestAuthCipher(_auth_cipher)

        auth_psk = d.pop("auth_psk", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WirelessLANRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WirelessLANRequestCustomFields.from_dict(_custom_fields)

        wireless_lan_request = cls(
            ssid=ssid,
            description=description,
            group=group,
            status=status,
            vlan=vlan,
            scope_type=scope_type,
            scope_id=scope_id,
            tenant=tenant,
            auth_type=auth_type,
            auth_cipher=auth_cipher,
            auth_psk=auth_psk,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        wireless_lan_request.additional_properties = d
        return wireless_lan_request

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
