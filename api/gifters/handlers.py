from fastapi import APIRouter
import aiosqlite
from schemas.gifters import GifterDataSchema, GifterSchema
import logging
from typing import List

router = APIRouter()

logger = logging.getLogger("app")


@router.get("/")
async def get_gifters() -> List[GifterSchema]:
    async with aiosqlite.connect("./toads.db") as db:
        cursor = await db.execute("SELECT * FROM toadgift")
        # просто сделать иннер джоин для получения имён
        resp = []
        for toad in await cursor.fetchall():
            schemated_toad = GifterSchema.from_list(toad)
            resp.append(schemated_toad)
        return resp


@router.post("/new")
async def create_gifter(data: GifterDataSchema):
    async with aiosqlite.connect("./toads.db") as db:
        await db.execute(
            f"""
                INSERT INTO toadgift (gift_manager, gift_receiver)
                VALUES ('{data.gift_manager}', '{data.gift_receiver}')
            """
        )
        await db.commit()


@router.delete("/{gifter_id}/delete")
async def delete_gifter(gifter_id: int):
    async with aiosqlite.connect("./toads.db") as db:
        await db.execute(
            f"""
                DELETE FROM toadgift WHERE id = {gifter_id}
            """
        )


@router.patch("/{gifter_id}/edit/")
async def edit_gifter(gifter_id: int, data: GifterDataSchema):
    async with aiosqlite.connect("./toads.db") as db:
        await db.execute(
            f"""
                UPDATE toadgift SET gift_manager = {data.gift_manager}
                                    gift_receiver = {data.gift_receiver}
                WHERE id = {gifter_id}
            """
        )
        await db.commit()
