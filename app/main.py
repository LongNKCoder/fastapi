from typing import Optional
from fastapi import FastAPI
from app.router import city_router

app = FastAPI()
app.include_router(city_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
