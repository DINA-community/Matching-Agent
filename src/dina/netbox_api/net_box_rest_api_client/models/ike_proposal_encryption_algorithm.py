from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_proposal_encryption_algorithm_label import IKEProposalEncryptionAlgorithmLabel
from ..models.ike_proposal_encryption_algorithm_value import IKEProposalEncryptionAlgorithmValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IKEProposalEncryptionAlgorithm")


@_attrs_define
class IKEProposalEncryptionAlgorithm:
    """
    Attributes:
        value (Union[Unset, IKEProposalEncryptionAlgorithmValue]): * `aes-128-cbc` - 128-bit AES (CBC)
            * `aes-128-gcm` - 128-bit AES (GCM)
            * `aes-192-cbc` - 192-bit AES (CBC)
            * `aes-192-gcm` - 192-bit AES (GCM)
            * `aes-256-cbc` - 256-bit AES (CBC)
            * `aes-256-gcm` - 256-bit AES (GCM)
            * `3des-cbc` - 3DES
            * `des-cbc` - DES
        label (Union[Unset, IKEProposalEncryptionAlgorithmLabel]):
    """

    value: Union[Unset, IKEProposalEncryptionAlgorithmValue] = UNSET
    label: Union[Unset, IKEProposalEncryptionAlgorithmLabel] = UNSET
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
        value: Union[Unset, IKEProposalEncryptionAlgorithmValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IKEProposalEncryptionAlgorithmValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IKEProposalEncryptionAlgorithmLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IKEProposalEncryptionAlgorithmLabel(_label)

        ike_proposal_encryption_algorithm = cls(
            value=value,
            label=label,
        )

        ike_proposal_encryption_algorithm.additional_properties = d
        return ike_proposal_encryption_algorithm

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
