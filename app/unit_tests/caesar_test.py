from utils.caesar import CaesarCipher as Caesar


class TestCaesarCipher:

    #  Encrypting test
    def test_caesar_cipher(self):
        text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
        shift = 3
        ciphered_text = Caesar.cipher(text=text, shift=shift)
        correctly_ciphered_text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"

        assert ciphered_text == correctly_ciphered_text

    #  Decrypting test
    def test_caesar_decipher(self):
        text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"
        shift = 3
        deciphered_text = Caesar.decipher(text=text, shift=shift)
        correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

        assert deciphered_text == correctly_deciphered_text

    #  Cipher breaking test
    def test_caesar_cipher_break(self):
        text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"
        deciphered_text = Caesar.break_cipher(text=text)
        correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

        assert deciphered_text == correctly_deciphered_text

    #  Test data validation - valid data - text: str, shift: int
    def test_caesar_validate_data_is_valid(self):
        assert Caesar._CaesarCipher__validate_data(text='text', shift=3) is True

    #  Test data validation - valid data - text: str, shift: not given
    def test_caesar_validate_data_no_shift_is_valid(self):
        assert Caesar._CaesarCipher__validate_data(text='text') is True

    #  Test data validation - invalid data - text is not a string
    def test_caesar_validate_data_invalid_text(self):
        assert Caesar._CaesarCipher__validate_data(text=1) is False

    #  Test data validation - invalid data - shift is not an integer
    def test_caesar_validate_data_invalid_shift(self):
        assert Caesar._CaesarCipher__validate_data(text='text', shift='shift') is False
