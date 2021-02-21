from fastapi import APIRouter
from web.api.api_v1.endpoints import cities, users

router = APIRouter()
router.include_router(cities.router, prefix="/cities", tags=["cities"])
router.include_router(users.router, prefix="/users", tags=["users"])
