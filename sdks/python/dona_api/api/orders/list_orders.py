import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.order_page import OrderPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scheme: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["page"] = page

    params["limit"] = limit

    params["updated_since"] = updated_since

    params["status"] = status

    params["scheme"] = scheme

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
        "url": "/orders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | OrderPage | None:
    if response.status_code == 200:
        response_200 = OrderPage.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | OrderPage]:
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
    page: int | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scheme: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | OrderPage]:
    """List orders (no buyer PII)

     The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`,
    `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span
    ≤ 90 d, `to` exclusive.

    Args:
        cursor (str | Unset):
        page (int | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `all`, `pending`,
            `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`.
        scheme (str | Unset): Known values (open set — tolerate new ones): `own_fleet`,
            `third_party`.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OrderPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        page=page,
        limit=limit,
        updated_since=updated_since,
        status=status,
        scheme=scheme,
        from_=from_,
        to=to,
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
    page: int | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scheme: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | OrderPage | None:
    """List orders (no buyer PII)

     The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`,
    `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span
    ≤ 90 d, `to` exclusive.

    Args:
        cursor (str | Unset):
        page (int | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `all`, `pending`,
            `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`.
        scheme (str | Unset): Known values (open set — tolerate new ones): `own_fleet`,
            `third_party`.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OrderPage
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        page=page,
        limit=limit,
        updated_since=updated_since,
        status=status,
        scheme=scheme,
        from_=from_,
        to=to,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scheme: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | OrderPage]:
    """List orders (no buyer PII)

     The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`,
    `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span
    ≤ 90 d, `to` exclusive.

    Args:
        cursor (str | Unset):
        page (int | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `all`, `pending`,
            `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`.
        scheme (str | Unset): Known values (open set — tolerate new ones): `own_fleet`,
            `third_party`.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OrderPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        page=page,
        limit=limit,
        updated_since=updated_since,
        status=status,
        scheme=scheme,
        from_=from_,
        to=to,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    page: int | Unset = UNSET,
    limit: int | Unset = 50,
    updated_since: str | Unset = UNSET,
    status: str | Unset = UNSET,
    scheme: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | OrderPage | None:
    """List orders (no buyer PII)

     The `orders:read` projection. `status` takes the portal buckets (`all`, `pending`, `paid`,
    `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`). `from`/`to` span
    ≤ 90 d, `to` exclusive.

    Args:
        cursor (str | Unset):
        page (int | Unset):
        limit (int | Unset):  Default: 50.
        updated_since (str | Unset):
        status (str | Unset): Known values (open set — tolerate new ones): `all`, `pending`,
            `paid`, `ready_to_ship`, `to_ship`, `shipped`, `delivered`, `cancelled`, `return_refund`.
        scheme (str | Unset): Known values (open set — tolerate new ones): `own_fleet`,
            `third_party`.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OrderPage
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            page=page,
            limit=limit,
            updated_since=updated_since,
            status=status,
            scheme=scheme,
            from_=from_,
            to=to,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
