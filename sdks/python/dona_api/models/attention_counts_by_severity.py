from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttentionCountsBySeverity")


@_attrs_define
class AttentionCountsBySeverity:
    """
    Attributes:
        low (int):
        medium (int):
        high (int):
        critical (int):
    """

    low: int
    medium: int
    high: int
    critical: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low = self.low

        medium = self.medium

        high = self.high

        critical = self.critical

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "low": low,
                "medium": medium,
                "high": high,
                "critical": critical,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low = d.pop("low")

        medium = d.pop("medium")

        high = d.pop("high")

        critical = d.pop("critical")

        attention_counts_by_severity = cls(
            low=low,
            medium=medium,
            high=high,
            critical=critical,
        )

        attention_counts_by_severity.additional_properties = d
        return attention_counts_by_severity

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
