from utils import caesar


def test_cipher():
    text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
    shift = 3
    ciphered_text = Caesar.cipher(text=text, shift=shift)
    correctly_ciphered_text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"

    assert ciphered_text == correctly_ciphered_text


def test_decipher():
    text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"
    shift = 3
    deciphered_text = Caesar.decipher(text=text, shift=shift)
    correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

    assert deciphered_text == correctly_deciphered_text


def test_cipher_break():
    text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"
    deciphered_text = Caesar.break_cipher(text=text)
    correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

    assert deciphered_text == correctly_deciphered_text
