from fastapi import APIRouter

from src.main.fast_api.routers import users
from src.main.fast_api.routers import swagger_api

router = APIRouter()

router.include_router(swagger_api.router, prefix="", tags=["Swagger Redirect"])
router.include_router(users.router, prefix="/users", tags=["User"])
