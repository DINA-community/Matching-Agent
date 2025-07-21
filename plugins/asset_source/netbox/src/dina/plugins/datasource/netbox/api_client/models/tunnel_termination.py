import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_address import BriefIPAddress
    from ..models.brief_tunnel import BriefTunnel
    from ..models.nested_tag import NestedTag
    from ..models.tunnel_termination_custom_fields import TunnelTerminationCustomFields
    from ..models.tunnel_termination_role import TunnelTerminationRole


T = TypeVar("T", bound="TunnelTermination")


@_attrs_define
class TunnelTermination:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        tunnel (BriefTunnel): Adds support for custom fields and tags.
        role (TunnelTerminationRole):
        termination_type (str):
        termination (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        termination_id (Union[None, Unset, int]):
        outside_ip (Union['BriefIPAddress', None, Unset]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, TunnelTerminationCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    tunnel: "BriefTunnel"
    role: "TunnelTerminationRole"
    termination_type: str
    termination: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    termination_id: Union[None, Unset, int] = UNSET
    outside_ip: Union["BriefIPAddress", None, Unset] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "TunnelTerminationCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ip_address import BriefIPAddress

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        tunnel = self.tunnel.to_dict()

        role = self.role.to_dict()

        termination_type = self.termination_type

        termination = self.termination

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

        termination_id: Union[None, Unset, int]
        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        else:
            termination_id = self.termination_id

        outside_ip: Union[None, Unset, dict[str, Any]]
        if isinstance(self.outside_ip, Unset):
            outside_ip = UNSET
        elif isinstance(self.outside_ip, BriefIPAddress):
            outside_ip = self.outside_ip.to_dict()
        else:
            outside_ip = self.outside_ip

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
                "tunnel": tunnel,
                "role": role,
                "termination_type": termination_type,
                "termination": termination,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id
        if outside_ip is not UNSET:
            field_dict["outside_ip"] = outside_ip
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_tunnel import BriefTunnel
        from ..models.nested_tag import NestedTag
        from ..models.tunnel_termination_custom_fields import (
            TunnelTerminationCustomFields,
        )
        from ..models.tunnel_termination_role import TunnelTerminationRole

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        tunnel = BriefTunnel.from_dict(d.pop("tunnel"))

        role = TunnelTerminationRole.from_dict(d.pop("role"))

        termination_type = d.pop("termination_type")

        termination = d.pop("termination")

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

        def _parse_termination_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        termination_id = _parse_termination_id(d.pop("termination_id", UNSET))

        def _parse_outside_ip(data: object) -> Union["BriefIPAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outside_ip_type_1 = BriefIPAddress.from_dict(data)

                return outside_ip_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddress", None, Unset], data)

        outside_ip = _parse_outside_ip(d.pop("outside_ip", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, TunnelTerminationCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TunnelTerminationCustomFields.from_dict(_custom_fields)

        tunnel_termination = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            tunnel=tunnel,
            role=role,
            termination_type=termination_type,
            termination=termination,
            created=created,
            last_updated=last_updated,
            termination_id=termination_id,
            outside_ip=outside_ip,
            tags=tags,
            custom_fields=custom_fields,
        )

        tunnel_termination.additional_properties = d
        return tunnel_termination

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
