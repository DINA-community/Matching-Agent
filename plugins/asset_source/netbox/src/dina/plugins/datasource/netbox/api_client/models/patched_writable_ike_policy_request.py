import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_ike_policy_request_mode_type_1 import (
    PatchedWritableIKEPolicyRequestModeType1,
)
from ..models.patched_writable_ike_policy_request_mode_type_2_type_1 import (
    PatchedWritableIKEPolicyRequestModeType2Type1,
)
from ..models.patched_writable_ike_policy_request_mode_type_3_type_1 import (
    PatchedWritableIKEPolicyRequestModeType3Type1,
)
from ..models.patched_writable_ike_policy_request_version import (
    PatchedWritableIKEPolicyRequestVersion,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_ike_policy_request_custom_fields import (
        PatchedWritableIKEPolicyRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableIKEPolicyRequest")


@_attrs_define
class PatchedWritableIKEPolicyRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        version (Union[Unset, PatchedWritableIKEPolicyRequestVersion]): * `1` - IKEv1
            * `2` - IKEv2
        mode (Union[None, PatchedWritableIKEPolicyRequestModeType1, PatchedWritableIKEPolicyRequestModeType2Type1,
            PatchedWritableIKEPolicyRequestModeType3Type1, Unset]): * `aggressive` - Aggressive
            * `main` - Main
        proposals (Union[Unset, list[int]]):
        preshared_key (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableIKEPolicyRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    version: Union[Unset, PatchedWritableIKEPolicyRequestVersion] = UNSET
    mode: Union[
        None,
        PatchedWritableIKEPolicyRequestModeType1,
        PatchedWritableIKEPolicyRequestModeType2Type1,
        PatchedWritableIKEPolicyRequestModeType3Type1,
        Unset,
    ] = UNSET
    proposals: Union[Unset, list[int]] = UNSET
    preshared_key: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableIKEPolicyRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        version: Union[Unset, int] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, PatchedWritableIKEPolicyRequestModeType1):
            mode = self.mode.value
        elif isinstance(self.mode, PatchedWritableIKEPolicyRequestModeType2Type1):
            mode = self.mode.value
        elif isinstance(self.mode, PatchedWritableIKEPolicyRequestModeType3Type1):
            mode = self.mode.value
        else:
            mode = self.mode

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
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

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        version: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.version, Unset):
            version = (None, str(self.version.value).encode(), "text/plain")

        mode: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        elif isinstance(self.mode, PatchedWritableIKEPolicyRequestModeType1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        elif isinstance(self.mode, PatchedWritableIKEPolicyRequestModeType2Type1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        else:
            mode = (None, str(self.mode.value).encode(), "text/plain")

        proposals: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.proposals, Unset):
            _temp_proposals = self.proposals
            proposals = (None, json.dumps(_temp_proposals).encode(), "application/json")

        preshared_key = (
            self.preshared_key
            if isinstance(self.preshared_key, Unset)
            else (None, str(self.preshared_key).encode(), "text/plain")
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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_ike_policy_request_custom_fields import (
            PatchedWritableIKEPolicyRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, PatchedWritableIKEPolicyRequestVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = PatchedWritableIKEPolicyRequestVersion(_version)

        def _parse_mode(
            data: object,
        ) -> Union[
            None,
            PatchedWritableIKEPolicyRequestModeType1,
            PatchedWritableIKEPolicyRequestModeType2Type1,
            PatchedWritableIKEPolicyRequestModeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = PatchedWritableIKEPolicyRequestModeType1(data)

                return mode_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_2_type_1 = PatchedWritableIKEPolicyRequestModeType2Type1(data)

                return mode_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_3_type_1 = PatchedWritableIKEPolicyRequestModeType3Type1(data)

                return mode_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableIKEPolicyRequestModeType1,
                    PatchedWritableIKEPolicyRequestModeType2Type1,
                    PatchedWritableIKEPolicyRequestModeType3Type1,
                    Unset,
                ],
                data,
            )

        mode = _parse_mode(d.pop("mode", UNSET))

        proposals = cast(list[int], d.pop("proposals", UNSET))

        preshared_key = d.pop("preshared_key", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableIKEPolicyRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableIKEPolicyRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_writable_ike_policy_request = cls(
            name=name,
            description=description,
            version=version,
            mode=mode,
            proposals=proposals,
            preshared_key=preshared_key,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_ike_policy_request.additional_properties = d
        return patched_writable_ike_policy_request

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
