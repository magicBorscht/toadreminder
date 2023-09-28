import asyncio
import traceback
from typing import Callable

import aiocron
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse, Response
from fastapi.security import HTTPBearer

import logging

import api.toads.router
import api.gifters.router
import api.system.router
from tasks.birthday_reminder import zhaba

security = HTTPBearer()

logger = logging.getLogger("app")


def create_app() -> FastAPI:
    logger.info("starting server")
    tags = [
        {"name": "toad", "description": "Жабовладельческий строй"},
        {"name": "gift", "description": "Управление дарениями"},
        {"name": "system", "description": "Это мне нужно чтобы срать"},
    ]
    app = FastAPI(openapi_tags=tags, default_response_class=ORJSONResponse)

    app.include_router(api.toads.router.router, tags=["toad"])
    app.include_router(api.gifters.router.router, tags=["gift"])
    app.include_router(api.system.router.router, tags=["system"])

    @app.on_event("shutdown")
    async def _() -> None:
        logger.info("whatever man")
        # await models.base.engine.dispose()

    @app.middleware("http")
    async def framework_error(request: Request, call_next: Callable) -> Response:
        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(
                f"""
                {request.url} {e} {getattr(e, "args", None)} {getattr(e, "body", None)} {getattr(e, "errors", lambda: None)()} {traceback.format_exc()}
            """
            )
            raise e
        return response

    return app


async def run():
    app: FastAPI = create_app()

    # tasks
    aiocron.crontab("10 4 * * *", zhaba)

    # uvicorn start
    config = uvicorn.Config(app, loop="asyncio", host="0.0.0.0", port=5010, workers=4)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(run())
