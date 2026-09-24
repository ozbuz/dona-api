from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountHealthEventData")


@_attrs_define
class AccountHealthEventData:
    """
    Attributes:
        health_label (str): Known values (open set — tolerate new ones): `good`, `fair`, `poor`.
        reputation_score (float | None):
        suppressed (bool):
    """

    health_label: str
    reputation_score: float | None
    suppressed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        health_label = self.health_label

        reputation_score: float | None
        reputation_score = self.reputation_score

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "health_label": health_label,
                "reputation_score": reputation_score,
                "suppressed": suppressed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        health_label = d.pop("health_label")

        def _parse_reputation_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        reputation_score = _parse_reputation_score(d.pop("reputation_score"))

        suppressed = d.pop("suppressed")

        account_health_event_data = cls(
            health_label=health_label,
            reputation_score=reputation_score,
            suppressed=suppressed,
        )

        account_health_event_data.additional_properties = d
        return account_health_event_data

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
