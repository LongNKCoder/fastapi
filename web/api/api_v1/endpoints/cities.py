from fastapi import APIRouter
from web.model.city import City

db = []
router = APIRouter()


@router.get("/")
async def get_cities():
    return db


@router.get("/{city_id}")
async def get_city(city_id: int):
    for city in db:
        if city.id == city_id:
            return city
    return {}


@router.post("/")
async def create_city(city: City):
    db.append(city)
    return db
