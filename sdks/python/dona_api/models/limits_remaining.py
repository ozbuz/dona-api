from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LimitsRemaining")


@_attrs_define
class LimitsRemaining:
    """Snapshot at response time.

    Attributes:
        requests_per_min (int | Unset):
        requests_per_day (int | Unset):
        writes_per_min (int | Unset):
        writes_per_day (int | Unset):
    """

    requests_per_min: int | Unset = UNSET
    requests_per_day: int | Unset = UNSET
    writes_per_min: int | Unset = UNSET
    writes_per_day: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests_per_min = self.requests_per_min

        requests_per_day = self.requests_per_day

        writes_per_min = self.writes_per_min

        writes_per_day = self.writes_per_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requests_per_min is not UNSET:
            field_dict["requests_per_min"] = requests_per_min
        if requests_per_day is not UNSET:
            field_dict["requests_per_day"] = requests_per_day
        if writes_per_min is not UNSET:
            field_dict["writes_per_min"] = writes_per_min
        if writes_per_day is not UNSET:
            field_dict["writes_per_day"] = writes_per_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests_per_min = d.pop("requests_per_min", UNSET)

        requests_per_day = d.pop("requests_per_day", UNSET)

        writes_per_min = d.pop("writes_per_min", UNSET)

        writes_per_day = d.pop("writes_per_day", UNSET)

        limits_remaining = cls(
            requests_per_min=requests_per_min,
            requests_per_day=requests_per_day,
            writes_per_min=writes_per_min,
            writes_per_day=writes_per_day,
        )

        limits_remaining.additional_properties = d
        return limits_remaining

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
