from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorMeta")


@_attrs_define
class ErrorMeta:
    """Code-specific facts, e.g. `oldest_event_id` with `cursor_expired`.

    Attributes:
        oldest_event_id (UUID | Unset):
    """

    oldest_event_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oldest_event_id: str | Unset = UNSET
        if not isinstance(self.oldest_event_id, Unset):
            oldest_event_id = str(self.oldest_event_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oldest_event_id is not UNSET:
            field_dict["oldest_event_id"] = oldest_event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _oldest_event_id = d.pop("oldest_event_id", UNSET)
        oldest_event_id: UUID | Unset
        if isinstance(_oldest_event_id, Unset):
            oldest_event_id = UNSET
        else:
            oldest_event_id = UUID(_oldest_event_id)

        error_meta = cls(
            oldest_event_id=oldest_event_id,
        )

        error_meta.additional_properties = d
        return error_meta

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
