import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_l2vpn_request import BriefL2VPNRequest
    from ..models.l2vpn_termination_request_custom_fields import L2VPNTerminationRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="L2VPNTerminationRequest")


@_attrs_define
class L2VPNTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        l2vpn (Union['BriefL2VPNRequest', int]):
        assigned_object_type (str):
        assigned_object_id (int):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, L2VPNTerminationRequestCustomFields]):
    """

    l2vpn: Union["BriefL2VPNRequest", int]
    assigned_object_type: str
    assigned_object_id: int
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "L2VPNTerminationRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_l2vpn_request import BriefL2VPNRequest

        l2vpn: Union[dict[str, Any], int]
        if isinstance(self.l2vpn, BriefL2VPNRequest):
            l2vpn = self.l2vpn.to_dict()
        else:
            l2vpn = self.l2vpn

        assigned_object_type = self.assigned_object_type

        assigned_object_id = self.assigned_object_id

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
                "l2vpn": l2vpn,
                "assigned_object_type": assigned_object_type,
                "assigned_object_id": assigned_object_id,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        l2vpn: tuple[None, bytes, str]

        if isinstance(self.l2vpn, int):
            l2vpn = (None, str(self.l2vpn).encode(), "text/plain")
        else:
            l2vpn = (None, json.dumps(self.l2vpn.to_dict()).encode(), "application/json")

        assigned_object_type = (None, str(self.assigned_object_type).encode(), "text/plain")

        assigned_object_id = (None, str(self.assigned_object_id).encode(), "text/plain")

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "l2vpn": l2vpn,
                "assigned_object_type": assigned_object_type,
                "assigned_object_id": assigned_object_id,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_l2vpn_request import BriefL2VPNRequest
        from ..models.l2vpn_termination_request_custom_fields import L2VPNTerminationRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)

        def _parse_l2vpn(data: object) -> Union["BriefL2VPNRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                l2vpn_type_1 = BriefL2VPNRequest.from_dict(data)

                return l2vpn_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefL2VPNRequest", int], data)

        l2vpn = _parse_l2vpn(d.pop("l2vpn"))

        assigned_object_type = d.pop("assigned_object_type")

        assigned_object_id = d.pop("assigned_object_id")

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, L2VPNTerminationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = L2VPNTerminationRequestCustomFields.from_dict(_custom_fields)

        l2vpn_termination_request = cls(
            l2vpn=l2vpn,
            assigned_object_type=assigned_object_type,
            assigned_object_id=assigned_object_id,
            tags=tags,
            custom_fields=custom_fields,
        )

        l2vpn_termination_request.additional_properties = d
        return l2vpn_termination_request

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
