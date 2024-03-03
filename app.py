from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


#  Caesar

@app.get("/caesar", response_class=HTMLResponse)
async def caesar(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text': 'input', 'output_text': 'output', 'shift': 3})


@app.post("/caesar_encode", response_class=HTMLResponse)
async def caesar_encode(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


@app.post("/caesar_decode", response_class=HTMLResponse)
async def caesar_decode(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


@app.get("/caesar_break_cipher", response_class=HTMLResponse)
async def caesar_break_cipher(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


# Vigenere

@app.get("/vigenere", response_class=HTMLResponse)
async def vigenere(request: Request):
    return templates.TemplateResponse(request=request, name="vigenere.html")


@app.post("/vigenere_encode", response_class=HTMLResponse)
async def vigenere_encode(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


@app.post("/vigenere_decode", response_class=HTMLResponse)
async def vigenere_decode(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


@app.get("/vigenere_break_cipher", response_class=HTMLResponse)
async def vigenere_break_cipher(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")
