from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
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
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        contact varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)


    async def create_table_bot(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Bots (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        username varchar(255) NULL
        );
        """
        await self.execute(sql, execute=True)


    async def create_table_site(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Sites (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        username varchar(255) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_link(self):
        sql = """
        CREATE TABLE IF NOT EXISTS link (
        id SERIAL PRIMARY KEY,
        link VARCHAR(255) NOT NULL
        );
        """
        await self.execute(sql, execute=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, contact, telegram_id):
        sql = "INSERT INTO users (full_name, username, contact, telegram_id) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, full_name, username, contact, telegram_id, fetchrow=True)
    

    async def add_bot(self, name, username,):
        sql = "INSERT INTO bots (name, username) VALUES($1, $2) returning *"
        return await self.execute(sql, name, username, fetchrow=True)
    

    async def add_sites(self, name, username,):
        sql = "INSERT INTO sites (name, username) VALUES($1, $2) returning *"
        return await self.execute(sql, name, username, fetchrow=True)
    
    async def add_link(self, link):
        sql = "INSERT INTO users (link) VALUES($1) returning *"
        return await self.execute(sql, link, fetchrow=True)


    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    
    async def select_all_link(self):
        sql = "SELECT * FROM link"
        return await self.execute(sql, fetch=True)

    async def select_all_bots(self):
        sql = "SELECT * FROM Bots"
        return await self.execute(sql, fetch=True)
    

    async def select_all_sites(self):
        sql = "SELECT * FROM Sites"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    

    async def select_vacance(self, **kwargs):
        sql = "SELECT * FROM vacance WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    

    async def select_bot(self, **kwargs):
        sql = "SELECT * FROM bots WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    

    async def select_site(self, **kwargs):
        sql = "SELECT * FROM Sites WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)
    
    async def count_bots(self):
        sql = "SELECT COUNT(*) FROM Bots"
        return await self.execute(sql, fetchval=True)
    
    async def count_sites(self):
        sql = "SELECT COUNT(*) FROM Sites"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def delete_bot(self):
        await self.execute("DELETE FROM Bots WHERE TRUE", execute=True)

    async def delete_bot(self):
        await self.execute("DELETE FROM Bots WHERE TRUE", execute=True)

    async def delete_site(self):
        await self.execute("DELETE FROM sites WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
