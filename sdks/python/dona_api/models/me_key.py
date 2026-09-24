from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeKey")


@_attrs_define
class MeKey:
    """
    Attributes:
        id (UUID):
        name (str):
        kind (str): `sk` seller integration · `ak` AI agent (MCP) · `it` vendor install (S6). Known values (open set —
            tolerate new ones): `sk`, `ak`, `it`.
        prefix (str): First 16 characters; not a secret.
        scopes (list[str]):
        expires_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        ip_allow (list[str]):
    """

    id: UUID
    name: str
    kind: str
    prefix: str
    scopes: list[str]
    expires_at: datetime.datetime
    ip_allow: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind = self.kind

        prefix = self.prefix

        scopes = self.scopes

        expires_at = self.expires_at.isoformat()

        ip_allow = self.ip_allow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "prefix": prefix,
                "scopes": scopes,
                "expires_at": expires_at,
                "ip_allow": ip_allow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = d.pop("kind")

        prefix = d.pop("prefix")

        scopes = cast(list[str], d.pop("scopes"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        ip_allow = cast(list[str], d.pop("ip_allow"))

        me_key = cls(
            id=id,
            name=name,
            kind=kind,
            prefix=prefix,
            scopes=scopes,
            expires_at=expires_at,
            ip_allow=ip_allow,
        )

        me_key.additional_properties = d
        return me_key

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
