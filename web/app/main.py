from fastapi import FastAPI, templating, Request, responses
from web.api import api

app = FastAPI()
templates = templating.Jinja2Templates("templates")
app.include_router(api.api_router, prefix="/api")


@app.get("/", response_class=responses.HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="main.html", context={"request": request})
