import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_data_file import BriefDataFile
    from ..models.brief_data_source import BriefDataSource
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ConfigTemplate")


@_attrs_define
class ConfigTemplate:
    """Introduces support for Tag assignment. Adds `tags` serialization, and handles tag assignment
    on create() and update().

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            name (str):
            template_code (str): Jinja template code.
            data_path (str): Path to remote file (relative to data source root)
            data_synced (Union[None, datetime.datetime]):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            description (Union[Unset, str]):
            environment_params (Union[Unset, Any]): Any <a
                href="https://jinja.palletsprojects.com/en/stable/api/#jinja2.Environment">additional parameters</a> to pass
                when constructing the Jinja environment
            mime_type (Union[Unset, str]): Defaults to <code>text/plain; charset=utf-8</code>
            file_name (Union[Unset, str]): Filename to give to the rendered export file
            file_extension (Union[Unset, str]): Extension to append to the rendered filename
            as_attachment (Union[Unset, bool]): Download file as attachment
            data_source (Union[Unset, BriefDataSource]): Adds support for custom fields and tags.
            data_file (Union[Unset, BriefDataFile]): Adds support for custom fields and tags.
            tags (Union[Unset, list['NestedTag']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    template_code: str
    data_path: str
    data_synced: Union[None, datetime.datetime]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    environment_params: Union[Unset, Any] = UNSET
    mime_type: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_extension: Union[Unset, str] = UNSET
    as_attachment: Union[Unset, bool] = UNSET
    data_source: Union[Unset, "BriefDataSource"] = UNSET
    data_file: Union[Unset, "BriefDataFile"] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        template_code = self.template_code

        data_path = self.data_path

        data_synced: Union[None, str]
        if isinstance(self.data_synced, datetime.datetime):
            data_synced = self.data_synced.isoformat()
        else:
            data_synced = self.data_synced

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

        description = self.description

        environment_params = self.environment_params

        mime_type = self.mime_type

        file_name = self.file_name

        file_extension = self.file_extension

        as_attachment = self.as_attachment

        data_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        data_file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_file, Unset):
            data_file = self.data_file.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "template_code": template_code,
                "data_path": data_path,
                "data_synced": data_synced,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if environment_params is not UNSET:
            field_dict["environment_params"] = environment_params
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_extension is not UNSET:
            field_dict["file_extension"] = file_extension
        if as_attachment is not UNSET:
            field_dict["as_attachment"] = as_attachment
        if data_source is not UNSET:
            field_dict["data_source"] = data_source
        if data_file is not UNSET:
            field_dict["data_file"] = data_file
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_data_file import BriefDataFile
        from ..models.brief_data_source import BriefDataSource
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        template_code = d.pop("template_code")

        data_path = d.pop("data_path")

        def _parse_data_synced(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_synced_type_0 = isoparse(data)

                return data_synced_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        data_synced = _parse_data_synced(d.pop("data_synced"))

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

        description = d.pop("description", UNSET)

        environment_params = d.pop("environment_params", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        file_name = d.pop("file_name", UNSET)

        file_extension = d.pop("file_extension", UNSET)

        as_attachment = d.pop("as_attachment", UNSET)

        _data_source = d.pop("data_source", UNSET)
        data_source: Union[Unset, BriefDataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = BriefDataSource.from_dict(_data_source)

        _data_file = d.pop("data_file", UNSET)
        data_file: Union[Unset, BriefDataFile]
        if isinstance(_data_file, Unset):
            data_file = UNSET
        else:
            data_file = BriefDataFile.from_dict(_data_file)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        config_template = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            template_code=template_code,
            data_path=data_path,
            data_synced=data_synced,
            created=created,
            last_updated=last_updated,
            description=description,
            environment_params=environment_params,
            mime_type=mime_type,
            file_name=file_name,
            file_extension=file_extension,
            as_attachment=as_attachment,
            data_source=data_source,
            data_file=data_file,
            tags=tags,
        )

        config_template.additional_properties = d
        return config_template

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
