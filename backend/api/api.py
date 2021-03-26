from fastapi import APIRouter
from api.api_v1 import api_v1

api_router = APIRouter()
api_router.include_router(api_v1.router, prefix="/v1")
