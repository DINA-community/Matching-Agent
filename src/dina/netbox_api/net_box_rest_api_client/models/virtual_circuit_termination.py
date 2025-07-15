import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_interface import BriefInterface
    from ..models.brief_virtual_circuit import BriefVirtualCircuit
    from ..models.nested_tag import NestedTag
    from ..models.virtual_circuit_termination_custom_fields import VirtualCircuitTerminationCustomFields
    from ..models.virtual_circuit_termination_role import VirtualCircuitTerminationRole


T = TypeVar("T", bound="VirtualCircuitTermination")


@_attrs_define
class VirtualCircuitTermination:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        virtual_circuit (BriefVirtualCircuit): Adds support for custom fields and tags.
        interface (BriefInterface): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        role (Union[Unset, VirtualCircuitTerminationRole]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VirtualCircuitTerminationCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    virtual_circuit: "BriefVirtualCircuit"
    interface: "BriefInterface"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    role: Union[Unset, "VirtualCircuitTerminationRole"] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VirtualCircuitTerminationCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        virtual_circuit = self.virtual_circuit.to_dict()

        interface = self.interface.to_dict()

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

        role: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "virtual_circuit": virtual_circuit,
                "interface": interface,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_interface import BriefInterface
        from ..models.brief_virtual_circuit import BriefVirtualCircuit
        from ..models.nested_tag import NestedTag
        from ..models.virtual_circuit_termination_custom_fields import VirtualCircuitTerminationCustomFields
        from ..models.virtual_circuit_termination_role import VirtualCircuitTerminationRole

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        virtual_circuit = BriefVirtualCircuit.from_dict(d.pop("virtual_circuit"))

        interface = BriefInterface.from_dict(d.pop("interface"))

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

        _role = d.pop("role", UNSET)
        role: Union[Unset, VirtualCircuitTerminationRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = VirtualCircuitTerminationRole.from_dict(_role)

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualCircuitTerminationCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualCircuitTerminationCustomFields.from_dict(_custom_fields)

        virtual_circuit_termination = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            virtual_circuit=virtual_circuit,
            interface=interface,
            created=created,
            last_updated=last_updated,
            role=role,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_circuit_termination.additional_properties = d
        return virtual_circuit_termination

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
