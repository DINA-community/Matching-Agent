from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rack_airflow_label import RackAirflowLabel
from ..models.rack_airflow_value import RackAirflowValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="RackAirflow")


@_attrs_define
class RackAirflow:
    """
    Attributes:
        value (Union[Unset, RackAirflowValue]): * `front-to-rear` - Front to rear
            * `rear-to-front` - Rear to front
        label (Union[Unset, RackAirflowLabel]):
    """

    value: Union[Unset, RackAirflowValue] = UNSET
    label: Union[Unset, RackAirflowLabel] = UNSET
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
        value: Union[Unset, RackAirflowValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RackAirflowValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, RackAirflowLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = RackAirflowLabel(_label)

        rack_airflow = cls(
            value=value,
            label=label,
        )

        rack_airflow.additional_properties = d
        return rack_airflow

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
