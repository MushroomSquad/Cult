from typing import (
    Type,
)
import sqlalchemy.exc as SQLAlchemyError

"""SQLAlchemyError for logging repeate elements
   SQLAlchemyError для логирования повторяющихся объектов"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table

"""Types for tables' models
   Типы для моделей таблиц"""

from sqlalchemy.orm import relationship, sessionmaker

"""Sessionmaker for creating session and relationship for relationship many to many relationship
   Sessionmaker для создания сессии и relationship для отношения многие к многим"""

from sqlalchemy.ext.declarative import declarative_base

"""Declarative base - function for constructing base tables' class
Declarative base - функция для создания базового класса таблиц"""


class SQL:
    # Function for saving data to DB | Сохранение информации в БД #
    @classmethod
    async def Save_to_SQL(
        cls: Type,
        Aio_Session,
        El_2_Save,
    ):
        try:
            Aio_Session.add(El_2_Save)
            Aio_Session.commit()
            return El_2_Save
        except SQLAlchemyError.IntegrityError as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]
            Aio_Session.rollback()
            print(El_2_Save.name, "-- Already exists! | Уже существует!")
            return False
        except Exception as exc:
            [print(f"\t{el}") for el in str(exc).splitlines()]
            Aio_Session.rollback()
            print("Something gone wrong! | Что-то пошло не так!")
            return False

    # Extract data from DB | Извлечение данных из БД #
    @classmethod
    async def SQL_Query(
        cls: Type,
        Aio_Session,
        Target,
        Filter,
        Searchable,
    ):
        selected = Aio_Session.execute(select(Target).where(Filter == Searchable))
        return selected.scalars().all()

    # Table initialization | Инициализация таблицы #
    @classmethod
    async def Table_Init(cls):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)