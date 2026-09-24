from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookUpdate")


@_attrs_define
class WebhookUpdate:
    """
    Attributes:
        url (str | Unset):
        event_types (list[str] | Unset): Exact event names or prefixes (`order.*`); `["*"]` (or omitted on create) =
            every event.
        status (str | Unset): `paused` = seller-side pause (deliveries accrue 30 d); `active` resumes a paused endpoint.
            A `disabled` endpoint is re-enabled only by a successful `/ping`. Known values (open set — tolerate new ones):
            `active`, `paused`.
    """

    url: str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        status = d.pop("status", UNSET)

        webhook_update = cls(
            url=url,
            event_types=event_types,
            status=status,
        )

        webhook_update.additional_properties = d
        return webhook_update

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
