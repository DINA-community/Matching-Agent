from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.brief_module_type_profile import BriefModuleTypeProfile


T = TypeVar("T", bound="BriefModuleType")


@_attrs_define
class BriefModuleType:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        manufacturer (BriefManufacturer): Adds support for custom fields and tags.
        model (str):
        profile (Union['BriefModuleTypeProfile', None, Unset]):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    manufacturer: "BriefManufacturer"
    model: str
    profile: Union["BriefModuleTypeProfile", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_module_type_profile import BriefModuleTypeProfile

        id = self.id

        url = self.url

        display = self.display

        manufacturer = self.manufacturer.to_dict()

        model = self.model

        profile: Union[None, Unset, dict[str, Any]]
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, BriefModuleTypeProfile):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "manufacturer": manufacturer,
                "model": model,
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.brief_module_type_profile import BriefModuleTypeProfile

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        manufacturer = BriefManufacturer.from_dict(d.pop("manufacturer"))

        model = d.pop("model")

        def _parse_profile(data: object) -> Union["BriefModuleTypeProfile", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_1 = BriefModuleTypeProfile.from_dict(data)

                return profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeProfile", None, Unset], data)

        profile = _parse_profile(d.pop("profile", UNSET))

        description = d.pop("description", UNSET)

        brief_module_type = cls(
            id=id,
            url=url,
            display=display,
            manufacturer=manufacturer,
            model=model,
            profile=profile,
            description=description,
        )

        brief_module_type.additional_properties = d
        return brief_module_type

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
