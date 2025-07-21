import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_ip_sec_profile_request_mode import (
    WritableIPSecProfileRequestMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
    from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_ip_sec_profile_request_custom_fields import (
        WritableIPSecProfileRequestCustomFields,
    )


T = TypeVar("T", bound="WritableIPSecProfileRequest")


@_attrs_define
class WritableIPSecProfileRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        mode (WritableIPSecProfileRequestMode): * `esp` - ESP
            * `ah` - AH
        ike_policy (Union['BriefIKEPolicyRequest', int]):
        ipsec_policy (Union['BriefIPSecPolicyRequest', int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableIPSecProfileRequestCustomFields]):
    """

    name: str
    mode: WritableIPSecProfileRequestMode
    ike_policy: Union["BriefIKEPolicyRequest", int]
    ipsec_policy: Union["BriefIPSecPolicyRequest", int]
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableIPSecProfileRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
        from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest

        name = self.name

        mode = self.mode.value

        ike_policy: Union[dict[str, Any], int]
        if isinstance(self.ike_policy, BriefIKEPolicyRequest):
            ike_policy = self.ike_policy.to_dict()
        else:
            ike_policy = self.ike_policy

        ipsec_policy: Union[dict[str, Any], int]
        if isinstance(self.ipsec_policy, BriefIPSecPolicyRequest):
            ipsec_policy = self.ipsec_policy.to_dict()
        else:
            ipsec_policy = self.ipsec_policy

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
                "name": name,
                "mode": mode,
                "ike_policy": ike_policy,
                "ipsec_policy": ipsec_policy,
            }
        )
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
        name = (None, str(self.name).encode(), "text/plain")

        mode = (None, str(self.mode.value).encode(), "text/plain")

        ike_policy: tuple[None, bytes, str]

        if isinstance(self.ike_policy, int):
            ike_policy = (None, str(self.ike_policy).encode(), "text/plain")
        else:
            ike_policy = (
                None,
                json.dumps(self.ike_policy.to_dict()).encode(),
                "application/json",
            )

        ipsec_policy: tuple[None, bytes, str]

        if isinstance(self.ipsec_policy, int):
            ipsec_policy = (None, str(self.ipsec_policy).encode(), "text/plain")
        else:
            ipsec_policy = (
                None,
                json.dumps(self.ipsec_policy.to_dict()).encode(),
                "application/json",
            )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
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
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "mode": mode,
                "ike_policy": ike_policy,
                "ipsec_policy": ipsec_policy,
            }
        )
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
        from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
        from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_ip_sec_profile_request_custom_fields import (
            WritableIPSecProfileRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        mode = WritableIPSecProfileRequestMode(d.pop("mode"))

        def _parse_ike_policy(data: object) -> Union["BriefIKEPolicyRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ike_policy_type_1 = BriefIKEPolicyRequest.from_dict(data)

                return ike_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIKEPolicyRequest", int], data)

        ike_policy = _parse_ike_policy(d.pop("ike_policy"))

        def _parse_ipsec_policy(data: object) -> Union["BriefIPSecPolicyRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ipsec_policy_type_1 = BriefIPSecPolicyRequest.from_dict(data)

                return ipsec_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPSecPolicyRequest", int], data)

        ipsec_policy = _parse_ipsec_policy(d.pop("ipsec_policy"))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableIPSecProfileRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableIPSecProfileRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_ip_sec_profile_request = cls(
            name=name,
            mode=mode,
            ike_policy=ike_policy,
            ipsec_policy=ipsec_policy,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_ip_sec_profile_request.additional_properties = d
        return writable_ip_sec_profile_request

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
