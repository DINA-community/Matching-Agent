from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_l2vpn_request import BriefL2VPNRequest


T = TypeVar("T", bound="BriefL2VPNTerminationRequest")


@_attrs_define
class BriefL2VPNTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        l2vpn (Union['BriefL2VPNRequest', int]):
    """

    l2vpn: Union["BriefL2VPNRequest", int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_l2vpn_request import BriefL2VPNRequest

        l2vpn: Union[dict[str, Any], int]
        if isinstance(self.l2vpn, BriefL2VPNRequest):
            l2vpn = self.l2vpn.to_dict()
        else:
            l2vpn = self.l2vpn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "l2vpn": l2vpn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_l2vpn_request import BriefL2VPNRequest

        d = dict(src_dict)

        def _parse_l2vpn(data: object) -> Union["BriefL2VPNRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                l2vpn_type_1 = BriefL2VPNRequest.from_dict(data)

                return l2vpn_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefL2VPNRequest", int], data)

        l2vpn = _parse_l2vpn(d.pop("l2vpn"))

        brief_l2vpn_termination_request = cls(
            l2vpn=l2vpn,
        )

        brief_l2vpn_termination_request.additional_properties = d
        return brief_l2vpn_termination_request

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
