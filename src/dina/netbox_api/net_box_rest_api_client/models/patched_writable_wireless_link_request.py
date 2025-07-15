import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_wireless_link_request_authentication_cipher import (
    PatchedWritableWirelessLinkRequestAuthenticationCipher,
)
from ..models.patched_writable_wireless_link_request_authentication_type import (
    PatchedWritableWirelessLinkRequestAuthenticationType,
)
from ..models.patched_writable_wireless_link_request_distance_unit_type_1 import (
    PatchedWritableWirelessLinkRequestDistanceUnitType1,
)
from ..models.patched_writable_wireless_link_request_distance_unit_type_2_type_1 import (
    PatchedWritableWirelessLinkRequestDistanceUnitType2Type1,
)
from ..models.patched_writable_wireless_link_request_distance_unit_type_3_type_1 import (
    PatchedWritableWirelessLinkRequestDistanceUnitType3Type1,
)
from ..models.patched_writable_wireless_link_request_status import PatchedWritableWirelessLinkRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_interface_request import BriefInterfaceRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_wireless_link_request_custom_fields import (
        PatchedWritableWirelessLinkRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableWirelessLinkRequest")


@_attrs_define
class PatchedWritableWirelessLinkRequest:
    """Adds support for custom fields and tags.

    Attributes:
        interface_a (Union['BriefInterfaceRequest', Unset, int]):
        interface_b (Union['BriefInterfaceRequest', Unset, int]):
        ssid (Union[Unset, str]):
        status (Union[Unset, PatchedWritableWirelessLinkRequestStatus]): * `connected` - Connected
            * `planned` - Planned
            * `decommissioning` - Decommissioning
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        auth_type (Union[None, PatchedWritableWirelessLinkRequestAuthenticationType, Unset]): * `open` - Open
            * `wep` - WEP
            * `wpa-personal` - WPA Personal (PSK)
            * `wpa-enterprise` - WPA Enterprise
        auth_cipher (Union[None, PatchedWritableWirelessLinkRequestAuthenticationCipher, Unset]): * `auto` - Auto
            * `tkip` - TKIP
            * `aes` - AES
        auth_psk (Union[Unset, str]):
        distance (Union[None, Unset, float]):
        distance_unit (Union[None, PatchedWritableWirelessLinkRequestDistanceUnitType1,
            PatchedWritableWirelessLinkRequestDistanceUnitType2Type1,
            PatchedWritableWirelessLinkRequestDistanceUnitType3Type1, Unset]): * `km` - Kilometers
            * `m` - Meters
            * `mi` - Miles
            * `ft` - Feet
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableWirelessLinkRequestCustomFields]):
    """

    interface_a: Union["BriefInterfaceRequest", Unset, int] = UNSET
    interface_b: Union["BriefInterfaceRequest", Unset, int] = UNSET
    ssid: Union[Unset, str] = UNSET
    status: Union[Unset, PatchedWritableWirelessLinkRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    auth_type: Union[None, PatchedWritableWirelessLinkRequestAuthenticationType, Unset] = UNSET
    auth_cipher: Union[None, PatchedWritableWirelessLinkRequestAuthenticationCipher, Unset] = UNSET
    auth_psk: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union[
        None,
        PatchedWritableWirelessLinkRequestDistanceUnitType1,
        PatchedWritableWirelessLinkRequestDistanceUnitType2Type1,
        PatchedWritableWirelessLinkRequestDistanceUnitType3Type1,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableWirelessLinkRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_interface_request import BriefInterfaceRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        interface_a: Union[Unset, dict[str, Any], int]
        if isinstance(self.interface_a, Unset):
            interface_a = UNSET
        elif isinstance(self.interface_a, BriefInterfaceRequest):
            interface_a = self.interface_a.to_dict()
        else:
            interface_a = self.interface_a

        interface_b: Union[Unset, dict[str, Any], int]
        if isinstance(self.interface_b, Unset):
            interface_b = UNSET
        elif isinstance(self.interface_b, BriefInterfaceRequest):
            interface_b = self.interface_b.to_dict()
        else:
            interface_b = self.interface_b

        ssid = self.ssid

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        auth_type: Union[None, Unset, str]
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, PatchedWritableWirelessLinkRequestAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, PatchedWritableWirelessLinkRequestAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, PatchedWritableWirelessLinkRequestAuthenticationType):
            auth_type = self.auth_type.value
        else:
            auth_type = self.auth_type

        auth_cipher: Union[None, Unset, str]
        if isinstance(self.auth_cipher, Unset):
            auth_cipher = UNSET
        elif isinstance(self.auth_cipher, PatchedWritableWirelessLinkRequestAuthenticationCipher):
            auth_cipher = self.auth_cipher.value
        elif isinstance(self.auth_cipher, PatchedWritableWirelessLinkRequestAuthenticationCipher):
            auth_cipher = self.auth_cipher.value
        elif isinstance(self.auth_cipher, PatchedWritableWirelessLinkRequestAuthenticationCipher):
            auth_cipher = self.auth_cipher.value
        else:
            auth_cipher = self.auth_cipher

        auth_psk = self.auth_psk

        distance: Union[None, Unset, float]
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        distance_unit: Union[None, Unset, str]
        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, PatchedWritableWirelessLinkRequestDistanceUnitType1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, PatchedWritableWirelessLinkRequestDistanceUnitType2Type1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, PatchedWritableWirelessLinkRequestDistanceUnitType3Type1):
            distance_unit = self.distance_unit.value
        else:
            distance_unit = self.distance_unit

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
        field_dict.update({})
        if interface_a is not UNSET:
            field_dict["interface_a"] = interface_a
        if interface_b is not UNSET:
            field_dict["interface_b"] = interface_b
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if auth_cipher is not UNSET:
            field_dict["auth_cipher"] = auth_cipher
        if auth_psk is not UNSET:
            field_dict["auth_psk"] = auth_psk
        if distance is not UNSET:
            field_dict["distance"] = distance
        if distance_unit is not UNSET:
            field_dict["distance_unit"] = distance_unit
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        interface_a: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.interface_a, Unset):
            interface_a = UNSET
        elif isinstance(self.interface_a, int):
            interface_a = (None, str(self.interface_a).encode(), "text/plain")
        else:
            interface_a = (None, json.dumps(self.interface_a.to_dict()).encode(), "application/json")

        interface_b: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.interface_b, Unset):
            interface_b = UNSET
        elif isinstance(self.interface_b, int):
            interface_b = (None, str(self.interface_b).encode(), "text/plain")
        else:
            interface_b = (None, json.dumps(self.interface_b.to_dict()).encode(), "application/json")

        ssid = self.ssid if isinstance(self.ssid, Unset) else (None, str(self.ssid).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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

        auth_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        elif isinstance(self.auth_type, PatchedWritableWirelessLinkRequestAuthenticationType):
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        elif isinstance(self.auth_type, PatchedWritableWirelessLinkRequestAuthenticationType):
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        else:
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")

        auth_cipher: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.auth_cipher, Unset):
            auth_cipher = UNSET
        elif isinstance(self.auth_cipher, None):
            auth_cipher = (None, str(self.auth_cipher).encode(), "text/plain")
        elif isinstance(self.auth_cipher, PatchedWritableWirelessLinkRequestAuthenticationCipher):
            auth_cipher = (None, str(self.auth_cipher.value).encode(), "text/plain")
        elif isinstance(self.auth_cipher, None):
            auth_cipher = (None, str(self.auth_cipher).encode(), "text/plain")
        elif isinstance(self.auth_cipher, PatchedWritableWirelessLinkRequestAuthenticationCipher):
            auth_cipher = (None, str(self.auth_cipher.value).encode(), "text/plain")
        elif isinstance(self.auth_cipher, None):
            auth_cipher = (None, str(self.auth_cipher).encode(), "text/plain")
        else:
            auth_cipher = (None, str(self.auth_cipher.value).encode(), "text/plain")

        auth_psk = (
            self.auth_psk if isinstance(self.auth_psk, Unset) else (None, str(self.auth_psk).encode(), "text/plain")
        )

        distance: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.distance, Unset):
            distance = UNSET
        elif isinstance(self.distance, float):
            distance = (None, str(self.distance).encode(), "text/plain")
        else:
            distance = (None, str(self.distance).encode(), "text/plain")

        distance_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        elif isinstance(self.distance_unit, PatchedWritableWirelessLinkRequestDistanceUnitType1):
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        elif isinstance(self.distance_unit, PatchedWritableWirelessLinkRequestDistanceUnitType2Type1):
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        else:
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

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

        field_dict.update({})
        if interface_a is not UNSET:
            field_dict["interface_a"] = interface_a
        if interface_b is not UNSET:
            field_dict["interface_b"] = interface_b
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if auth_cipher is not UNSET:
            field_dict["auth_cipher"] = auth_cipher
        if auth_psk is not UNSET:
            field_dict["auth_psk"] = auth_psk
        if distance is not UNSET:
            field_dict["distance"] = distance
        if distance_unit is not UNSET:
            field_dict["distance_unit"] = distance_unit
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
        from ..models.brief_interface_request import BriefInterfaceRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_wireless_link_request_custom_fields import (
            PatchedWritableWirelessLinkRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_interface_a(data: object) -> Union["BriefInterfaceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interface_a_type_1 = BriefInterfaceRequest.from_dict(data)

                return interface_a_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInterfaceRequest", Unset, int], data)

        interface_a = _parse_interface_a(d.pop("interface_a", UNSET))

        def _parse_interface_b(data: object) -> Union["BriefInterfaceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interface_b_type_1 = BriefInterfaceRequest.from_dict(data)

                return interface_b_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInterfaceRequest", Unset, int], data)

        interface_b = _parse_interface_b(d.pop("interface_b", UNSET))

        ssid = d.pop("ssid", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableWirelessLinkRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableWirelessLinkRequestStatus(_status)

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

        def _parse_auth_type(data: object) -> Union[None, PatchedWritableWirelessLinkRequestAuthenticationType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_1 = PatchedWritableWirelessLinkRequestAuthenticationType(data)

                return auth_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_2_type_1 = PatchedWritableWirelessLinkRequestAuthenticationType(data)

                return auth_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_3_type_1 = PatchedWritableWirelessLinkRequestAuthenticationType(data)

                return auth_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableWirelessLinkRequestAuthenticationType, Unset], data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))

        def _parse_auth_cipher(
            data: object,
        ) -> Union[None, PatchedWritableWirelessLinkRequestAuthenticationCipher, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_cipher_type_1 = PatchedWritableWirelessLinkRequestAuthenticationCipher(data)

                return auth_cipher_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_cipher_type_2_type_1 = PatchedWritableWirelessLinkRequestAuthenticationCipher(data)

                return auth_cipher_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_cipher_type_3_type_1 = PatchedWritableWirelessLinkRequestAuthenticationCipher(data)

                return auth_cipher_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableWirelessLinkRequestAuthenticationCipher, Unset], data)

        auth_cipher = _parse_auth_cipher(d.pop("auth_cipher", UNSET))

        auth_psk = d.pop("auth_psk", UNSET)

        def _parse_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        distance = _parse_distance(d.pop("distance", UNSET))

        def _parse_distance_unit(
            data: object,
        ) -> Union[
            None,
            PatchedWritableWirelessLinkRequestDistanceUnitType1,
            PatchedWritableWirelessLinkRequestDistanceUnitType2Type1,
            PatchedWritableWirelessLinkRequestDistanceUnitType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_1 = PatchedWritableWirelessLinkRequestDistanceUnitType1(data)

                return distance_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_2_type_1 = PatchedWritableWirelessLinkRequestDistanceUnitType2Type1(data)

                return distance_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_3_type_1 = PatchedWritableWirelessLinkRequestDistanceUnitType3Type1(data)

                return distance_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableWirelessLinkRequestDistanceUnitType1,
                    PatchedWritableWirelessLinkRequestDistanceUnitType2Type1,
                    PatchedWritableWirelessLinkRequestDistanceUnitType3Type1,
                    Unset,
                ],
                data,
            )

        distance_unit = _parse_distance_unit(d.pop("distance_unit", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableWirelessLinkRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableWirelessLinkRequestCustomFields.from_dict(_custom_fields)

        patched_writable_wireless_link_request = cls(
            interface_a=interface_a,
            interface_b=interface_b,
            ssid=ssid,
            status=status,
            tenant=tenant,
            auth_type=auth_type,
            auth_cipher=auth_cipher,
            auth_psk=auth_psk,
            distance=distance,
            distance_unit=distance_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_wireless_link_request.additional_properties = d
        return patched_writable_wireless_link_request

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
