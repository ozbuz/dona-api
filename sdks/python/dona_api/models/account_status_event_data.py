from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountStatusEventData")


@_attrs_define
class AccountStatusEventData:
    """
    Attributes:
        status (str):
        can_sell (bool):
        action_url (str):
        reason_code (None | str | Unset):
    """

    status: str
    can_sell: bool
    action_url: str
    reason_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        can_sell = self.can_sell

        action_url = self.action_url

        reason_code: None | str | Unset
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "can_sell": can_sell,
                "action_url": action_url,
            }
        )
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        can_sell = d.pop("can_sell")

        action_url = d.pop("action_url")

        def _parse_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_code = _parse_reason_code(d.pop("reason_code", UNSET))

        account_status_event_data = cls(
            status=status,
            can_sell=can_sell,
            action_url=action_url,
            reason_code=reason_code,
        )

        account_status_event_data.additional_properties = d
        return account_status_event_data

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
