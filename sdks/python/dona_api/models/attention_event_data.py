from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attention_event_data_subject_type_0 import AttentionEventDataSubjectType0


T = TypeVar("T", bound="AttentionEventData")


@_attrs_define
class AttentionEventData:
    """
    Attributes:
        attention_id (UUID):
        kind (str): Known values (open set — tolerate new ones): `documents_pending`, `documents_rejected`,
            `kyc_reopened`, `bank_pending`, `agreement_owed`, `shop_suspended`, `shop_restricted`, `shop_blocked`,
            `suppressed`, `penalty_points`, `product_held`, `product_rejected`, `product_violation`, `listing_issue`,
            `order_accept_due`, `order_ship_overdue`, `return_decision_due`, `stock_out`, `stock_low`, `health_warning`,
            `health_suppressed`, `live_ban`, `live_strike`, `write_held`, `key_expiring`, `key_suspended`, `key_dormant`,
            `ip_blocked`, `webhook_failing`, `api_anomaly`.
        severity (str): Known values (open set — tolerate new ones): `low`, `medium`, `high`, `critical`.
        action_required (bool):
        subject (AttentionEventDataSubjectType0 | None):
        deadline_at (datetime.datetime | None | Unset):
    """

    attention_id: UUID
    kind: str
    severity: str
    action_required: bool
    subject: AttentionEventDataSubjectType0 | None
    deadline_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attention_event_data_subject_type_0 import AttentionEventDataSubjectType0  # noqa: PLC0415

        attention_id = str(self.attention_id)

        kind = self.kind

        severity = self.severity

        action_required = self.action_required

        subject: dict[str, Any] | None
        if isinstance(self.subject, AttentionEventDataSubjectType0):
            subject = self.subject.to_dict()
        else:
            subject = self.subject

        deadline_at: None | str | Unset
        if isinstance(self.deadline_at, Unset):
            deadline_at = UNSET
        elif isinstance(self.deadline_at, datetime.datetime):
            deadline_at = self.deadline_at.isoformat()
        else:
            deadline_at = self.deadline_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attention_id": attention_id,
                "kind": kind,
                "severity": severity,
                "action_required": action_required,
                "subject": subject,
            }
        )
        if deadline_at is not UNSET:
            field_dict["deadline_at"] = deadline_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attention_event_data_subject_type_0 import AttentionEventDataSubjectType0  # noqa: PLC0415

        d = dict(src_dict)
        attention_id = UUID(d.pop("attention_id"))

        kind = d.pop("kind")

        severity = d.pop("severity")

        action_required = d.pop("action_required")

        def _parse_subject(data: object) -> AttentionEventDataSubjectType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subject_type_0 = AttentionEventDataSubjectType0.from_dict(data)

                return subject_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttentionEventDataSubjectType0 | None, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_deadline_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deadline_at_type_0 = datetime.datetime.fromisoformat(data)

                return deadline_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deadline_at = _parse_deadline_at(d.pop("deadline_at", UNSET))

        attention_event_data = cls(
            attention_id=attention_id,
            kind=kind,
            severity=severity,
            action_required=action_required,
            subject=subject,
            deadline_at=deadline_at,
        )

        attention_event_data.additional_properties = d
        return attention_event_data

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
