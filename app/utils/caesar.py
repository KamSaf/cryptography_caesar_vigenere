from collections import Counter
import enchant

class CaesarCipher:

    # Characters in order of their frequency in english language
    CHARS_BY_FREQUENCY = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c',
        'm', 'f', 'w', 'g', 'y', 'p', 'b', 'v', 'k', 'x', 'j', 'q', 'z'
    ]
    LOWERCASE_A_CODE = 97
    LOWERCASE_Z_CODE = 122

    @staticmethod
    def __validate_data(text: str, shift: int = None) -> bool:
        """
            Function validating data given by user
        """
        if not isinstance(text, str):
            return False
        if shift and not isinstance(shift, int):
            return False
        return True

    @staticmethod
    def cipher(text: str, shift: int) -> str | bool:
        """
            Function which encrypts given text with a Caesar cipher
            using given shift parameter
        """
        if not CaesarCipher.__validate_data(text=text, shift=shift):
            return False
        
        ciphered_text = []
        for char in text:
            if not char.isalpha():
                ciphered_text.append(char)
                continue
            char = ord(char) + shift
            if char > CaesarCipher.LOWERCASE_Z_CODE:
                char = (CaesarCipher.LOWERCASE_A_CODE - 1) + (char - CaesarCipher.LOWERCASE_Z_CODE)
            char = chr(char)
            ciphered_text.append(char)
        return ''.join(ciphered_text)

    @staticmethod
    def decipher(text: str, shift: int) -> str | bool:
        """
            Function which decrypts given text encrypted from Caesar cipher
            using given shift parameter
        """
        if not CaesarCipher.__validate_data(text=text, shift=shift):
            return False

        deciphered_text = []
        for char in text:
            if not char.isalpha():
                deciphered_text.append(char)
                continue
            char = ord(char) - shift
            if char < CaesarCipher.LOWERCASE_A_CODE:
                char = CaesarCipher.LOWERCASE_Z_CODE - (CaesarCipher.LOWERCASE_A_CODE - 1 - char)
            char = chr(char)
            deciphered_text.append(char)
        return ''.join(deciphered_text)

    @staticmethod
    def break_cipher(text: str) -> str | bool:
        """
            Function which decrypts given text encrypted with Caesar cipher
            with unknown shift parameter
        """
        if not CaesarCipher.__validate_data(text=text):
            return False

        dictionary = enchant.Dict("en_US")
        characters = [char for char in text if char.isalpha()]
        most_common_char = Counter(characters).most_common(1)[0][0]
        longest_word = max(text.split(), key=len)
        for char in CaesarCipher.CHARS_BY_FREQUENCY:
            shift_parameter = abs(ord(most_common_char) - ord(char))
            deciphered_word = CaesarCipher.decipher(text=longest_word, shift=shift_parameter)
            if dictionary.check(deciphered_word):
                return CaesarCipher.decipher(text=text, shift=shift_parameter)
