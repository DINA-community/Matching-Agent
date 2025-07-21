from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inventory_item_status_label import InventoryItemStatusLabel
from ..models.inventory_item_status_value import InventoryItemStatusValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemStatus")


@_attrs_define
class InventoryItemStatus:
    """
    Attributes:
        value (Union[Unset, InventoryItemStatusValue]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `decommissioning` - Decommissioning
        label (Union[Unset, InventoryItemStatusLabel]):
    """

    value: Union[Unset, InventoryItemStatusValue] = UNSET
    label: Union[Unset, InventoryItemStatusLabel] = UNSET
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
        value: Union[Unset, InventoryItemStatusValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = InventoryItemStatusValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, InventoryItemStatusLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = InventoryItemStatusLabel(_label)

        inventory_item_status = cls(
            value=value,
            label=label,
        )

        inventory_item_status.additional_properties = d
        return inventory_item_status

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
