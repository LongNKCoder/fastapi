from fastapi import FastAPI
from api import api

app = FastAPI()
app.include_router(api.api_router, prefix="/api")


@app.get("/")
async def home():
    return {"No": "Static files"}
