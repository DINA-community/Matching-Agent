from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_network_request import BriefProviderNetworkRequest


T = TypeVar("T", bound="BriefVirtualCircuitRequest")


@_attrs_define
class BriefVirtualCircuitRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cid (str): Unique circuit ID
        provider_network (Union['BriefProviderNetworkRequest', int]):
        description (Union[Unset, str]):
    """

    cid: str
    provider_network: Union["BriefProviderNetworkRequest", int]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_network_request import BriefProviderNetworkRequest

        cid = self.cid

        provider_network: Union[dict[str, Any], int]
        if isinstance(self.provider_network, BriefProviderNetworkRequest):
            provider_network = self.provider_network.to_dict()
        else:
            provider_network = self.provider_network

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cid": cid,
                "provider_network": provider_network,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_provider_network_request import BriefProviderNetworkRequest

        d = dict(src_dict)
        cid = d.pop("cid")

        def _parse_provider_network(data: object) -> Union["BriefProviderNetworkRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_network_type_1 = BriefProviderNetworkRequest.from_dict(data)

                return provider_network_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderNetworkRequest", int], data)

        provider_network = _parse_provider_network(d.pop("provider_network"))

        description = d.pop("description", UNSET)

        brief_virtual_circuit_request = cls(
            cid=cid,
            provider_network=provider_network,
            description=description,
        )

        brief_virtual_circuit_request.additional_properties = d
        return brief_virtual_circuit_request

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
