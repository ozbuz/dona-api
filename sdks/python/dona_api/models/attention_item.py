from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attention_item_subject_type_0 import AttentionItemSubjectType0
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="AttentionItem")


@_attrs_define
class AttentionItem:
    """`seller_attention_items` minus `source_ref`. Text is Dona/staff-authored only; never buyer text.

    Attributes:
        id (UUID):
        kind (str): Known values (open set — tolerate new ones): `documents_pending`, `documents_rejected`,
            `kyc_reopened`, `bank_pending`, `agreement_owed`, `shop_suspended`, `shop_restricted`, `shop_blocked`,
            `suppressed`, `penalty_points`, `product_held`, `product_rejected`, `product_violation`, `listing_issue`,
            `order_accept_due`, `order_ship_overdue`, `return_decision_due`, `stock_out`, `stock_low`, `health_warning`,
            `health_suppressed`, `live_ban`, `live_strike`, `write_held`, `key_expiring`, `key_suspended`, `key_dormant`,
            `ip_blocked`, `webhook_failing`, `api_anomaly`.
        severity (str): Known values (open set — tolerate new ones): `low`, `medium`, `high`, `critical`.
        action_required (bool): True only when the SELLER can clear it.
        resolves_by (str): Known values (open set — tolerate new ones): `condition`, `decision`, `deadline`, `expiry`,
            `ack`.
        subject (AttentionItemSubjectType0 | None):
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        body (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        deadline_at (datetime.datetime | None):
        action_url (None | str): Portal deep link.
        opened_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        acked_at (datetime.datetime | None):
        acked_via (None | str): Known values (open set — tolerate new ones): `portal`, `api`, `mcp`.
        resolved_at (datetime.datetime | None):
        resolved_reason (None | str): Known values (open set — tolerate new ones): `condition_cleared`, `decided`,
            `deadline_passed`, `expired`, `acked`.
    """

    id: UUID
    kind: str
    severity: str
    action_required: bool
    resolves_by: str
    subject: AttentionItemSubjectType0 | None
    title: LocalizedText
    body: LocalizedText
    deadline_at: datetime.datetime | None
    action_url: None | str
    opened_at: datetime.datetime
    updated_at: datetime.datetime
    acked_at: datetime.datetime | None
    acked_via: None | str
    resolved_at: datetime.datetime | None
    resolved_reason: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attention_item_subject_type_0 import AttentionItemSubjectType0  # noqa: PLC0415

        id = str(self.id)

        kind = self.kind

        severity = self.severity

        action_required = self.action_required

        resolves_by = self.resolves_by

        subject: dict[str, Any] | None
        if isinstance(self.subject, AttentionItemSubjectType0):
            subject = self.subject.to_dict()
        else:
            subject = self.subject

        title = self.title.to_dict()

        body = self.body.to_dict()

        deadline_at: None | str
        if isinstance(self.deadline_at, datetime.datetime):
            deadline_at = self.deadline_at.isoformat()
        else:
            deadline_at = self.deadline_at

        action_url: None | str
        action_url = self.action_url

        opened_at = self.opened_at.isoformat()

        updated_at = self.updated_at.isoformat()

        acked_at: None | str
        if isinstance(self.acked_at, datetime.datetime):
            acked_at = self.acked_at.isoformat()
        else:
            acked_at = self.acked_at

        acked_via: None | str
        acked_via = self.acked_via

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        resolved_reason: None | str
        resolved_reason = self.resolved_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "severity": severity,
                "action_required": action_required,
                "resolves_by": resolves_by,
                "subject": subject,
                "title": title,
                "body": body,
                "deadline_at": deadline_at,
                "action_url": action_url,
                "opened_at": opened_at,
                "updated_at": updated_at,
                "acked_at": acked_at,
                "acked_via": acked_via,
                "resolved_at": resolved_at,
                "resolved_reason": resolved_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attention_item_subject_type_0 import AttentionItemSubjectType0  # noqa: PLC0415
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = d.pop("kind")

        severity = d.pop("severity")

        action_required = d.pop("action_required")

        resolves_by = d.pop("resolves_by")

        def _parse_subject(data: object) -> AttentionItemSubjectType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = AttentionItemSubjectType0.from_dict(data)

                return subject_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttentionItemSubjectType0 | None, data)

        subject = _parse_subject(d.pop("subject"))

        title = LocalizedText.from_dict(d.pop("title"))

        body = LocalizedText.from_dict(d.pop("body"))

        def _parse_deadline_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_at_type_0 = datetime.datetime.fromisoformat(data)

                return deadline_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deadline_at = _parse_deadline_at(d.pop("deadline_at"))

        def _parse_action_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        action_url = _parse_action_url(d.pop("action_url"))

        opened_at = datetime.datetime.fromisoformat(d.pop("opened_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_acked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acked_at_type_0 = datetime.datetime.fromisoformat(data)

                return acked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        acked_at = _parse_acked_at(d.pop("acked_at"))

        def _parse_acked_via(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acked_via = _parse_acked_via(d.pop("acked_via"))

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

        def _parse_resolved_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_reason = _parse_resolved_reason(d.pop("resolved_reason"))

        attention_item = cls(
            id=id,
            kind=kind,
            severity=severity,
            action_required=action_required,
            resolves_by=resolves_by,
            subject=subject,
            title=title,
            body=body,
            deadline_at=deadline_at,
            action_url=action_url,
            opened_at=opened_at,
            updated_at=updated_at,
            acked_at=acked_at,
            acked_via=acked_via,
            resolved_at=resolved_at,
            resolved_reason=resolved_reason,
        )

        attention_item.additional_properties = d
        return attention_item

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
