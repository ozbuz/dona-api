from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.status import Status
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(dona_seller, Unset):
        headers["Dona-Seller"] = dona_seller

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/status",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | Status | None:
    if response.status_code == 200:
        response_200 = Status.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | Status]:
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
) -> Response[Any | Error | Status]:
    """Service status

     Public; edge-cacheable 60 s; linked from every 503's `doc_url`.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Status]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
        dona_seller=dona_seller,
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
) -> Any | Error | Status | None:
    """Service status

     Public; edge-cacheable 60 s; linked from every 503's `doc_url`.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Status
    """

    return sync_detailed(
        client=client,
        accept_language=accept_language,
        dona_seller=dona_seller,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
) -> Response[Any | Error | Status]:
    """Service status

     Public; edge-cacheable 60 s; linked from every 503's `doc_url`.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Status]
    """

    kwargs = _get_kwargs(
        accept_language=accept_language,
        dona_seller=dona_seller,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
) -> Any | Error | Status | None:
    """Service status

     Public; edge-cacheable 60 s; linked from every 503's `doc_url`.

    Args:
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Status
    """

    return (
        await asyncio_detailed(
            client=client,
            accept_language=accept_language,
            dona_seller=dona_seller,
        )
    ).parsed
