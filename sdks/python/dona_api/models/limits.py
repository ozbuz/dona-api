from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.limits_remaining import LimitsRemaining


T = TypeVar("T", bound="Limits")


@_attrs_define
class Limits:
    """
    Attributes:
        requests_per_min (int):
        burst (int):
        requests_per_day (int):
        writes_per_min (int):
        writes_per_day (int):
        in_flight (int):
        seller_requests_per_min (int):
        remaining (LimitsRemaining): Snapshot at response time.
    """

    requests_per_min: int
    burst: int
    requests_per_day: int
    writes_per_min: int
    writes_per_day: int
    in_flight: int
    seller_requests_per_min: int
    remaining: LimitsRemaining
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests_per_min = self.requests_per_min

        burst = self.burst

        requests_per_day = self.requests_per_day

        writes_per_min = self.writes_per_min

        writes_per_day = self.writes_per_day

        in_flight = self.in_flight

        seller_requests_per_min = self.seller_requests_per_min

        remaining = self.remaining.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests_per_min": requests_per_min,
                "burst": burst,
                "requests_per_day": requests_per_day,
                "writes_per_min": writes_per_min,
                "writes_per_day": writes_per_day,
                "in_flight": in_flight,
                "seller_requests_per_min": seller_requests_per_min,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limits_remaining import LimitsRemaining  # noqa: PLC0415

        d = dict(src_dict)
        requests_per_min = d.pop("requests_per_min")

        burst = d.pop("burst")

        requests_per_day = d.pop("requests_per_day")

        writes_per_min = d.pop("writes_per_min")

        writes_per_day = d.pop("writes_per_day")

        in_flight = d.pop("in_flight")

        seller_requests_per_min = d.pop("seller_requests_per_min")

        remaining = LimitsRemaining.from_dict(d.pop("remaining"))

        limits = cls(
            requests_per_min=requests_per_min,
            burst=burst,
            requests_per_day=requests_per_day,
            writes_per_min=writes_per_min,
            writes_per_day=writes_per_day,
            in_flight=in_flight,
            seller_requests_per_min=seller_requests_per_min,
            remaining=remaining,
        )

        limits.additional_properties = d
        return limits

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
