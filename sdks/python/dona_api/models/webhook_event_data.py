from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookEventData")


@_attrs_define
class WebhookEventData:
    """
    Attributes:
        webhook_id (UUID):
        failing_since (datetime.datetime | None):
        attempts (int):
        last_status (int | None):
    """

    webhook_id: UUID
    failing_since: datetime.datetime | None
    attempts: int
    last_status: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_id = str(self.webhook_id)

        failing_since: None | str
        if isinstance(self.failing_since, datetime.datetime):
            failing_since = self.failing_since.isoformat()
        else:
            failing_since = self.failing_since

        attempts = self.attempts

        last_status: int | None
        last_status = self.last_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook_id": webhook_id,
                "failing_since": failing_since,
                "attempts": attempts,
                "last_status": last_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_id = UUID(d.pop("webhook_id"))

        def _parse_failing_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failing_since_type_0 = datetime.datetime.fromisoformat(data)

                return failing_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        failing_since = _parse_failing_since(d.pop("failing_since"))

        attempts = d.pop("attempts")

        def _parse_last_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        last_status = _parse_last_status(d.pop("last_status"))

        webhook_event_data = cls(
            webhook_id=webhook_id,
            failing_since=failing_since,
            attempts=attempts,
            last_status=last_status,
        )

        webhook_event_data.additional_properties = d
        return webhook_event_data

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
