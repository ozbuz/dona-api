from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail
    from ..models.error_meta import ErrorMeta


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """The estate `{"error":"<code>"}` envelope (`internal/platform/web/respond.go` `WriteErrorWith`) plus the Dona API
    fields. Provider/DB detail never leaves; it goes to the redacted error copy.

        Attributes:
            error (str): Stable code (glossary / docs/error-codes.md). Clients branch on this, never on `message`.
            message (str): Localised by `Accept-Language` (uz default).
            request_id (str):
            details (list[ErrorDetail]): Always present; `[]` when there is nothing field-level.
            doc_url (str): Anchor into the docs for this code: `https://dona.uz/<lang>/developers/errors#<code>` — `<lang>`
                is the key owner's language (uz | ru | en) when a key authenticated the request, else `Accept-Language`, else
                `uz`. The docs site is per language; there is no language-less `/developers` page.
            retry_after_seconds (int | Unset): Mirrors `Retry-After` on 429/503/`key_suspended`.
            required_scope (str | Unset): The 14 issuable scopes (glossary). `returns:write` is reserved and unissued. Known
                values (open set — tolerate new ones): `catalog:read`, `catalog:stock`, `catalog:write`, `orders:read`,
                `orders:write`, `orders:cancel`, `orders:pii`, `returns:read`, `health:read`, `attention:read`, `events:read`,
                `webhooks:manage`, `finance:read`, `mcp`.
            rotate_url (str | Unset): On `401 api_key_expired`: the portal page to mint a successor.
            suspended_until (datetime.datetime | Unset): On `403 key_suspended`.
            reason (str | Unset): On `403 key_suspended` / `403 api_blocked`: why (`error_storm`, `unauthorized_storm`,
                `ip_blocked`, `credential_stuffing`, `leak_reported`, `staff`).
            meta (ErrorMeta | Unset): Code-specific facts, e.g. `oldest_event_id` with `cursor_expired`.
    """

    error: str
    message: str
    request_id: str
    details: list[ErrorDetail]
    doc_url: str
    retry_after_seconds: int | Unset = UNSET
    required_scope: str | Unset = UNSET
    rotate_url: str | Unset = UNSET
    suspended_until: datetime.datetime | Unset = UNSET
    reason: str | Unset = UNSET
    meta: ErrorMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        request_id = self.request_id

        details = []
        for details_item_data in self.details:
            details_item = details_item_data.to_dict()
            details.append(details_item)

        doc_url = self.doc_url

        retry_after_seconds = self.retry_after_seconds

        required_scope = self.required_scope

        rotate_url = self.rotate_url

        suspended_until: str | Unset = UNSET
        if not isinstance(self.suspended_until, Unset):
            suspended_until = self.suspended_until.isoformat()

        reason = self.reason

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "request_id": request_id,
                "details": details,
                "doc_url": doc_url,
            }
        )
        if retry_after_seconds is not UNSET:
            field_dict["retry_after_seconds"] = retry_after_seconds
        if required_scope is not UNSET:
            field_dict["required_scope"] = required_scope
        if rotate_url is not UNSET:
            field_dict["rotate_url"] = rotate_url
        if suspended_until is not UNSET:
            field_dict["suspended_until"] = suspended_until
        if reason is not UNSET:
            field_dict["reason"] = reason
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_detail import ErrorDetail  # noqa: PLC0415
        from ..models.error_meta import ErrorMeta  # noqa: PLC0415

        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        request_id = d.pop("request_id")

        details = []
        _details = d.pop("details")
        for details_item_data in _details:
            details_item = ErrorDetail.from_dict(details_item_data)

            details.append(details_item)

        doc_url = d.pop("doc_url")

        retry_after_seconds = d.pop("retry_after_seconds", UNSET)

        required_scope = d.pop("required_scope", UNSET)

        rotate_url = d.pop("rotate_url", UNSET)

        _suspended_until = d.pop("suspended_until", UNSET)
        suspended_until: datetime.datetime | Unset
        if isinstance(_suspended_until, Unset):
            suspended_until = UNSET
        else:
            suspended_until = datetime.datetime.fromisoformat(_suspended_until)

        reason = d.pop("reason", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: ErrorMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ErrorMeta.from_dict(_meta)

        error = cls(
            error=error,
            message=message,
            request_id=request_id,
            details=details,
            doc_url=doc_url,
            retry_after_seconds=retry_after_seconds,
            required_scope=required_scope,
            rotate_url=rotate_url,
            suspended_until=suspended_until,
            reason=reason,
            meta=meta,
        )

        error.additional_properties = d
        return error

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
