from .Settings import *


class Tanya:
    post_url_list: list[str] = []
    post_list: list[object] = []
    variable_request: Union[object, None] = None

    @classmethod
    async def Get_More_Source(
        cls: Type,
        aio_session: object,
        url: str,
        indx: int,
    ) -> NoReturn:
        cls.variable_request: object = Dark_Mother.Variable_Requests()
        response: str = await cls.variable_request.Get_Request(
            aio_session,
            url,
            headers,
        )
        page_soup: object = await Dark_Mother.Utils.Soup(response)
        for next_page_tag in await Dark_Mother.Utils.Find(
            page_soup,
            next_page_class,
            "href",
        ):
            if next_page_tag.contents[0] == "Next":
                next_page_link: str = "https://www.deviantart.com" + (
                    await Dark_Mother.Utils.Get_ST(
                        next_page_tag,
                        "href",
                        headers,
                    )
                )
                ALL_URL_LIST.append(next_page_link)
                if indx < next_index:
                    indx += 1
                    await cls.Get_More_Source(
                        aio_session,
                        next_page_link,
                        indx,
                    )

    @classmethod
    async def Get_More_Source_Task(cls: Type) -> NoReturn:
        async with aiohttp.ClientSession() as aio_session:
            tasks: List[object] = []
            for url in ALL_URL_LIST:
                task: object = asyncio.create_task(
                    cls.Get_More_Source(
                        aio_session,
                        url,
                        0,
                    )
                )
                tasks.append(task)
            async for item in Dark_Mother.Utils.progressBar(tasks, prefix = 'Progress:', suffix = 'Complete', length = 50):
                await asyncio.gather(*tasks)

    @classmethod
    async def Get_Posts_Links(
        cls: Type,
        aio_session: object,
        url: str,
    ) -> NoReturn:
        cls.variable_request: object = Dark_Mother.Variable_Requests()
        response: str = await Dark_Mother.Variable_Requests.Get_Request(
            aio_session,
            url,
            headers,
        )
        page_soup: object = await Dark_Mother.Utils.Soup(response)
        find_pages: object = await Dark_Mother.Utils.Find(
            page_soup, pages_class, "href"
        )
        for find_page in find_pages:
            post_link: str = await Dark_Mother.Utils.Get_ST(find_page, "href", headers)
            if post_link not in cls.post_url_list:
                cls.post_url_list.append(post_link)

    @classmethod
    async def Task2(cls):
        async with aiohttp.ClientSession() as aio_session:
            tasks = []
            for url in ALL_URL_LIST:
                task = asyncio.create_task(cls.Get_Posts_Links(aio_session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    @classmethod
    async def Parse_Posts(cls, aio_session, post_url):
        cls.variable_request: object = Dark_Mother.Variable_Requests()
        response: str = await Dark_Mother.Variable_Requests.Get_Request(
            aio_session,
            url=post_url,
            headers=headers,
        )
        post_soup = await Dark_Mother.Utils.Soup(response)
        try:
            find_tags = await Dark_Mother.Utils.Find(post_soup, tags_class, "href")
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]
        try:
            find_image = await Dark_Mother.Utils.Find(post_soup, images_class, "src")
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]
        image_link = await Dark_Mother.Utils.Get_ST(find_image, "src", headers)
        tag_list = []
        for tag_el in find_tags:
            tag_link = await Dark_Mother.Utils.Get_ST(tag_el, "href", headers)
            tag = await Dark_Mother.Utils.Cut(tag_link, "/", -1)
            tag_list.append(tag)
            pass
        cls.post_list.append(
            Dark_Mother.SQL.Post(
                await Dark_Mother.Utils.Cut(
                    post_url,
                    "/",
                    -1,
                ),
                tag_list,
                post_url,
                image_link,
            )
        )

    @classmethod
    async def Task3(cls):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for post_url in cls.post_url_list:
                task = asyncio.create_task(cls.Parse_Posts(session, post_url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    @classmethod
    async def Save_Post(
        cls,
        Path,
        Name,
        Extension,
        aio_session,
        Link,
    ):
        cls.variable_request: object = Dark_Mother.Variable_Requests()
        try:
            File_Name = Path + Name + Extension
            response: str = await Dark_Mother.Variable_Requests.Get_Request(
                aio_session,
                url=Link,
                headers=headers,
                )
            async with aiofiles.open(File_Name, "wb") as f:
                await f.write(response)

        except Exception as exc:
            [print("\t", el) for el in str(exc).splitlines()]

    @classmethod
    async def Task4(cls):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for post in cls.post_list:
                task = asyncio.create_task(
                    cls.Save_Post(
                        "./Downloads/Deviant_Downloads/",
                        post.name,
                        ".png",
                        session,
                        post.attachments,
                    ),
                )
                tasks.append(task)
                await asyncio.gather(*tasks)

    @classmethod
    def run(cls):
        print(
            f"\n{f' Root pages ({len(ALL_URL_LIST)}) | Основные страницы ({len(ALL_URL_LIST)}) ':#^{os.get_terminal_size().columns}}"
        )
        for url_1, url_2 in zip_longest(*[iter(ALL_URL_LIST)]*2):
            if url_2:
                print(f"{f'{url_1}':<{int((os.get_terminal_size().columns)/2)}}{f'{url_2}'}")
            else:
                print(f"{f'{url_1}'}")


        print(f"{'':#^{os.get_terminal_size().columns}}")
        asyncio.run(cls.Get_More_Source_Task())
        print(
            f"\n{f' Links for parse: {len(ALL_URL_LIST)}) | Ссылок для парсинга: {len(ALL_URL_LIST)}) ':#^{os.get_terminal_size().columns}}"
        )
        asyncio.run(cls.Task2())
        print(
            f"\n{f' Posts for parse: {len(cls.post_url_list)} | Постов для парсинга: {len(cls.post_url_list)} ':#^{os.get_terminal_size().columns}}"
        )
        asyncio.run(cls.Task3())
        asyncio.run(cls.Task4())
