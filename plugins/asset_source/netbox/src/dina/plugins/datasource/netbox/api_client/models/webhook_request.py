import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_request_http_method import WebhookRequestHttpMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.webhook_request_custom_fields import WebhookRequestCustomFields


T = TypeVar("T", bound="WebhookRequest")


@_attrs_define
class WebhookRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        payload_url (str): This URL will be called using the HTTP method defined when the webhook is called. Jinja2
            template processing is supported with the same context as the request body.
        description (Union[Unset, str]):
        http_method (Union[Unset, WebhookRequestHttpMethod]): * `GET` - GET
            * `POST` - POST
            * `PUT` - PUT
            * `PATCH` - PATCH
            * `DELETE` - DELETE
        http_content_type (Union[Unset, str]): The complete list of official content types is available <a
            href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.
        additional_headers (Union[Unset, str]): User-supplied HTTP headers to be sent with the request in addition to
            the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template
            processing is supported with the same context as the request body (below).
        body_template (Union[Unset, str]): Jinja2 template for a custom request body. If blank, a JSON object
            representing the change will be included. Available context data includes: <code>event</code>,
            <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and
            <code>data</code>.
        secret (Union[Unset, str]): When provided, the request will include a <code>X-Hook-Signature</code> header
            containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in
            the request.
        ssl_verification (Union[Unset, bool]): Enable SSL certificate verification. Disable with caution!
        ca_file_path (Union[None, Unset, str]): The specific CA certificate file to use for SSL verification. Leave
            blank to use the system defaults.
        custom_fields (Union[Unset, WebhookRequestCustomFields]):
        tags (Union[Unset, list['NestedTagRequest']]):
    """

    name: str
    payload_url: str
    description: Union[Unset, str] = UNSET
    http_method: Union[Unset, WebhookRequestHttpMethod] = UNSET
    http_content_type: Union[Unset, str] = UNSET
    additional_headers: Union[Unset, str] = UNSET
    body_template: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    ssl_verification: Union[Unset, bool] = UNSET
    ca_file_path: Union[None, Unset, str] = UNSET
    custom_fields: Union[Unset, "WebhookRequestCustomFields"] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        payload_url = self.payload_url

        description = self.description

        http_method: Union[Unset, str] = UNSET
        if not isinstance(self.http_method, Unset):
            http_method = self.http_method.value

        http_content_type = self.http_content_type

        additional_headers = self.additional_headers

        body_template = self.body_template

        secret = self.secret

        ssl_verification = self.ssl_verification

        ca_file_path: Union[None, Unset, str]
        if isinstance(self.ca_file_path, Unset):
            ca_file_path = UNSET
        else:
            ca_file_path = self.ca_file_path

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

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
                "name": name,
                "payload_url": payload_url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if http_method is not UNSET:
            field_dict["http_method"] = http_method
        if http_content_type is not UNSET:
            field_dict["http_content_type"] = http_content_type
        if additional_headers is not UNSET:
            field_dict["additional_headers"] = additional_headers
        if body_template is not UNSET:
            field_dict["body_template"] = body_template
        if secret is not UNSET:
            field_dict["secret"] = secret
        if ssl_verification is not UNSET:
            field_dict["ssl_verification"] = ssl_verification
        if ca_file_path is not UNSET:
            field_dict["ca_file_path"] = ca_file_path
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        payload_url = (None, str(self.payload_url).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        http_method: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.http_method, Unset):
            http_method = (None, str(self.http_method.value).encode(), "text/plain")

        http_content_type = (
            self.http_content_type
            if isinstance(self.http_content_type, Unset)
            else (None, str(self.http_content_type).encode(), "text/plain")
        )

        additional_headers = (
            self.additional_headers
            if isinstance(self.additional_headers, Unset)
            else (None, str(self.additional_headers).encode(), "text/plain")
        )

        body_template = (
            self.body_template
            if isinstance(self.body_template, Unset)
            else (None, str(self.body_template).encode(), "text/plain")
        )

        secret = (
            self.secret
            if isinstance(self.secret, Unset)
            else (None, str(self.secret).encode(), "text/plain")
        )

        ssl_verification = (
            self.ssl_verification
            if isinstance(self.ssl_verification, Unset)
            else (None, str(self.ssl_verification).encode(), "text/plain")
        )

        ca_file_path: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ca_file_path, Unset):
            ca_file_path = UNSET
        elif isinstance(self.ca_file_path, str):
            ca_file_path = (None, str(self.ca_file_path).encode(), "text/plain")
        else:
            ca_file_path = (None, str(self.ca_file_path).encode(), "text/plain")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "payload_url": payload_url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if http_method is not UNSET:
            field_dict["http_method"] = http_method
        if http_content_type is not UNSET:
            field_dict["http_content_type"] = http_content_type
        if additional_headers is not UNSET:
            field_dict["additional_headers"] = additional_headers
        if body_template is not UNSET:
            field_dict["body_template"] = body_template
        if secret is not UNSET:
            field_dict["secret"] = secret
        if ssl_verification is not UNSET:
            field_dict["ssl_verification"] = ssl_verification
        if ca_file_path is not UNSET:
            field_dict["ca_file_path"] = ca_file_path
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.webhook_request_custom_fields import WebhookRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        payload_url = d.pop("payload_url")

        description = d.pop("description", UNSET)

        _http_method = d.pop("http_method", UNSET)
        http_method: Union[Unset, WebhookRequestHttpMethod]
        if isinstance(_http_method, Unset):
            http_method = UNSET
        else:
            http_method = WebhookRequestHttpMethod(_http_method)

        http_content_type = d.pop("http_content_type", UNSET)

        additional_headers = d.pop("additional_headers", UNSET)

        body_template = d.pop("body_template", UNSET)

        secret = d.pop("secret", UNSET)

        ssl_verification = d.pop("ssl_verification", UNSET)

        def _parse_ca_file_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ca_file_path = _parse_ca_file_path(d.pop("ca_file_path", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WebhookRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WebhookRequestCustomFields.from_dict(_custom_fields)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        webhook_request = cls(
            name=name,
            payload_url=payload_url,
            description=description,
            http_method=http_method,
            http_content_type=http_content_type,
            additional_headers=additional_headers,
            body_template=body_template,
            secret=secret,
            ssl_verification=ssl_verification,
            ca_file_path=ca_file_path,
            custom_fields=custom_fields,
            tags=tags,
        )

        webhook_request.additional_properties = d
        return webhook_request

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
