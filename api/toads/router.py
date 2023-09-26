from fastapi import APIRouter

from api.toads.handlers import router as toad_router

router = APIRouter(prefix="/toads")

router.include_router(toad_router)
