import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_link_button_class import CustomLinkButtonClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomLink")


@_attrs_define
class CustomLink:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            object_types (list[str]):
            name (str):
            link_text (str): Jinja2 template code for link text
            link_url (str): Jinja2 template code for link URL
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            enabled (Union[Unset, bool]):
            weight (Union[Unset, int]):
            group_name (Union[Unset, str]): Links with the same group will appear as a dropdown menu
            button_class (Union[Unset, CustomLinkButtonClass]): The class of the first link in a group will be used for the
                dropdown button

                * `default` - Default
                * `blue` - Blue
                * `indigo` - Indigo
                * `purple` - Purple
                * `pink` - Pink
                * `red` - Red
                * `orange` - Orange
                * `yellow` - Yellow
                * `green` - Green
                * `teal` - Teal
                * `cyan` - Cyan
                * `gray` - Gray
                * `black` - Black
                * `white` - White
                * `ghost-dark` - Link
            new_window (Union[Unset, bool]): Force link to open in a new window
    """

    id: int
    url: str
    display_url: str
    display: str
    object_types: list[str]
    name: str
    link_text: str
    link_url: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    enabled: Union[Unset, bool] = UNSET
    weight: Union[Unset, int] = UNSET
    group_name: Union[Unset, str] = UNSET
    button_class: Union[Unset, CustomLinkButtonClass] = UNSET
    new_window: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        object_types = self.object_types

        name = self.name

        link_text = self.link_text

        link_url = self.link_url

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

        enabled = self.enabled

        weight = self.weight

        group_name = self.group_name

        button_class: Union[Unset, str] = UNSET
        if not isinstance(self.button_class, Unset):
            button_class = self.button_class.value

        new_window = self.new_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "object_types": object_types,
                "name": name,
                "link_text": link_text,
                "link_url": link_url,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if weight is not UNSET:
            field_dict["weight"] = weight
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if button_class is not UNSET:
            field_dict["button_class"] = button_class
        if new_window is not UNSET:
            field_dict["new_window"] = new_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        object_types = cast(list[str], d.pop("object_types"))

        name = d.pop("name")

        link_text = d.pop("link_text")

        link_url = d.pop("link_url")

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

        enabled = d.pop("enabled", UNSET)

        weight = d.pop("weight", UNSET)

        group_name = d.pop("group_name", UNSET)

        _button_class = d.pop("button_class", UNSET)
        button_class: Union[Unset, CustomLinkButtonClass]
        if isinstance(_button_class, Unset):
            button_class = UNSET
        else:
            button_class = CustomLinkButtonClass(_button_class)

        new_window = d.pop("new_window", UNSET)

        custom_link = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            object_types=object_types,
            name=name,
            link_text=link_text,
            link_url=link_url,
            created=created,
            last_updated=last_updated,
            enabled=enabled,
            weight=weight,
            group_name=group_name,
            button_class=button_class,
            new_window=new_window,
        )

        custom_link.additional_properties = d
        return custom_link

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
