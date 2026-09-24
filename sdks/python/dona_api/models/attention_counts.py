from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attention_counts_by_severity import AttentionCountsBySeverity


T = TypeVar("T", bound="AttentionCounts")


@_attrs_define
class AttentionCounts:
    """
    Attributes:
        open_ (int):
        action_required (int):
        by_severity (AttentionCountsBySeverity):
    """

    open_: int
    action_required: int
    by_severity: AttentionCountsBySeverity
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        action_required = self.action_required

        by_severity = self.by_severity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "action_required": action_required,
                "by_severity": by_severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attention_counts_by_severity import AttentionCountsBySeverity  # noqa: PLC0415

        d = dict(src_dict)
        open_ = d.pop("open")

        action_required = d.pop("action_required")

        by_severity = AttentionCountsBySeverity.from_dict(d.pop("by_severity"))

        attention_counts = cls(
            open_=open_,
            action_required=action_required,
            by_severity=by_severity,
        )

        attention_counts.additional_properties = d
        return attention_counts

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
