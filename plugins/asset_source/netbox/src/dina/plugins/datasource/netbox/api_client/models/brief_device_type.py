from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer


T = TypeVar("T", bound="BriefDeviceType")


@_attrs_define
class BriefDeviceType:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        manufacturer (BriefManufacturer): Adds support for custom fields and tags.
        model (str):
        slug (str):
        description (Union[Unset, str]):
        device_count (Union[Unset, int]):
    """

    id: int
    url: str
    display: str
    manufacturer: "BriefManufacturer"
    model: str
    slug: str
    description: Union[Unset, str] = UNSET
    device_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        manufacturer = self.manufacturer.to_dict()

        model = self.model

        slug = self.slug

        description = self.description

        device_count = self.device_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if device_count is not UNSET:
            field_dict["device_count"] = device_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_manufacturer import BriefManufacturer

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        manufacturer = BriefManufacturer.from_dict(d.pop("manufacturer"))

        model = d.pop("model")

        slug = d.pop("slug")

        description = d.pop("description", UNSET)

        device_count = d.pop("device_count", UNSET)

        brief_device_type = cls(
            id=id,
            url=url,
            display=display,
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            description=description,
            device_count=device_count,
        )

        brief_device_type.additional_properties = d
        return brief_device_type

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
