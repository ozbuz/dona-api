from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.ikpu_page import IkpuPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["q"] = q

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ikpu",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | IkpuPage | None:
    if response.status_code == 200:
        response_200 = IkpuPage.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | IkpuPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | IkpuPage]:
    """IKPU (tax classifier) search

     From the local `tasnif` copy.

    Args:
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IkpuPage]
    """

    kwargs = _get_kwargs(
        q=q,
        cursor=cursor,
        limit=limit,
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
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | IkpuPage | None:
    """IKPU (tax classifier) search

     From the local `tasnif` copy.

    Args:
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IkpuPage
    """

    return sync_detailed(
        client=client,
        q=q,
        cursor=cursor,
        limit=limit,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | IkpuPage]:
    """IKPU (tax classifier) search

     From the local `tasnif` copy.

    Args:
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IkpuPage]
    """

    kwargs = _get_kwargs(
        q=q,
        cursor=cursor,
        limit=limit,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | IkpuPage | None:
    """IKPU (tax classifier) search

     From the local `tasnif` copy.

    Args:
        q (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IkpuPage
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            cursor=cursor,
            limit=limit,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
