from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorDetail")


@_attrs_define
class ErrorDetail:
    """
    Attributes:
        code (str): Stable field-level code, e.g. `required`, `ikpu_required`, `cursor_expired`, `stock_locked`.
        message (str): Localised by `Accept-Language`.
        index (int | Unset): Line index in a bulk body.
        field (str | Unset): Field or header name.
        locked_until (datetime.datetime | Unset): With `code: stock_locked` — the line of an atomic `POST /stock` that
            the 24-hour out-of-stock lock refused: when that lock ends (the same wire shape as `Error.locked_until`).
    """

    code: str
    message: str
    index: int | Unset = UNSET
    field: str | Unset = UNSET
    locked_until: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        index = self.index

        field = self.field

        locked_until: str | Unset = UNSET
        if not isinstance(self.locked_until, Unset):
            locked_until = self.locked_until.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if index is not UNSET:
            field_dict["index"] = index
        if field is not UNSET:
            field_dict["field"] = field
        if locked_until is not UNSET:
            field_dict["locked_until"] = locked_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        index = d.pop("index", UNSET)

        field = d.pop("field", UNSET)

        _locked_until = d.pop("locked_until", UNSET)
        locked_until: datetime.datetime | Unset
        if isinstance(_locked_until, Unset):
            locked_until = UNSET
        else:
            locked_until = datetime.datetime.fromisoformat(_locked_until)

        error_detail = cls(
            code=code,
            message=message,
            index=index,
            field=field,
            locked_until=locked_until,
        )

        error_detail.additional_properties = d
        return error_detail

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
