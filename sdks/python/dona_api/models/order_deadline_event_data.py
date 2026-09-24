from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderDeadlineEventData")


@_attrs_define
class OrderDeadlineEventData:
    """
    Attributes:
        order_id (UUID):
        deadline_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        overdue_by_seconds (int | None | Unset):
    """

    order_id: UUID
    deadline_at: datetime.datetime
    overdue_by_seconds: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = str(self.order_id)

        deadline_at = self.deadline_at.isoformat()

        overdue_by_seconds: int | None | Unset
        if isinstance(self.overdue_by_seconds, Unset):
            overdue_by_seconds = UNSET
        else:
            overdue_by_seconds = self.overdue_by_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "deadline_at": deadline_at,
            }
        )
        if overdue_by_seconds is not UNSET:
            field_dict["overdue_by_seconds"] = overdue_by_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = UUID(d.pop("order_id"))

        deadline_at = datetime.datetime.fromisoformat(d.pop("deadline_at"))

        def _parse_overdue_by_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overdue_by_seconds = _parse_overdue_by_seconds(d.pop("overdue_by_seconds", UNSET))

        order_deadline_event_data = cls(
            order_id=order_id,
            deadline_at=deadline_at,
            overdue_by_seconds=overdue_by_seconds,
        )

        order_deadline_event_data.additional_properties = d
        return order_deadline_event_data

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
