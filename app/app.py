from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers import caesar, vigenere


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(caesar.router)
app.include_router(vigenere.router)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
