import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_ip_sec_profile_request_mode import PatchedWritableIPSecProfileRequestMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
    from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_ip_sec_profile_request_custom_fields import (
        PatchedWritableIPSecProfileRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableIPSecProfileRequest")


@_attrs_define
class PatchedWritableIPSecProfileRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        mode (Union[Unset, PatchedWritableIPSecProfileRequestMode]): * `esp` - ESP
            * `ah` - AH
        ike_policy (Union['BriefIKEPolicyRequest', Unset, int]):
        ipsec_policy (Union['BriefIPSecPolicyRequest', Unset, int]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableIPSecProfileRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, PatchedWritableIPSecProfileRequestMode] = UNSET
    ike_policy: Union["BriefIKEPolicyRequest", Unset, int] = UNSET
    ipsec_policy: Union["BriefIPSecPolicyRequest", Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableIPSecProfileRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
        from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest

        name = self.name

        description = self.description

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        ike_policy: Union[Unset, dict[str, Any], int]
        if isinstance(self.ike_policy, Unset):
            ike_policy = UNSET
        elif isinstance(self.ike_policy, BriefIKEPolicyRequest):
            ike_policy = self.ike_policy.to_dict()
        else:
            ike_policy = self.ike_policy

        ipsec_policy: Union[Unset, dict[str, Any], int]
        if isinstance(self.ipsec_policy, Unset):
            ipsec_policy = UNSET
        elif isinstance(self.ipsec_policy, BriefIPSecPolicyRequest):
            ipsec_policy = self.ipsec_policy.to_dict()
        else:
            ipsec_policy = self.ipsec_policy

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
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if ike_policy is not UNSET:
            field_dict["ike_policy"] = ike_policy
        if ipsec_policy is not UNSET:
            field_dict["ipsec_policy"] = ipsec_policy
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        mode: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = (None, str(self.mode.value).encode(), "text/plain")

        ike_policy: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ike_policy, Unset):
            ike_policy = UNSET
        elif isinstance(self.ike_policy, int):
            ike_policy = (None, str(self.ike_policy).encode(), "text/plain")
        else:
            ike_policy = (None, json.dumps(self.ike_policy.to_dict()).encode(), "application/json")

        ipsec_policy: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ipsec_policy, Unset):
            ipsec_policy = UNSET
        elif isinstance(self.ipsec_policy, int):
            ipsec_policy = (None, str(self.ipsec_policy).encode(), "text/plain")
        else:
            ipsec_policy = (None, json.dumps(self.ipsec_policy.to_dict()).encode(), "application/json")

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
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if ike_policy is not UNSET:
            field_dict["ike_policy"] = ike_policy
        if ipsec_policy is not UNSET:
            field_dict["ipsec_policy"] = ipsec_policy
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
        from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_ip_sec_profile_request_custom_fields import (
            PatchedWritableIPSecProfileRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, PatchedWritableIPSecProfileRequestMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = PatchedWritableIPSecProfileRequestMode(_mode)

        def _parse_ike_policy(data: object) -> Union["BriefIKEPolicyRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ike_policy_type_1 = BriefIKEPolicyRequest.from_dict(data)

                return ike_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIKEPolicyRequest", Unset, int], data)

        ike_policy = _parse_ike_policy(d.pop("ike_policy", UNSET))

        def _parse_ipsec_policy(data: object) -> Union["BriefIPSecPolicyRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ipsec_policy_type_1 = BriefIPSecPolicyRequest.from_dict(data)

                return ipsec_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPSecPolicyRequest", Unset, int], data)

        ipsec_policy = _parse_ipsec_policy(d.pop("ipsec_policy", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableIPSecProfileRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableIPSecProfileRequestCustomFields.from_dict(_custom_fields)

        patched_writable_ip_sec_profile_request = cls(
            name=name,
            description=description,
            mode=mode,
            ike_policy=ike_policy,
            ipsec_policy=ipsec_policy,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_ip_sec_profile_request.additional_properties = d
        return patched_writable_ip_sec_profile_request

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
