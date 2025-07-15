from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_policy_request_mode import IKEPolicyRequestMode
from ..models.ike_policy_request_version import IKEPolicyRequestVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ike_policy_request_custom_fields import IKEPolicyRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IKEPolicyRequest")


@_attrs_define
class IKEPolicyRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        version (IKEPolicyRequestVersion): * `1` - IKEv1
            * `2` - IKEv2
        description (Union[Unset, str]):
        mode (Union[Unset, IKEPolicyRequestMode]): * `aggressive` - Aggressive
            * `main` - Main
        proposals (Union[Unset, list[int]]):
        preshared_key (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IKEPolicyRequestCustomFields]):
    """

    name: str
    version: IKEPolicyRequestVersion
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, IKEPolicyRequestMode] = UNSET
    proposals: Union[Unset, list[int]] = UNSET
    preshared_key: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IKEPolicyRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version.value

        description = self.description

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        proposals: Union[Unset, list[int]] = UNSET
        if not isinstance(self.proposals, Unset):
            proposals = self.proposals

        preshared_key = self.preshared_key

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
                "version": version,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if proposals is not UNSET:
            field_dict["proposals"] = proposals
        if preshared_key is not UNSET:
            field_dict["preshared_key"] = preshared_key
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ike_policy_request_custom_fields import IKEPolicyRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        version = IKEPolicyRequestVersion(d.pop("version"))

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, IKEPolicyRequestMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IKEPolicyRequestMode(_mode)

        proposals = cast(list[int], d.pop("proposals", UNSET))

        preshared_key = d.pop("preshared_key", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IKEPolicyRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IKEPolicyRequestCustomFields.from_dict(_custom_fields)

        ike_policy_request = cls(
            name=name,
            version=version,
            description=description,
            mode=mode,
            proposals=proposals,
            preshared_key=preshared_key,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ike_policy_request.additional_properties = d
        return ike_policy_request

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
