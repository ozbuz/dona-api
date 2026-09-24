from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyEventData")


@_attrs_define
class KeyEventData:
    """Never the secret.

    Attributes:
        key_id (UUID):
        prefix (str):
        expires_at (datetime.datetime | None | Unset):
        suspended_until (datetime.datetime | None | Unset):
        reason_code (None | str | Unset): `key.suspended` only: the suspension's code (`error_storm`, `ip_blocked`,
            `staff`, …) — never the words staff typed (an internal note); null for anything outside the vocabulary.
    """

    key_id: UUID
    prefix: str
    expires_at: datetime.datetime | None | Unset = UNSET
    suspended_until: datetime.datetime | None | Unset = UNSET
    reason_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = str(self.key_id)

        prefix = self.prefix

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        suspended_until: None | str | Unset
        if isinstance(self.suspended_until, Unset):
            suspended_until = UNSET
        elif isinstance(self.suspended_until, datetime.datetime):
            suspended_until = self.suspended_until.isoformat()
        else:
            suspended_until = self.suspended_until

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "prefix": prefix,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if suspended_until is not UNSET:
            field_dict["suspended_until"] = suspended_until
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = UUID(d.pop("key_id"))

        prefix = d.pop("prefix")

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_suspended_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_until_type_0 = datetime.datetime.fromisoformat(data)

                return suspended_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        suspended_until = _parse_suspended_until(d.pop("suspended_until", UNSET))

        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reason_code", UNSET))

        key_event_data = cls(
            key_id=key_id,
            prefix=prefix,
            expires_at=expires_at,
            suspended_until=suspended_until,
            reason_code=reason_code,
        )

        key_event_data.additional_properties = d
        return key_event_data

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
