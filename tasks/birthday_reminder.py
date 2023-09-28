import datetime
import logging

import aiosqlite

from schemas.toads import ToadSchema

from config import settings

logger = logging.getLogger("app")


async def zhaba() -> None:
    logger.info("THE TOAD CROAKS")
    today = datetime.date.today().strftime("%Y-%m-%d")
    not_today = datetime.date.today() + datetime.timedelta(days=settings.days_to_prepare + 1)
    not_today = not_today.strftime("%Y-%m-%d")
    async with aiosqlite.connect("./toads.db") as db:
        cursor = await db.execute(
            f"""
                SELECT * FROM toads 
                    WHERE date('{today}') < date(toads.birthday)
                    AND date(toads.birthday) < date('{not_today}')
                    AND toads.manager_notified = 0
            """
        )
        toads = await cursor.fetchall()
        if not toads:
            logger.info("No toads for today, going back to sleep. . .")
            return

        for toad in await cursor.fetchall():
            toad = ToadSchema.from_list(toad)
            # сделать выборку рандомных строк, или здесь, или каким-то образом через конст
            # но нужен инсерт переменных, притом разных (падежи пердежи)

            # сделать выборку ответственного через toadgift и toads одним запросом
            strings = [

            ]
