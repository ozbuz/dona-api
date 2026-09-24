from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook import Webhook


T = TypeVar("T", bound="WebhookPing")


@_attrs_define
class WebhookPing:
    """
    Attributes:
        ok (bool):
        response_status (int | None):
        response_ms (int | None):
        failure (None | str): Known values (open set — tolerate new ones): `timeout`, `tls`, `dns`, `status`.
        webhook (Webhook):
    """

    ok: bool
    response_status: int | None
    response_ms: int | None
    failure: None | str
    webhook: Webhook
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        response_status: int | None
        response_status = self.response_status

        response_ms: int | None
        response_ms = self.response_ms

        failure: None | str
        failure = self.failure

        webhook = self.webhook.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ok": ok,
                "response_status": response_status,
                "response_ms": response_ms,
                "failure": failure,
                "webhook": webhook,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook import Webhook  # noqa: PLC0415

        d = dict(src_dict)
        ok = d.pop("ok")

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("response_status"))

        def _parse_response_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_ms = _parse_response_ms(d.pop("response_ms"))

        def _parse_failure(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure = _parse_failure(d.pop("failure"))

        webhook = Webhook.from_dict(d.pop("webhook"))

        webhook_ping = cls(
            ok=ok,
            response_status=response_status,
            response_ms=response_ms,
            failure=failure,
            webhook=webhook,
        )

        webhook_ping.additional_properties = d
        return webhook_ping

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
