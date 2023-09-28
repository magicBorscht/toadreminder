import logging
from typing import List

import aiosqlite
from fastapi import APIRouter

from schemas.toads import ToadDataSchema, ToadSchema

router = APIRouter()

logger = logging.getLogger("app")


@router.get("/")
async def get_toads() -> List[ToadSchema]:
    async with aiosqlite.connect("./toads.db") as db:
        cursor = await db.execute("SELECT * FROM toads")
        resp = [ToadSchema.from_list(toad) for toad in await cursor.fetchall()]
        return resp


@router.post("/toads/new")
async def create_toad(data: ToadDataSchema):
    async with aiosqlite.connect("./toads.db") as db:
        await db.execute(
            f"""
                INSERT INTO toads (name,name_gen,tg_handler,birthday, name_dat)
                VALUES ('{data.name}', '{data.name_gen}', 
                '{data.tg_handler}', '{data.birthday}',
                '{data.name_dat}')
            """
        )
        await db.commit()


@router.delete("/toads/{toad_id}/delete")
async def delete_toad(toad_id: int):
    async with aiosqlite.connect("./toads.db") as db:
        await db.execute(
            f"""
                DELETE FROM toads WHERE id = {toad_id}
            """
        )
