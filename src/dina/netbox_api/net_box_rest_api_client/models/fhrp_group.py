import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.fhrp_group_authentication_type import FHRPGroupAuthenticationType
from ..models.fhrp_group_protocol import FHRPGroupProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_address import BriefIPAddress
    from ..models.fhrp_group_custom_fields import FHRPGroupCustomFields
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="FHRPGroup")


@_attrs_define
class FHRPGroup:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        protocol (FHRPGroupProtocol): * `vrrp2` - VRRPv2
            * `vrrp3` - VRRPv3
            * `carp` - CARP
            * `clusterxl` - ClusterXL
            * `hsrp` - HSRP
            * `glbp` - GLBP
            * `other` - Other
        group_id (int):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        ip_addresses (list['BriefIPAddress']):
        name (Union[Unset, str]):
        auth_type (Union[FHRPGroupAuthenticationType, None, Unset]): * `plaintext` - Plaintext
            * `md5` - MD5
        auth_key (Union[Unset, str]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, FHRPGroupCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    protocol: FHRPGroupProtocol
    group_id: int
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    ip_addresses: list["BriefIPAddress"]
    name: Union[Unset, str] = UNSET
    auth_type: Union[FHRPGroupAuthenticationType, None, Unset] = UNSET
    auth_key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "FHRPGroupCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        protocol = self.protocol.value

        group_id = self.group_id

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

        ip_addresses = []
        for ip_addresses_item_data in self.ip_addresses:
            ip_addresses_item = ip_addresses_item_data.to_dict()
            ip_addresses.append(ip_addresses_item)

        name = self.name

        auth_type: Union[None, Unset, str]
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, FHRPGroupAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, FHRPGroupAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, FHRPGroupAuthenticationType):
            auth_type = self.auth_type.value
        else:
            auth_type = self.auth_type

        auth_key = self.auth_key

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
                "protocol": protocol,
                "group_id": group_id,
                "created": created,
                "last_updated": last_updated,
                "ip_addresses": ip_addresses,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if auth_key is not UNSET:
            field_dict["auth_key"] = auth_key
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
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.fhrp_group_custom_fields import FHRPGroupCustomFields
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        protocol = FHRPGroupProtocol(d.pop("protocol"))

        group_id = d.pop("group_id")

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

        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses")
        for ip_addresses_item_data in _ip_addresses:
            ip_addresses_item = BriefIPAddress.from_dict(ip_addresses_item_data)

            ip_addresses.append(ip_addresses_item)

        name = d.pop("name", UNSET)

        def _parse_auth_type(data: object) -> Union[FHRPGroupAuthenticationType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_1 = FHRPGroupAuthenticationType(data)

                return auth_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_2_type_1 = FHRPGroupAuthenticationType(data)

                return auth_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_3_type_1 = FHRPGroupAuthenticationType(data)

                return auth_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[FHRPGroupAuthenticationType, None, Unset], data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))

        auth_key = d.pop("auth_key", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, FHRPGroupCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = FHRPGroupCustomFields.from_dict(_custom_fields)

        fhrp_group = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            protocol=protocol,
            group_id=group_id,
            created=created,
            last_updated=last_updated,
            ip_addresses=ip_addresses,
            name=name,
            auth_type=auth_type,
            auth_key=auth_key,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        fhrp_group.additional_properties = d
        return fhrp_group

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
