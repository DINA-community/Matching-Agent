import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_custom_field_request_filter_logic import PatchedWritableCustomFieldRequestFilterLogic
from ..models.patched_writable_custom_field_request_type import PatchedWritableCustomFieldRequestType
from ..models.patched_writable_custom_field_request_ui_editable import PatchedWritableCustomFieldRequestUiEditable
from ..models.patched_writable_custom_field_request_ui_visible import PatchedWritableCustomFieldRequestUiVisible
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_custom_field_choice_set_request import BriefCustomFieldChoiceSetRequest


T = TypeVar("T", bound="PatchedWritableCustomFieldRequest")


@_attrs_define
class PatchedWritableCustomFieldRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_types (Union[Unset, list[str]]):
            type_ (Union[Unset, PatchedWritableCustomFieldRequestType]): The type of data this custom field holds

                * `text` - Text
                * `longtext` - Text (long)
                * `integer` - Integer
                * `decimal` - Decimal
                * `boolean` - Boolean (true/false)
                * `date` - Date
                * `datetime` - Date & time
                * `url` - URL
                * `json` - JSON
                * `select` - Selection
                * `multiselect` - Multiple selection
                * `object` - Object
                * `multiobject` - Multiple objects
            related_object_type (Union[None, Unset, str]):
            name (Union[Unset, str]): Internal field name
            label (Union[Unset, str]): Name of the field as displayed to users (if not provided, 'the field's name will be
                used)
            group_name (Union[Unset, str]): Custom fields within the same group will be displayed together
            description (Union[Unset, str]):
            required (Union[Unset, bool]): This field is required when creating new objects or editing an existing object.
            unique (Union[Unset, bool]): The value of this field must be unique for the assigned object
            search_weight (Union[Unset, int]): Weighting for search. Lower values are considered more important. Fields with
                a search weight of zero will be ignored.
            filter_logic (Union[Unset, PatchedWritableCustomFieldRequestFilterLogic]): Loose matches any instance of a given
                string; exact matches the entire field.

                * `disabled` - Disabled
                * `loose` - Loose
                * `exact` - Exact
            ui_visible (Union[Unset, PatchedWritableCustomFieldRequestUiVisible]): Specifies whether the custom field is
                displayed in the UI

                * `always` - Always
                * `if-set` - If set
                * `hidden` - Hidden
            ui_editable (Union[Unset, PatchedWritableCustomFieldRequestUiEditable]): Specifies whether the custom field
                value can be edited in the UI

                * `yes` - Yes
                * `no` - No
                * `hidden` - Hidden
            is_cloneable (Union[Unset, bool]): Replicate this value when cloning objects
            default (Union[Unset, Any]): Default value for the field (must be a JSON value). Encapsulate strings with double
                quotes (e.g. "Foo").
            related_object_filter (Union[Unset, Any]): Filter the object selection choices using a query_params dict (must
                be a JSON value).Encapsulate strings with double quotes (e.g. "Foo").
            weight (Union[Unset, int]): Fields with higher weights appear lower in a form.
            validation_minimum (Union[None, Unset, int]): Minimum allowed value (for numeric fields)
            validation_maximum (Union[None, Unset, int]): Maximum allowed value (for numeric fields)
            validation_regex (Union[Unset, str]): Regular expression to enforce on text field values. Use ^ and $ to force
                matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase
                letters.
            choice_set (Union['BriefCustomFieldChoiceSetRequest', None, Unset, int]):
            comments (Union[Unset, str]):
    """

    object_types: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, PatchedWritableCustomFieldRequestType] = UNSET
    related_object_type: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    unique: Union[Unset, bool] = UNSET
    search_weight: Union[Unset, int] = UNSET
    filter_logic: Union[Unset, PatchedWritableCustomFieldRequestFilterLogic] = UNSET
    ui_visible: Union[Unset, PatchedWritableCustomFieldRequestUiVisible] = UNSET
    ui_editable: Union[Unset, PatchedWritableCustomFieldRequestUiEditable] = UNSET
    is_cloneable: Union[Unset, bool] = UNSET
    default: Union[Unset, Any] = UNSET
    related_object_filter: Union[Unset, Any] = UNSET
    weight: Union[Unset, int] = UNSET
    validation_minimum: Union[None, Unset, int] = UNSET
    validation_maximum: Union[None, Unset, int] = UNSET
    validation_regex: Union[Unset, str] = UNSET
    choice_set: Union["BriefCustomFieldChoiceSetRequest", None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_custom_field_choice_set_request import BriefCustomFieldChoiceSetRequest

        object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        related_object_type: Union[None, Unset, str]
        if isinstance(self.related_object_type, Unset):
            related_object_type = UNSET
        else:
            related_object_type = self.related_object_type

        name = self.name

        label = self.label

        group_name = self.group_name

        description = self.description

        required = self.required

        unique = self.unique

        search_weight = self.search_weight

        filter_logic: Union[Unset, str] = UNSET
        if not isinstance(self.filter_logic, Unset):
            filter_logic = self.filter_logic.value

        ui_visible: Union[Unset, str] = UNSET
        if not isinstance(self.ui_visible, Unset):
            ui_visible = self.ui_visible.value

        ui_editable: Union[Unset, str] = UNSET
        if not isinstance(self.ui_editable, Unset):
            ui_editable = self.ui_editable.value

        is_cloneable = self.is_cloneable

        default = self.default

        related_object_filter = self.related_object_filter

        weight = self.weight

        validation_minimum: Union[None, Unset, int]
        if isinstance(self.validation_minimum, Unset):
            validation_minimum = UNSET
        else:
            validation_minimum = self.validation_minimum

        validation_maximum: Union[None, Unset, int]
        if isinstance(self.validation_maximum, Unset):
            validation_maximum = UNSET
        else:
            validation_maximum = self.validation_maximum

        validation_regex = self.validation_regex

        choice_set: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.choice_set, Unset):
            choice_set = UNSET
        elif isinstance(self.choice_set, BriefCustomFieldChoiceSetRequest):
            choice_set = self.choice_set.to_dict()
        else:
            choice_set = self.choice_set

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if type_ is not UNSET:
            field_dict["type"] = type_
        if related_object_type is not UNSET:
            field_dict["related_object_type"] = related_object_type
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if unique is not UNSET:
            field_dict["unique"] = unique
        if search_weight is not UNSET:
            field_dict["search_weight"] = search_weight
        if filter_logic is not UNSET:
            field_dict["filter_logic"] = filter_logic
        if ui_visible is not UNSET:
            field_dict["ui_visible"] = ui_visible
        if ui_editable is not UNSET:
            field_dict["ui_editable"] = ui_editable
        if is_cloneable is not UNSET:
            field_dict["is_cloneable"] = is_cloneable
        if default is not UNSET:
            field_dict["default"] = default
        if related_object_filter is not UNSET:
            field_dict["related_object_filter"] = related_object_filter
        if weight is not UNSET:
            field_dict["weight"] = weight
        if validation_minimum is not UNSET:
            field_dict["validation_minimum"] = validation_minimum
        if validation_maximum is not UNSET:
            field_dict["validation_maximum"] = validation_maximum
        if validation_regex is not UNSET:
            field_dict["validation_regex"] = validation_regex
        if choice_set is not UNSET:
            field_dict["choice_set"] = choice_set
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.object_types, Unset):
            _temp_object_types = self.object_types
            object_types = (None, json.dumps(_temp_object_types).encode(), "application/json")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        related_object_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.related_object_type, Unset):
            related_object_type = UNSET
        elif isinstance(self.related_object_type, str):
            related_object_type = (None, str(self.related_object_type).encode(), "text/plain")
        else:
            related_object_type = (None, str(self.related_object_type).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        group_name = (
            self.group_name
            if isinstance(self.group_name, Unset)
            else (None, str(self.group_name).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        required = (
            self.required if isinstance(self.required, Unset) else (None, str(self.required).encode(), "text/plain")
        )

        unique = self.unique if isinstance(self.unique, Unset) else (None, str(self.unique).encode(), "text/plain")

        search_weight = (
            self.search_weight
            if isinstance(self.search_weight, Unset)
            else (None, str(self.search_weight).encode(), "text/plain")
        )

        filter_logic: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.filter_logic, Unset):
            filter_logic = (None, str(self.filter_logic.value).encode(), "text/plain")

        ui_visible: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.ui_visible, Unset):
            ui_visible = (None, str(self.ui_visible.value).encode(), "text/plain")

        ui_editable: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.ui_editable, Unset):
            ui_editable = (None, str(self.ui_editable.value).encode(), "text/plain")

        is_cloneable = (
            self.is_cloneable
            if isinstance(self.is_cloneable, Unset)
            else (None, str(self.is_cloneable).encode(), "text/plain")
        )

        default = self.default if isinstance(self.default, Unset) else (None, str(self.default).encode(), "text/plain")

        related_object_filter = (
            self.related_object_filter
            if isinstance(self.related_object_filter, Unset)
            else (None, str(self.related_object_filter).encode(), "text/plain")
        )

        weight = self.weight if isinstance(self.weight, Unset) else (None, str(self.weight).encode(), "text/plain")

        validation_minimum: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.validation_minimum, Unset):
            validation_minimum = UNSET
        elif isinstance(self.validation_minimum, int):
            validation_minimum = (None, str(self.validation_minimum).encode(), "text/plain")
        else:
            validation_minimum = (None, str(self.validation_minimum).encode(), "text/plain")

        validation_maximum: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.validation_maximum, Unset):
            validation_maximum = UNSET
        elif isinstance(self.validation_maximum, int):
            validation_maximum = (None, str(self.validation_maximum).encode(), "text/plain")
        else:
            validation_maximum = (None, str(self.validation_maximum).encode(), "text/plain")

        validation_regex = (
            self.validation_regex
            if isinstance(self.validation_regex, Unset)
            else (None, str(self.validation_regex).encode(), "text/plain")
        )

        choice_set: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.choice_set, Unset):
            choice_set = UNSET
        elif isinstance(self.choice_set, int):
            choice_set = (None, str(self.choice_set).encode(), "text/plain")
        elif isinstance(self.choice_set, None):
            choice_set = (None, str(self.choice_set).encode(), "text/plain")
        elif isinstance(self.choice_set, BriefCustomFieldChoiceSetRequest):
            choice_set = (None, json.dumps(self.choice_set.to_dict()).encode(), "application/json")
        else:
            choice_set = (None, str(self.choice_set).encode(), "text/plain")

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if type_ is not UNSET:
            field_dict["type"] = type_
        if related_object_type is not UNSET:
            field_dict["related_object_type"] = related_object_type
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if unique is not UNSET:
            field_dict["unique"] = unique
        if search_weight is not UNSET:
            field_dict["search_weight"] = search_weight
        if filter_logic is not UNSET:
            field_dict["filter_logic"] = filter_logic
        if ui_visible is not UNSET:
            field_dict["ui_visible"] = ui_visible
        if ui_editable is not UNSET:
            field_dict["ui_editable"] = ui_editable
        if is_cloneable is not UNSET:
            field_dict["is_cloneable"] = is_cloneable
        if default is not UNSET:
            field_dict["default"] = default
        if related_object_filter is not UNSET:
            field_dict["related_object_filter"] = related_object_filter
        if weight is not UNSET:
            field_dict["weight"] = weight
        if validation_minimum is not UNSET:
            field_dict["validation_minimum"] = validation_minimum
        if validation_maximum is not UNSET:
            field_dict["validation_maximum"] = validation_maximum
        if validation_regex is not UNSET:
            field_dict["validation_regex"] = validation_regex
        if choice_set is not UNSET:
            field_dict["choice_set"] = choice_set
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_custom_field_choice_set_request import BriefCustomFieldChoiceSetRequest

        d = dict(src_dict)
        object_types = cast(list[str], d.pop("object_types", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PatchedWritableCustomFieldRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchedWritableCustomFieldRequestType(_type_)

        def _parse_related_object_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        related_object_type = _parse_related_object_type(d.pop("related_object_type", UNSET))

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        group_name = d.pop("group_name", UNSET)

        description = d.pop("description", UNSET)

        required = d.pop("required", UNSET)

        unique = d.pop("unique", UNSET)

        search_weight = d.pop("search_weight", UNSET)

        _filter_logic = d.pop("filter_logic", UNSET)
        filter_logic: Union[Unset, PatchedWritableCustomFieldRequestFilterLogic]
        if isinstance(_filter_logic, Unset):
            filter_logic = UNSET
        else:
            filter_logic = PatchedWritableCustomFieldRequestFilterLogic(_filter_logic)

        _ui_visible = d.pop("ui_visible", UNSET)
        ui_visible: Union[Unset, PatchedWritableCustomFieldRequestUiVisible]
        if isinstance(_ui_visible, Unset):
            ui_visible = UNSET
        else:
            ui_visible = PatchedWritableCustomFieldRequestUiVisible(_ui_visible)

        _ui_editable = d.pop("ui_editable", UNSET)
        ui_editable: Union[Unset, PatchedWritableCustomFieldRequestUiEditable]
        if isinstance(_ui_editable, Unset):
            ui_editable = UNSET
        else:
            ui_editable = PatchedWritableCustomFieldRequestUiEditable(_ui_editable)

        is_cloneable = d.pop("is_cloneable", UNSET)

        default = d.pop("default", UNSET)

        related_object_filter = d.pop("related_object_filter", UNSET)

        weight = d.pop("weight", UNSET)

        def _parse_validation_minimum(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        validation_minimum = _parse_validation_minimum(d.pop("validation_minimum", UNSET))

        def _parse_validation_maximum(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        validation_maximum = _parse_validation_maximum(d.pop("validation_maximum", UNSET))

        validation_regex = d.pop("validation_regex", UNSET)

        def _parse_choice_set(data: object) -> Union["BriefCustomFieldChoiceSetRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                choice_set_type_1_type_1 = BriefCustomFieldChoiceSetRequest.from_dict(data)

                return choice_set_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCustomFieldChoiceSetRequest", None, Unset, int], data)

        choice_set = _parse_choice_set(d.pop("choice_set", UNSET))

        comments = d.pop("comments", UNSET)

        patched_writable_custom_field_request = cls(
            object_types=object_types,
            type_=type_,
            related_object_type=related_object_type,
            name=name,
            label=label,
            group_name=group_name,
            description=description,
            required=required,
            unique=unique,
            search_weight=search_weight,
            filter_logic=filter_logic,
            ui_visible=ui_visible,
            ui_editable=ui_editable,
            is_cloneable=is_cloneable,
            default=default,
            related_object_filter=related_object_filter,
            weight=weight,
            validation_minimum=validation_minimum,
            validation_maximum=validation_maximum,
            validation_regex=validation_regex,
            choice_set=choice_set,
            comments=comments,
        )

        patched_writable_custom_field_request.additional_properties = d
        return patched_writable_custom_field_request

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
