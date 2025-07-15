import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_interface import BriefInterface
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.wireless_link_auth_cipher import WirelessLinkAuthCipher
    from ..models.wireless_link_auth_type import WirelessLinkAuthType
    from ..models.wireless_link_custom_fields import WirelessLinkCustomFields
    from ..models.wireless_link_distance_unit_type_0 import WirelessLinkDistanceUnitType0
    from ..models.wireless_link_status import WirelessLinkStatus


T = TypeVar("T", bound="WirelessLink")


@_attrs_define
class WirelessLink:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        interface_a (BriefInterface): Adds support for custom fields and tags.
        interface_b (BriefInterface): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        ssid (Union[Unset, str]):
        status (Union[Unset, WirelessLinkStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        auth_type (Union[Unset, WirelessLinkAuthType]):
        auth_cipher (Union[Unset, WirelessLinkAuthCipher]):
        auth_psk (Union[Unset, str]):
        distance (Union[None, Unset, float]):
        distance_unit (Union['WirelessLinkDistanceUnitType0', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, WirelessLinkCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    interface_a: "BriefInterface"
    interface_b: "BriefInterface"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    ssid: Union[Unset, str] = UNSET
    status: Union[Unset, "WirelessLinkStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    auth_type: Union[Unset, "WirelessLinkAuthType"] = UNSET
    auth_cipher: Union[Unset, "WirelessLinkAuthCipher"] = UNSET
    auth_psk: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union["WirelessLinkDistanceUnitType0", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "WirelessLinkCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant
        from ..models.wireless_link_distance_unit_type_0 import WirelessLinkDistanceUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        interface_a = self.interface_a.to_dict()

        interface_b = self.interface_b.to_dict()

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

        ssid = self.ssid

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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

        distance: Union[None, Unset, float]
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        distance_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, WirelessLinkDistanceUnitType0):
            distance_unit = self.distance_unit.to_dict()
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_interface import BriefInterface
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.wireless_link_auth_cipher import WirelessLinkAuthCipher
        from ..models.wireless_link_auth_type import WirelessLinkAuthType
        from ..models.wireless_link_custom_fields import WirelessLinkCustomFields
        from ..models.wireless_link_distance_unit_type_0 import WirelessLinkDistanceUnitType0
        from ..models.wireless_link_status import WirelessLinkStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        interface_a = BriefInterface.from_dict(d.pop("interface_a"))

        interface_b = BriefInterface.from_dict(d.pop("interface_b"))

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

        ssid = d.pop("ssid", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WirelessLinkStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WirelessLinkStatus.from_dict(_status)

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
        auth_type: Union[Unset, WirelessLinkAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = WirelessLinkAuthType.from_dict(_auth_type)

        _auth_cipher = d.pop("auth_cipher", UNSET)
        auth_cipher: Union[Unset, WirelessLinkAuthCipher]
        if isinstance(_auth_cipher, Unset):
            auth_cipher = UNSET
        else:
            auth_cipher = WirelessLinkAuthCipher.from_dict(_auth_cipher)

        auth_psk = d.pop("auth_psk", UNSET)

        def _parse_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        distance = _parse_distance(d.pop("distance", UNSET))

        def _parse_distance_unit(data: object) -> Union["WirelessLinkDistanceUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distance_unit_type_0 = WirelessLinkDistanceUnitType0.from_dict(data)

                return distance_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WirelessLinkDistanceUnitType0", None, Unset], data)

        distance_unit = _parse_distance_unit(d.pop("distance_unit", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WirelessLinkCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WirelessLinkCustomFields.from_dict(_custom_fields)

        wireless_link = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            interface_a=interface_a,
            interface_b=interface_b,
            created=created,
            last_updated=last_updated,
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

        wireless_link.additional_properties = d
        return wireless_link

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
