from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Ping")


@_attrs_define
class Ping:
    """
    Attributes:
        ok (Literal['pong']):
        time (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        authenticated (bool): True only when a valid key was presented.
    """

    ok: Literal["pong"]
    time: datetime.datetime
    authenticated: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        time = self.time.isoformat()

        authenticated = self.authenticated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ok": ok,
                "time": time,
                "authenticated": authenticated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = cast(Literal["pong"], d.pop("ok"))
        if ok != "pong":
            raise ValueError(f"ok must match const 'pong', got '{ok}'")

        time = datetime.datetime.fromisoformat(d.pop("time"))

        authenticated = d.pop("authenticated")

        ping = cls(
            ok=ok,
            time=time,
            authenticated=authenticated,
        )

        ping.additional_properties = d
        return ping

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
