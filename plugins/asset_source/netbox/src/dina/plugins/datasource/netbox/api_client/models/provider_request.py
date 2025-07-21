import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.provider_request_custom_fields import ProviderRequestCustomFields


T = TypeVar("T", bound="ProviderRequest")


@_attrs_define
class ProviderRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str): Full name of the provider
        slug (str):
        accounts (Union[Unset, list[int]]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        asns (Union[Unset, list[int]]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, ProviderRequestCustomFields]):
    """

    name: str
    slug: str
    accounts: Union[Unset, list[int]] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    asns: Union[Unset, list[int]] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ProviderRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        accounts: Union[Unset, list[int]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts

        description = self.description

        comments = self.comments

        asns: Union[Unset, list[int]] = UNSET
        if not isinstance(self.asns, Unset):
            asns = self.asns

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
                "slug": slug,
            }
        )
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if asns is not UNSET:
            field_dict["asns"] = asns
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        accounts: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.accounts, Unset):
            _temp_accounts = self.accounts
            accounts = (None, json.dumps(_temp_accounts).encode(), "application/json")

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

        asns: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.asns, Unset):
            _temp_asns = self.asns
            asns = (None, json.dumps(_temp_asns).encode(), "application/json")

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
                "slug": slug,
            }
        )
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if asns is not UNSET:
            field_dict["asns"] = asns
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.provider_request_custom_fields import ProviderRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        accounts = cast(list[int], d.pop("accounts", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        asns = cast(list[int], d.pop("asns", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ProviderRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ProviderRequestCustomFields.from_dict(_custom_fields)

        provider_request = cls(
            name=name,
            slug=slug,
            accounts=accounts,
            description=description,
            comments=comments,
            asns=asns,
            tags=tags,
            custom_fields=custom_fields,
        )

        provider_request.additional_properties = d
        return provider_request

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
