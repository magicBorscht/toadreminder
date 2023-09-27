from fastapi import APIRouter

from api.system.handlers import router as system_router

router = APIRouter(prefix="/system")

router.include_router(system_router)
