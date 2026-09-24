from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText
    from ..models.product_create_attributes import ProductCreateAttributes
    from ..models.variant_input import VariantInput


T = TypeVar("T", bound="ProductCreate")


@_attrs_define
class ProductCreate:
    """
    Attributes:
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        category_id (UUID):
        seller_sku (str):
        price_uzs (int):
        stock (int):
        description (LocalizedText | Unset): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        brand (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset): Your system's id, e.g. `1c:0f2a…`.
        compare_at_uzs (int | None | Unset):
        ikpu (str | Unset):
        package_code (str | Unset):
        image_urls (list[str] | Unset):
        video_url (str | Unset):
        attributes (ProductCreateAttributes | Unset):
        variants (list[VariantInput] | Unset):
        publish (bool | Unset): Ask to publish after create; a pending shop's product is held until documents approval.
    """

    title: LocalizedText
    category_id: UUID
    seller_sku: str
    price_uzs: int
    stock: int
    description: LocalizedText | Unset = UNSET
    brand: str | Unset = UNSET
    barcode: str | Unset = UNSET
    external_id: str | Unset = UNSET
    compare_at_uzs: int | None | Unset = UNSET
    ikpu: str | Unset = UNSET
    package_code: str | Unset = UNSET
    image_urls: list[str] | Unset = UNSET
    video_url: str | Unset = UNSET
    attributes: ProductCreateAttributes | Unset = UNSET
    variants: list[VariantInput] | Unset = UNSET
    publish: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title.to_dict()

        category_id = str(self.category_id)

        seller_sku = self.seller_sku

        price_uzs = self.price_uzs

        stock = self.stock

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        brand = self.brand

        barcode = self.barcode

        external_id = self.external_id

        compare_at_uzs: int | None | Unset
        if isinstance(self.compare_at_uzs, Unset):
            compare_at_uzs = UNSET
        else:
            compare_at_uzs = self.compare_at_uzs

        ikpu = self.ikpu

        package_code = self.package_code

        image_urls: list[str] | Unset = UNSET
        if not isinstance(self.image_urls, Unset):
            image_urls = self.image_urls

        video_url = self.video_url

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)

        publish = self.publish

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "category_id": category_id,
                "seller_sku": seller_sku,
                "price_uzs": price_uzs,
                "stock": stock,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if brand is not UNSET:
            field_dict["brand"] = brand
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if compare_at_uzs is not UNSET:
            field_dict["compare_at_uzs"] = compare_at_uzs
        if ikpu is not UNSET:
            field_dict["ikpu"] = ikpu
        if package_code is not UNSET:
            field_dict["package_code"] = package_code
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls
        if video_url is not UNSET:
            field_dict["video_url"] = video_url
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if variants is not UNSET:
            field_dict["variants"] = variants
        if publish is not UNSET:
            field_dict["publish"] = publish

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415
        from ..models.product_create_attributes import ProductCreateAttributes  # noqa: PLC0415
        from ..models.variant_input import VariantInput  # noqa: PLC0415

        d = dict(src_dict)
        title = LocalizedText.from_dict(d.pop("title"))

        category_id = UUID(d.pop("category_id"))

        seller_sku = d.pop("seller_sku")

        price_uzs = d.pop("price_uzs")

        stock = d.pop("stock")

        _description = d.pop("description", UNSET)
        description: LocalizedText | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = LocalizedText.from_dict(_description)

        brand = d.pop("brand", UNSET)

        barcode = d.pop("barcode", UNSET)

        external_id = d.pop("external_id", UNSET)

        def _parse_compare_at_uzs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs", UNSET))

        ikpu = d.pop("ikpu", UNSET)

        package_code = d.pop("package_code", UNSET)

        image_urls = cast(list[str], d.pop("image_urls", UNSET))

        video_url = d.pop("video_url", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ProductCreateAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ProductCreateAttributes.from_dict(_attributes)

        _variants = d.pop("variants", UNSET)
        variants: list[VariantInput] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = VariantInput.from_dict(variants_item_data)

                variants.append(variants_item)

        publish = d.pop("publish", UNSET)

        product_create = cls(
            title=title,
            category_id=category_id,
            seller_sku=seller_sku,
            price_uzs=price_uzs,
            stock=stock,
            description=description,
            brand=brand,
            barcode=barcode,
            external_id=external_id,
            compare_at_uzs=compare_at_uzs,
            ikpu=ikpu,
            package_code=package_code,
            image_urls=image_urls,
            video_url=video_url,
            attributes=attributes,
            variants=variants,
            publish=publish,
        )

        product_create.additional_properties = d
        return product_create

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
