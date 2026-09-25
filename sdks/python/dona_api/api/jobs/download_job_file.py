from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    token: str,
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

    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs/{id}/download".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | str]:
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
    token: str,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | str]:
    """Download an export's file

     What a ready export's `file_url` points at. Needs BOTH a key of the job's shop that holds the scope
    the job's kind needs (any key of the shop — the file is the shop's; a key of another shop is `404
    not_found` whatever token it carries) AND the job's own `token` from `file_url`, valid 15 min (`401
    download_token_invalid` when absent, forged or another job's; `401 download_token_expired` past its
    time — re-read `GET /jobs/{id}` for a fresh one). The file is kept in the database, never on a
    public origin, and is swept with its job after `expires_at` (7 d) ⇒ `404 not_found`. Not gated by
    `writes_enabled`.

    Args:
        id (UUID):
        token (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
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
    token: str,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | str | None:
    """Download an export's file

     What a ready export's `file_url` points at. Needs BOTH a key of the job's shop that holds the scope
    the job's kind needs (any key of the shop — the file is the shop's; a key of another shop is `404
    not_found` whatever token it carries) AND the job's own `token` from `file_url`, valid 15 min (`401
    download_token_invalid` when absent, forged or another job's; `401 download_token_expired` past its
    time — re-read `GET /jobs/{id}` for a fresh one). The file is kept in the database, never on a
    public origin, and is swept with its job after `expires_at` (7 d) ⇒ `404 not_found`. Not gated by
    `writes_enabled`.

    Args:
        id (UUID):
        token (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
    """

    return sync_detailed(
        id=id,
        client=client,
        token=token,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    token: str,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | str]:
    """Download an export's file

     What a ready export's `file_url` points at. Needs BOTH a key of the job's shop that holds the scope
    the job's kind needs (any key of the shop — the file is the shop's; a key of another shop is `404
    not_found` whatever token it carries) AND the job's own `token` from `file_url`, valid 15 min (`401
    download_token_invalid` when absent, forged or another job's; `401 download_token_expired` past its
    time — re-read `GET /jobs/{id}` for a fresh one). The file is kept in the database, never on a
    public origin, and is swept with its job after `expires_at` (7 d) ⇒ `404 not_found`. Not gated by
    `writes_enabled`.

    Args:
        id (UUID):
        token (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
    """

    kwargs = _get_kwargs(
        id=id,
        token=token,
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
    token: str,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Error | str | None:
    """Download an export's file

     What a ready export's `file_url` points at. Needs BOTH a key of the job's shop that holds the scope
    the job's kind needs (any key of the shop — the file is the shop's; a key of another shop is `404
    not_found` whatever token it carries) AND the job's own `token` from `file_url`, valid 15 min (`401
    download_token_invalid` when absent, forged or another job's; `401 download_token_expired` past its
    time — re-read `GET /jobs/{id}` for a fresh one). The file is kept in the database, never on a
    public origin, and is swept with its job after `expires_at` (7 d) ⇒ `404 not_found`. Not gated by
    `writes_enabled`.

    Args:
        id (UUID):
        token (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            token=token,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
