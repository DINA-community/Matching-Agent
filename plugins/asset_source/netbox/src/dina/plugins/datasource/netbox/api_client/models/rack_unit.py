from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.rack_unit_face import RackUnitFace


T = TypeVar("T", bound="RackUnit")


@_attrs_define
class RackUnit:
    """A rack unit is an abstraction formed by the set (rack, position, face); it does not exist as a row in the database.

    Attributes:
        id (float):
        name (str):
        face (RackUnitFace):
        device (BriefDevice): Adds support for custom fields and tags.
        occupied (bool):
        display (str):
    """

    id: float
    name: str
    face: "RackUnitFace"
    device: "BriefDevice"
    occupied: bool
    display: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        face = self.face.to_dict()

        device = self.device.to_dict()

        occupied = self.occupied

        display = self.display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "face": face,
                "device": device,
                "occupied": occupied,
                "display": display,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device import BriefDevice
        from ..models.rack_unit_face import RackUnitFace

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        face = RackUnitFace.from_dict(d.pop("face"))

        device = BriefDevice.from_dict(d.pop("device"))

        occupied = d.pop("occupied")

        display = d.pop("display")

        rack_unit = cls(
            id=id,
            name=name,
            face=face,
            device=device,
            occupied=occupied,
            display=display,
        )

        rack_unit.additional_properties = d
        return rack_unit

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
