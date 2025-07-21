import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_request import BriefProviderRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.provider_account_request_custom_fields import (
        ProviderAccountRequestCustomFields,
    )


T = TypeVar("T", bound="ProviderAccountRequest")


@_attrs_define
class ProviderAccountRequest:
    """Adds support for custom fields and tags.

    Attributes:
        provider (Union['BriefProviderRequest', int]):
        account (str):
        name (Union[Unset, str]):  Default: ''.
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, ProviderAccountRequestCustomFields]):
    """

    provider: Union["BriefProviderRequest", int]
    account: str
    name: Union[Unset, str] = ""
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ProviderAccountRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_request import BriefProviderRequest

        provider: Union[dict[str, Any], int]
        if isinstance(self.provider, BriefProviderRequest):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        account = self.account

        name = self.name

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
                "provider": provider,
                "account": account,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
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
        provider: tuple[None, bytes, str]

        if isinstance(self.provider, int):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (
                None,
                json.dumps(self.provider.to_dict()).encode(),
                "application/json",
            )

        account = (None, str(self.account).encode(), "text/plain")

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
                "provider": provider,
                "account": account,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.provider_account_request_custom_fields import (
            ProviderAccountRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_provider(data: object) -> Union["BriefProviderRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_1 = BriefProviderRequest.from_dict(data)

                return provider_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderRequest", int], data)

        provider = _parse_provider(d.pop("provider"))

        account = d.pop("account")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ProviderAccountRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ProviderAccountRequestCustomFields.from_dict(_custom_fields)

        provider_account_request = cls(
            provider=provider,
            account=account,
            name=name,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        provider_account_request.additional_properties = d
        return provider_account_request

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
