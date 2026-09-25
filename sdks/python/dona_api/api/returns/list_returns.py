from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.return_page import ReturnPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
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

    params["updated_since"] = updated_since

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/returns",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReturnPage | None:
    if response.status_code == 200:
        response_200 = ReturnPage.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReturnPage]:
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
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | ReturnPage]:
    """List returns

     Read-only in v1 — approving a return is `orders.refund`, never issuable.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `requested`,
            `approved`, `refunded`, `rejected`, `disputed`, `closed`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReturnPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
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
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | ReturnPage | None:
    """List returns

     Read-only in v1 — approving a return is `orders.refund`, never issuable.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `requested`,
            `approved`, `refunded`, `rejected`, `disputed`, `closed`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReturnPage
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | ReturnPage]:
    """List returns

     Read-only in v1 — approving a return is `orders.refund`, never issuable.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `requested`,
            `approved`, `refunded`, `rejected`, `disputed`, `closed`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReturnPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
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
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | ReturnPage | None:
    """List returns

     Read-only in v1 — approving a return is `orders.refund`, never issuable.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `requested`,
            `approved`, `refunded`, `rejected`, `disputed`, `closed`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReturnPage
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            updated_since=updated_since,
            status=status,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
