from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_source_request_sync_interval_type_1 import (
    DataSourceRequestSyncIntervalType1,
)
from ..models.data_source_request_sync_interval_type_2_type_1 import (
    DataSourceRequestSyncIntervalType2Type1,
)
from ..models.data_source_request_sync_interval_type_3_type_1 import (
    DataSourceRequestSyncIntervalType3Type1,
)
from ..models.data_source_request_type_type_1 import DataSourceRequestTypeType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_request_custom_fields import DataSourceRequestCustomFields


T = TypeVar("T", bound="DataSourceRequest")


@_attrs_define
class DataSourceRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        type_ (Union[DataSourceRequestTypeType1, None]): * `None` - ---------
            * `local` - Local
            * `git` - Git
            * `amazon-s3` - Amazon S3
        source_url (str):
        enabled (Union[Unset, bool]):
        description (Union[Unset, str]):
        sync_interval (Union[DataSourceRequestSyncIntervalType1, DataSourceRequestSyncIntervalType2Type1,
            DataSourceRequestSyncIntervalType3Type1, None, Unset]): * `1` - Minutely
            * `60` - Hourly
            * `720` - 12 hours
            * `1440` - Daily
            * `10080` - Weekly
            * `43200` - 30 days
        parameters (Union[Unset, Any]):
        ignore_rules (Union[Unset, str]): Patterns (one per line) matching files to ignore when syncing
        comments (Union[Unset, str]):
        custom_fields (Union[Unset, DataSourceRequestCustomFields]):
    """

    name: str
    type_: Union[DataSourceRequestTypeType1, None]
    source_url: str
    enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    sync_interval: Union[
        DataSourceRequestSyncIntervalType1,
        DataSourceRequestSyncIntervalType2Type1,
        DataSourceRequestSyncIntervalType3Type1,
        None,
        Unset,
    ] = UNSET
    parameters: Union[Unset, Any] = UNSET
    ignore_rules: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "DataSourceRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: Union[None, str]
        if isinstance(self.type_, DataSourceRequestTypeType1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        source_url = self.source_url

        enabled = self.enabled

        description = self.description

        sync_interval: Union[None, Unset, int]
        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        elif isinstance(self.sync_interval, DataSourceRequestSyncIntervalType1):
            sync_interval = self.sync_interval.value
        elif isinstance(self.sync_interval, DataSourceRequestSyncIntervalType2Type1):
            sync_interval = self.sync_interval.value
        elif isinstance(self.sync_interval, DataSourceRequestSyncIntervalType3Type1):
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_request_custom_fields import (
            DataSourceRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_type_(data: object) -> Union[DataSourceRequestTypeType1, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = DataSourceRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[DataSourceRequestTypeType1, None], data)

        type_ = _parse_type_(d.pop("type"))

        source_url = d.pop("source_url")

        enabled = d.pop("enabled", UNSET)

        description = d.pop("description", UNSET)

        def _parse_sync_interval(
            data: object,
        ) -> Union[
            DataSourceRequestSyncIntervalType1,
            DataSourceRequestSyncIntervalType2Type1,
            DataSourceRequestSyncIntervalType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_1 = DataSourceRequestSyncIntervalType1(data)

                return sync_interval_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_2_type_1 = DataSourceRequestSyncIntervalType2Type1(
                    data
                )

                return sync_interval_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_3_type_1 = DataSourceRequestSyncIntervalType3Type1(
                    data
                )

                return sync_interval_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    DataSourceRequestSyncIntervalType1,
                    DataSourceRequestSyncIntervalType2Type1,
                    DataSourceRequestSyncIntervalType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        sync_interval = _parse_sync_interval(d.pop("sync_interval", UNSET))

        parameters = d.pop("parameters", UNSET)

        ignore_rules = d.pop("ignore_rules", UNSET)

        comments = d.pop("comments", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, DataSourceRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DataSourceRequestCustomFields.from_dict(_custom_fields)

        data_source_request = cls(
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

        data_source_request.additional_properties = d
        return data_source_request

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
