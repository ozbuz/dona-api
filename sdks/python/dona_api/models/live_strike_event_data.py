from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LiveStrikeEventData")


@_attrs_define
class LiveStrikeEventData:
    """
    Attributes:
        strike_count (int):
        expires_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    strike_count: int
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strike_count = self.strike_count

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strike_count": strike_count,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strike_count = d.pop("strike_count")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        live_strike_event_data = cls(
            strike_count=strike_count,
            expires_at=expires_at,
        )

        live_strike_event_data.additional_properties = d
        return live_strike_event_data

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
