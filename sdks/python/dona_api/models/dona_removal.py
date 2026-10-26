from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="DonaRemoval")


@_attrs_define
class DonaRemoval:
    """Why Dona keeps a product off sale and what clears it (OZB architecture/DB/catalog/removed-by-dona-marker.md).
    Tolerate new values in every enum-like field.

        Attributes:
            source (str): `moderation_ban` · `ip_notice` · `staff_delist` · `staff_hide` · `ai_review`.
            by (str): `dona_team` · `dona_ai`.
            reason_code (str): `prohibited_goods` · `unsafe_product` · `adult_content` · `violence_hate` ·
                `misleading_listing` · `intellectual_property` · `duplicate_spam` · `other` · `shop_closing` · `listing_review`.
            reason (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
            title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
            note (None | str): The Dona team's explanation to the seller (a ban, a staff removal); null otherwise.
            since (datetime.datetime | None): ISO 8601 with offset (Tashkent `+05:00`); null when nothing recorded the
                start.
            state (None | str): The ban notice's state or the listing review's state; null otherwise.
            clears_by (str): `staff` · `seller`.
            action (str): `contact_support` · `dispute` · `wait` · `fix_review`.
            ref (None | UUID): The ban / review case / staff removal id; null for an IP notice.
    """

    source: str
    by: str
    reason_code: str
    reason: LocalizedText
    title: LocalizedText
    note: None | str
    since: datetime.datetime | None
    state: None | str
    clears_by: str
    action: str
    ref: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        by = self.by

        reason_code = self.reason_code

        reason = self.reason.to_dict()

        title = self.title.to_dict()

        note: None | str
        note = self.note

        since: None | str
        if isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        state: None | str
        state = self.state

        clears_by = self.clears_by

        action = self.action

        ref: None | str
        if isinstance(self.ref, UUID):
            ref = str(self.ref)
        else:
            ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "by": by,
                "reason_code": reason_code,
                "reason": reason,
                "title": title,
                "note": note,
                "since": since,
                "state": state,
                "clears_by": clears_by,
                "action": action,
                "ref": ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        source = d.pop("source")

        by = d.pop("by")

        reason_code = d.pop("reason_code")

        reason = LocalizedText.from_dict(d.pop("reason"))

        title = LocalizedText.from_dict(d.pop("title"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        def _parse_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = datetime.datetime.fromisoformat(data)

                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        since = _parse_since(d.pop("since"))

        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))

        clears_by = d.pop("clears_by")

        action = d.pop("action")

        def _parse_ref(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ref_type_0 = UUID(data)

                return ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        ref = _parse_ref(d.pop("ref"))

        dona_removal = cls(
            source=source,
            by=by,
            reason_code=reason_code,
            reason=reason,
            title=title,
            note=note,
            since=since,
            state=state,
            clears_by=clears_by,
            action=action,
            ref=ref,
        )

        dona_removal.additional_properties = d
        return dona_removal

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
