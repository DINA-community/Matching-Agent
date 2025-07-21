import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asn import ASN
    from ..models.nested_provider_account import NestedProviderAccount
    from ..models.nested_tag import NestedTag
    from ..models.provider_custom_fields import ProviderCustomFields


T = TypeVar("T", bound="Provider")


@_attrs_define
class Provider:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str): Full name of the provider
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        circuit_count (int):
        accounts (Union[Unset, list['NestedProviderAccount']]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        asns (Union[Unset, list['ASN']]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ProviderCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    circuit_count: int
    accounts: Union[Unset, list["NestedProviderAccount"]] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    asns: Union[Unset, list["ASN"]] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ProviderCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        slug = self.slug

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        circuit_count = self.circuit_count

        accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()
                accounts.append(accounts_item)

        description = self.description

        comments = self.comments

        asns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.asns, Unset):
            asns = []
            for asns_item_data in self.asns:
                asns_item = asns_item_data.to_dict()
                asns.append(asns_item)

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
                "circuit_count": circuit_count,
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
        from ..models.asn import ASN
        from ..models.nested_provider_account import NestedProviderAccount
        from ..models.nested_tag import NestedTag
        from ..models.provider_custom_fields import ProviderCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

        circuit_count = d.pop("circuit_count")

        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = NestedProviderAccount.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        asns = []
        _asns = d.pop("asns", UNSET)
        for asns_item_data in _asns or []:
            asns_item = ASN.from_dict(asns_item_data)

            asns.append(asns_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ProviderCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ProviderCustomFields.from_dict(_custom_fields)

        provider = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            created=created,
            last_updated=last_updated,
            circuit_count=circuit_count,
            accounts=accounts,
            description=description,
            comments=comments,
            asns=asns,
            tags=tags,
            custom_fields=custom_fields,
        )

        provider.additional_properties = d
        return provider

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
