from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_site_group_request import NestedSiteGroupRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.site_group_request_custom_fields import SiteGroupRequestCustomFields


T = TypeVar("T", bound="SiteGroupRequest")


@_attrs_define
class SiteGroupRequest:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        name (str):
        slug (str):
        parent (Union['NestedSiteGroupRequest', None, Unset]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, SiteGroupRequestCustomFields]):
        comments (Union[Unset, str]):
    """

    name: str
    slug: str
    parent: Union["NestedSiteGroupRequest", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "SiteGroupRequestCustomFields"] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_site_group_request import NestedSiteGroupRequest

        name = self.name

        slug = self.slug

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedSiteGroupRequest):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        description = self.description

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_site_group_request import NestedSiteGroupRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.site_group_request_custom_fields import (
            SiteGroupRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_parent(data: object) -> Union["NestedSiteGroupRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedSiteGroupRequest.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedSiteGroupRequest", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, SiteGroupRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = SiteGroupRequestCustomFields.from_dict(_custom_fields)

        comments = d.pop("comments", UNSET)

        site_group_request = cls(
            name=name,
            slug=slug,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            comments=comments,
        )

        site_group_request.additional_properties = d
        return site_group_request

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
