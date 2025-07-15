from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_with_config_context_status_label import DeviceWithConfigContextStatusLabel
from ..models.device_with_config_context_status_value import DeviceWithConfigContextStatusValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceWithConfigContextStatus")


@_attrs_define
class DeviceWithConfigContextStatus:
    """
    Attributes:
        value (Union[Unset, DeviceWithConfigContextStatusValue]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `inventory` - Inventory
            * `decommissioning` - Decommissioning
        label (Union[Unset, DeviceWithConfigContextStatusLabel]):
    """

    value: Union[Unset, DeviceWithConfigContextStatusValue] = UNSET
    label: Union[Unset, DeviceWithConfigContextStatusLabel] = UNSET
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
        value: Union[Unset, DeviceWithConfigContextStatusValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = DeviceWithConfigContextStatusValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, DeviceWithConfigContextStatusLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = DeviceWithConfigContextStatusLabel(_label)

        device_with_config_context_status = cls(
            value=value,
            label=label,
        )

        device_with_config_context_status.additional_properties = d
        return device_with_config_context_status

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
