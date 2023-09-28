from __future__ import annotations

import logging

import aiohttp

from secret_stuff import settings

logger = logging.getLogger("app")


class TelegramSenderBuilder:
    def __init__(
            self: TelegramSenderBuilder
    ) -> None:
        self._credentials = {"BOT_TOKEN": settings.tg_bot}

    async def send_message(self: TelegramSenderBuilder, recipient: str, text: str) -> None:
        url = f"https://api.telegram.org/bot{self._credentials['BOT_TOKEN']}/sendMessage"
        async with aiohttp.ClientSession() as session:
            message = {
                "chat_id": recipient,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": "true",
            }
            async with session.request("POST", url, json=message) as response:
                if response.status != 200:
                    logger.error(
                        "unable to send telegram status: {0} content : {1}".format(
                            response.status, await response.json()
                        )
                    )

    async def send(self: TelegramSenderBuilder, recipient: str, message: str) -> None:
        await self.send_message(recipient, message)
