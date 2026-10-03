from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commission import Commission
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/commission",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Commission | Error | None:
    if response.status_code == 200:
        response_200 = Commission.from_dict(response.json())

        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Commission | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Commission | Error]:
    """What Dona charges this shop — the rate card and the running offer

     The same body as the seller portal's `GET /seller/commission` (built by the same function): every
    active root category with the range of its leaves' rates, `start_pct` (the lowest rate on the card),
    and `offer` — the shop-wide commission rule that prices this shop now (`running`) or will from the
    day it opens (`promised`), e.g. the launch offer `launch_v1` at 0 %. Since BE-C7 it also carries the
    shop's commission campaigns: `campaigns[]` (every promised or running grant whose campaign prices
    the shop), `offer.code = campaign` when an all-categories campaign beats the offer, and
    `roots[].effective_min_pct / effective_max_pct` (this shop's range after its rules and campaigns).
    Per category, `GET /categories/{id}/requirements` answers the rate a sale is charged
    (`effective_commission_pct`). Read only; the key's own shop only.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Commission | Error]
    """

    kwargs = _get_kwargs(
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
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Commission | Error | None:
    """What Dona charges this shop — the rate card and the running offer

     The same body as the seller portal's `GET /seller/commission` (built by the same function): every
    active root category with the range of its leaves' rates, `start_pct` (the lowest rate on the card),
    and `offer` — the shop-wide commission rule that prices this shop now (`running`) or will from the
    day it opens (`promised`), e.g. the launch offer `launch_v1` at 0 %. Since BE-C7 it also carries the
    shop's commission campaigns: `campaigns[]` (every promised or running grant whose campaign prices
    the shop), `offer.code = campaign` when an all-categories campaign beats the offer, and
    `roots[].effective_min_pct / effective_max_pct` (this shop's range after its rules and campaigns).
    Per category, `GET /categories/{id}/requirements` answers the rate a sale is charged
    (`effective_commission_pct`). Read only; the key's own shop only.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Commission | Error
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Commission | Error]:
    """What Dona charges this shop — the rate card and the running offer

     The same body as the seller portal's `GET /seller/commission` (built by the same function): every
    active root category with the range of its leaves' rates, `start_pct` (the lowest rate on the card),
    and `offer` — the shop-wide commission rule that prices this shop now (`running`) or will from the
    day it opens (`promised`), e.g. the launch offer `launch_v1` at 0 %. Since BE-C7 it also carries the
    shop's commission campaigns: `campaigns[]` (every promised or running grant whose campaign prices
    the shop), `offer.code = campaign` when an all-categories campaign beats the offer, and
    `roots[].effective_min_pct / effective_max_pct` (this shop's range after its rules and campaigns).
    Per category, `GET /categories/{id}/requirements` answers the rate a sale is charged
    (`effective_commission_pct`). Read only; the key's own shop only.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Commission | Error]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Commission | Error | None:
    """What Dona charges this shop — the rate card and the running offer

     The same body as the seller portal's `GET /seller/commission` (built by the same function): every
    active root category with the range of its leaves' rates, `start_pct` (the lowest rate on the card),
    and `offer` — the shop-wide commission rule that prices this shop now (`running`) or will from the
    day it opens (`promised`), e.g. the launch offer `launch_v1` at 0 %. Since BE-C7 it also carries the
    shop's commission campaigns: `campaigns[]` (every promised or running grant whose campaign prices
    the shop), `offer.code = campaign` when an all-categories campaign beats the offer, and
    `roots[].effective_min_pct / effective_max_pct` (this shop's range after its rules and campaigns).
    Per category, `GET /categories/{id}/requirements` answers the rate a sale is charged
    (`effective_commission_pct`). Read only; the key's own shop only.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Commission | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
