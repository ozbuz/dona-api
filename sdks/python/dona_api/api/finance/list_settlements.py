import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.settlement_page import SettlementPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    order_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(dona_seller, Unset):
        headers["Dona-Seller"] = dona_seller

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_order_id: str | Unset = UNSET
    if not isinstance(order_id, Unset):
        json_order_id = str(order_id)
    params["order_id"] = json_order_id

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/settlements",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SettlementPage | None:
    if response.status_code == 200:
        response_200 = SettlementPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SettlementPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    order_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | SettlementPage]:
    """Settlement lines

     The wallet statement's lines for the shop, newest first (asked as the shop's current owner). `memo`
    is the line's machine `kind` from the wallet's CLOSED vocabulary (`sale_income`, `escrow_hold`,
    `escrow_release`, `refund`, `return`, `adjustment`, `withdrawal`, `withdrawal_failed`, `fee`,
    `commission`, `hold_placed`, `hold_captured`, `hold_released`, `cod_collected`, `cod_remitted`,
    `transfer`) or `other` — never the wallet's free-text title (C57). A line whose `id` or `txn_id` is
    not a UUID, or a `next_cursor` that is not an opaque ≤ 512-character URL-safe token, refuses the
    whole page. `503 wallet_unavailable` / `role_unavailable` as `/finance/balance`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        order_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SettlementPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        order_id=order_id,
        from_=from_,
        to=to,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    order_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | SettlementPage | None:
    """Settlement lines

     The wallet statement's lines for the shop, newest first (asked as the shop's current owner). `memo`
    is the line's machine `kind` from the wallet's CLOSED vocabulary (`sale_income`, `escrow_hold`,
    `escrow_release`, `refund`, `return`, `adjustment`, `withdrawal`, `withdrawal_failed`, `fee`,
    `commission`, `hold_placed`, `hold_captured`, `hold_released`, `cod_collected`, `cod_remitted`,
    `transfer`) or `other` — never the wallet's free-text title (C57). A line whose `id` or `txn_id` is
    not a UUID, or a `next_cursor` that is not an opaque ≤ 512-character URL-safe token, refuses the
    whole page. `503 wallet_unavailable` / `role_unavailable` as `/finance/balance`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        order_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SettlementPage
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        order_id=order_id,
        from_=from_,
        to=to,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    order_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | SettlementPage]:
    """Settlement lines

     The wallet statement's lines for the shop, newest first (asked as the shop's current owner). `memo`
    is the line's machine `kind` from the wallet's CLOSED vocabulary (`sale_income`, `escrow_hold`,
    `escrow_release`, `refund`, `return`, `adjustment`, `withdrawal`, `withdrawal_failed`, `fee`,
    `commission`, `hold_placed`, `hold_captured`, `hold_released`, `cod_collected`, `cod_remitted`,
    `transfer`) or `other` — never the wallet's free-text title (C57). A line whose `id` or `txn_id` is
    not a UUID, or a `next_cursor` that is not an opaque ≤ 512-character URL-safe token, refuses the
    whole page. `503 wallet_unavailable` / `role_unavailable` as `/finance/balance`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        order_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SettlementPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        order_id=order_id,
        from_=from_,
        to=to,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    order_id: UUID | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | SettlementPage | None:
    """Settlement lines

     The wallet statement's lines for the shop, newest first (asked as the shop's current owner). `memo`
    is the line's machine `kind` from the wallet's CLOSED vocabulary (`sale_income`, `escrow_hold`,
    `escrow_release`, `refund`, `return`, `adjustment`, `withdrawal`, `withdrawal_failed`, `fee`,
    `commission`, `hold_placed`, `hold_captured`, `hold_released`, `cod_collected`, `cod_remitted`,
    `transfer`) or `other` — never the wallet's free-text title (C57). A line whose `id` or `txn_id` is
    not a UUID, or a `next_cursor` that is not an opaque ≤ 512-character URL-safe token, refuses the
    whole page. `503 wallet_unavailable` / `role_unavailable` as `/finance/balance`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        order_id (UUID | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SettlementPage
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            order_id=order_id,
            from_=from_,
            to=to,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
