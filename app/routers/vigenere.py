from fastapi import Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.vigenere import VigenereCipher as Vigenere


router = APIRouter()
templates = Jinja2Templates(directory="templates")


# Vigenere routes

@router.get("/vigenere", response_class=HTMLResponse)
async def vigenere(request: Request):
    return templates.TemplateResponse(request=request, name="vigenere.html")


@router.post("/vigenere_encode", response_class=HTMLResponse)
async def vigenere_encode(request: Request, text: str = Form(..., description='text'), keyword: str = Form(..., description='keyword')):
    encoded_text = Vigenere.cipher(text=text, keyword=keyword)
    if encoded_text:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_encode': text, 'encoded_text': encoded_text, 'keyword_encode': keyword, 'error_encode': False})
    else:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_encode': text, 'keyword_encode': keyword, 'error_encode': True})


@router.post("/vigenere_decode", response_class=HTMLResponse)
async def vigenere_decode(request: Request, text: str = Form(..., description='text'), keyword: str = Form(..., description='keyword')):
    decoded_text = Vigenere.decipher(text=text, keyword=keyword)
    if decoded_text:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_decode': text, 'decoded_text': decoded_text, 'keyword_decode': keyword, 'error_decode': False})
    else:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_decode': text, 'keyword_decode': keyword, 'error_decode': True})


@router.post("/vigenere_break_cipher", response_class=HTMLResponse)
async def vigenere_break_cipher(request: Request, text: str = Form(..., description='text')):
    decoded_text = Vigenere.break_cipher(text=text)
    if decoded_text:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_break_code': text, 'broken_code': decoded_text, 'error_break_code': False})
    else:
        return templates.TemplateResponse(request=request, name="vigenere.html", context={'input_text_break_code': text, 'error_break_code': True})
