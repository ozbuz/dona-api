from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusComponents")


@_attrs_define
class StatusComponents:
    """
    Attributes:
        api (str): Known values (open set — tolerate new ones): `operational`, `degraded`, `outage`, `disabled`.
        mcp (str): Known values (open set — tolerate new ones): `operational`, `degraded`, `outage`, `disabled`.
        webhooks (str): Known values (open set — tolerate new ones): `operational`, `degraded`, `outage`, `disabled`.
        events (str): Known values (open set — tolerate new ones): `operational`, `degraded`, `outage`, `disabled`.
    """

    api: str
    mcp: str
    webhooks: str
    events: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api = self.api

        mcp = self.mcp

        webhooks = self.webhooks

        events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api": api,
                "mcp": mcp,
                "webhooks": webhooks,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api = d.pop("api")

        mcp = d.pop("mcp")

        webhooks = d.pop("webhooks")

        events = d.pop("events")

        status_components = cls(
            api=api,
            mcp=mcp,
            webhooks=webhooks,
            events=events,
        )

        status_components.additional_properties = d
        return status_components

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
