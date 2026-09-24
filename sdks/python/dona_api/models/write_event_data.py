from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WriteEventData")


@_attrs_define
class WriteEventData:
    """
    Attributes:
        approval_id (UUID):
        kind (str): Known values (open set — tolerate new ones): `price`, `stock`, `product`, `delist`.
        subject_type (str): Known values (open set — tolerate new ones): `product`, `product_variant`, `batch`.
        subject_id (None | UUID):
        rule (str): Known values (open set — tolerate new ones): `price_floor`, `drop_100x`, `stock_jump_10x`,
            `mass_zero_50pct`, `delist_30pct`, `confirmation_required`.
        decided_by_kind (None | str | Unset): Known values (open set — tolerate new ones): `owner`, `staff`.
    """

    approval_id: UUID
    kind: str
    subject_type: str
    subject_id: None | UUID
    rule: str
    decided_by_kind: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_id = str(self.approval_id)

        kind = self.kind

        subject_type = self.subject_type

        subject_id: None | str
        if isinstance(self.subject_id, UUID):
            subject_id = str(self.subject_id)
        else:
            subject_id = self.subject_id

        rule = self.rule

        decided_by_kind: None | str | Unset
        if isinstance(self.decided_by_kind, Unset):
            decided_by_kind = UNSET
        else:
            decided_by_kind = self.decided_by_kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approval_id": approval_id,
                "kind": kind,
                "subject_type": subject_type,
                "subject_id": subject_id,
                "rule": rule,
            }
        )
        if decided_by_kind is not UNSET:
            field_dict["decided_by_kind"] = decided_by_kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approval_id = UUID(d.pop("approval_id"))

        kind = d.pop("kind")

        subject_type = d.pop("subject_type")

        def _parse_subject_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_id_type_0 = UUID(data)

                return subject_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subject_id = _parse_subject_id(d.pop("subject_id"))

        rule = d.pop("rule")

        def _parse_decided_by_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decided_by_kind = _parse_decided_by_kind(d.pop("decided_by_kind", UNSET))

        write_event_data = cls(
            approval_id=approval_id,
            kind=kind,
            subject_type=subject_type,
            subject_id=subject_id,
            rule=rule,
            decided_by_kind=decided_by_kind,
        )

        write_event_data.additional_properties = d
        return write_event_data

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
