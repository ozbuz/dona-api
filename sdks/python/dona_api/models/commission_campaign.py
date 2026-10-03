from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.commission_campaign_category import CommissionCampaignCategory
    from ..models.commission_campaign_progress_type_0 import CommissionCampaignProgressType0
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="CommissionCampaign")


@_attrs_define
class CommissionCampaign:
    """
    Attributes:
        campaign_id (UUID):
        grant_id (UUID):
        code (str): The campaign's handle (e.g. `LAUNCH-0`).
        name (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        kind (str): Known values (open set — tolerate new ones): `new_registration`, `existing_seller`, `invite`,
            `sales_target`.
        state (str): `running`: the grant prices the shop now (a grant that starts later is listed from its start).
            `promised`: it opens the day the shop opens; nothing is dated until then. Known values (open set — tolerate new
            ones): `running`, `promised`.
        scope (str): Known values (open set — tolerate new ones): `all`, `categories`.
        categories (list[CommissionCampaignCategory]): Every category-scoped rate of the campaign (each covers its
            category's subtree).
        effect_type (str): Known values (open set — tolerate new ones): `absolute_pct`, `relative_discount_pct`.
        effect_pct (float): The all-categories rate when `scope` is `all`, else the first category's.
        combinable (bool):
        days (int | None): The whole days the grant runs (a promise — the days it will run from the shop's opening).
        starts_at (datetime.datetime | None):
        ends_at (datetime.datetime | None): The last second the grant prices (23:59:59 Tashkent on its last day); `null`
            = until the campaign closes, or a promise.
        days_left (int | None): Whole days left, counted to the grant's anchor + `days` (the count a cohort offer
            shows), never past `ends_at`; `null` for a promise.
        progress (CommissionCampaignProgressType0 | None): Invite or sales-target progress; `null` until those campaign
            types ship.
    """

    campaign_id: UUID
    grant_id: UUID
    code: str
    name: LocalizedText
    kind: str
    state: str
    scope: str
    categories: list[CommissionCampaignCategory]
    effect_type: str
    effect_pct: float
    combinable: bool
    days: int | None
    starts_at: datetime.datetime | None
    ends_at: datetime.datetime | None
    days_left: int | None
    progress: CommissionCampaignProgressType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.commission_campaign_progress_type_0 import CommissionCampaignProgressType0  # noqa: PLC0415

        campaign_id = str(self.campaign_id)

        grant_id = str(self.grant_id)

        code = self.code

        name = self.name.to_dict()

        kind = self.kind

        state = self.state

        scope = self.scope

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        effect_type = self.effect_type

        effect_pct = self.effect_pct

        combinable = self.combinable

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

        progress: dict[str, Any] | None
        if isinstance(self.progress, CommissionCampaignProgressType0):
            progress = self.progress.to_dict()
        else:
            progress = self.progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaign_id": campaign_id,
                "grant_id": grant_id,
                "code": code,
                "name": name,
                "kind": kind,
                "state": state,
                "scope": scope,
                "categories": categories,
                "effect_type": effect_type,
                "effect_pct": effect_pct,
                "combinable": combinable,
                "days": days,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "days_left": days_left,
                "progress": progress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commission_campaign_category import CommissionCampaignCategory  # noqa: PLC0415
        from ..models.commission_campaign_progress_type_0 import CommissionCampaignProgressType0  # noqa: PLC0415
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        campaign_id = UUID(d.pop("campaign_id"))

        grant_id = UUID(d.pop("grant_id"))

        code = d.pop("code")

        name = LocalizedText.from_dict(d.pop("name"))

        kind = d.pop("kind")

        state = d.pop("state")

        scope = d.pop("scope")

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = CommissionCampaignCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        effect_type = d.pop("effect_type")

        effect_pct = d.pop("effect_pct")

        combinable = d.pop("combinable")

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

        def _parse_progress(data: object) -> CommissionCampaignProgressType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                progress_type_0 = CommissionCampaignProgressType0.from_dict(data)

                return progress_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommissionCampaignProgressType0 | None, data)

        progress = _parse_progress(d.pop("progress"))

        commission_campaign = cls(
            campaign_id=campaign_id,
            grant_id=grant_id,
            code=code,
            name=name,
            kind=kind,
            state=state,
            scope=scope,
            categories=categories,
            effect_type=effect_type,
            effect_pct=effect_pct,
            combinable=combinable,
            days=days,
            starts_at=starts_at,
            ends_at=ends_at,
            days_left=days_left,
            progress=progress,
        )

        commission_campaign.additional_properties = d
        return commission_campaign

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
