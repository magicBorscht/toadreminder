from fastapi import APIRouter

from api.gifters.handlers import router as gift_router

router = APIRouter(prefix="/gifters")

router.include_router(gift_router)
