from typing import Union

import asyncpg
from asyncpg import Pool, Connection

from tgbot.config import load_config


class DataBase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create_pool(self):
        config = load_config()
        self.pool = await asyncpg.create_pool(
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            database=config.db.database,
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result

    async def create_table_users(self):
        sql = """ CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE,
        username VARCHAR(255) NULL,
        full_name VARCHAR(255) NOT NULL,
        lang_code VARCHAR(255) NOT NULL,
        is_premium VARCHAR(255) NOT NULL,
        registered_time VARCHAR(255) NOT NULL
        
        );
        """

        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item}=${num}" for item, num in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id: int, username: str, full_name: str, lang_code: str, is_premium: str,
                       registered_time: str):
        sql = "INSERT INTO Users(telegram_id, username, full_name, lang_code, is_premium, registered_time) VALUES($1, $2, $3, $4, $5, $6)"
        return await self.execute(sql, telegram_id, username, full_name, lang_code, is_premium, registered_time,
                                  execute=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users "
        return await self.execute(sql, fetch=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        return await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_table(self):
        return await self.execute("DROP TABLE Users", execute=True)
