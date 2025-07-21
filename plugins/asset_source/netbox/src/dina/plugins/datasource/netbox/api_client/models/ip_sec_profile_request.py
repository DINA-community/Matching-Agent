from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_sec_profile_request_mode import IPSecProfileRequestMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
    from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
    from ..models.ip_sec_profile_request_custom_fields import (
        IPSecProfileRequestCustomFields,
    )
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IPSecProfileRequest")


@_attrs_define
class IPSecProfileRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        mode (IPSecProfileRequestMode): * `esp` - ESP
            * `ah` - AH
        ike_policy (Union['BriefIKEPolicyRequest', int]):
        ipsec_policy (Union['BriefIPSecPolicyRequest', int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IPSecProfileRequestCustomFields]):
    """

    name: str
    mode: IPSecProfileRequestMode
    ike_policy: Union["BriefIKEPolicyRequest", int]
    ipsec_policy: Union["BriefIPSecPolicyRequest", int]
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IPSecProfileRequestCustomFields"] = UNSET
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_ike_policy_request import BriefIKEPolicyRequest
        from ..models.brief_ip_sec_policy_request import BriefIPSecPolicyRequest
        from ..models.ip_sec_profile_request_custom_fields import (
            IPSecProfileRequestCustomFields,
        )
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        mode = IPSecProfileRequestMode(d.pop("mode"))

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
        custom_fields: Union[Unset, IPSecProfileRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPSecProfileRequestCustomFields.from_dict(_custom_fields)

        ip_sec_profile_request = cls(
            name=name,
            mode=mode,
            ike_policy=ike_policy,
            ipsec_policy=ipsec_policy,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ip_sec_profile_request.additional_properties = d
        return ip_sec_profile_request

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
