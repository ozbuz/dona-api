from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_components import StatusComponents
    from ..models.status_incidents_item import StatusIncidentsItem


T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        status (str): Known values (open set — tolerate new ones): `operational`, `degraded`, `outage`.
        components (StatusComponents):
        incidents (list[StatusIncidentsItem]):
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    status: str
    components: StatusComponents
    incidents: list[StatusIncidentsItem]
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        components = self.components.to_dict()

        incidents = []
        for incidents_item_data in self.incidents:
            incidents_item = incidents_item_data.to_dict()
            incidents.append(incidents_item)

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "components": components,
                "incidents": incidents,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_components import StatusComponents  # noqa: PLC0415
        from ..models.status_incidents_item import StatusIncidentsItem  # noqa: PLC0415

        d = dict(src_dict)
        status = d.pop("status")

        components = StatusComponents.from_dict(d.pop("components"))

        incidents = []
        _incidents = d.pop("incidents")
        for incidents_item_data in _incidents:
            incidents_item = StatusIncidentsItem.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status = cls(
            status=status,
            components=components,
            incidents=incidents,
            updated_at=updated_at,
        )

        status.additional_properties = d
        return status

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
