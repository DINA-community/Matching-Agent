from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardRequest")


@_attrs_define
class DashboardRequest:
    """
    Attributes:
        layout (Union[Unset, Any]):
        config (Union[Unset, Any]):
    """

    layout: Union[Unset, Any] = UNSET
    config: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout = self.layout

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout is not UNSET:
            field_dict["layout"] = layout
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        layout = (
            self.layout
            if isinstance(self.layout, Unset)
            else (None, str(self.layout).encode(), "text/plain")
        )

        config = (
            self.config
            if isinstance(self.config, Unset)
            else (None, str(self.config).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if layout is not UNSET:
            field_dict["layout"] = layout
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layout = d.pop("layout", UNSET)

        config = d.pop("config", UNSET)

        dashboard_request = cls(
            layout=layout,
            config=config,
        )

        dashboard_request.additional_properties = d
        return dashboard_request

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
