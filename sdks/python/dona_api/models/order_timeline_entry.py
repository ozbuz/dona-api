from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderTimelineEntry")


@_attrs_define
class OrderTimelineEntry:
    """
    Attributes:
        id (UUID):
        type_ (str): `placed`, `paid`, `accepted`, `declined`, `shipped`, `delivered`, `cancelled`, `line_cancelled`, …
        actor (str): `system`, `seller`, `buyer`, `courier`, `support`
        note (None | str): Dona/staff-authored only; buyer text never appears here.
        occurred_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    type_: str
    actor: str
    note: None | str
    occurred_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        actor = self.actor

        note: None | str
        note = self.note

        occurred_at = self.occurred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "actor": actor,
                "note": note,
                "occurred_at": occurred_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        actor = d.pop("actor")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        order_timeline_entry = cls(
            id=id,
            type_=type_,
            actor=actor,
            note=note,
            occurred_at=occurred_at,
        )

        order_timeline_entry.additional_properties = d
        return order_timeline_entry

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
