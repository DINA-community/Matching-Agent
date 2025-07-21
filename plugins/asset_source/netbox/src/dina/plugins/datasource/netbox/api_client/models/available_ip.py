from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_vrf import BriefVRF


T = TypeVar("T", bound="AvailableIP")


@_attrs_define
class AvailableIP:
    """Representation of an IP address which does not exist in the database.

    Attributes:
        family (int):
        address (str):
        vrf (Union['BriefVRF', None]):
        description (Union[Unset, str]):
    """

    family: int
    address: str
    vrf: Union["BriefVRF", None]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_vrf import BriefVRF

        family = self.family

        address = self.address

        vrf: Union[None, dict[str, Any]]
        if isinstance(self.vrf, BriefVRF):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "family": family,
                "address": address,
                "vrf": vrf,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_vrf import BriefVRF

        d = dict(src_dict)
        family = d.pop("family")

        address = d.pop("address")

        def _parse_vrf(data: object) -> Union["BriefVRF", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrf_type_1 = BriefVRF.from_dict(data)

                return vrf_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVRF", None], data)

        vrf = _parse_vrf(d.pop("vrf"))

        description = d.pop("description", UNSET)

        available_ip = cls(
            family=family,
            address=address,
            vrf=vrf,
            description=description,
        )

        available_ip.additional_properties = d
        return available_ip

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
