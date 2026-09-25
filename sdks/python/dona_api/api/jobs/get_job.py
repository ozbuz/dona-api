from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.job import Job
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
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
        "url": "/jobs/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Job | None:
    if response.status_code == 200:
        response_200 = Job.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Job]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | Job]:
    """Poll a job

     Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for
    `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`);
    otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After
    `expires_at` (7 d) ⇒ `404 not_found`.

    Args:
        id (UUID):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Job]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | Job | None:
    """Poll a job

     Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for
    `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`);
    otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After
    `expires_at` (7 d) ⇒ `404 not_found`.

    Args:
        id (UUID):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Job
    """

    return sync_detailed(
        id=id,
        client=client,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | Job]:
    """Poll a job

     Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for
    `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`);
    otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After
    `expires_at` (7 d) ⇒ `404 not_found`.

    Args:
        id (UUID):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Job]
    """

    kwargs = _get_kwargs(
        id=id,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | Job | None:
    """Poll a job

     Readable by any key of the shop that holds the scope the job's kind needs (`catalog:read` for
    `export_products`, `orders:read` for `export_orders`, `catalog:write` for `products_batch`);
    otherwise `404 not_found`. Poll ≥ 5 s (`Retry-After` is set while pending/running). After
    `expires_at` (7 d) ⇒ `404 not_found`.

    Args:
        id (UUID):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Job
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
