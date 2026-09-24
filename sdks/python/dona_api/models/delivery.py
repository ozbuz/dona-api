from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Delivery")


@_attrs_define
class Delivery:
    """
    Attributes:
        id (UUID):
        webhook_id (UUID):
        event_id (UUID):
        event_type (str): The glossary event catalogue. New types are additive. Known values (open set — tolerate new
            ones): `order.created`, `order.paid`, `order.accepted`, `order.declined`, `order.ready`, `order.shipped`,
            `order.delivered`, `order.cancelled`, `order.line_cancelled`, `order.accept_due_soon`, `order.ship_overdue`,
            `return.requested`, `return.status_changed`, `product.published`, `product.held`, `product.rejected`,
            `product.demoted`, `product.violation`, `product.deleted`, `stock.low`, `stock.out`, `write.held`,
            `write.approved`, `write.rejected`, `write.expired`, `account.status_changed`, `account.documents_decided`,
            `account.kyc_reopened`, `account.suppressed`, `account.health_changed`, `account.agreement_owed`,
            `live.access_changed`, `live.strike`, `attention.opened`, `attention.resolved`, `key.expiring`, `key.suspended`,
            `key.unsuspended`, `webhook.failing`, `webhook.disabled`, `ping`.
        attempt (int):
        status (str): Known values (open set — tolerate new ones): `queued`, `delivered`, `failed`, `dead`.
        next_attempt_at (datetime.datetime | None):
        delivered_at (datetime.datetime | None):
        response_status (int | None):
        response_ms (int | None):
        error (None | str):
        occurred_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    webhook_id: UUID
    event_id: UUID
    event_type: str
    attempt: int
    status: str
    next_attempt_at: datetime.datetime | None
    delivered_at: datetime.datetime | None
    response_status: int | None
    response_ms: int | None
    error: None | str
    occurred_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        webhook_id = str(self.webhook_id)

        event_id = str(self.event_id)

        event_type = self.event_type

        attempt = self.attempt

        status = self.status

        next_attempt_at: None | str
        if isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        delivered_at: None | str
        if isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        response_status: int | None
        response_status = self.response_status

        response_ms: int | None
        response_ms = self.response_ms

        error: None | str
        error = self.error

        occurred_at = self.occurred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "webhook_id": webhook_id,
                "event_id": event_id,
                "event_type": event_type,
                "attempt": attempt,
                "status": status,
                "next_attempt_at": next_attempt_at,
                "delivered_at": delivered_at,
                "response_status": response_status,
                "response_ms": response_ms,
                "error": error,
                "occurred_at": occurred_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        webhook_id = UUID(d.pop("webhook_id"))

        event_id = UUID(d.pop("event_id"))

        event_type = d.pop("event_type")

        attempt = d.pop("attempt")

        status = d.pop("status")

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        def _parse_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("response_status"))

        def _parse_response_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_ms = _parse_response_ms(d.pop("response_ms"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        delivery = cls(
            id=id,
            webhook_id=webhook_id,
            event_id=event_id,
            event_type=event_type,
            attempt=attempt,
            status=status,
            next_attempt_at=next_attempt_at,
            delivered_at=delivered_at,
            response_status=response_status,
            response_ms=response_ms,
            error=error,
            occurred_at=occurred_at,
        )

        delivery.additional_properties = d
        return delivery

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
