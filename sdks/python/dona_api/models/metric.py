from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Metric")


@_attrs_define
class Metric:
    """Row shape of `accounthealth.buildMetrics` — one vocabulary with the portal.

    Attributes:
        id (str):
        group (str):
        current_value (Any): null when no data One of: number, string (or null).
        target (str):
        applied_to (list[str]):
        passing (bool):
        has_detail (bool):
    """

    id: str
    group: str
    current_value: Any
    target: str
    applied_to: list[str]
    passing: bool
    has_detail: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group = self.group

        current_value = self.current_value

        target = self.target

        applied_to = self.applied_to

        passing = self.passing

        has_detail = self.has_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group": group,
                "current_value": current_value,
                "target": target,
                "applied_to": applied_to,
                "passing": passing,
                "has_detail": has_detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        group = d.pop("group")

        current_value = d.pop("current_value")

        target = d.pop("target")

        applied_to = cast(list[str], d.pop("applied_to"))

        passing = d.pop("passing")

        has_detail = d.pop("has_detail")

        metric = cls(
            id=id,
            group=group,
            current_value=current_value,
            target=target,
            applied_to=applied_to,
            passing=passing,
            has_detail=has_detail,
        )

        metric.additional_properties = d
        return metric

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
