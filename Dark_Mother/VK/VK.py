class Vk:
    # Get wall vk upload server | Получение сервера загрузки на стену VK #
    @classmethod
    async def GetWallUploadServer(
        cls: Type,
        Timer_Index,
        Aio_Session,
        User_Token,
        Group_ID,
    ):
        await asyncio.sleep(randint(1 + Timer_Index, 3 + Timer_Index))
        print(f"Получаем Сервер Загрузки")
        async with Aio_Session.get(
            "https://api.vk.com/method/photos.getWallUploadServer?",
            params={
                "acces_token": User_Token,
                "group_id": Group_ID,
                "v": "5.130",
            },
        ) as response:
            await asyncio.sleep(randint(1 + Timer_Index, 3 + Timer_Index))
            response_text = await response.json()
            response = response_text["response"]["upload_url"]
            print(f"Получен Сервер Для Загрузки")
            return response

    # Upload file | Загрузка файла #
    @classmethod
    async def Upload_File(
        cls: Type,
        Timer_Index,
        Aio_Session,
        User_Token,
        Group_ID,
        File,
    ):
        Upload_URL = await cls.GetWallUploadServer(
            Timer_Index,
            Aio_Session,
            User_Token,
            Group_ID,
        )
        print(f"Делаем запрос")
        async with Aio_Session.post(Upload_URL, data=File) as request:
            upload_response = await request.json(content_type="text/html")
        print(f"Запрос выполнен")
        return upload_response

    # Save wall photo | Сохранить фотографию на стене #
    @classmethod
    async def SaveWallPhoto(
        cls: Type,
        Timer_Index,
        Aio_Session,
        User_Token,
        Group_ID,
        File,
    ):
        Upload_Response = await cls.Upload_File(
            Timer_Index,
            Aio_Session,
            User_Token,
            Group_ID,
            File,
        )
        print(f"Сохраняем пост")
        async with Aio_Session.get(
            "https://api.vk.com/method/photos.saveWallPhoto?",
            params={
                "acces_token": User_Token,
                "group_id": Group_ID,
                "photo": Upload_Response["photo"],
                "server": Upload_Response["server"],
                "hash": Upload_Response["hash"],
            },
        ) as request:
            Save_Response = await request.json()
        return (
            "photo"
            + str(Save_Response["response"][0]["owner_id"])
            + "_"
            + str(Save_Response["response"][0]["id"])
            + "&access_key="
            + str(Save_Response["response"][0]["access_key"])
        )
        print(f"Пост сохранён")

    # Create wall post | Создание поста #
    @classmethod
    async def MakeWallPost(
        cls: Type,
        Timer_Index,
        Aio_Session,
        User_Tokenm,
        Group_ID,
        File,
        Group_Token,
        Message,
        Date,
        Link,
    ):
        await asyncio.sleep(Timer_Index)
        Response = await cls.SaveWallPhoto(
            Timer_Index,
            Aio_Session,
            User_Token,
            Group_ID,
            File,
        )
        async with Aio_Session.get(
            "https://api.vk.com/method/wall.post?",
            params={
                "attachments": Response,
                "owner_id": f"-{Group_ID}",
                "acces_token": Group_Token,
                "from_group": "1",
                "message": Message,
                "publish_date": Date,
                "copyright": Link,
                "v": "5.130",
            },
        ) as request:
            response = await request.json()

    # Authorization data saving for VK | Сохранение данных авторизации для VK #
    @classmethod
    async def Create_VK_Session(cls):
        vk_list = []
        for root, dirs, files in os.walk("./Janna/Authorization/VK"):
            for file in files:
                if file.endswith("_VK_Session.json"):
                    file_name = os.path.join(file)
                    vk_list.append(file_name)
        print("Создаю")
        group_id = input("Введите id группы:\n")
        user_token = input("Введите токен пользователя:\n")
        group_token = input("Введите токен группы:\n")
        vk_data = {
            "group_id": group_id,
            "user_token": user_token,
            "group_token": group_token,
        }
        async with aiofiles.open(
            f"./Janna/Authorization/VK/{len(vk_list)+1}_VK_Session.json", "w"
        ) as file:
            json.dump(vk_data, file)
