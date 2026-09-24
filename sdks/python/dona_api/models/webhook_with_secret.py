from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookWithSecret")


@_attrs_define
class WebhookWithSecret:
    """
    Attributes:
        id (UUID):
        url (str):
        event_types (list[str]): Exact event names or prefixes (`order.*`); `["*"]` (or omitted on create) = every
            event.
        status (str): Known values (open set — tolerate new ones): `active`, `paused`, `disabled`.
        failing_since (datetime.datetime | None):
        disabled_reason (None | str): Known values (open set — tolerate new ones): `ladder_exhausted`, `success_rate`,
            `owner`, `staff`, `ssrf_recheck`.
        consecutive_failures (int):
        last_delivered_at (datetime.datetime | None):
        success_rate_24h (float | None):
        secret_rotating_until (datetime.datetime | None): While set, deliveries carry two signatures.
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        secret (None | str): `whsec_…` — shown ONCE. An idempotent replay of this call returns `null`: the secret is
            never stored in the replay table.
    """

    id: UUID
    url: str
    event_types: list[str]
    status: str
    failing_since: datetime.datetime | None
    disabled_reason: None | str
    consecutive_failures: int
    last_delivered_at: datetime.datetime | None
    success_rate_24h: float | None
    secret_rotating_until: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    secret: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        url = self.url

        event_types = self.event_types

        status = self.status

        failing_since: None | str
        if isinstance(self.failing_since, datetime.datetime):
            failing_since = self.failing_since.isoformat()
        else:
            failing_since = self.failing_since

        disabled_reason: None | str
        disabled_reason = self.disabled_reason

        consecutive_failures = self.consecutive_failures

        last_delivered_at: None | str
        if isinstance(self.last_delivered_at, datetime.datetime):
            last_delivered_at = self.last_delivered_at.isoformat()
        else:
            last_delivered_at = self.last_delivered_at

        success_rate_24h: float | None
        success_rate_24h = self.success_rate_24h

        secret_rotating_until: None | str
        if isinstance(self.secret_rotating_until, datetime.datetime):
            secret_rotating_until = self.secret_rotating_until.isoformat()
        else:
            secret_rotating_until = self.secret_rotating_until

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        secret: None | str
        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "event_types": event_types,
                "status": status,
                "failing_since": failing_since,
                "disabled_reason": disabled_reason,
                "consecutive_failures": consecutive_failures,
                "last_delivered_at": last_delivered_at,
                "success_rate_24h": success_rate_24h,
                "secret_rotating_until": secret_rotating_until,
                "created_at": created_at,
                "updated_at": updated_at,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        url = d.pop("url")

        event_types = cast(list[str], d.pop("event_types"))

        status = d.pop("status")

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

        def _parse_disabled_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason"))

        consecutive_failures = d.pop("consecutive_failures")

        def _parse_last_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_delivered_at = _parse_last_delivered_at(d.pop("last_delivered_at"))

        def _parse_success_rate_24h(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        success_rate_24h = _parse_success_rate_24h(d.pop("success_rate_24h"))

        def _parse_secret_rotating_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secret_rotating_until_type_0 = datetime.datetime.fromisoformat(data)

                return secret_rotating_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        secret_rotating_until = _parse_secret_rotating_until(d.pop("secret_rotating_until"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_secret(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        secret = _parse_secret(d.pop("secret"))

        webhook_with_secret = cls(
            id=id,
            url=url,
            event_types=event_types,
            status=status,
            failing_since=failing_since,
            disabled_reason=disabled_reason,
            consecutive_failures=consecutive_failures,
            last_delivered_at=last_delivered_at,
            success_rate_24h=success_rate_24h,
            secret_rotating_until=secret_rotating_until,
            created_at=created_at,
            updated_at=updated_at,
            secret=secret,
        )

        webhook_with_secret.additional_properties = d
        return webhook_with_secret

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
