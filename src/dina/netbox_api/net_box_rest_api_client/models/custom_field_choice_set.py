import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_choice_set_base_choices import CustomFieldChoiceSetBaseChoices


T = TypeVar("T", bound="CustomFieldChoiceSet")


@_attrs_define
class CustomFieldChoiceSet:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            name (str):
            extra_choices (list[list[Any]]):
            choices_count (str):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            description (Union[Unset, str]):
            base_choices (Union[Unset, CustomFieldChoiceSetBaseChoices]):
            order_alphabetically (Union[Unset, bool]): Choices are automatically ordered alphabetically
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    extra_choices: list[list[Any]]
    choices_count: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    base_choices: Union[Unset, "CustomFieldChoiceSetBaseChoices"] = UNSET
    order_alphabetically: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        extra_choices = []
        for extra_choices_item_data in self.extra_choices:
            extra_choices_item = extra_choices_item_data

            extra_choices.append(extra_choices_item)

        choices_count = self.choices_count

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        description = self.description

        base_choices: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_choices, Unset):
            base_choices = self.base_choices.to_dict()

        order_alphabetically = self.order_alphabetically

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "extra_choices": extra_choices,
                "choices_count": choices_count,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.custom_field_choice_set_base_choices import CustomFieldChoiceSetBaseChoices

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        extra_choices = []
        _extra_choices = d.pop("extra_choices")
        for extra_choices_item_data in _extra_choices:
            extra_choices_item = cast(list[Any], extra_choices_item_data)

            extra_choices.append(extra_choices_item)

        choices_count = d.pop("choices_count")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

        description = d.pop("description", UNSET)

        _base_choices = d.pop("base_choices", UNSET)
        base_choices: Union[Unset, CustomFieldChoiceSetBaseChoices]
        if isinstance(_base_choices, Unset):
            base_choices = UNSET
        else:
            base_choices = CustomFieldChoiceSetBaseChoices.from_dict(_base_choices)

        order_alphabetically = d.pop("order_alphabetically", UNSET)

        custom_field_choice_set = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            extra_choices=extra_choices,
            choices_count=choices_count,
            created=created,
            last_updated=last_updated,
            description=description,
            base_choices=base_choices,
            order_alphabetically=order_alphabetically,
        )

        custom_field_choice_set.additional_properties = d
        return custom_field_choice_set

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
