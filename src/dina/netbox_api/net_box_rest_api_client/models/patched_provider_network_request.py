import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_request import BriefProviderRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_provider_network_request_custom_fields import PatchedProviderNetworkRequestCustomFields


T = TypeVar("T", bound="PatchedProviderNetworkRequest")


@_attrs_define
class PatchedProviderNetworkRequest:
    """Adds support for custom fields and tags.

    Attributes:
        provider (Union['BriefProviderRequest', Unset, int]):
        name (Union[Unset, str]):
        service_id (Union[Unset, str]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedProviderNetworkRequestCustomFields]):
    """

    provider: Union["BriefProviderRequest", Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedProviderNetworkRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_request import BriefProviderRequest

        provider: Union[Unset, dict[str, Any], int]
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, BriefProviderRequest):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        name = self.name

        service_id = self.service_id

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
        if provider is not UNSET:
            field_dict["provider"] = provider
        if name is not UNSET:
            field_dict["name"] = name
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
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
        provider: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, int):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, json.dumps(self.provider.to_dict()).encode(), "application/json")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        service_id = (
            self.service_id
            if isinstance(self.service_id, Unset)
            else (None, str(self.service_id).encode(), "text/plain")
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
        if provider is not UNSET:
            field_dict["provider"] = provider
        if name is not UNSET:
            field_dict["name"] = name
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
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
        from ..models.brief_provider_request import BriefProviderRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_provider_network_request_custom_fields import PatchedProviderNetworkRequestCustomFields

        d = dict(src_dict)

        def _parse_provider(data: object) -> Union["BriefProviderRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_1 = BriefProviderRequest.from_dict(data)

                return provider_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderRequest", Unset, int], data)

        provider = _parse_provider(d.pop("provider", UNSET))

        name = d.pop("name", UNSET)

        service_id = d.pop("service_id", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedProviderNetworkRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedProviderNetworkRequestCustomFields.from_dict(_custom_fields)

        patched_provider_network_request = cls(
            provider=provider,
            name=name,
            service_id=service_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_provider_network_request.additional_properties = d
        return patched_provider_network_request

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
