from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.brief_module_type_profile_request import BriefModuleTypeProfileRequest


T = TypeVar("T", bound="BriefModuleTypeRequest")


@_attrs_define
class BriefModuleTypeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        manufacturer (Union['BriefManufacturerRequest', int]):
        model (str):
        profile (Union['BriefModuleTypeProfileRequest', None, Unset, int]):
        description (Union[Unset, str]):
    """

    manufacturer: Union["BriefManufacturerRequest", int]
    model: str
    profile: Union["BriefModuleTypeProfileRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.brief_module_type_profile_request import BriefModuleTypeProfileRequest

        manufacturer: Union[dict[str, Any], int]
        if isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        model = self.model

        profile: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, BriefModuleTypeProfileRequest):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.brief_module_type_profile_request import BriefModuleTypeProfileRequest

        d = dict(src_dict)

        def _parse_manufacturer(data: object) -> Union["BriefManufacturerRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1 = BriefManufacturerRequest.from_dict(data)

                return manufacturer_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturerRequest", int], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer"))

        model = d.pop("model")

        def _parse_profile(data: object) -> Union["BriefModuleTypeProfileRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_1_type_1 = BriefModuleTypeProfileRequest.from_dict(data)

                return profile_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeProfileRequest", None, Unset, int], data)

        profile = _parse_profile(d.pop("profile", UNSET))

        description = d.pop("description", UNSET)

        brief_module_type_request = cls(
            manufacturer=manufacturer,
            model=model,
            profile=profile,
            description=description,
        )

        brief_module_type_request.additional_properties = d
        return brief_module_type_request

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
