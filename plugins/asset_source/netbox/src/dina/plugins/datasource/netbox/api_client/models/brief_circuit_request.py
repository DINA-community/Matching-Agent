from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_request import BriefProviderRequest


T = TypeVar("T", bound="BriefCircuitRequest")


@_attrs_define
class BriefCircuitRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cid (str): Unique circuit ID
        provider (Union['BriefProviderRequest', int]):
        description (Union[Unset, str]):
    """

    cid: str
    provider: Union["BriefProviderRequest", int]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_request import BriefProviderRequest

        cid = self.cid

        provider: Union[dict[str, Any], int]
        if isinstance(self.provider, BriefProviderRequest):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cid": cid,
                "provider": provider,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_provider_request import BriefProviderRequest

        d = dict(src_dict)
        cid = d.pop("cid")

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

        description = d.pop("description", UNSET)

        brief_circuit_request = cls(
            cid=cid,
            provider=provider,
            description=description,
        )

        brief_circuit_request.additional_properties = d
        return brief_circuit_request

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
