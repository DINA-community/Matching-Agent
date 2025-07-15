import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.brief_data_source import BriefDataSource


T = TypeVar("T", bound="DataFile")


@_attrs_define
class DataFile:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        source (BriefDataSource): Adds support for custom fields and tags.
        path (str): File path relative to the data source's root
        last_updated (datetime.datetime):
        size (int):
        hash_ (str): SHA256 hash of the file data
    """

    id: int
    url: str
    display_url: str
    display: str
    source: "BriefDataSource"
    path: str
    last_updated: datetime.datetime
    size: int
    hash_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        source = self.source.to_dict()

        path = self.path

        last_updated = self.last_updated.isoformat()

        size = self.size

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "source": source,
                "path": path,
                "last_updated": last_updated,
                "size": size,
                "hash": hash_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_data_source import BriefDataSource

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        source = BriefDataSource.from_dict(d.pop("source"))

        path = d.pop("path")

        last_updated = isoparse(d.pop("last_updated"))

        size = d.pop("size")

        hash_ = d.pop("hash")

        data_file = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            source=source,
            path=path,
            last_updated=last_updated,
            size=size,
            hash_=hash_,
        )

        data_file.additional_properties = d
        return data_file

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
