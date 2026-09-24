from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText
    from ..models.product_update_attributes import ProductUpdateAttributes


T = TypeVar("T", bound="ProductUpdate")


@_attrs_define
class ProductUpdate:
    """Partial update: an absent field is unchanged.

    Attributes:
        title (LocalizedText | Unset): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        description (LocalizedText | Unset): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        category_id (UUID | Unset):
        brand (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        price_uzs (int | Unset):
        compare_at_uzs (int | None | Unset):
        stock (int | Unset): Refused (`details[].code=stock_not_editable`) when the product has variants — use `POST
            /stock` with `variant_id`.
        ikpu (str | Unset):
        package_code (str | Unset):
        image_urls (list[str] | Unset):
        video_url (None | str | Unset):
        attributes (ProductUpdateAttributes | Unset):
        version (str | Unset): Optional optimistic lock; stale ⇒ `409 version_conflict`.
    """

    title: LocalizedText | Unset = UNSET
    description: LocalizedText | Unset = UNSET
    category_id: UUID | Unset = UNSET
    brand: str | Unset = UNSET
    barcode: str | Unset = UNSET
    external_id: str | Unset = UNSET
    price_uzs: int | Unset = UNSET
    compare_at_uzs: int | None | Unset = UNSET
    stock: int | Unset = UNSET
    ikpu: str | Unset = UNSET
    package_code: str | Unset = UNSET
    image_urls: list[str] | Unset = UNSET
    video_url: None | str | Unset = UNSET
    attributes: ProductUpdateAttributes | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        brand = self.brand

        barcode = self.barcode

        external_id = self.external_id

        price_uzs = self.price_uzs

        compare_at_uzs: int | None | Unset
        if isinstance(self.compare_at_uzs, Unset):
            compare_at_uzs = UNSET
        else:
            compare_at_uzs = self.compare_at_uzs

        stock = self.stock

        ikpu = self.ikpu

        package_code = self.package_code

        image_urls: list[str] | Unset = UNSET
        if not isinstance(self.image_urls, Unset):
            image_urls = self.image_urls

        video_url: None | str | Unset
        if isinstance(self.video_url, Unset):
            video_url = UNSET
        else:
            video_url = self.video_url

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if brand is not UNSET:
            field_dict["brand"] = brand
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if price_uzs is not UNSET:
            field_dict["price_uzs"] = price_uzs
        if compare_at_uzs is not UNSET:
            field_dict["compare_at_uzs"] = compare_at_uzs
        if stock is not UNSET:
            field_dict["stock"] = stock
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
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415
        from ..models.product_update_attributes import ProductUpdateAttributes  # noqa: PLC0415

        d = dict(src_dict)
        _title = d.pop("title", UNSET)
        title: LocalizedText | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = LocalizedText.from_dict(_title)

        _description = d.pop("description", UNSET)
        description: LocalizedText | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = LocalizedText.from_dict(_description)

        _category_id = d.pop("category_id", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        brand = d.pop("brand", UNSET)

        barcode = d.pop("barcode", UNSET)

        external_id = d.pop("external_id", UNSET)

        price_uzs = d.pop("price_uzs", UNSET)

        def _parse_compare_at_uzs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs", UNSET))

        stock = d.pop("stock", UNSET)

        ikpu = d.pop("ikpu", UNSET)

        package_code = d.pop("package_code", UNSET)

        image_urls = cast(list[str], d.pop("image_urls", UNSET))

        def _parse_video_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        video_url = _parse_video_url(d.pop("video_url", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: ProductUpdateAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ProductUpdateAttributes.from_dict(_attributes)

        version = d.pop("version", UNSET)

        product_update = cls(
            title=title,
            description=description,
            category_id=category_id,
            brand=brand,
            barcode=barcode,
            external_id=external_id,
            price_uzs=price_uzs,
            compare_at_uzs=compare_at_uzs,
            stock=stock,
            ikpu=ikpu,
            package_code=package_code,
            image_urls=image_urls,
            video_url=video_url,
            attributes=attributes,
            version=version,
        )

        product_update.additional_properties = d
        return product_update

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
