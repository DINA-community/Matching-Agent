import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_custom_field_choice_set_request_base_choices_type_1 import (
    WritableCustomFieldChoiceSetRequestBaseChoicesType1,
)
from ..models.writable_custom_field_choice_set_request_base_choices_type_2_type_1 import (
    WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1,
)
from ..models.writable_custom_field_choice_set_request_base_choices_type_3_type_1 import (
    WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WritableCustomFieldChoiceSetRequest")


@_attrs_define
class WritableCustomFieldChoiceSetRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str):
            extra_choices (list[list[Any]]):
            description (Union[Unset, str]):
            base_choices (Union[None, Unset, WritableCustomFieldChoiceSetRequestBaseChoicesType1,
                WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1,
                WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1]): Base set of predefined choices (optional)

                * `IATA` - IATA (Airport codes)
                * `ISO_3166` - ISO 3166 (Country codes)
                * `UN_LOCODE` - UN/LOCODE (Location codes)
            order_alphabetically (Union[Unset, bool]): Choices are automatically ordered alphabetically
    """

    name: str
    extra_choices: list[list[Any]]
    description: Union[Unset, str] = UNSET
    base_choices: Union[
        None,
        Unset,
        WritableCustomFieldChoiceSetRequestBaseChoicesType1,
        WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1,
        WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1,
    ] = UNSET
    order_alphabetically: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        extra_choices = []
        for extra_choices_item_data in self.extra_choices:
            extra_choices_item = extra_choices_item_data

            extra_choices.append(extra_choices_item)

        description = self.description

        base_choices: Union[None, Unset, str]
        if isinstance(self.base_choices, Unset):
            base_choices = UNSET
        elif isinstance(self.base_choices, WritableCustomFieldChoiceSetRequestBaseChoicesType1):
            base_choices = self.base_choices.value
        elif isinstance(self.base_choices, WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1):
            base_choices = self.base_choices.value
        elif isinstance(self.base_choices, WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1):
            base_choices = self.base_choices.value
        else:
            base_choices = self.base_choices

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

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        _temp_extra_choices = []
        for extra_choices_item_data in self.extra_choices:
            extra_choices_item = extra_choices_item_data

            _temp_extra_choices.append(extra_choices_item)
        extra_choices = (None, json.dumps(_temp_extra_choices).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        base_choices: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.base_choices, Unset):
            base_choices = UNSET
        elif isinstance(self.base_choices, None):
            base_choices = (None, str(self.base_choices).encode(), "text/plain")
        elif isinstance(self.base_choices, WritableCustomFieldChoiceSetRequestBaseChoicesType1):
            base_choices = (None, str(self.base_choices.value).encode(), "text/plain")
        elif isinstance(self.base_choices, None):
            base_choices = (None, str(self.base_choices).encode(), "text/plain")
        elif isinstance(self.base_choices, WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1):
            base_choices = (None, str(self.base_choices.value).encode(), "text/plain")
        elif isinstance(self.base_choices, None):
            base_choices = (None, str(self.base_choices).encode(), "text/plain")
        else:
            base_choices = (None, str(self.base_choices.value).encode(), "text/plain")

        order_alphabetically = (
            self.order_alphabetically
            if isinstance(self.order_alphabetically, Unset)
            else (None, str(self.order_alphabetically).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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

        def _parse_base_choices(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableCustomFieldChoiceSetRequestBaseChoicesType1,
            WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1,
            WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_choices_type_1 = WritableCustomFieldChoiceSetRequestBaseChoicesType1(data)

                return base_choices_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_choices_type_2_type_1 = WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1(data)

                return base_choices_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_choices_type_3_type_1 = WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1(data)

                return base_choices_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableCustomFieldChoiceSetRequestBaseChoicesType1,
                    WritableCustomFieldChoiceSetRequestBaseChoicesType2Type1,
                    WritableCustomFieldChoiceSetRequestBaseChoicesType3Type1,
                ],
                data,
            )

        base_choices = _parse_base_choices(d.pop("base_choices", UNSET))

        order_alphabetically = d.pop("order_alphabetically", UNSET)

        writable_custom_field_choice_set_request = cls(
            name=name,
            extra_choices=extra_choices,
            description=description,
            base_choices=base_choices,
            order_alphabetically=order_alphabetically,
        )

        writable_custom_field_choice_set_request.additional_properties = d
        return writable_custom_field_choice_set_request

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
