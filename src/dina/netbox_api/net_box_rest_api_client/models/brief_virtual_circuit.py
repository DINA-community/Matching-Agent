from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_network import BriefProviderNetwork


T = TypeVar("T", bound="BriefVirtualCircuit")


@_attrs_define
class BriefVirtualCircuit:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        cid (str): Unique circuit ID
        provider_network (BriefProviderNetwork): Adds support for custom fields and tags.
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    cid: str
    provider_network: "BriefProviderNetwork"
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        cid = self.cid

        provider_network = self.provider_network.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "cid": cid,
                "provider_network": provider_network,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_provider_network import BriefProviderNetwork

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        cid = d.pop("cid")

        provider_network = BriefProviderNetwork.from_dict(d.pop("provider_network"))

        description = d.pop("description", UNSET)

        brief_virtual_circuit = cls(
            id=id,
            url=url,
            display=display,
            cid=cid,
            provider_network=provider_network,
            description=description,
        )

        brief_virtual_circuit.additional_properties = d
        return brief_virtual_circuit

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
