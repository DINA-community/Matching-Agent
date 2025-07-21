from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_sec_policy_request_pfs_group import IPSecPolicyRequestPfsGroup
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_policy_request_custom_fields import (
        IPSecPolicyRequestCustomFields,
    )
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IPSecPolicyRequest")


@_attrs_define
class IPSecPolicyRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        description (Union[Unset, str]):
        proposals (Union[Unset, list[int]]):
        pfs_group (Union[Unset, IPSecPolicyRequestPfsGroup]): * `1` - Group 1
            * `2` - Group 2
            * `5` - Group 5
            * `14` - Group 14
            * `15` - Group 15
            * `16` - Group 16
            * `17` - Group 17
            * `18` - Group 18
            * `19` - Group 19
            * `20` - Group 20
            * `21` - Group 21
            * `22` - Group 22
            * `23` - Group 23
            * `24` - Group 24
            * `25` - Group 25
            * `26` - Group 26
            * `27` - Group 27
            * `28` - Group 28
            * `29` - Group 29
            * `30` - Group 30
            * `31` - Group 31
            * `32` - Group 32
            * `33` - Group 33
            * `34` - Group 34
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IPSecPolicyRequestCustomFields]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    proposals: Union[Unset, list[int]] = UNSET
    pfs_group: Union[Unset, IPSecPolicyRequestPfsGroup] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IPSecPolicyRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        proposals: Union[Unset, list[int]] = UNSET
        if not isinstance(self.proposals, Unset):
            proposals = self.proposals

        pfs_group: Union[Unset, int] = UNSET
        if not isinstance(self.pfs_group, Unset):
            pfs_group = self.pfs_group.value

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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if proposals is not UNSET:
            field_dict["proposals"] = proposals
        if pfs_group is not UNSET:
            field_dict["pfs_group"] = pfs_group
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_policy_request_custom_fields import (
            IPSecPolicyRequestCustomFields,
        )
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        proposals = cast(list[int], d.pop("proposals", UNSET))

        _pfs_group = d.pop("pfs_group", UNSET)
        pfs_group: Union[Unset, IPSecPolicyRequestPfsGroup]
        if isinstance(_pfs_group, Unset):
            pfs_group = UNSET
        else:
            pfs_group = IPSecPolicyRequestPfsGroup(_pfs_group)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IPSecPolicyRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPSecPolicyRequestCustomFields.from_dict(_custom_fields)

        ip_sec_policy_request = cls(
            name=name,
            description=description,
            proposals=proposals,
            pfs_group=pfs_group,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ip_sec_policy_request.additional_properties = d
        return ip_sec_policy_request

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
