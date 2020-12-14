from fastapi import APIRouter
from app.model.city import City

db = []
router = APIRouter()


@router.get("/cities")
def get_cities():
    return db


@router.get("/cities/{city_id}")
def get_city(city_id: int):
    for city in db:
        if city.id == city_id:
            return city
    return {}


@router.post("/cities")
def create_city(city: City):
    db.append(city)
    return db
