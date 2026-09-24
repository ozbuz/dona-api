from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_request_filters import ExportRequestFilters


T = TypeVar("T", bound="ExportRequest")


@_attrs_define
class ExportRequest:
    """
    Attributes:
        format_ (str | Unset): Known values (open set — tolerate new ones): `csv`, `jsonl`. Default: 'jsonl'.
        filters (ExportRequestFilters | Unset): Same meaning as the list filters; `from`/`to` only on orders (≤ 90 d).
    """

    format_: str | Unset = "jsonl"
    filters: ExportRequestFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_request_filters import ExportRequestFilters  # noqa: PLC0415

        d = dict(src_dict)
        format_ = d.pop("format", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: ExportRequestFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ExportRequestFilters.from_dict(_filters)

        export_request = cls(
            format_=format_,
            filters=filters,
        )

        export_request.additional_properties = d
        return export_request

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
