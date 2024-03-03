from utils.vigenere import VigenereCipher as Vigenere


class TestVigenereCipher:

    #  Encrypting test
    def test_vigenere_cipher(self):
        text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
        keyword = 'keyword'
        ciphered_text = Vigenere.cipher(text=text, keyword=keyword)
        correctly_ciphered_text = "dlc mizfu fpkke iyb hqagv yzcn o cdjc bku rqn e qswww repa rrvriq pvirekf pvv jbicj avdnsu svzoo xfa kzqn kcjhcb glgodvuc ml pvv wkpj cfrvc"

        assert ciphered_text == correctly_ciphered_text

    #  Decrypting test
    def test_vigenere_decipher(self):
        text = "dlc mizfu fpkke iyb hqagv yzcn o cdjc bku rqn e qswww repa rrvriq pvirekf pvv jbicj avdnsu svzoo xfa kzqn kcjhcb glgodvuc ml pvv wkpj cfrvc"
        keyword = 'keyword'
        deciphered_text = Vigenere.decipher(text=text, keyword=keyword)
        correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

        assert deciphered_text == correctly_deciphered_text

    #  Cipher breaking test
    def test_vigenere_cipher_break(self):
        text = "dlc aygmo zbsux jmh nswtq yzcb e jkdw nse krb k wusjr repo hyclcc xfbssql rri ebicx qckhmg afspc dlc gmln kcxxji afswnovq sr rri rkpj qvycw"
        #  Assuming keyword is 3 characters long english word
        deciphered_text = Vigenere.break_cipher(text=text)
        correctly_deciphered_text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"

        assert deciphered_text == correctly_deciphered_text

    #  Test plaintext column generation
    def test_plaintext_column(self):
        correct_column = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
        assert Vigenere._VigenereCipher__plain_text_colummn(char='d') == correct_column

    #  Test data validation - valid data - text: str, keyword: str, keyword_length: int
    def test_vigenere_validate_data_is_valid(self):
        assert Vigenere._VigenereCipher__validate_data(text='text', keyword='key', keyword_length=3) is True

    #  Test data validation - invalid data - text is not a string
    def test_vigenere_validate_data_invalid_text(self):
        assert Vigenere._VigenereCipher__validate_data(text=1) is False

    #  Test data validation - invalid data - keyword is not a string
    def test_vigenere_validate_data_invalid_keyword(self):
        assert Vigenere._VigenereCipher__validate_data(text='text', keyword=123) is False

    #  Test data validation - invalid data - keyword_length is not an integer
    def test_vigenere_validate_data_invalid_keyword_length(self):
        assert Vigenere._VigenereCipher__validate_data(text='text', keyword='key', keyword_length='123') is False

    #  Test data validation - invalid data - keyword_length is not equal to length of keyword
    def test_vigenere_validate_data_invalid_keyword_length_not_equal(self):
        assert Vigenere._VigenereCipher__validate_data(text='text', keyword='key', keyword_length=4) is False
