import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_custom_field_choice_set import BriefCustomFieldChoiceSet
    from ..models.custom_field_filter_logic import CustomFieldFilterLogic
    from ..models.custom_field_type import CustomFieldType
    from ..models.custom_field_ui_editable import CustomFieldUiEditable
    from ..models.custom_field_ui_visible import CustomFieldUiVisible


T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            object_types (list[str]):
            type_ (CustomFieldType):
            data_type (str):
            name (str): Internal field name
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            related_object_type (Union[None, Unset, str]):
            label (Union[Unset, str]): Name of the field as displayed to users (if not provided, 'the field's name will be
                used)
            group_name (Union[Unset, str]): Custom fields within the same group will be displayed together
            description (Union[Unset, str]):
            required (Union[Unset, bool]): This field is required when creating new objects or editing an existing object.
            unique (Union[Unset, bool]): The value of this field must be unique for the assigned object
            search_weight (Union[Unset, int]): Weighting for search. Lower values are considered more important. Fields with
                a search weight of zero will be ignored.
            filter_logic (Union[Unset, CustomFieldFilterLogic]):
            ui_visible (Union[Unset, CustomFieldUiVisible]):
            ui_editable (Union[Unset, CustomFieldUiEditable]):
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
            choice_set (Union['BriefCustomFieldChoiceSet', None, Unset]):
            comments (Union[Unset, str]):
    """

    id: int
    url: str
    display_url: str
    display: str
    object_types: list[str]
    type_: "CustomFieldType"
    data_type: str
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    related_object_type: Union[None, Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    unique: Union[Unset, bool] = UNSET
    search_weight: Union[Unset, int] = UNSET
    filter_logic: Union[Unset, "CustomFieldFilterLogic"] = UNSET
    ui_visible: Union[Unset, "CustomFieldUiVisible"] = UNSET
    ui_editable: Union[Unset, "CustomFieldUiEditable"] = UNSET
    is_cloneable: Union[Unset, bool] = UNSET
    default: Union[Unset, Any] = UNSET
    related_object_filter: Union[Unset, Any] = UNSET
    weight: Union[Unset, int] = UNSET
    validation_minimum: Union[None, Unset, int] = UNSET
    validation_maximum: Union[None, Unset, int] = UNSET
    validation_regex: Union[Unset, str] = UNSET
    choice_set: Union["BriefCustomFieldChoiceSet", None, Unset] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_custom_field_choice_set import BriefCustomFieldChoiceSet

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        object_types = self.object_types

        type_ = self.type_.to_dict()

        data_type = self.data_type

        name = self.name

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

        related_object_type: Union[None, Unset, str]
        if isinstance(self.related_object_type, Unset):
            related_object_type = UNSET
        else:
            related_object_type = self.related_object_type

        label = self.label

        group_name = self.group_name

        description = self.description

        required = self.required

        unique = self.unique

        search_weight = self.search_weight

        filter_logic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filter_logic, Unset):
            filter_logic = self.filter_logic.to_dict()

        ui_visible: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_visible, Unset):
            ui_visible = self.ui_visible.to_dict()

        ui_editable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ui_editable, Unset):
            ui_editable = self.ui_editable.to_dict()

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

        choice_set: Union[None, Unset, dict[str, Any]]
        if isinstance(self.choice_set, Unset):
            choice_set = UNSET
        elif isinstance(self.choice_set, BriefCustomFieldChoiceSet):
            choice_set = self.choice_set.to_dict()
        else:
            choice_set = self.choice_set

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "object_types": object_types,
                "type": type_,
                "data_type": data_type,
                "name": name,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if related_object_type is not UNSET:
            field_dict["related_object_type"] = related_object_type
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
        from ..models.brief_custom_field_choice_set import BriefCustomFieldChoiceSet
        from ..models.custom_field_filter_logic import CustomFieldFilterLogic
        from ..models.custom_field_type import CustomFieldType
        from ..models.custom_field_ui_editable import CustomFieldUiEditable
        from ..models.custom_field_ui_visible import CustomFieldUiVisible

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        object_types = cast(list[str], d.pop("object_types"))

        type_ = CustomFieldType.from_dict(d.pop("type"))

        data_type = d.pop("data_type")

        name = d.pop("name")

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

        def _parse_related_object_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        related_object_type = _parse_related_object_type(
            d.pop("related_object_type", UNSET)
        )

        label = d.pop("label", UNSET)

        group_name = d.pop("group_name", UNSET)

        description = d.pop("description", UNSET)

        required = d.pop("required", UNSET)

        unique = d.pop("unique", UNSET)

        search_weight = d.pop("search_weight", UNSET)

        _filter_logic = d.pop("filter_logic", UNSET)
        filter_logic: Union[Unset, CustomFieldFilterLogic]
        if isinstance(_filter_logic, Unset):
            filter_logic = UNSET
        else:
            filter_logic = CustomFieldFilterLogic.from_dict(_filter_logic)

        _ui_visible = d.pop("ui_visible", UNSET)
        ui_visible: Union[Unset, CustomFieldUiVisible]
        if isinstance(_ui_visible, Unset):
            ui_visible = UNSET
        else:
            ui_visible = CustomFieldUiVisible.from_dict(_ui_visible)

        _ui_editable = d.pop("ui_editable", UNSET)
        ui_editable: Union[Unset, CustomFieldUiEditable]
        if isinstance(_ui_editable, Unset):
            ui_editable = UNSET
        else:
            ui_editable = CustomFieldUiEditable.from_dict(_ui_editable)

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

        validation_minimum = _parse_validation_minimum(
            d.pop("validation_minimum", UNSET)
        )

        def _parse_validation_maximum(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        validation_maximum = _parse_validation_maximum(
            d.pop("validation_maximum", UNSET)
        )

        validation_regex = d.pop("validation_regex", UNSET)

        def _parse_choice_set(
            data: object,
        ) -> Union["BriefCustomFieldChoiceSet", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                choice_set_type_1 = BriefCustomFieldChoiceSet.from_dict(data)

                return choice_set_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCustomFieldChoiceSet", None, Unset], data)

        choice_set = _parse_choice_set(d.pop("choice_set", UNSET))

        comments = d.pop("comments", UNSET)

        custom_field = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            object_types=object_types,
            type_=type_,
            data_type=data_type,
            name=name,
            created=created,
            last_updated=last_updated,
            related_object_type=related_object_type,
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

        custom_field.additional_properties = d
        return custom_field

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
