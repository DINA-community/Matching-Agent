import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_location_request import BriefLocationRequest
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.power_panel_request_custom_fields import PowerPanelRequestCustomFields


T = TypeVar("T", bound="PowerPanelRequest")


@_attrs_define
class PowerPanelRequest:
    """Adds support for custom fields and tags.

    Attributes:
        site (Union['BriefSiteRequest', int]):
        name (str):
        location (Union['BriefLocationRequest', None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PowerPanelRequestCustomFields]):
    """

    site: Union["BriefSiteRequest", int]
    name: str
    location: Union["BriefLocationRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PowerPanelRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_site_request import BriefSiteRequest

        site: Union[dict[str, Any], int]
        if isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        name = self.name

        location: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, BriefLocationRequest):
            location = self.location.to_dict()
        else:
            location = self.location

        description = self.description

        comments = self.comments

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site": site,
                "name": name,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        site: tuple[None, bytes, str]

        if isinstance(self.site, int):
            site = (None, str(self.site).encode(), "text/plain")
        else:
            site = (None, json.dumps(self.site.to_dict()).encode(), "application/json")

        name = (None, str(self.name).encode(), "text/plain")

        location: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, int):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, None):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, BriefLocationRequest):
            location = (
                None,
                json.dumps(self.location.to_dict()).encode(),
                "application/json",
            )
        else:
            location = (None, str(self.location).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "site": site,
                "name": name,
            }
        )
        if location is not UNSET:
            field_dict["location"] = location
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.power_panel_request_custom_fields import (
            PowerPanelRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_site(data: object) -> Union["BriefSiteRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", int], data)

        site = _parse_site(d.pop("site"))

        name = d.pop("name")

        def _parse_location(
            data: object,
        ) -> Union["BriefLocationRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1_type_1 = BriefLocationRequest.from_dict(data)

                return location_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefLocationRequest", None, Unset, int], data)

        location = _parse_location(d.pop("location", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PowerPanelRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PowerPanelRequestCustomFields.from_dict(_custom_fields)

        power_panel_request = cls(
            site=site,
            name=name,
            location=location,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        power_panel_request.additional_properties = d
        return power_panel_request

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
