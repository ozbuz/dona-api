from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="StatusIncidentsItem")


@_attrs_define
class StatusIncidentsItem:
    """
    Attributes:
        id (str):
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        status (str): Known values (open set — tolerate new ones): `investigating`, `monitoring`, `resolved`.
        started_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        resolved_at (datetime.datetime | None):
    """

    id: str
    title: LocalizedText
    status: str
    started_at: datetime.datetime
    resolved_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title.to_dict()

        status = self.status

        started_at = self.started_at.isoformat()

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "status": status,
                "started_at": started_at,
                "resolved_at": resolved_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        title = LocalizedText.from_dict(d.pop("title"))

        status = d.pop("status")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))

        status_incidents_item = cls(
            id=id,
            title=title,
            status=status,
            started_at=started_at,
            resolved_at=resolved_at,
        )

        status_incidents_item.additional_properties = d
        return status_incidents_item

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
