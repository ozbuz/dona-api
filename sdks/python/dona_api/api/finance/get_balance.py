from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.balance import Balance
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
        "url": "/finance/balance",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Balance | Error | None:
    if response.status_code == 200:
        response_200 = Balance.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Balance | Error]:
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
) -> Response[Balance | Error]:
    """Balance

     The wallet's answer for the key's shop, asked as the shop's CURRENT owner (the portal's own finance
    bridge), projected field by field. Never error-copied. No requisites, PAN or statement URLs. The
    wallet unreachable, erroring or not knowing the shop ⇒ `503 wallet_unavailable` (`Retry-After: 30`),
    never its body (C57). Served by the marketplace process only: a SERVER_ROLE=seller-api server
    answers `503 role_unavailable` before any read (D3).

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Balance | Error]
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
) -> Balance | Error | None:
    """Balance

     The wallet's answer for the key's shop, asked as the shop's CURRENT owner (the portal's own finance
    bridge), projected field by field. Never error-copied. No requisites, PAN or statement URLs. The
    wallet unreachable, erroring or not knowing the shop ⇒ `503 wallet_unavailable` (`Retry-After: 30`),
    never its body (C57). Served by the marketplace process only: a SERVER_ROLE=seller-api server
    answers `503 role_unavailable` before any read (D3).

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Balance | Error
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
) -> Response[Balance | Error]:
    """Balance

     The wallet's answer for the key's shop, asked as the shop's CURRENT owner (the portal's own finance
    bridge), projected field by field. Never error-copied. No requisites, PAN or statement URLs. The
    wallet unreachable, erroring or not knowing the shop ⇒ `503 wallet_unavailable` (`Retry-After: 30`),
    never its body (C57). Served by the marketplace process only: a SERVER_ROLE=seller-api server
    answers `503 role_unavailable` before any read (D3).

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Balance | Error]
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
) -> Balance | Error | None:
    """Balance

     The wallet's answer for the key's shop, asked as the shop's CURRENT owner (the portal's own finance
    bridge), projected field by field. Never error-copied. No requisites, PAN or statement URLs. The
    wallet unreachable, erroring or not knowing the shop ⇒ `503 wallet_unavailable` (`Retry-After: 30`),
    never its body (C57). Served by the marketplace process only: a SERVER_ROLE=seller-api server
    answers `503 role_unavailable` before any read (D3).

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Balance | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
