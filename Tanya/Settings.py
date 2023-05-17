"""
Settings and imports for mother class
Настройки и импорты для материнского класса
"""

import os

# Python base libraries | Стандартные бибилиотеки питона #\

import asyncio

"""Asyncio for async functions of python
   Asyncio для асинхронного функционала питона"""

import re

"""Re for regular expressions
   Re для регулярных выражений"""

from typing import Dict, List, NoReturn, Optional, Pattern, Type, Union

"""Typing for types annotation
   Typing для аннотации типов"""

import aiohttp

"""Aiohttp for async requests
   Aiohttp для асинхронных запросов"""

# Python third-party modules | Сторонние модули питонa #

import aiofiles

"""Aiofiles for async work with files
   Aiofiles для ассинхронной работы с файлами"""

from itertools import zip_longest
import Dark_Mother

"""Mother code. Inherits scripts from this
   Материнский код. Наследует программы от него"""

# Links to pages | Ссылки на стрницы #
ALL_URL_LIST: List[str] = [
    # FAN_ART_URL =
    "https://www.deviantart.com/topic/fan-art",
    # # FANTASY_ART_URL =
    # "https://www.deviantart.com/topic/fantasy",
    # # ANIME_ART_URL =
    # "https://www.deviantart.com/topic/anime-and-manga",
    # # DIGITAL_ART_URL =
    # "https://www.deviantart.com/topic/digital-art",
    # # HOME_URL =
    # "https://www.deviantart.com/",
    # # GENSHIN_IMPACT_URL =
    # "https://www.deviantart.com/tag/genshinimpact",
    # "https://www.deviantart.com/tag/genshin",
    # # ZELDA_URL =
    # "https://www.deviantart.com/tag/zelda",
    # # COMICS_URL =
    # "https://www.deviantart.com/topic/comics",
    # # FAN_FICTION_URL =
    # "https://www.deviantart.com/topic/fan-fiction",
]

"""Root urls to parse posts and links to next pages
   Начальные ссылки для парсинга постов и 'следующих страниц'"""

# Headers for responses | Заголовки для запросов #
headers: Dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

"""Header with user agent for requests
   Заголовки с юзер агентом для запросов"""

# Regular expressions for parsing | Регулярные выражения для парсинга #
pages_class: Pattern = re.compile("^https://www.deviantart.com/(\w+)/art(\S+)(\d)$")

"""Regular expression for parsing posts' links
   Регулярное выражение для парсинга ссылок на посты
   Example | Пример: https://www.deviantart.com/koriarredondo/art/Spirit-on-the-Outside-931149987"""

tags_class: Pattern = re.compile("^https://www.deviantart.com/tag/(\S+)$")

"""Regular expression for parsing tags' links
   Регулярное выражение для парсинга ссылок на тэги
   Example | Пример: https://www.deviantart.com/tag/fanart"""

images_class: Pattern = re.compile("^https://images-wixmp-(\S*).wixmp.com/f/(\S*)$")
# https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3ca6e6a4-4db6-4336-9e52-051f60f5b358/dfv2v8e-70e66195-5abf-47c6-aa43-0a45bfe5bf5f.png/v1/fill/w_1280,h_911,q_80,strp/yoga_29__dancer_pose_by_sirafima_dfv2v8e-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTExIiwicGF0aCI6IlwvZlwvM2NhNmU2YTQtNGRiNi00MzM2LTllNTItMDUxZjYwZjViMzU4XC9kZnYydjhlLTcwZTY2MTk1LTVhYmYtNDdjNi1hYTQzLTBhNDViZmU1YmY1Zi5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.gshTORv8Fr7FcbU_4FKSgruvsHIoXRSuTSRN0ZVkfVM


"""Regular expression for parsing images' links
   Регулярное выражение для парсинга ссылок на изображения
   Example | Пример: https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/81164306-3d04-48d0-aaff-709455e43bf6/dfedrxf-592dc0b6-3ebc-42df-b4db-b46b445e8c79.png/v1/fill/w_1192,h_670,q_70"""

next_page_class: Pattern = re.compile("^(\S*)?cursor=(\S+)$")

"""Regular expression for parsing 'next' pages' links
   Регулярное выражение для парсинга ссылок на 'next' страницы
   Example | Пример: https://www.deviantart.com/topic/fan-art?cursor=MTQwYWI2MjA9MiY1OTBhY2FkMD0yNCZkMTc0YjZiYz1OJTJGQQ"""

# Other | Другое #
next_index: int = 1

"""How many 'next' pages' links will be parsed
   Сколько ссылок на 'next' страницы будет спаршено"""

__all__: List[str] = [
    "os",
    "re",
    "asyncio",
    "Dict",
    "List",
    "NoReturn",
    "Optional",
    "Type",
    "Union",
    "aiohttp",
    "Dark_Mother",
    "ALL_URL_LIST",
    "headers",
    "pages_class",
    "tags_class",
    "images_class",
    "next_page_class",
    "next_index",
    "aiofiles",
    "aiofiles",
    "zip_longest",
]
