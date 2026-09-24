from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText
    from ..models.product_attributes import ProductAttributes
    from ..models.product_hold_type_0 import ProductHoldType0
    from ..models.variant import Variant


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        id (UUID):
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        description (LocalizedText | None):
        status (str): `draft`, `ai_review`, `active`, `hidden` today; tolerate new values.
        category_id (None | UUID):
        brand (None | str):
        seller_sku (None | str):
        barcode (None | str):
        external_id (None | str):
        price_uzs (int): Integer soʻm (no decimals).
        compare_at_uzs (int | None): Must exceed `price_uzs` (0020 CHECK).
        stock (int): Sum over variants when `has_variants`.
        has_variants (bool):
        variants (list[Variant]):
        ikpu (None | str):
        package_code (None | str):
        image_urls (list[str]):
        video_url (None | str):
        attributes (ProductAttributes):
        created_via (str): `manual`, `mass_upload`, `api`, … (products_created_via_check).
        hold (None | ProductHoldType0):
        open_issues (int): Open `listing_issues` + `product_violations`.
        version (str): Opaque (today the full-precision `updated_at`); echo verbatim.
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    title: LocalizedText
    description: LocalizedText | None
    status: str
    category_id: None | UUID
    brand: None | str
    seller_sku: None | str
    barcode: None | str
    external_id: None | str
    price_uzs: int
    compare_at_uzs: int | None
    stock: int
    has_variants: bool
    variants: list[Variant]
    ikpu: None | str
    package_code: None | str
    image_urls: list[str]
    video_url: None | str
    attributes: ProductAttributes
    created_via: str
    hold: None | ProductHoldType0
    open_issues: int
    version: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415
        from ..models.product_hold_type_0 import ProductHoldType0  # noqa: PLC0415

        id = str(self.id)

        title = self.title.to_dict()

        description: dict[str, Any] | None
        if isinstance(self.description, LocalizedText):
            description = self.description.to_dict()
        else:
            description = self.description

        status = self.status

        category_id: None | str
        if isinstance(self.category_id, UUID):
            category_id = str(self.category_id)
        else:
            category_id = self.category_id

        brand: None | str
        brand = self.brand

        seller_sku: None | str
        seller_sku = self.seller_sku

        barcode: None | str
        barcode = self.barcode

        external_id: None | str
        external_id = self.external_id

        price_uzs = self.price_uzs

        compare_at_uzs: int | None
        compare_at_uzs = self.compare_at_uzs

        stock = self.stock

        has_variants = self.has_variants

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        ikpu: None | str
        ikpu = self.ikpu

        package_code: None | str
        package_code = self.package_code

        image_urls = self.image_urls

        video_url: None | str
        video_url = self.video_url

        attributes = self.attributes.to_dict()

        created_via = self.created_via

        hold: dict[str, Any] | None
        if isinstance(self.hold, ProductHoldType0):
            hold = self.hold.to_dict()
        else:
            hold = self.hold

        open_issues = self.open_issues

        version = self.version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "description": description,
                "status": status,
                "category_id": category_id,
                "brand": brand,
                "seller_sku": seller_sku,
                "barcode": barcode,
                "external_id": external_id,
                "price_uzs": price_uzs,
                "compare_at_uzs": compare_at_uzs,
                "stock": stock,
                "has_variants": has_variants,
                "variants": variants,
                "ikpu": ikpu,
                "package_code": package_code,
                "image_urls": image_urls,
                "video_url": video_url,
                "attributes": attributes,
                "created_via": created_via,
                "hold": hold,
                "open_issues": open_issues,
                "version": version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415
        from ..models.product_attributes import ProductAttributes  # noqa: PLC0415
        from ..models.product_hold_type_0 import ProductHoldType0  # noqa: PLC0415
        from ..models.variant import Variant  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        title = LocalizedText.from_dict(d.pop("title"))

        def _parse_description(data: object) -> LocalizedText | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                description_type_0 = LocalizedText.from_dict(data)

                return description_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | None, data)

        description = _parse_description(d.pop("description"))

        status = d.pop("status")

        def _parse_category_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_id_type_0 = UUID(data)

                return category_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        category_id = _parse_category_id(d.pop("category_id"))

        def _parse_brand(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        brand = _parse_brand(d.pop("brand"))

        def _parse_seller_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seller_sku = _parse_seller_sku(d.pop("seller_sku"))

        def _parse_barcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        barcode = _parse_barcode(d.pop("barcode"))

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("external_id"))

        price_uzs = d.pop("price_uzs")

        def _parse_compare_at_uzs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs"))

        stock = d.pop("stock")

        has_variants = d.pop("has_variants")

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = Variant.from_dict(variants_item_data)

            variants.append(variants_item)

        def _parse_ikpu(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ikpu = _parse_ikpu(d.pop("ikpu"))

        def _parse_package_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        package_code = _parse_package_code(d.pop("package_code"))

        image_urls = cast(list[str], d.pop("image_urls"))

        def _parse_video_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        video_url = _parse_video_url(d.pop("video_url"))

        attributes = ProductAttributes.from_dict(d.pop("attributes"))

        created_via = d.pop("created_via")

        def _parse_hold(data: object) -> None | ProductHoldType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hold_type_0 = ProductHoldType0.from_dict(data)

                return hold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductHoldType0, data)

        hold = _parse_hold(d.pop("hold"))

        open_issues = d.pop("open_issues")

        version = d.pop("version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        product = cls(
            id=id,
            title=title,
            description=description,
            status=status,
            category_id=category_id,
            brand=brand,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            price_uzs=price_uzs,
            compare_at_uzs=compare_at_uzs,
            stock=stock,
            has_variants=has_variants,
            variants=variants,
            ikpu=ikpu,
            package_code=package_code,
            image_urls=image_urls,
            video_url=video_url,
            attributes=attributes,
            created_via=created_via,
            hold=hold,
            open_issues=open_issues,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
        )

        product.additional_properties = d
        return product

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
