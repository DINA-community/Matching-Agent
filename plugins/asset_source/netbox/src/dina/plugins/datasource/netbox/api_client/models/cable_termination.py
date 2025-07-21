import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cable_termination_end import CableTerminationEnd

T = TypeVar("T", bound="CableTermination")


@_attrs_define
class CableTermination:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        cable (int):
        cable_end (CableTerminationEnd): * `A` - A
            * `B` - B
        termination_type (str):
        termination_id (int):
        termination (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
    """

    id: int
    url: str
    display: str
    cable: int
    cable_end: CableTerminationEnd
    termination_type: str
    termination_id: int
    termination: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        cable = self.cable

        cable_end = self.cable_end.value

        termination_type = self.termination_type

        termination_id = self.termination_id

        termination = self.termination

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "cable": cable,
                "cable_end": cable_end,
                "termination_type": termination_type,
                "termination_id": termination_id,
                "termination": termination,
                "created": created,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        cable = d.pop("cable")

        cable_end = CableTerminationEnd(d.pop("cable_end"))

        termination_type = d.pop("termination_type")

        termination_id = d.pop("termination_id")

        termination = d.pop("termination")

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

        cable_termination = cls(
            id=id,
            url=url,
            display=display,
            cable=cable,
            cable_end=cable_end,
            termination_type=termination_type,
            termination_id=termination_id,
            termination=termination,
            created=created,
            last_updated=last_updated,
        )

        cable_termination.additional_properties = d
        return cable_termination

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
