import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_data_source_request import BriefDataSourceRequest


T = TypeVar("T", bound="ExportTemplateRequest")


@_attrs_define
class ExportTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_types (list[str]):
            name (str):
            template_code (str): Jinja template code.
            description (Union[Unset, str]):
            environment_params (Union[Unset, Any]): Any <a
                href="https://jinja.palletsprojects.com/en/stable/api/#jinja2.Environment">additional parameters</a> to pass
                when constructing the Jinja environment
            mime_type (Union[Unset, str]): Defaults to <code>text/plain; charset=utf-8</code>
            file_name (Union[Unset, str]): Filename to give to the rendered export file
            file_extension (Union[Unset, str]): Extension to append to the rendered filename
            as_attachment (Union[Unset, bool]): Download file as attachment
            data_source (Union['BriefDataSourceRequest', Unset, int]):
    """

    object_types: list[str]
    name: str
    template_code: str
    description: Union[Unset, str] = UNSET
    environment_params: Union[Unset, Any] = UNSET
    mime_type: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_extension: Union[Unset, str] = UNSET
    as_attachment: Union[Unset, bool] = UNSET
    data_source: Union["BriefDataSourceRequest", Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_data_source_request import BriefDataSourceRequest

        object_types = self.object_types

        name = self.name

        template_code = self.template_code

        description = self.description

        environment_params = self.environment_params

        mime_type = self.mime_type

        file_name = self.file_name

        file_extension = self.file_extension

        as_attachment = self.as_attachment

        data_source: Union[Unset, dict[str, Any], int]
        if isinstance(self.data_source, Unset):
            data_source = UNSET
        elif isinstance(self.data_source, BriefDataSourceRequest):
            data_source = self.data_source.to_dict()
        else:
            data_source = self.data_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_types": object_types,
                "name": name,
                "template_code": template_code,
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        _temp_object_types = self.object_types
        object_types = (None, json.dumps(_temp_object_types).encode(), "application/json")

        name = (None, str(self.name).encode(), "text/plain")

        template_code = (None, str(self.template_code).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        environment_params = (
            self.environment_params
            if isinstance(self.environment_params, Unset)
            else (None, str(self.environment_params).encode(), "text/plain")
        )

        mime_type = (
            self.mime_type if isinstance(self.mime_type, Unset) else (None, str(self.mime_type).encode(), "text/plain")
        )

        file_name = (
            self.file_name if isinstance(self.file_name, Unset) else (None, str(self.file_name).encode(), "text/plain")
        )

        file_extension = (
            self.file_extension
            if isinstance(self.file_extension, Unset)
            else (None, str(self.file_extension).encode(), "text/plain")
        )

        as_attachment = (
            self.as_attachment
            if isinstance(self.as_attachment, Unset)
            else (None, str(self.as_attachment).encode(), "text/plain")
        )

        data_source: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.data_source, Unset):
            data_source = UNSET
        elif isinstance(self.data_source, int):
            data_source = (None, str(self.data_source).encode(), "text/plain")
        else:
            data_source = (None, json.dumps(self.data_source.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "object_types": object_types,
                "name": name,
                "template_code": template_code,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_data_source_request import BriefDataSourceRequest

        d = dict(src_dict)
        object_types = cast(list[str], d.pop("object_types"))

        name = d.pop("name")

        template_code = d.pop("template_code")

        description = d.pop("description", UNSET)

        environment_params = d.pop("environment_params", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        file_name = d.pop("file_name", UNSET)

        file_extension = d.pop("file_extension", UNSET)

        as_attachment = d.pop("as_attachment", UNSET)

        def _parse_data_source(data: object) -> Union["BriefDataSourceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_source_type_1 = BriefDataSourceRequest.from_dict(data)

                return data_source_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDataSourceRequest", Unset, int], data)

        data_source = _parse_data_source(d.pop("data_source", UNSET))

        export_template_request = cls(
            object_types=object_types,
            name=name,
            template_code=template_code,
            description=description,
            environment_params=environment_params,
            mime_type=mime_type,
            file_name=file_name,
            file_extension=file_extension,
            as_attachment=as_attachment,
            data_source=data_source,
        )

        export_template_request.additional_properties = d
        return export_template_request

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
