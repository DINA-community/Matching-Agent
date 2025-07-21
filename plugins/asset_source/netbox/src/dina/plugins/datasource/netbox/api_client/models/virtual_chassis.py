import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_device import NestedDevice
    from ..models.nested_tag import NestedTag
    from ..models.virtual_chassis_custom_fields import VirtualChassisCustomFields


T = TypeVar("T", bound="VirtualChassis")


@_attrs_define
class VirtualChassis:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        member_count (int):
        members (list['NestedDevice']):
        domain (Union[Unset, str]):
        master (Union['NestedDevice', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VirtualChassisCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    member_count: int
    members: list["NestedDevice"]
    domain: Union[Unset, str] = UNSET
    master: Union["NestedDevice", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VirtualChassisCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_device import NestedDevice

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

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

        member_count = self.member_count

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        domain = self.domain

        master: Union[None, Unset, dict[str, Any]]
        if isinstance(self.master, Unset):
            master = UNSET
        elif isinstance(self.master, NestedDevice):
            master = self.master.to_dict()
        else:
            master = self.master

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "created": created,
                "last_updated": last_updated,
                "member_count": member_count,
                "members": members,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if master is not UNSET:
            field_dict["master"] = master
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
        from ..models.nested_device import NestedDevice
        from ..models.nested_tag import NestedTag
        from ..models.virtual_chassis_custom_fields import VirtualChassisCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

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

        member_count = d.pop("member_count")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = NestedDevice.from_dict(members_item_data)

            members.append(members_item)

        domain = d.pop("domain", UNSET)

        def _parse_master(data: object) -> Union["NestedDevice", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                master_type_1 = NestedDevice.from_dict(data)

                return master_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDevice", None, Unset], data)

        master = _parse_master(d.pop("master", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualChassisCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualChassisCustomFields.from_dict(_custom_fields)

        virtual_chassis = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            created=created,
            last_updated=last_updated,
            member_count=member_count,
            members=members,
            domain=domain,
            master=master,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_chassis.additional_properties = d
        return virtual_chassis

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
