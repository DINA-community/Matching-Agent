import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_source_sync_interval_type_1 import DataSourceSyncIntervalType1
from ..models.data_source_sync_interval_type_2_type_1 import (
    DataSourceSyncIntervalType2Type1,
)
from ..models.data_source_sync_interval_type_3_type_1 import (
    DataSourceSyncIntervalType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_custom_fields import DataSourceCustomFields
    from ..models.data_source_status import DataSourceStatus
    from ..models.data_source_type import DataSourceType


T = TypeVar("T", bound="DataSource")


@_attrs_define
class DataSource:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        type_ (DataSourceType):
        source_url (str):
        status (DataSourceStatus):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        last_synced (Union[None, datetime.datetime]):
        file_count (int):
        enabled (Union[Unset, bool]):
        description (Union[Unset, str]):
        sync_interval (Union[DataSourceSyncIntervalType1, DataSourceSyncIntervalType2Type1,
            DataSourceSyncIntervalType3Type1, None, Unset]): * `1` - Minutely
            * `60` - Hourly
            * `720` - 12 hours
            * `1440` - Daily
            * `10080` - Weekly
            * `43200` - 30 days
        parameters (Union[Unset, Any]):
        ignore_rules (Union[Unset, str]): Patterns (one per line) matching files to ignore when syncing
        comments (Union[Unset, str]):
        custom_fields (Union[Unset, DataSourceCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    type_: "DataSourceType"
    source_url: str
    status: "DataSourceStatus"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    last_synced: Union[None, datetime.datetime]
    file_count: int
    enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    sync_interval: Union[
        DataSourceSyncIntervalType1,
        DataSourceSyncIntervalType2Type1,
        DataSourceSyncIntervalType3Type1,
        None,
        Unset,
    ] = UNSET
    parameters: Union[Unset, Any] = UNSET
    ignore_rules: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "DataSourceCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        type_ = self.type_.to_dict()

        source_url = self.source_url

        status = self.status.to_dict()

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

        last_synced: Union[None, str]
        if isinstance(self.last_synced, datetime.datetime):
            last_synced = self.last_synced.isoformat()
        else:
            last_synced = self.last_synced

        file_count = self.file_count

        enabled = self.enabled

        description = self.description

        sync_interval: Union[None, Unset, int]
        if isinstance(self.sync_interval, Unset):
            sync_interval = UNSET
        elif isinstance(self.sync_interval, DataSourceSyncIntervalType1):
            sync_interval = self.sync_interval.value
        elif isinstance(self.sync_interval, DataSourceSyncIntervalType2Type1):
            sync_interval = self.sync_interval.value
        elif isinstance(self.sync_interval, DataSourceSyncIntervalType3Type1):
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "type": type_,
                "source_url": source_url,
                "status": status,
                "created": created,
                "last_updated": last_updated,
                "last_synced": last_synced,
                "file_count": file_count,
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
        from ..models.data_source_custom_fields import DataSourceCustomFields
        from ..models.data_source_status import DataSourceStatus
        from ..models.data_source_type import DataSourceType

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        type_ = DataSourceType.from_dict(d.pop("type"))

        source_url = d.pop("source_url")

        status = DataSourceStatus.from_dict(d.pop("status"))

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

        def _parse_last_synced(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_type_0 = isoparse(data)

                return last_synced_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_synced = _parse_last_synced(d.pop("last_synced"))

        file_count = d.pop("file_count")

        enabled = d.pop("enabled", UNSET)

        description = d.pop("description", UNSET)

        def _parse_sync_interval(
            data: object,
        ) -> Union[
            DataSourceSyncIntervalType1,
            DataSourceSyncIntervalType2Type1,
            DataSourceSyncIntervalType3Type1,
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
                sync_interval_type_1 = DataSourceSyncIntervalType1(data)

                return sync_interval_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_2_type_1 = DataSourceSyncIntervalType2Type1(data)

                return sync_interval_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                sync_interval_type_3_type_1 = DataSourceSyncIntervalType3Type1(data)

                return sync_interval_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    DataSourceSyncIntervalType1,
                    DataSourceSyncIntervalType2Type1,
                    DataSourceSyncIntervalType3Type1,
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
        custom_fields: Union[Unset, DataSourceCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DataSourceCustomFields.from_dict(_custom_fields)

        data_source = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            type_=type_,
            source_url=source_url,
            status=status,
            created=created,
            last_updated=last_updated,
            last_synced=last_synced,
            file_count=file_count,
            enabled=enabled,
            description=description,
            sync_interval=sync_interval,
            parameters=parameters,
            ignore_rules=ignore_rules,
            comments=comments,
            custom_fields=custom_fields,
        )

        data_source.additional_properties = d
        return data_source

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
