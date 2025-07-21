from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_device_request import NestedDeviceRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.virtual_chassis_request_custom_fields import (
        VirtualChassisRequestCustomFields,
    )


T = TypeVar("T", bound="VirtualChassisRequest")


@_attrs_define
class VirtualChassisRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        domain (Union[Unset, str]):
        master (Union['NestedDeviceRequest', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, VirtualChassisRequestCustomFields]):
    """

    name: str
    domain: Union[Unset, str] = UNSET
    master: Union["NestedDeviceRequest", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "VirtualChassisRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_device_request import NestedDeviceRequest

        name = self.name

        domain = self.domain

        master: Union[None, Unset, dict[str, Any]]
        if isinstance(self.master, Unset):
            master = UNSET
        elif isinstance(self.master, NestedDeviceRequest):
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
                "name": name,
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
        from ..models.nested_device_request import NestedDeviceRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.virtual_chassis_request_custom_fields import (
            VirtualChassisRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        domain = d.pop("domain", UNSET)

        def _parse_master(data: object) -> Union["NestedDeviceRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                master_type_1 = NestedDeviceRequest.from_dict(data)

                return master_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDeviceRequest", None, Unset], data)

        master = _parse_master(d.pop("master", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualChassisRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualChassisRequestCustomFields.from_dict(_custom_fields)

        virtual_chassis_request = cls(
            name=name,
            domain=domain,
            master=master,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_chassis_request.additional_properties = d
        return virtual_chassis_request

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
