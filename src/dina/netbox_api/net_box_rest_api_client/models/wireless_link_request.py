from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wireless_link_request_auth_cipher import WirelessLinkRequestAuthCipher
from ..models.wireless_link_request_auth_type import WirelessLinkRequestAuthType
from ..models.wireless_link_request_distance_unit_type_1 import WirelessLinkRequestDistanceUnitType1
from ..models.wireless_link_request_distance_unit_type_2_type_1 import WirelessLinkRequestDistanceUnitType2Type1
from ..models.wireless_link_request_distance_unit_type_3_type_1 import WirelessLinkRequestDistanceUnitType3Type1
from ..models.wireless_link_request_status import WirelessLinkRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_interface_request import BriefInterfaceRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.wireless_link_request_custom_fields import WirelessLinkRequestCustomFields


T = TypeVar("T", bound="WirelessLinkRequest")


@_attrs_define
class WirelessLinkRequest:
    """Adds support for custom fields and tags.

    Attributes:
        interface_a (Union['BriefInterfaceRequest', int]):
        interface_b (Union['BriefInterfaceRequest', int]):
        ssid (Union[Unset, str]):
        status (Union[Unset, WirelessLinkRequestStatus]): * `connected` - Connected
            * `planned` - Planned
            * `decommissioning` - Decommissioning
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        auth_type (Union[Unset, WirelessLinkRequestAuthType]): * `open` - Open
            * `wep` - WEP
            * `wpa-personal` - WPA Personal (PSK)
            * `wpa-enterprise` - WPA Enterprise
        auth_cipher (Union[Unset, WirelessLinkRequestAuthCipher]): * `auto` - Auto
            * `tkip` - TKIP
            * `aes` - AES
        auth_psk (Union[Unset, str]):
        distance (Union[None, Unset, float]):
        distance_unit (Union[None, Unset, WirelessLinkRequestDistanceUnitType1,
            WirelessLinkRequestDistanceUnitType2Type1, WirelessLinkRequestDistanceUnitType3Type1]): * `km` - Kilometers
            * `m` - Meters
            * `mi` - Miles
            * `ft` - Feet
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WirelessLinkRequestCustomFields]):
    """

    interface_a: Union["BriefInterfaceRequest", int]
    interface_b: Union["BriefInterfaceRequest", int]
    ssid: Union[Unset, str] = UNSET
    status: Union[Unset, WirelessLinkRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    auth_type: Union[Unset, WirelessLinkRequestAuthType] = UNSET
    auth_cipher: Union[Unset, WirelessLinkRequestAuthCipher] = UNSET
    auth_psk: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union[
        None,
        Unset,
        WirelessLinkRequestDistanceUnitType1,
        WirelessLinkRequestDistanceUnitType2Type1,
        WirelessLinkRequestDistanceUnitType3Type1,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WirelessLinkRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_interface_request import BriefInterfaceRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        interface_a: Union[dict[str, Any], int]
        if isinstance(self.interface_a, BriefInterfaceRequest):
            interface_a = self.interface_a.to_dict()
        else:
            interface_a = self.interface_a

        interface_b: Union[dict[str, Any], int]
        if isinstance(self.interface_b, BriefInterfaceRequest):
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

        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        auth_cipher: Union[Unset, str] = UNSET
        if not isinstance(self.auth_cipher, Unset):
            auth_cipher = self.auth_cipher.value

        auth_psk = self.auth_psk

        distance: Union[None, Unset, float]
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        distance_unit: Union[None, Unset, str]
        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, WirelessLinkRequestDistanceUnitType1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, WirelessLinkRequestDistanceUnitType2Type1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, WirelessLinkRequestDistanceUnitType3Type1):
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
        field_dict.update(
            {
                "interface_a": interface_a,
                "interface_b": interface_b,
            }
        )
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
        from ..models.wireless_link_request_custom_fields import WirelessLinkRequestCustomFields

        d = dict(src_dict)

        def _parse_interface_a(data: object) -> Union["BriefInterfaceRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interface_a_type_1 = BriefInterfaceRequest.from_dict(data)

                return interface_a_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInterfaceRequest", int], data)

        interface_a = _parse_interface_a(d.pop("interface_a"))

        def _parse_interface_b(data: object) -> Union["BriefInterfaceRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interface_b_type_1 = BriefInterfaceRequest.from_dict(data)

                return interface_b_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInterfaceRequest", int], data)

        interface_b = _parse_interface_b(d.pop("interface_b"))

        ssid = d.pop("ssid", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WirelessLinkRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WirelessLinkRequestStatus(_status)

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
        auth_type: Union[Unset, WirelessLinkRequestAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = WirelessLinkRequestAuthType(_auth_type)

        _auth_cipher = d.pop("auth_cipher", UNSET)
        auth_cipher: Union[Unset, WirelessLinkRequestAuthCipher]
        if isinstance(_auth_cipher, Unset):
            auth_cipher = UNSET
        else:
            auth_cipher = WirelessLinkRequestAuthCipher(_auth_cipher)

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
            Unset,
            WirelessLinkRequestDistanceUnitType1,
            WirelessLinkRequestDistanceUnitType2Type1,
            WirelessLinkRequestDistanceUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_1 = WirelessLinkRequestDistanceUnitType1(data)

                return distance_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_2_type_1 = WirelessLinkRequestDistanceUnitType2Type1(data)

                return distance_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_3_type_1 = WirelessLinkRequestDistanceUnitType3Type1(data)

                return distance_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WirelessLinkRequestDistanceUnitType1,
                    WirelessLinkRequestDistanceUnitType2Type1,
                    WirelessLinkRequestDistanceUnitType3Type1,
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
        custom_fields: Union[Unset, WirelessLinkRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WirelessLinkRequestCustomFields.from_dict(_custom_fields)

        wireless_link_request = cls(
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

        wireless_link_request.additional_properties = d
        return wireless_link_request

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
