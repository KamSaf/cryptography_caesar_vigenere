from english_words import get_english_words_set
import enchant


class VigenereCipher:

    ALPHABET_LENGTH = 26
    ALPHABET = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    CHARS_BY_FREQUENCY = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c',
        'm', 'f', 'w', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z'
    ]

    @staticmethod
    def __validate_data(text: str, keyword: str = None, keyword_length: int = None) -> bool:
        """
            Function validating data given by user
        """
        if not isinstance(text, str):
            return False
        if keyword_length and not isinstance(keyword_length, int):
            return False
        if keyword and (not isinstance(keyword, str) or len(keyword) != keyword_length):
            return False
        return True

    @staticmethod
    def __plain_text_colummn(char: str) -> str | bool:
        """
            Function which creates plaintext array column required for Vigenere cipher
        """
        char_index = VigenereCipher.ALPHABET.index(char)
        plain_text_column = VigenereCipher.ALPHABET[char_index:(VigenereCipher.ALPHABET_LENGTH)] + VigenereCipher.ALPHABET[0:char_index]
        return plain_text_column

    @staticmethod
    def cipher(text: str, keyword: str) -> str | bool:
        """
            Function which encrypts given text with a Vigenere cipher
            using given keyword. Encrypted text is lower case
        """
        if not VigenereCipher.__validate_data(text=text, keyword=keyword, keyword_length=len(keyword)):
            return False

        ciphered_text = []
        keyword_char_counter = 0
        for i in range(len(text)):
            if not text[i].isalpha():
                ciphered_text.append(text[i])
                continue

            keyword_char = keyword[keyword_char_counter].lower()
            keyword_char_counter = (keyword_char_counter + 1) % len(keyword)
            plain_text_column = VigenereCipher.__plain_text_colummn(text[i].lower())
            ciphered_text.append(plain_text_column[VigenereCipher.ALPHABET.index(keyword_char)])
        return ''.join(ciphered_text)

    @staticmethod
    def decipher(text: str, keyword: str) -> str | bool:
        """
            Function which decrypts given text from a Vigenere cipher
            using given keyword. Decrypted text is lower case
        """
        #  The keyword is being reversed and then used as a new keyword in cipher operation which results in encrypted text
        reversed_keyword = [VigenereCipher.ALPHABET[(VigenereCipher.ALPHABET_LENGTH - (ord(keyword[i]) - 97)) % VigenereCipher.ALPHABET_LENGTH] for i in range(len(keyword))]
        return VigenereCipher.cipher(text=text, keyword=''.join(reversed_keyword))

    @staticmethod
    def break_cipher(text: str) -> str | bool:
        """
            Function which decrypts given text encrypted with Vigenere cipher
            with unknown 3 letter long keyword (english). Decrypted text is lower case
        """
        if not VigenereCipher.__validate_data(text=text, keyword_length=3):
            return False

        KEYWORD_LENGTH = 3
        keys = [word for word in get_english_words_set(['web2'], lower=True, alpha=True) if len(word) == KEYWORD_LENGTH]
        dictionary = enchant.Dict("en_US")

        for key in keys:
            deciphered_text = VigenereCipher.decipher(text=text, keyword=key)

            if dictionary.check(max(deciphered_text.split(), key=len)):
                return deciphered_text
        return None
