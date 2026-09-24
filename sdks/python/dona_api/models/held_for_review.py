from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.held_for_review_subject import HeldForReviewSubject


T = TypeVar("T", bound="HeldForReview")


@_attrs_define
class HeldForReview:
    """`202` success envelope — `error` is ABSENT. Nothing was written. A replay of the same `Idempotency-Key` re-derives
    from the held row (approved ⇒ the applied outcome · rejected ⇒ 409 · pending ⇒ this 202 again) — never a second
    hold.

        Attributes:
            code (Literal['held_for_review']):
            status (Literal['held']):
            approval_id (UUID): `seller_api_held_writes.id` — follow `write.approved|rejected|expired` events.
            rule (str): Known values (open set — tolerate new ones): `price_floor`, `drop_100x`, `stock_jump_10x`,
                `mass_zero_50pct`, `delist_30pct`, `confirmation_required`.
            kind (str): Known values (open set — tolerate new ones): `price`, `stock`, `product`, `delist`.
            subject (HeldForReviewSubject):
            approver (str): `owner` when the value effect ≤ `owner_approval_max_uzs` (D18) and no repeat/suspension/health
                rule applies; else `staff` (`api.approve`). Known values (open set — tolerate new ones): `owner`, `staff`.
            expires_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
            message (str):
            request_id (str):
    """

    code: Literal["held_for_review"]
    status: Literal["held"]
    approval_id: UUID
    rule: str
    kind: str
    subject: HeldForReviewSubject
    approver: str
    expires_at: datetime.datetime
    message: str
    request_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        approval_id = str(self.approval_id)

        rule = self.rule

        kind = self.kind

        subject = self.subject.to_dict()

        approver = self.approver

        expires_at = self.expires_at.isoformat()

        message = self.message

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "approval_id": approval_id,
                "rule": rule,
                "kind": kind,
                "subject": subject,
                "approver": approver,
                "expires_at": expires_at,
                "message": message,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.held_for_review_subject import HeldForReviewSubject  # noqa: PLC0415

        d = dict(src_dict)
        code = cast(Literal["held_for_review"], d.pop("code"))
        if code != "held_for_review":
            raise ValueError(f"code must match const 'held_for_review', got '{code}'")

        status = cast(Literal["held"], d.pop("status"))
        if status != "held":
            raise ValueError(f"status must match const 'held', got '{status}'")

        approval_id = UUID(d.pop("approval_id"))

        rule = d.pop("rule")

        kind = d.pop("kind")

        subject = HeldForReviewSubject.from_dict(d.pop("subject"))

        approver = d.pop("approver")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        message = d.pop("message")

        request_id = d.pop("request_id")

        held_for_review = cls(
            code=code,
            status=status,
            approval_id=approval_id,
            rule=rule,
            kind=kind,
            subject=subject,
            approver=approver,
            expires_at=expires_at,
            message=message,
            request_id=request_id,
        )

        held_for_review.additional_properties = d
        return held_for_review

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
