from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_device import NestedDevice


T = TypeVar("T", bound="NestedInterface")


@_attrs_define
class NestedInterface:
    """Represents an object related through a ForeignKey field. On write, it accepts a primary key (PK) value or a
    dictionary of attributes which can be used to uniquely identify the related object. This class should be
    subclassed to return a full representation of the related object on read.

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            device (NestedDevice): Represents an object related through a ForeignKey field. On write, it accepts a primary
                key (PK) value or a
                dictionary of attributes which can be used to uniquely identify the related object. This class should be
                subclassed to return a full representation of the related object on read.
            name (str):
            field_occupied (bool):
            cable (Union[None, Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "NestedDevice"
    name: str
    field_occupied: bool
    cable: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        name = self.name

        field_occupied = self.field_occupied

        cable: Union[None, Unset, int]
        if isinstance(self.cable, Unset):
            cable = UNSET
        else:
            cable = self.cable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "device": device,
                "name": name,
                "_occupied": field_occupied,
            }
        )
        if cable is not UNSET:
            field_dict["cable"] = cable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_device import NestedDevice

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = NestedDevice.from_dict(d.pop("device"))

        name = d.pop("name")

        field_occupied = d.pop("_occupied")

        def _parse_cable(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cable = _parse_cable(d.pop("cable", UNSET))

        nested_interface = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            field_occupied=field_occupied,
            cable=cable,
        )

        nested_interface.additional_properties = d
        return nested_interface

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
