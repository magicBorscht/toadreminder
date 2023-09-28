import logging

from fastapi import APIRouter

from tools.sender import TelegramSenderBuilder

router = APIRouter()

logger = logging.getLogger("app")


@router.post("/tg_ping")
async def ping_telegram():
    sender = TelegramSenderBuilder()
    await sender.send("2243149", "ping")
