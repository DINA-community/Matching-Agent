from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_vrf import BriefVRF


T = TypeVar("T", bound="AvailablePrefix")


@_attrs_define
class AvailablePrefix:
    """Representation of a prefix which does not exist in the database.

    Attributes:
        family (int):
        prefix (str):
        vrf (Union['BriefVRF', None]):
    """

    family: int
    prefix: str
    vrf: Union["BriefVRF", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_vrf import BriefVRF

        family = self.family

        prefix = self.prefix

        vrf: Union[None, dict[str, Any]]
        if isinstance(self.vrf, BriefVRF):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "family": family,
                "prefix": prefix,
                "vrf": vrf,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_vrf import BriefVRF

        d = dict(src_dict)
        family = d.pop("family")

        prefix = d.pop("prefix")

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

        available_prefix = cls(
            family=family,
            prefix=prefix,
            vrf=vrf,
        )

        available_prefix.additional_properties = d
        return available_prefix

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
