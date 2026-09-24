from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Issue")


@_attrs_define
class Issue:
    """
    Attributes:
        id (UUID):
        source (str): Known values (open set — tolerate new ones): `listing_issue`, `violation`, `shop_hold`.
        severity (str): Known values (open set — tolerate new ones): `error`, `warning`.
        type_ (str):
        field (None | str):
        detail (None | str):
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    source: str
    severity: str
    type_: str
    field: None | str
    detail: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        source = self.source

        severity = self.severity

        type_ = self.type_

        field: None | str
        field = self.field

        detail: None | str
        detail = self.detail

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "severity": severity,
                "type": type_,
                "field": field,
                "detail": detail,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        source = d.pop("source")

        severity = d.pop("severity")

        type_ = d.pop("type")

        def _parse_field(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        field = _parse_field(d.pop("field"))

        def _parse_detail(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detail = _parse_detail(d.pop("detail"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        issue = cls(
            id=id,
            source=source,
            severity=severity,
            type_=type_,
            field=field,
            detail=detail,
            created_at=created_at,
        )

        issue.additional_properties = d
        return issue

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
