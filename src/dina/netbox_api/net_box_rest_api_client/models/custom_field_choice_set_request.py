from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_choice_set_request_base_choices import CustomFieldChoiceSetRequestBaseChoices
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldChoiceSetRequest")


@_attrs_define
class CustomFieldChoiceSetRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str):
            extra_choices (list[list[Any]]):
            description (Union[Unset, str]):
            base_choices (Union[Unset, CustomFieldChoiceSetRequestBaseChoices]): * `IATA` - IATA (Airport codes)
                * `ISO_3166` - ISO 3166 (Country codes)
                * `UN_LOCODE` - UN/LOCODE (Location codes)
            order_alphabetically (Union[Unset, bool]): Choices are automatically ordered alphabetically
    """

    name: str
    extra_choices: list[list[Any]]
    description: Union[Unset, str] = UNSET
    base_choices: Union[Unset, CustomFieldChoiceSetRequestBaseChoices] = UNSET
    order_alphabetically: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        extra_choices = []
        for extra_choices_item_data in self.extra_choices:
            extra_choices_item = extra_choices_item_data

            extra_choices.append(extra_choices_item)

        description = self.description

        base_choices: Union[Unset, str] = UNSET
        if not isinstance(self.base_choices, Unset):
            base_choices = self.base_choices.value

        order_alphabetically = self.order_alphabetically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "extra_choices": extra_choices,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if base_choices is not UNSET:
            field_dict["base_choices"] = base_choices
        if order_alphabetically is not UNSET:
            field_dict["order_alphabetically"] = order_alphabetically

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        extra_choices = []
        _extra_choices = d.pop("extra_choices")
        for extra_choices_item_data in _extra_choices:
            extra_choices_item = cast(list[Any], extra_choices_item_data)

            extra_choices.append(extra_choices_item)

        description = d.pop("description", UNSET)

        _base_choices = d.pop("base_choices", UNSET)
        base_choices: Union[Unset, CustomFieldChoiceSetRequestBaseChoices]
        if isinstance(_base_choices, Unset):
            base_choices = UNSET
        else:
            base_choices = CustomFieldChoiceSetRequestBaseChoices(_base_choices)

        order_alphabetically = d.pop("order_alphabetically", UNSET)

        custom_field_choice_set_request = cls(
            name=name,
            extra_choices=extra_choices,
            description=description,
            base_choices=base_choices,
            order_alphabetically=order_alphabetically,
        )

        custom_field_choice_set_request.additional_properties = d
        return custom_field_choice_set_request

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
