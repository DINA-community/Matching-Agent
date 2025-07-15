from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_proposal_group_label import IKEProposalGroupLabel
from ..models.ike_proposal_group_value import IKEProposalGroupValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IKEProposalGroup")


@_attrs_define
class IKEProposalGroup:
    """
    Attributes:
        value (Union[Unset, IKEProposalGroupValue]): * `1` - Group 1
            * `2` - Group 2
            * `5` - Group 5
            * `14` - Group 14
            * `15` - Group 15
            * `16` - Group 16
            * `17` - Group 17
            * `18` - Group 18
            * `19` - Group 19
            * `20` - Group 20
            * `21` - Group 21
            * `22` - Group 22
            * `23` - Group 23
            * `24` - Group 24
            * `25` - Group 25
            * `26` - Group 26
            * `27` - Group 27
            * `28` - Group 28
            * `29` - Group 29
            * `30` - Group 30
            * `31` - Group 31
            * `32` - Group 32
            * `33` - Group 33
            * `34` - Group 34
        label (Union[Unset, IKEProposalGroupLabel]):
    """

    value: Union[Unset, IKEProposalGroupValue] = UNSET
    label: Union[Unset, IKEProposalGroupLabel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[Unset, int] = UNSET
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
        value: Union[Unset, IKEProposalGroupValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IKEProposalGroupValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IKEProposalGroupLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IKEProposalGroupLabel(_label)

        ike_proposal_group = cls(
            value=value,
            label=label,
        )

        ike_proposal_group.additional_properties = d
        return ike_proposal_group

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
