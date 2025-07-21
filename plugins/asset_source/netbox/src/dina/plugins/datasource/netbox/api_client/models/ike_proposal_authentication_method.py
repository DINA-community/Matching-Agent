from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_proposal_authentication_method_label import (
    IKEProposalAuthenticationMethodLabel,
)
from ..models.ike_proposal_authentication_method_value import (
    IKEProposalAuthenticationMethodValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IKEProposalAuthenticationMethod")


@_attrs_define
class IKEProposalAuthenticationMethod:
    """
    Attributes:
        value (Union[Unset, IKEProposalAuthenticationMethodValue]): * `preshared-keys` - Pre-shared keys
            * `certificates` - Certificates
            * `rsa-signatures` - RSA signatures
            * `dsa-signatures` - DSA signatures
        label (Union[Unset, IKEProposalAuthenticationMethodLabel]):
    """

    value: Union[Unset, IKEProposalAuthenticationMethodValue] = UNSET
    label: Union[Unset, IKEProposalAuthenticationMethodLabel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.value

        label: Union[Unset, str] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _value = d.pop("value", UNSET)
        value: Union[Unset, IKEProposalAuthenticationMethodValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IKEProposalAuthenticationMethodValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IKEProposalAuthenticationMethodLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IKEProposalAuthenticationMethodLabel(_label)

        ike_proposal_authentication_method = cls(
            value=value,
            label=label,
        )

        ike_proposal_authentication_method.additional_properties = d
        return ike_proposal_authentication_method

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
