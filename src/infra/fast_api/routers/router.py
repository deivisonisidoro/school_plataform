from fastapi import APIRouter

from src.infra.fast_api.routers import user

router = APIRouter()

router.include_router(user.router, prefix="/users", tags=["User"])
