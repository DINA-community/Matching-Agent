import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_fhrp_group_request_authentication_type import PatchedFHRPGroupRequestAuthenticationType
from ..models.patched_fhrp_group_request_protocol import PatchedFHRPGroupRequestProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_fhrp_group_request_custom_fields import PatchedFHRPGroupRequestCustomFields


T = TypeVar("T", bound="PatchedFHRPGroupRequest")


@_attrs_define
class PatchedFHRPGroupRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        protocol (Union[Unset, PatchedFHRPGroupRequestProtocol]): * `vrrp2` - VRRPv2
            * `vrrp3` - VRRPv3
            * `carp` - CARP
            * `clusterxl` - ClusterXL
            * `hsrp` - HSRP
            * `glbp` - GLBP
            * `other` - Other
        group_id (Union[Unset, int]):
        auth_type (Union[None, PatchedFHRPGroupRequestAuthenticationType, Unset]): * `plaintext` - Plaintext
            * `md5` - MD5
        auth_key (Union[Unset, str]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedFHRPGroupRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    protocol: Union[Unset, PatchedFHRPGroupRequestProtocol] = UNSET
    group_id: Union[Unset, int] = UNSET
    auth_type: Union[None, PatchedFHRPGroupRequestAuthenticationType, Unset] = UNSET
    auth_key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedFHRPGroupRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        group_id = self.group_id

        auth_type: Union[None, Unset, str]
        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, PatchedFHRPGroupRequestAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, PatchedFHRPGroupRequestAuthenticationType):
            auth_type = self.auth_type.value
        elif isinstance(self.auth_type, PatchedFHRPGroupRequestAuthenticationType):
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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
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

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        protocol: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = (None, str(self.protocol.value).encode(), "text/plain")

        group_id = (
            self.group_id if isinstance(self.group_id, Unset) else (None, str(self.group_id).encode(), "text/plain")
        )

        auth_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.auth_type, Unset):
            auth_type = UNSET
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        elif isinstance(self.auth_type, PatchedFHRPGroupRequestAuthenticationType):
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        elif isinstance(self.auth_type, PatchedFHRPGroupRequestAuthenticationType):
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")
        elif isinstance(self.auth_type, None):
            auth_type = (None, str(self.auth_type).encode(), "text/plain")
        else:
            auth_type = (None, str(self.auth_type.value).encode(), "text/plain")

        auth_key = (
            self.auth_key if isinstance(self.auth_key, Unset) else (None, str(self.auth_key).encode(), "text/plain")
        )

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
        if name is not UNSET:
            field_dict["name"] = name
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_fhrp_group_request_custom_fields import PatchedFHRPGroupRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, PatchedFHRPGroupRequestProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = PatchedFHRPGroupRequestProtocol(_protocol)

        group_id = d.pop("group_id", UNSET)

        def _parse_auth_type(data: object) -> Union[None, PatchedFHRPGroupRequestAuthenticationType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_1 = PatchedFHRPGroupRequestAuthenticationType(data)

                return auth_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_2_type_1 = PatchedFHRPGroupRequestAuthenticationType(data)

                return auth_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auth_type_type_3_type_1 = PatchedFHRPGroupRequestAuthenticationType(data)

                return auth_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedFHRPGroupRequestAuthenticationType, Unset], data)

        auth_type = _parse_auth_type(d.pop("auth_type", UNSET))

        auth_key = d.pop("auth_key", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedFHRPGroupRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedFHRPGroupRequestCustomFields.from_dict(_custom_fields)

        patched_fhrp_group_request = cls(
            name=name,
            protocol=protocol,
            group_id=group_id,
            auth_type=auth_type,
            auth_key=auth_key,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_fhrp_group_request.additional_properties = d
        return patched_fhrp_group_request

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
