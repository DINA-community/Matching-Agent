from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cable_termination_request_end import CableTerminationRequestEnd

T = TypeVar("T", bound="CableTerminationRequest")


@_attrs_define
class CableTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cable (int):
        cable_end (CableTerminationRequestEnd): * `A` - A
            * `B` - B
        termination_type (str):
        termination_id (int):
    """

    cable: int
    cable_end: CableTerminationRequestEnd
    termination_type: str
    termination_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cable = self.cable

        cable_end = self.cable_end.value

        termination_type = self.termination_type

        termination_id = self.termination_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cable": cable,
                "cable_end": cable_end,
                "termination_type": termination_type,
                "termination_id": termination_id,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        cable = (None, str(self.cable).encode(), "text/plain")

        cable_end = (None, str(self.cable_end.value).encode(), "text/plain")

        termination_type = (None, str(self.termination_type).encode(), "text/plain")

        termination_id = (None, str(self.termination_id).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "cable": cable,
                "cable_end": cable_end,
                "termination_type": termination_type,
                "termination_id": termination_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cable = d.pop("cable")

        cable_end = CableTerminationRequestEnd(d.pop("cable_end"))

        termination_type = d.pop("termination_type")

        termination_id = d.pop("termination_id")

        cable_termination_request = cls(
            cable=cable,
            cable_end=cable_end,
            termination_type=termination_type,
            termination_id=termination_id,
        )

        cable_termination_request.additional_properties = d
        return cable_termination_request

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
