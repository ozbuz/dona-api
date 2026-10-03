from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="CommissionOffer")


@_attrs_define
class CommissionOffer:
    """
    Attributes:
        code (str): `campaign` · `launch_v1` · `cohort_new` · `cohort_existing` · `seller` · `seller_group` · `country`
            · `platform`.
        rule_id (str): The commission rule; empty while a launch offer is promised (its rule is created the day the shop
            opens) and for a `campaign` (a campaign is not a rule).
        state (str): Known values (open set — tolerate new ones): `running`, `promised`.
        effect_type (str): Known values (open set — tolerate new ones): `absolute_pct`, `relative_discount_pct`.
        effect_pct (float): `absolute_pct`: the rate. `relative_discount_pct`: the share taken off each category rate.
        days (int | None):
        starts_at (datetime.datetime | None):
        ends_at (datetime.datetime | None): Every `code` but `campaign`: exclusive — orders placed before it keep the
            offer's rate. `campaign`: the LAST second the campaign's grant prices (23:59:59 Tashkent on its last day — the
            grant ends at the 00:00 after it), the same instant as that grant's `campaigns[].ends_at`.
        days_left (int | None):
        campaign_id (UUID | Unset): Only when `code` is `campaign`.
        name (LocalizedText | Unset): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
    """

    code: str
    rule_id: str
    state: str
    effect_type: str
    effect_pct: float
    days: int | None
    starts_at: datetime.datetime | None
    ends_at: datetime.datetime | None
    days_left: int | None
    campaign_id: UUID | Unset = UNSET
    name: LocalizedText | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        rule_id = self.rule_id

        state = self.state

        effect_type = self.effect_type

        effect_pct = self.effect_pct

        days: int | None
        days = self.days

        starts_at: None | str
        if isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        ends_at: None | str
        if isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        days_left: int | None
        days_left = self.days_left

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "rule_id": rule_id,
                "state": state,
                "effect_type": effect_type,
                "effect_pct": effect_pct,
                "days": days,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "days_left": days_left,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        rule_id = d.pop("rule_id")

        state = d.pop("state")

        effect_type = d.pop("effect_type")

        effect_pct = d.pop("effect_pct")

        def _parse_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days = _parse_days(d.pop("days"))

        def _parse_starts_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        starts_at = _parse_starts_at(d.pop("starts_at"))

        def _parse_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ends_at = _parse_ends_at(d.pop("ends_at"))

        def _parse_days_left(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        days_left = _parse_days_left(d.pop("days_left"))

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _name = d.pop("name", UNSET)
        name: LocalizedText | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LocalizedText.from_dict(_name)

        commission_offer = cls(
            code=code,
            rule_id=rule_id,
            state=state,
            effect_type=effect_type,
            effect_pct=effect_pct,
            days=days,
            starts_at=starts_at,
            ends_at=ends_at,
            days_left=days_left,
            campaign_id=campaign_id,
            name=name,
        )

        commission_offer.additional_properties = d
        return commission_offer

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
