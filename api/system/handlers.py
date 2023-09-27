from fastapi import APIRouter
import aiosqlite
from schemas.toads import ToadDataSchema, ToadSchema
import logging
from typing import List
from tools.sender import TelegramSenderBuilder

router = APIRouter()

logger = logging.getLogger("app")


@router.post("/tg_ping")
async def ping_telegram():
    with TelegramSenderBuilder() as sender:
        pass
