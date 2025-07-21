from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nested_virtual_machine import NestedVirtualMachine


T = TypeVar("T", bound="NestedVMInterface")


@_attrs_define
class NestedVMInterface:
    """Represents an object related through a ForeignKey field. On write, it accepts a primary key (PK) value or a
    dictionary of attributes which can be used to uniquely identify the related object. This class should be
    subclassed to return a full representation of the related object on read.

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            virtual_machine (NestedVirtualMachine): Represents an object related through a ForeignKey field. On write, it
                accepts a primary key (PK) value or a
                dictionary of attributes which can be used to uniquely identify the related object. This class should be
                subclassed to return a full representation of the related object on read.
            name (str):
    """

    id: int
    url: str
    display_url: str
    display: str
    virtual_machine: "NestedVirtualMachine"
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        virtual_machine = self.virtual_machine.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "virtual_machine": virtual_machine,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_virtual_machine import NestedVirtualMachine

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        virtual_machine = NestedVirtualMachine.from_dict(d.pop("virtual_machine"))

        name = d.pop("name")

        nested_vm_interface = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            virtual_machine=virtual_machine,
            name=name,
        )

        nested_vm_interface.additional_properties = d
        return nested_vm_interface

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
