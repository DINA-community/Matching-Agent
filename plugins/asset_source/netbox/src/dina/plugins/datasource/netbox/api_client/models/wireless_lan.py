import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_vlan import BriefVLAN
    from ..models.brief_wireless_lan_group import BriefWirelessLANGroup
    from ..models.nested_tag import NestedTag
    from ..models.wireless_lan_auth_cipher import WirelessLANAuthCipher
    from ..models.wireless_lan_auth_type import WirelessLANAuthType
    from ..models.wireless_lan_custom_fields import WirelessLANCustomFields
    from ..models.wireless_lan_status import WirelessLANStatus


T = TypeVar("T", bound="WirelessLAN")


@_attrs_define
class WirelessLAN:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        ssid (str):
        scope (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        description (Union[Unset, str]):
        group (Union['BriefWirelessLANGroup', None, Unset]):
        status (Union[Unset, WirelessLANStatus]):
        vlan (Union['BriefVLAN', None, Unset]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        tenant (Union['BriefTenant', None, Unset]):
        auth_type (Union[Unset, WirelessLANAuthType]):
        auth_cipher (Union[Unset, WirelessLANAuthCipher]):
        auth_psk (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, WirelessLANCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    ssid: str
    scope: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    group: Union["BriefWirelessLANGroup", None, Unset] = UNSET
    status: Union[Unset, "WirelessLANStatus"] = UNSET
    vlan: Union["BriefVLAN", None, Unset] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    auth_type: Union[Unset, "WirelessLANAuthType"] = UNSET
    auth_cipher: Union[Unset, "WirelessLANAuthCipher"] = UNSET
    auth_psk: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "WirelessLANCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_wireless_lan_group import BriefWirelessLANGroup

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        ssid = self.ssid

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

        description = self.description

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefWirelessLANGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        vlan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vlan, Unset):
            vlan = UNSET
        elif isinstance(self.vlan, BriefVLAN):
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

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        auth_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.to_dict()

        auth_cipher: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth_cipher, Unset):
            auth_cipher = self.auth_cipher.to_dict()

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "ssid": ssid,
                "scope": scope,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_wireless_lan_group import BriefWirelessLANGroup
        from ..models.nested_tag import NestedTag
        from ..models.wireless_lan_auth_cipher import WirelessLANAuthCipher
        from ..models.wireless_lan_auth_type import WirelessLANAuthType
        from ..models.wireless_lan_custom_fields import WirelessLANCustomFields
        from ..models.wireless_lan_status import WirelessLANStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        ssid = d.pop("ssid")

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

        description = d.pop("description", UNSET)

        def _parse_group(data: object) -> Union["BriefWirelessLANGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefWirelessLANGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefWirelessLANGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WirelessLANStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WirelessLANStatus.from_dict(_status)

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

        _auth_type = d.pop("auth_type", UNSET)
        auth_type: Union[Unset, WirelessLANAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = WirelessLANAuthType.from_dict(_auth_type)

        _auth_cipher = d.pop("auth_cipher", UNSET)
        auth_cipher: Union[Unset, WirelessLANAuthCipher]
        if isinstance(_auth_cipher, Unset):
            auth_cipher = UNSET
        else:
            auth_cipher = WirelessLANAuthCipher.from_dict(_auth_cipher)

        auth_psk = d.pop("auth_psk", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WirelessLANCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WirelessLANCustomFields.from_dict(_custom_fields)

        wireless_lan = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            ssid=ssid,
            scope=scope,
            created=created,
            last_updated=last_updated,
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

        wireless_lan.additional_properties = d
        return wireless_lan

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
