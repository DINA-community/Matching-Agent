from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cable import BriefCable
    from ..models.brief_device import BriefDevice


T = TypeVar("T", bound="BriefPowerPort")


@_attrs_define
class BriefPowerPort:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        name (str):
        cable (Union['BriefCable', None]):
        field_occupied (bool):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    device: "BriefDevice"
    name: str
    cable: Union["BriefCable", None]
    field_occupied: bool
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cable import BriefCable

        id = self.id

        url = self.url

        display = self.display

        device = self.device.to_dict()

        name = self.name

        cable: Union[None, dict[str, Any]]
        if isinstance(self.cable, BriefCable):
            cable = self.cable.to_dict()
        else:
            cable = self.cable

        field_occupied = self.field_occupied

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "device": device,
                "name": name,
                "cable": cable,
                "_occupied": field_occupied,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cable import BriefCable
        from ..models.brief_device import BriefDevice

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        name = d.pop("name")

        def _parse_cable(data: object) -> Union["BriefCable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cable_type_1 = BriefCable.from_dict(data)

                return cable_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCable", None], data)

        cable = _parse_cable(d.pop("cable"))

        field_occupied = d.pop("_occupied")

        description = d.pop("description", UNSET)

        brief_power_port = cls(
            id=id,
            url=url,
            display=display,
            device=device,
            name=name,
            cable=cable,
            field_occupied=field_occupied,
            description=description,
        )

        brief_power_port.additional_properties = d
        return brief_power_port

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
