from fastapi import Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.caesar import CaesarCipher as Caesar


router = APIRouter()
templates = Jinja2Templates(directory="templates")


#  Caesar routes

@router.get("/caesar", response_class=HTMLResponse)
async def caesar(request: Request):
    return templates.TemplateResponse(request=request, name="caesar.html")


@router.post("/caesar_encode", response_class=HTMLResponse)
async def caesar_encode(request: Request, text: str = Form(..., description='text'), shift: int = Form(..., description='shift')):
    encoded_text = Caesar.cipher(text=text, shift=shift)
    if encoded_text:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_encode': text, 'encoded_text': encoded_text, 'shift_encode': shift, 'error_encode': False})
    else:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_encode': text, 'shift_encode': shift, 'error_encode': True})


@router.post("/caesar_decode", response_class=HTMLResponse)
async def caesar_decode(request: Request, text: str = Form(..., description='text'), shift: int = Form(..., description='shift')):
    decoded_text = Caesar.decipher(text=text, shift=shift)
    if decoded_text:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_decode': text, 'decoded_text': decoded_text, 'shift_decode': shift, 'error_decode': False})
    else:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_decode': text, 'shift_decode': shift, 'error_decode': True})


@router.post("/caesar_break_cipher", response_class=HTMLResponse)
async def caesar_break_cipher(request: Request, text: str = Form(..., description='text')):
    decoded_text = Caesar.break_cipher(text=text)
    if decoded_text:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_break_code': text, 'broken_code': decoded_text, 'error_break_code': False})
    else:
        return templates.TemplateResponse(request=request, name="caesar.html", context={'input_text_break_code': text, 'error_break_code': True})
