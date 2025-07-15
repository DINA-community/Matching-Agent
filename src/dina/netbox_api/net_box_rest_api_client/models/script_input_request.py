import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScriptInputRequest")


@_attrs_define
class ScriptInputRequest:
    """
    Attributes:
        data (Any):
        commit (bool):
        schedule_at (Union[None, Unset, datetime.datetime]):
        interval (Union[None, Unset, int]):
    """

    data: Any
    commit: bool
    schedule_at: Union[None, Unset, datetime.datetime] = UNSET
    interval: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        commit = self.commit

        schedule_at: Union[None, Unset, str]
        if isinstance(self.schedule_at, Unset):
            schedule_at = UNSET
        elif isinstance(self.schedule_at, datetime.datetime):
            schedule_at = self.schedule_at.isoformat()
        else:
            schedule_at = self.schedule_at

        interval: Union[None, Unset, int]
        if isinstance(self.interval, Unset):
            interval = UNSET
        else:
            interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "commit": commit,
            }
        )
        if schedule_at is not UNSET:
            field_dict["schedule_at"] = schedule_at
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        data = (None, str(self.data).encode(), "text/plain")

        commit = (None, str(self.commit).encode(), "text/plain")

        schedule_at: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.schedule_at, Unset):
            schedule_at = UNSET
        elif isinstance(self.schedule_at, datetime.datetime):
            schedule_at = self.schedule_at.isoformat().encode()
        else:
            schedule_at = (None, str(self.schedule_at).encode(), "text/plain")

        interval: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.interval, Unset):
            interval = UNSET
        elif isinstance(self.interval, int):
            interval = (None, str(self.interval).encode(), "text/plain")
        else:
            interval = (None, str(self.interval).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "data": data,
                "commit": commit,
            }
        )
        if schedule_at is not UNSET:
            field_dict["schedule_at"] = schedule_at
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data")

        commit = d.pop("commit")

        def _parse_schedule_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_at_type_0 = isoparse(data)

                return schedule_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        schedule_at = _parse_schedule_at(d.pop("schedule_at", UNSET))

        def _parse_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        interval = _parse_interval(d.pop("interval", UNSET))

        script_input_request = cls(
            data=data,
            commit=commit,
            schedule_at=schedule_at,
            interval=interval,
        )

        script_input_request.additional_properties = d
        return script_input_request

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
