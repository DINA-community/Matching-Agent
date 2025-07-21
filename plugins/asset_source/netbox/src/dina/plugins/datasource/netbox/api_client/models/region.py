import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_region import NestedRegion
    from ..models.nested_tag import NestedTag
    from ..models.region_custom_fields import RegionCustomFields


T = TypeVar("T", bound="Region")


@_attrs_define
class Region:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        site_count (int):  Default: 0.
        prefix_count (int):
        field_depth (int):
        parent (Union['NestedRegion', None, Unset]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, RegionCustomFields]):
        comments (Union[Unset, str]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    prefix_count: int
    field_depth: int
    site_count: int = 0
    parent: Union["NestedRegion", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "RegionCustomFields"] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_region import NestedRegion

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        slug = self.slug

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

        site_count = self.site_count

        prefix_count = self.prefix_count

        field_depth = self.field_depth

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedRegion):
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
                "site_count": site_count,
                "prefix_count": prefix_count,
                "_depth": field_depth,
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
        from ..models.nested_region import NestedRegion
        from ..models.nested_tag import NestedTag
        from ..models.region_custom_fields import RegionCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

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

        site_count = d.pop("site_count")

        prefix_count = d.pop("prefix_count")

        field_depth = d.pop("_depth")

        def _parse_parent(data: object) -> Union["NestedRegion", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedRegion.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedRegion", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, RegionCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = RegionCustomFields.from_dict(_custom_fields)

        comments = d.pop("comments", UNSET)

        region = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            created=created,
            last_updated=last_updated,
            site_count=site_count,
            prefix_count=prefix_count,
            field_depth=field_depth,
            parent=parent,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            comments=comments,
        )

        region.additional_properties = d
        return region

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
