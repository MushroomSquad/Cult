"""
Settings and imports for requests class
Настройки и импорты для класса запросов
"""


# Python base libraries | Стандартные бибилиотеки питона #

import os

"""OS module for work with system
   Мудуль os для работы с системой"""

import json

"""Json for dumping and containing authorization data
   Json для хранения данных авторизации"""

from random import randint

"""Randint for random spread timeout
   Randint для рандомных пауз"""

import asyncio

"""Asyncio for async functions of python
   Asyncio для асинхронного функционала питона"""


# Python third-party libraries | Сторонние библиотеки питонa #

from typing import Any, Dict, List, Optional, Pattern, Type, Union

"""Typing for types annotation
   Typing для аннотации типов"""

from telethon import TelegramClient, events, functions, sync

"""Imports for telegram api
   Импорты для api телеграма"""

from aiohttp.client_exceptions import ClientConnectorError

"""ClientConnectorError for detictinf that need proxy connection
   ClientConnectorError для обнаружения необходимости подключения через прокси"""

import aiohttp

"""Aiohttp for async requests
   Aiohttp для асинхронных запросов"""

# Proxy list | Список прокси #

own_proxy_list: list[str] = []

"""List of your proxy
   Список ваших прокси"""

proxy_grub_list: list[str] = [
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
]

"""List of sources with proxies
   Список ссылок на паки прокси"""

# Timeout setting #

timeout: int = 10

"""Requests timeout
   Timeout для запросов"""

"""
# Сlass for requests through the proxy
Класс для запросов через прокси
"""


# Сlass for requests through the proxy | Класс для запросов через прокси #
class Variable_Requests:
    work_proxy: Union[str, None] = None

    @classmethod
    async def Grub_Proxies(
        cls: Type,
        Aio_Session,
    ):
        # for root, dirs, files in os.walk("."):
        #     for file in files:
        #         if file.endswith("Proxy.json"):
        #             async with aiofiles.open(
        #                 file,
        #                 "r",
        #             ) as file:
        #                 own_proxy_list.append(file)
        if len(own_proxy_list) > 0:
            pass
        proxies: List[str] = []
        if len(own_proxy_list) <= 0:
            for url in proxy_grub_list:
                async with Aio_Session.get(url=url) as response:
                    read_response = await response.read()
                    text_response = read_response.decode("utf-8")
                    proxy_list = text_response.split()
                    for proxy in proxy_list:
                        proxies.append(proxy)
        return proxies

    @classmethod
    async def Proxy_Get_Request(
        cls: Type,
        Aio_Session,
        url,
        headers,
    ):
        async with Aio_Session.get(
            url=url,
            proxy=cls.work_proxy,
            headers=headers,
            timeout=timeout,
        ) as response:
            return await response.text()

    @classmethod
    async def Proxy_Check(
        cls: Type,
        Aio_Session,
        url_to_check,
        headers,
    ):
        for proxy in await cls.Grub_Proxies(Aio_Session):
            try:
                async with Aio_Session.get(
                    url=url_to_check,
                    proxy=f"http://{proxy}",
                    timeout=timeout,
                    headers=headers,
                ) as response:
                    if response.status == 200:
                        print(
                            f"Using: http://{proxy}"
                            + " | "
                            + f"Используем: http://{proxy}"
                        )
                        cls.work_proxy = f"http://{proxy}"
            except Exception as exc:
                [print(f"\t{el}") for el in str(exc).splitlines()]

    @classmethod
    async def Get_Request(
        cls,
        Aio_Session,
        url,
        headers,
    ):
        if cls.work_proxy is None:
            try:
                async with Aio_Session.get(
                    url=url,
                    timeout=timeout,
                    headers=headers,
                ) as response:
                    if response.status == 403:
                        raise ConnectionResetError("\n403 errore | 403 ошибка")
                    return await response.text()
            except ConnectionResetError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except ClientConnectorError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except asyncio.exceptions.TimeoutError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except aiohttp.client_exceptions.ServerDisconnectedError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
        if cls.work_proxy is not None:
            try:
                async with Aio_Session.get(
                    url=url,
                    headers=headers,
                    proxy=cls.work_proxy,
                    timeout=timeout,
                ) as response:
                    if response.status == 403:
                        raise ConnectionResetError("\n403 errore | 403 ошибка")
                    return await response.text()
            except ConnectionResetError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except ClientConnectorError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except asyncio.exceptions.TimeoutError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)
            except aiohttp.client_exceptions.ServerDisconnectedError as exc:
                await cls.Proxy_Check(Aio_Session, url, headers)
                return await cls.Proxy_Get_Request(Aio_Session, url_to_check, headers)


__all__: list[str] = [
    "os",
    "json",
    "randint",
    "asyncio",
    "List",
    "Optional",
    "Dict",
    "Any",
    "Pattern",
    "Type",
    "Union",
    "TelegramClient",
    "events",
    "sync",
    "functions",
    "ClientConnectorError",
    "aiohttp",
    "own_proxy_list",
    "proxy_grub_list",
    "timeout",
    "Variable_Requests",
]
