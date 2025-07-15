from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefProviderAccount")


@_attrs_define
class BriefProviderAccount:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        account (str):
        name (Union[Unset, str]):  Default: ''.
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    account: str
    name: Union[Unset, str] = ""
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        account = self.account

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "account": account,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        account = d.pop("account")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        brief_provider_account = cls(
            id=id,
            url=url,
            display=display,
            account=account,
            name=name,
            description=description,
        )

        brief_provider_account.additional_properties = d
        return brief_provider_account

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
