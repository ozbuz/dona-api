from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.commission_campaign import CommissionCampaign
    from ..models.commission_offer import CommissionOffer
    from ..models.commission_root import CommissionRoot


T = TypeVar("T", bound="Commission")


@_attrs_define
class Commission:
    """The seller portal's `GET /seller/commission` body, byte for byte.

    Attributes:
        seller_id (UUID):
        default_pct (float): The platform rate when a category tree carries none.
        start_pct (float): The lowest rate on the card (MIN of `roots[].min_pct`; `default_pct` when there are no
            roots).
        roots (list[CommissionRoot]):
        offer (CommissionOffer | None):
        saved_uzs (int | None): What the launch offer and the commission campaigns spared this shop so far (orders not
            cancelled), in som, from the order-line snapshots only. A number while `offer.code` is `launch_v1` or the shop
            has a campaign-priced line; otherwise `null`.
        campaigns (list[CommissionCampaign]): Every promised or running grant whose campaign prices this shop now (a
            paused campaign disappears at once). Empty while campaigns do not apply to the shop.
    """

    seller_id: UUID
    default_pct: float
    start_pct: float
    roots: list[CommissionRoot]
    offer: CommissionOffer | None
    saved_uzs: int | None
    campaigns: list[CommissionCampaign]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.commission_offer import CommissionOffer  # noqa: PLC0415

        seller_id = str(self.seller_id)

        default_pct = self.default_pct

        start_pct = self.start_pct

        roots = []
        for roots_item_data in self.roots:
            roots_item = roots_item_data.to_dict()
            roots.append(roots_item)

        offer: dict[str, Any] | None
        if isinstance(self.offer, CommissionOffer):
            offer = self.offer.to_dict()
        else:
            offer = self.offer

        saved_uzs: int | None
        saved_uzs = self.saved_uzs

        campaigns = []
        for campaigns_item_data in self.campaigns:
            campaigns_item = campaigns_item_data.to_dict()
            campaigns.append(campaigns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seller_id": seller_id,
                "default_pct": default_pct,
                "start_pct": start_pct,
                "roots": roots,
                "offer": offer,
                "saved_uzs": saved_uzs,
                "campaigns": campaigns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commission_campaign import CommissionCampaign  # noqa: PLC0415
        from ..models.commission_offer import CommissionOffer  # noqa: PLC0415
        from ..models.commission_root import CommissionRoot  # noqa: PLC0415

        d = dict(src_dict)
        seller_id = UUID(d.pop("seller_id"))

        default_pct = d.pop("default_pct")

        start_pct = d.pop("start_pct")

        roots = []
        _roots = d.pop("roots")
        for roots_item_data in _roots:
            roots_item = CommissionRoot.from_dict(roots_item_data)

            roots.append(roots_item)

        def _parse_offer(data: object) -> CommissionOffer | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                offer_type_0 = CommissionOffer.from_dict(data)

                return offer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommissionOffer | None, data)

        offer = _parse_offer(d.pop("offer"))

        def _parse_saved_uzs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        saved_uzs = _parse_saved_uzs(d.pop("saved_uzs"))

        campaigns = []
        _campaigns = d.pop("campaigns")
        for campaigns_item_data in _campaigns:
            campaigns_item = CommissionCampaign.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        commission = cls(
            seller_id=seller_id,
            default_pct=default_pct,
            start_pct=start_pct,
            roots=roots,
            offer=offer,
            saved_uzs=saved_uzs,
            campaigns=campaigns,
        )

        commission.additional_properties = d
        return commission

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
