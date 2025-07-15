import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_custom_link_request_button_class import PatchedCustomLinkRequestButtonClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCustomLinkRequest")


@_attrs_define
class PatchedCustomLinkRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_types (Union[Unset, list[str]]):
            name (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            link_text (Union[Unset, str]): Jinja2 template code for link text
            link_url (Union[Unset, str]): Jinja2 template code for link URL
            weight (Union[Unset, int]):
            group_name (Union[Unset, str]): Links with the same group will appear as a dropdown menu
            button_class (Union[Unset, PatchedCustomLinkRequestButtonClass]): The class of the first link in a group will be
                used for the dropdown button

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

    object_types: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    link_text: Union[Unset, str] = UNSET
    link_url: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    group_name: Union[Unset, str] = UNSET
    button_class: Union[Unset, PatchedCustomLinkRequestButtonClass] = UNSET
    new_window: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        name = self.name

        enabled = self.enabled

        link_text = self.link_text

        link_url = self.link_url

        weight = self.weight

        group_name = self.group_name

        button_class: Union[Unset, str] = UNSET
        if not isinstance(self.button_class, Unset):
            button_class = self.button_class.value

        new_window = self.new_window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if link_text is not UNSET:
            field_dict["link_text"] = link_text
        if link_url is not UNSET:
            field_dict["link_url"] = link_url
        if weight is not UNSET:
            field_dict["weight"] = weight
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if button_class is not UNSET:
            field_dict["button_class"] = button_class
        if new_window is not UNSET:
            field_dict["new_window"] = new_window

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.object_types, Unset):
            _temp_object_types = self.object_types
            object_types = (None, json.dumps(_temp_object_types).encode(), "application/json")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")

        link_text = (
            self.link_text if isinstance(self.link_text, Unset) else (None, str(self.link_text).encode(), "text/plain")
        )

        link_url = (
            self.link_url if isinstance(self.link_url, Unset) else (None, str(self.link_url).encode(), "text/plain")
        )

        weight = self.weight if isinstance(self.weight, Unset) else (None, str(self.weight).encode(), "text/plain")

        group_name = (
            self.group_name
            if isinstance(self.group_name, Unset)
            else (None, str(self.group_name).encode(), "text/plain")
        )

        button_class: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.button_class, Unset):
            button_class = (None, str(self.button_class.value).encode(), "text/plain")

        new_window = (
            self.new_window
            if isinstance(self.new_window, Unset)
            else (None, str(self.new_window).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if link_text is not UNSET:
            field_dict["link_text"] = link_text
        if link_url is not UNSET:
            field_dict["link_url"] = link_url
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
        object_types = cast(list[str], d.pop("object_types", UNSET))

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        link_text = d.pop("link_text", UNSET)

        link_url = d.pop("link_url", UNSET)

        weight = d.pop("weight", UNSET)

        group_name = d.pop("group_name", UNSET)

        _button_class = d.pop("button_class", UNSET)
        button_class: Union[Unset, PatchedCustomLinkRequestButtonClass]
        if isinstance(_button_class, Unset):
            button_class = UNSET
        else:
            button_class = PatchedCustomLinkRequestButtonClass(_button_class)

        new_window = d.pop("new_window", UNSET)

        patched_custom_link_request = cls(
            object_types=object_types,
            name=name,
            enabled=enabled,
            link_text=link_text,
            link_url=link_url,
            weight=weight,
            group_name=group_name,
            button_class=button_class,
            new_window=new_window,
        )

        patched_custom_link_request.additional_properties = d
        return patched_custom_link_request

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
