import datetime
import logging

logger = logging.getLogger("app")


async def zhaba() -> None:
    logger.info("THE TOAD CROAKS")
    await analytics_sync("websites")
    await analytics_sync("pages")
    await analytics_sync("userhaswebsites")
