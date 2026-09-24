from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.health_summary_suppression_type_0 import HealthSummarySuppressionType0
    from ..models.metric import Metric


T = TypeVar("T", bound="HealthSummary")


@_attrs_define
class HealthSummary:
    """Projection of `accounthealth.BuildSummary` (extracted in S0 from the portal `summary` handler; the portal JSON stays
    byte-identical).

        Attributes:
            health_label (str): Known values (open set — tolerate new ones): `good`, `fair`, `poor`.
            reputation_score (float | None):
            penalty_points (int):
            penalty_max (int):
            punishment_active (bool):
            suppression (HealthSummarySuppressionType0 | None):
            metrics (list[Metric]):
            open_attention (int):
            computed_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    health_label: str
    reputation_score: float | None
    penalty_points: int
    penalty_max: int
    punishment_active: bool
    suppression: HealthSummarySuppressionType0 | None
    metrics: list[Metric]
    open_attention: int
    computed_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.health_summary_suppression_type_0 import HealthSummarySuppressionType0  # noqa: PLC0415

        health_label = self.health_label

        reputation_score: float | None
        reputation_score = self.reputation_score

        penalty_points = self.penalty_points

        penalty_max = self.penalty_max

        punishment_active = self.punishment_active

        suppression: dict[str, Any] | None
        if isinstance(self.suppression, HealthSummarySuppressionType0):
            suppression = self.suppression.to_dict()
        else:
            suppression = self.suppression

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        open_attention = self.open_attention

        computed_at = self.computed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "health_label": health_label,
                "reputation_score": reputation_score,
                "penalty_points": penalty_points,
                "penalty_max": penalty_max,
                "punishment_active": punishment_active,
                "suppression": suppression,
                "metrics": metrics,
                "open_attention": open_attention,
                "computed_at": computed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.health_summary_suppression_type_0 import HealthSummarySuppressionType0  # noqa: PLC0415
        from ..models.metric import Metric  # noqa: PLC0415

        d = dict(src_dict)
        health_label = d.pop("health_label")

        def _parse_reputation_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        reputation_score = _parse_reputation_score(d.pop("reputation_score"))

        penalty_points = d.pop("penalty_points")

        penalty_max = d.pop("penalty_max")

        punishment_active = d.pop("punishment_active")

        def _parse_suppression(data: object) -> HealthSummarySuppressionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                suppression_type_0 = HealthSummarySuppressionType0.from_dict(data)

                return suppression_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HealthSummarySuppressionType0 | None, data)

        suppression = _parse_suppression(d.pop("suppression"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = Metric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        open_attention = d.pop("open_attention")

        computed_at = datetime.datetime.fromisoformat(d.pop("computed_at"))

        health_summary = cls(
            health_label=health_label,
            reputation_score=reputation_score,
            penalty_points=penalty_points,
            penalty_max=penalty_max,
            punishment_active=punishment_active,
            suppression=suppression,
            metrics=metrics,
            open_attention=open_attention,
            computed_at=computed_at,
        )

        health_summary.additional_properties = d
        return health_summary

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
