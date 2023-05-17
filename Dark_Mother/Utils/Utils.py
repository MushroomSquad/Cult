from typing import (
    Type,
    Any,
    Optional,
    Dict,
    Union,
    Pattern,
)

"""Typing for types annotation
   Typing для аннотации типов"""

import aiofiles

"""Aiofiles for async work with files
   Aiofiles для ассинхронной работы с файлами"""

from bs4 import BeautifulSoup

"""BeautifulSoup for parsing HTML
   BeautifulSoup для парсинга HTML"""

from datetime import datetime

"""Datetime for working with date and time
   Datetime для работы с датой и временем"""

import jinja2

"""Jinja for working with templates
   Jinja для работы с шаблонами"""


class Utils:
    @classmethod
    def progressBar(
        cls,
        iterable,
        prefix = '',
        suffix = '',
        decimals = 1,
        length = 100,
        fill = '█',
        printEnd = "\r",
    ):
        """
        Call in a loop to create terminal progress bar
        @params:
            iterable    - Required  : iterable object (Iterable)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        total = len(iterable)
        # Progress Bar Printing Function
        def printProgressBar (iteration):
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filledLength = int(length * iteration // total)
            bar = fill * filledLength + '-' * (length - filledLength)
            print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Initial Call
        printProgressBar(0)
        # Update Progress Bar
        for i, item in enumerate(iterable):
            yield item
            printProgressBar(i + 1)
        # Print New Line on Complete
        print()

    # Get function | Функция Get #
    @classmethod
    async def Get_ST(
        cls: Type,
        Argument: Any,
        Gettable: Any,
        Headers: Optional[Dict[str, str]] = None,
    ) -> Union[str, object]:
        try:
            if Headers is not None:
                return Argument.get(Gettable, Headers)
            else:
                return Argument.get(Gettable)
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]

    # Function for page soping | Функция Soup #
    @classmethod
    async def Soup(
        cls: Type,
        Souppable: str,
    ) -> object:
        try:
            return BeautifulSoup(Souppable, "html.parser")
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]

    # Find function | Функция поиска #
    @classmethod
    async def Find(
        cls: Type,
        Find_IN: object,
        Searchable: Pattern,
        Choice: Optional[str] = None,
    ) -> Union[object, object]:
        try:
            if Choice is None:
                return Find_IN.find(Searchable)
            elif Choice == "all":
                return Find_IN.findAll(Searchable)
            elif Choice == "href":
                return Find_IN.findAll(
                    "a",
                    attrs={"href": Searchable},
                )
            elif Choice == "img":
                return Find_IN.find(
                    "img",
                    attrs={"href": Searchable},
                )
            elif Choice == "src":
                return Find_IN.find(
                    "img",
                    attrs={"src": Searchable},
                )
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]

    # Cutting str function | Функция вырезания из строк #
    @classmethod
    async def Cut(
        cls: Type,
        Input: str,
        Spliter: str,
        Index: int,
    ):
        return Input.split(Spliter)[Index]

    # Cropping str function | Функция для обрезания строк #
    @classmethod
    async def Crop(
        cls: Type,
        Input: str,
        Spliter: str,
        Index: int,
    ):
        return Spliter.join(Input.split(Spliter)[:Index])

    # Function for download files | Функция для скачивания файлов #
    @classmethod
    async def Download_File(
        cls: Type,
        Name: str,
        Extension: str,
        Aio_Session,
        Link: str,
        Headers: Optional[Dict[str, str]],
    ):
        try:
            async with Aio_Session.get(url=Link, headers=Headers) as response:
                File = await aiofiles.open(Name + Extension, mode="wb")
                await File.write(await response.read())
                await File.close()
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]

    # Function for take present datetime | Функция для получения текущего времени #
    @classmethod
    async def DateTime_Now(cls: Type):
        return datetime.now()

    # Convert datetime to unix | Конвертация времени в юникс формат #
    @classmethod
    async def DateTime2Unix(
        cls: Type,
        Time2Conv,
    ):
        return datetime.timestamp(Time2Conv)

    # Fill the template function | Функция заполнения шаблона #
    @classmethod
    async def Templater(
        cls: Type,
        Path,
        Template,
        Data,
    ):
        Loader = jinja2.FileSystemLoader(Path)
        Env = jinja2.Environment(loader=Loader, trim_blocks=True)
        return Template.render(Data)
