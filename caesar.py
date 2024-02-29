from collections import Counter
import enchant

# jeszcze walidacja danych

class CaesarCipher:

    # Characters in order of their frequency in english language
    CHARS_BY_FREQUENCY = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c',
        'm', 'f', 'w', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z'
    ]
    LOWERCASE_A_CODE = 97
    LOWERCASE_Z_CODE = 122

    @staticmethod
    def cipher(text: str, shift: int) -> str:
        """
            Function which encrypts given text with a Caesar cipher
            using given shift parameter
        """
        ciphered_text = ''
        for char in text:
            if not char.isalpha():
                ciphered_text += char
                continue
            char = ord(char) + shift
            if char > CaesarCipher.LOWERCASE_Z_CODE:
                char = (CaesarCipher.LOWERCASE_A_CODE - 1) + (char - CaesarCipher.LOWERCASE_Z_CODE)
            char = chr(char)
            ciphered_text += char
        return ciphered_text

    @staticmethod
    def decipher(text: str, shift: int) -> str:
        """
            Function which decrypts given text encrypted from Caesar cipher
            using given shift parameter
        """
        deciphered_text = ''
        for char in text:
            if not char.isalpha():
                deciphered_text += char
                continue
            char = ord(char) - shift
            if char < CaesarCipher.LOWERCASE_A_CODE:
                char = CaesarCipher.LOWERCASE_Z_CODE - (CaesarCipher.LOWERCASE_A_CODE - 1 - char)
            char = chr(char)
            deciphered_text += char
        return deciphered_text

    @staticmethod
    def break_cipher(text: str) -> str:
        """
            Function which decrypts given text encrypted from Caesar cipher
            with unknown shift parameter
        """
        dictionary = enchant.Dict("en_US")
        characters = [char for char in text if char.isalpha()]
        most_common_char = Counter(characters).most_common(1)[0][0]
        longest_word = max(text.split(), key=len)
        for char in CaesarCipher.CHARS_BY_FREQUENCY:
            shift_parameter = abs(ord(most_common_char) - ord(char))
            deciphered_word = CaesarCipher.decipher(text=longest_word, shift=shift_parameter)
            if dictionary.check(deciphered_word):
                return CaesarCipher.decipher(text=text, shift=shift_parameter)
