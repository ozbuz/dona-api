from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Key")


@_attrs_define
class Key:
    """Never a secret: no field of any GET matches `dona_(sk|ak|it)_live_` beyond `prefix`.

    Attributes:
        id (UUID):
        name (str):
        kind (str): `sk` seller integration · `ak` AI agent (MCP) · `it` vendor install (S6). Known values (open set —
            tolerate new ones): `sk`, `ak`, `it`.
        env (str): Known values (open set — tolerate new ones): `live`.
        prefix (str):
        last4 (str):
        scopes (list[str]):
        state (str): Known values (open set — tolerate new ones): `active`, `suspended`, `revoked`, `expired`.
        expiring_soon (bool): True in the last 30 days (the first `key_expiring` step).
        expires_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        last_used_at (datetime.datetime | None):
        ip_allow (list[str]):
        rotated_from (None | UUID):
        overlap_until (datetime.datetime | None):
        suspended_until (datetime.datetime | None):
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    name: str
    kind: str
    env: str
    prefix: str
    last4: str
    scopes: list[str]
    state: str
    expiring_soon: bool
    expires_at: datetime.datetime
    last_used_at: datetime.datetime | None
    ip_allow: list[str]
    rotated_from: None | UUID
    overlap_until: datetime.datetime | None
    suspended_until: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind = self.kind

        env = self.env

        prefix = self.prefix

        last4 = self.last4

        scopes = self.scopes

        state = self.state

        expiring_soon = self.expiring_soon

        expires_at = self.expires_at.isoformat()

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        ip_allow = self.ip_allow

        rotated_from: None | str
        if isinstance(self.rotated_from, UUID):
            rotated_from = str(self.rotated_from)
        else:
            rotated_from = self.rotated_from

        overlap_until: None | str
        if isinstance(self.overlap_until, datetime.datetime):
            overlap_until = self.overlap_until.isoformat()
        else:
            overlap_until = self.overlap_until

        suspended_until: None | str
        if isinstance(self.suspended_until, datetime.datetime):
            suspended_until = self.suspended_until.isoformat()
        else:
            suspended_until = self.suspended_until

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "env": env,
                "prefix": prefix,
                "last4": last4,
                "scopes": scopes,
                "state": state,
                "expiring_soon": expiring_soon,
                "expires_at": expires_at,
                "last_used_at": last_used_at,
                "ip_allow": ip_allow,
                "rotated_from": rotated_from,
                "overlap_until": overlap_until,
                "suspended_until": suspended_until,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = d.pop("kind")

        env = d.pop("env")

        prefix = d.pop("prefix")

        last4 = d.pop("last4")

        scopes = cast(list[str], d.pop("scopes"))

        state = d.pop("state")

        expiring_soon = d.pop("expiring_soon")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        ip_allow = cast(list[str], d.pop("ip_allow"))

        def _parse_rotated_from(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rotated_from_type_0 = UUID(data)

                return rotated_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        rotated_from = _parse_rotated_from(d.pop("rotated_from"))

        def _parse_overlap_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                overlap_until_type_0 = datetime.datetime.fromisoformat(data)

                return overlap_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        overlap_until = _parse_overlap_until(d.pop("overlap_until"))

        def _parse_suspended_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_until_type_0 = datetime.datetime.fromisoformat(data)

                return suspended_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        suspended_until = _parse_suspended_until(d.pop("suspended_until"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        key = cls(
            id=id,
            name=name,
            kind=kind,
            env=env,
            prefix=prefix,
            last4=last4,
            scopes=scopes,
            state=state,
            expiring_soon=expiring_soon,
            expires_at=expires_at,
            last_used_at=last_used_at,
            ip_allow=ip_allow,
            rotated_from=rotated_from,
            overlap_until=overlap_until,
            suspended_until=suspended_until,
            created_at=created_at,
        )

        key.additional_properties = d
        return key

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
