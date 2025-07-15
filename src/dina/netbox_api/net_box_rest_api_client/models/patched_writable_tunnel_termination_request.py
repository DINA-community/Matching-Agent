import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_tunnel_termination_request_role import PatchedWritableTunnelTerminationRequestRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_address_request import BriefIPAddressRequest
    from ..models.brief_tunnel_request import BriefTunnelRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_tunnel_termination_request_custom_fields import (
        PatchedWritableTunnelTerminationRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableTunnelTerminationRequest")


@_attrs_define
class PatchedWritableTunnelTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        tunnel (Union['BriefTunnelRequest', Unset, int]):
        role (Union[Unset, PatchedWritableTunnelTerminationRequestRole]): * `peer` - Peer
            * `hub` - Hub
            * `spoke` - Spoke
        termination_type (Union[Unset, str]):
        termination_id (Union[None, Unset, int]):
        outside_ip (Union['BriefIPAddressRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableTunnelTerminationRequestCustomFields]):
    """

    tunnel: Union["BriefTunnelRequest", Unset, int] = UNSET
    role: Union[Unset, PatchedWritableTunnelTerminationRequestRole] = UNSET
    termination_type: Union[Unset, str] = UNSET
    termination_id: Union[None, Unset, int] = UNSET
    outside_ip: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableTunnelTerminationRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_tunnel_request import BriefTunnelRequest

        tunnel: Union[Unset, dict[str, Any], int]
        if isinstance(self.tunnel, Unset):
            tunnel = UNSET
        elif isinstance(self.tunnel, BriefTunnelRequest):
            tunnel = self.tunnel.to_dict()
        else:
            tunnel = self.tunnel

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        termination_type = self.termination_type

        termination_id: Union[None, Unset, int]
        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        else:
            termination_id = self.termination_id

        outside_ip: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.outside_ip, Unset):
            outside_ip = UNSET
        elif isinstance(self.outside_ip, BriefIPAddressRequest):
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
        field_dict.update({})
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel
        if role is not UNSET:
            field_dict["role"] = role
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id
        if outside_ip is not UNSET:
            field_dict["outside_ip"] = outside_ip
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        tunnel: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tunnel, Unset):
            tunnel = UNSET
        elif isinstance(self.tunnel, int):
            tunnel = (None, str(self.tunnel).encode(), "text/plain")
        else:
            tunnel = (None, json.dumps(self.tunnel.to_dict()).encode(), "application/json")

        role: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.role, Unset):
            role = (None, str(self.role.value).encode(), "text/plain")

        termination_type = (
            self.termination_type
            if isinstance(self.termination_type, Unset)
            else (None, str(self.termination_type).encode(), "text/plain")
        )

        termination_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        elif isinstance(self.termination_id, int):
            termination_id = (None, str(self.termination_id).encode(), "text/plain")
        else:
            termination_id = (None, str(self.termination_id).encode(), "text/plain")

        outside_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.outside_ip, Unset):
            outside_ip = UNSET
        elif isinstance(self.outside_ip, int):
            outside_ip = (None, str(self.outside_ip).encode(), "text/plain")
        elif isinstance(self.outside_ip, None):
            outside_ip = (None, str(self.outside_ip).encode(), "text/plain")
        elif isinstance(self.outside_ip, BriefIPAddressRequest):
            outside_ip = (None, json.dumps(self.outside_ip.to_dict()).encode(), "application/json")
        else:
            outside_ip = (None, str(self.outside_ip).encode(), "text/plain")

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
        if tunnel is not UNSET:
            field_dict["tunnel"] = tunnel
        if role is not UNSET:
            field_dict["role"] = role
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
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
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_tunnel_request import BriefTunnelRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_tunnel_termination_request_custom_fields import (
            PatchedWritableTunnelTerminationRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_tunnel(data: object) -> Union["BriefTunnelRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tunnel_type_1 = BriefTunnelRequest.from_dict(data)

                return tunnel_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTunnelRequest", Unset, int], data)

        tunnel = _parse_tunnel(d.pop("tunnel", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, PatchedWritableTunnelTerminationRequestRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = PatchedWritableTunnelTerminationRequestRole(_role)

        termination_type = d.pop("termination_type", UNSET)

        def _parse_termination_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        termination_id = _parse_termination_id(d.pop("termination_id", UNSET))

        def _parse_outside_ip(data: object) -> Union["BriefIPAddressRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outside_ip_type_1_type_1 = BriefIPAddressRequest.from_dict(data)

                return outside_ip_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddressRequest", None, Unset, int], data)

        outside_ip = _parse_outside_ip(d.pop("outside_ip", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableTunnelTerminationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableTunnelTerminationRequestCustomFields.from_dict(_custom_fields)

        patched_writable_tunnel_termination_request = cls(
            tunnel=tunnel,
            role=role,
            termination_type=termination_type,
            termination_id=termination_id,
            outside_ip=outside_ip,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_tunnel_termination_request.additional_properties = d
        return patched_writable_tunnel_termination_request

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
