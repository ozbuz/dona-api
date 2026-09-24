from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_data import EventData
    from ..models.event_links import EventLinks


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (UUID): uuidv7 — also the `/events` cursor and the webhook `webhook-id`.
        type_ (str): The glossary event catalogue. New types are additive. Known values (open set — tolerate new ones):
            `order.created`, `order.paid`, `order.accepted`, `order.declined`, `order.ready`, `order.shipped`,
            `order.delivered`, `order.cancelled`, `order.line_cancelled`, `order.accept_due_soon`, `order.ship_overdue`,
            `return.requested`, `return.status_changed`, `product.published`, `product.held`, `product.rejected`,
            `product.demoted`, `product.violation`, `product.deleted`, `stock.low`, `stock.out`, `write.held`,
            `write.approved`, `write.rejected`, `write.expired`, `account.status_changed`, `account.documents_decided`,
            `account.kyc_reopened`, `account.suppressed`, `account.health_changed`, `account.agreement_owed`,
            `live.access_changed`, `live.strike`, `attention.opened`, `attention.resolved`, `key.expiring`, `key.suspended`,
            `key.unsuspended`, `webhook.failing`, `webhook.disabled`, `ping`.
        occurred_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        seller_id (UUID):
        api_version (Literal['v1']):
        data (EventData): Thin payload per `type` (ids + new state, never PII) — see the top-level `webhooks` for each
            shape.
        links (EventLinks):
    """

    id: UUID
    type_: str
    occurred_at: datetime.datetime
    seller_id: UUID
    api_version: Literal["v1"]
    data: EventData
    links: EventLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        occurred_at = self.occurred_at.isoformat()

        seller_id = str(self.seller_id)

        api_version = self.api_version

        data = self.data.to_dict()

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "occurred_at": occurred_at,
                "seller_id": seller_id,
                "api_version": api_version,
                "data": data,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_data import EventData  # noqa: PLC0415
        from ..models.event_links import EventLinks  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        seller_id = UUID(d.pop("seller_id"))

        api_version = cast(Literal["v1"], d.pop("api_version"))
        if api_version != "v1":
            raise ValueError(f"api_version must match const 'v1', got '{api_version}'")

        data = EventData.from_dict(d.pop("data"))

        links = EventLinks.from_dict(d.pop("links"))

        event = cls(
            id=id,
            type_=type_,
            occurred_at=occurred_at,
            seller_id=seller_id,
            api_version=api_version,
            data=data,
            links=links,
        )

        event.additional_properties = d
        return event

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
