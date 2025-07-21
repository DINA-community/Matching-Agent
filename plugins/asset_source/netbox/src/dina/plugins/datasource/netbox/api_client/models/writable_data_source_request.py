import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_data_source_request_sync_interval_type_1 import (
    WritableDataSourceRequestSyncIntervalType1,
)
from ..models.writable_data_source_request_sync_interval_type_2_type_1 import (
    WritableDataSourceRequestSyncIntervalType2Type1,
)
from ..models.writable_data_source_request_sync_interval_type_3_type_1 import (
    WritableDataSourceRequestSyncIntervalType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.writable_data_source_request_custom_fields import (
        WritableDataSourceRequestCustomFields,
    )


T = TypeVar("T", bound="WritableDataSourceRequest")


@_attrs_define
class WritableDataSourceRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        type_ (str):
        source_url (str):
        enabled (Union[Unset, bool]):
        description (Union[Unset, str]):
        sync_interval (Union[None, Unset, WritableDataSourceRequestSyncIntervalType1,
            WritableDataSourceRequestSyncIntervalType2Type1, WritableDataSourceRequestSyncIntervalType3Type1]): * `1` -
            Minutely
            * `60` - Hourly
            * `720` - 12 hours
            * `1440` - Daily
            * `10080` - Weekly
            * `43200` - 30 days
        parameters (Union[Unset, Any]):
        ignore_rules (Union[Unset, str]): Patterns (one per line) matching files to ignore when syncing
        comments (Union[Unset, str]):
        custom_fields (Union[Unset, WritableDataSourceRequestCustomFields]):
    """

    name: str
    type_: str
    source_url: str
    enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    sync_interval: Union[
        None,
        Unset,
        WritableDataSourceRequestSyncIntervalType1,
        WritableDataSourceRequestSyncIntervalType2Type1,
        WritableDataSourceRequestSyncIntervalType3Type1,
    ] = UNSET
    parameters: Union[Unset, Any] = UNSET
    ignore_rules: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "WritableDataSourceRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        source_url = self.source_url

        enabled = self.enabled

        description = self.description

        sync_interval: Union[None, Unset, int]
        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        elif isinstance(self.sync_interval, WritableDataSourceRequestSyncIntervalType1):
            sync_interval = self.sync_interval.value
        elif isinstance(
            self.sync_interval, WritableDataSourceRequestSyncIntervalType2Type1
        ):
            sync_interval = self.sync_interval.value
        elif isinstance(
            self.sync_interval, WritableDataSourceRequestSyncIntervalType3Type1
        ):
            sync_interval = self.sync_interval.value
        else:
            sync_interval = self.sync_interval

        parameters = self.parameters

        ignore_rules = self.ignore_rules

        comments = self.comments

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "source_url": source_url,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if description is not UNSET:
            field_dict["description"] = description
        if sync_interval is not UNSET:
            field_dict["sync_interval"] = sync_interval
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if ignore_rules is not UNSET:
            field_dict["ignore_rules"] = ignore_rules
        if comments is not UNSET:
            field_dict["comments"] = comments
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        type_ = (None, str(self.type_).encode(), "text/plain")

        source_url = (None, str(self.source_url).encode(), "text/plain")

        enabled = (
            self.enabled
            if isinstance(self.enabled, Unset)
            else (None, str(self.enabled).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        sync_interval: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        elif isinstance(self.sync_interval, None):
            sync_interval = (None, str(self.sync_interval).encode(), "text/plain")
        elif isinstance(self.sync_interval, WritableDataSourceRequestSyncIntervalType1):
            sync_interval = (None, str(self.sync_interval.value).encode(), "text/plain")
        elif isinstance(self.sync_interval, None):
            sync_interval = (None, str(self.sync_interval).encode(), "text/plain")
        elif isinstance(
            self.sync_interval, WritableDataSourceRequestSyncIntervalType2Type1
        ):
            sync_interval = (None, str(self.sync_interval.value).encode(), "text/plain")
        elif isinstance(self.sync_interval, None):
            sync_interval = (None, str(self.sync_interval).encode(), "text/plain")
        else:
            sync_interval = (None, str(self.sync_interval.value).encode(), "text/plain")

        parameters = (
            self.parameters
            if isinstance(self.parameters, Unset)
            else (None, str(self.parameters).encode(), "text/plain")
        )

        ignore_rules = (
            self.ignore_rules
            if isinstance(self.ignore_rules, Unset)
            else (None, str(self.ignore_rules).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

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
                "name": name,
                "type": type_,
                "source_url": source_url,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if description is not UNSET:
            field_dict["description"] = description
        if sync_interval is not UNSET:
            field_dict["sync_interval"] = sync_interval
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if ignore_rules is not UNSET:
            field_dict["ignore_rules"] = ignore_rules
        if comments is not UNSET:
            field_dict["comments"] = comments
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.writable_data_source_request_custom_fields import (
            WritableDataSourceRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        source_url = d.pop("source_url")

        enabled = d.pop("enabled", UNSET)

        description = d.pop("description", UNSET)

        def _parse_sync_interval(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableDataSourceRequestSyncIntervalType1,
            WritableDataSourceRequestSyncIntervalType2Type1,
            WritableDataSourceRequestSyncIntervalType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_1 = WritableDataSourceRequestSyncIntervalType1(data)

                return sync_interval_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_2_type_1 = (
                    WritableDataSourceRequestSyncIntervalType2Type1(data)
                )

                return sync_interval_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_3_type_1 = (
                    WritableDataSourceRequestSyncIntervalType3Type1(data)
                )

                return sync_interval_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableDataSourceRequestSyncIntervalType1,
                    WritableDataSourceRequestSyncIntervalType2Type1,
                    WritableDataSourceRequestSyncIntervalType3Type1,
                ],
                data,
            )

        sync_interval = _parse_sync_interval(d.pop("sync_interval", UNSET))

        parameters = d.pop("parameters", UNSET)

        ignore_rules = d.pop("ignore_rules", UNSET)

        comments = d.pop("comments", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableDataSourceRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableDataSourceRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_data_source_request = cls(
            name=name,
            type_=type_,
            source_url=source_url,
            enabled=enabled,
            description=description,
            sync_interval=sync_interval,
            parameters=parameters,
            ignore_rules=ignore_rules,
            comments=comments,
            custom_fields=custom_fields,
        )

        writable_data_source_request.additional_properties = d
        return writable_data_source_request

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
