class Telegram:
    # Create Telegram session | Создание телеграм сессии #
    @classmethod
    async def Create_Telethon_Session(
        cls: Type,
        Session_Name,
        API_ID,
        API_Hash,
    ):
        Client = TelegramClient(
            Session_Name,
            API_ID,
            API_Hash,
        )
        Client.start()
        return Client

    # Send Telegram message | Отправка сообщения в телеграм #
    @classmethod
    async def TelegramSendMessage(
        cls: Type,
        Client,
        Channel,
        Message,
        Upload_Datetime,
        File,
    ):
        try:
            await Client.send_message(
                entity=Channel,
                message=Message,
                schedule=Upload_Datetime,
                file=File,
                parse_mode="md",
            )
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]

    # Authorization data saving for Telegram | Сохранение данных авторизации для Telegram #
    @classmethod
    async def Create_Telegram_Session(cls: Type):
        tg_list: list = []
        for root, dirs, files in os.walk("./Janna/Authorization/Telegram"):
            for file in files:
                if file.endswith("_TG_Session.json"):
                    file_name = os.path.join(file)
                    tg_list.append(file_name)
        print("Создаю")
        API_ID = input("Введите API_ID:\n")
        API_Hash = input("Введите API_Hash:\n")
        Session_Name = input("Введите название сессии:\n")
        TG_Channel = input("Введите id телеграм канала:\n")
        TG_Data = {
            "API_ID": API_ID,
            "API_Hash": API_Hash,
            "Session_Name": Session_Name,
            "TG_Channel": TG_Channel,
        }
        async with aiofiles.open(
            f"./Janna/Authorization/Telegram/{len(tg_list)+1}_TG_Session.json", "w"
        ) as file:
            json.dump(TG_Data, file)


