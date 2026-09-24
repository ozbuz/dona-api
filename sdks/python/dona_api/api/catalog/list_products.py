from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.product_page import ProductPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    seller_sku: str | Unset = UNSET,
    barcode: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["updated_since"] = updated_since

    params["status"] = status

    params["seller_sku"] = seller_sku

    params["barcode"] = barcode

    params["external_id"] = external_id

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/products",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | ProductPage | None:
    if response.status_code == 200:
        response_200 = ProductPage.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

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
) -> Response[Any | Error | ProductPage]:
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
    seller_sku: str | Unset = UNSET,
    barcode: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | Error | ProductPage]:
    """List products

     Keyset list of the shop's products (`deleted_at IS NULL`). Deletions never appear in a delta — read
    `/products/deleted`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        q (str | Unset):
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ProductPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
        seller_sku=seller_sku,
        barcode=barcode,
        external_id=external_id,
        q=q,
        if_none_match=if_none_match,
        accept_language=accept_language,
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
    seller_sku: str | Unset = UNSET,
    barcode: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Any | Error | ProductPage | None:
    """List products

     Keyset list of the shop's products (`deleted_at IS NULL`). Deletions never appear in a delta — read
    `/products/deleted`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        q (str | Unset):
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | ProductPage
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
        seller_sku=seller_sku,
        barcode=barcode,
        external_id=external_id,
        q=q,
        if_none_match=if_none_match,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    seller_sku: str | Unset = UNSET,
    barcode: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | Error | ProductPage]:
    """List products

     Keyset list of the shop's products (`deleted_at IS NULL`). Deletions never appear in a delta — read
    `/products/deleted`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        q (str | Unset):
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ProductPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        updated_since=updated_since,
        status=status,
        seller_sku=seller_sku,
        barcode=barcode,
        external_id=external_id,
        q=q,
        if_none_match=if_none_match,
        accept_language=accept_language,
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
    seller_sku: str | Unset = UNSET,
    barcode: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Any | Error | ProductPage | None:
    """List products

     Keyset list of the shop's products (`deleted_at IS NULL`). Deletions never appear in a delta — read
    `/products/deleted`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        q (str | Unset):
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | ProductPage
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            updated_since=updated_since,
            status=status,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            q=q,
            if_none_match=if_none_match,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
