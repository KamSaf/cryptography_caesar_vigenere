# from collections import Counter
# import enchant

# jeszcze walidacja danych

class VigenereCipher:

    ALPHABET_LENGTH = 26
    ALPHABET = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def __plain_text_colummn(char: str) -> str:
        """
            Function which creates plaintext array column required for Vigenere cipher
        """
        char_index = VigenereCipher.ALPHABET.index(char)
        plain_text_column = VigenereCipher.ALPHABET[char_index:(VigenereCipher.ALPHABET_LENGTH)] + VigenereCipher.ALPHABET[0:char_index]
        return plain_text_column

    @staticmethod
    def cipher(text: str, keyword: str) -> str:
        """
            Function which encrypts given text with a Vigenere cipher
            using given keyword
        """
        ciphered_text = []
        keyword_char_counter = 0
        for i in range(len(text)):
            if not text[i].isalpha():
                ciphered_text.append(text[i])
                continue

            keyword_char = keyword[keyword_char_counter]
            keyword_char_counter = (keyword_char_counter + 1) % len(keyword)
            plain_text_column = VigenereCipher.__plain_text_colummn(text[i])
            ciphered_text.append(plain_text_column[VigenereCipher.ALPHABET.index(keyword_char)])
        return ''.join(ciphered_text)

    @staticmethod
    def decipher(text: str, keyword: str) -> str:
        """
            Function which decrypts given text from a Vigenere cipher
            using given keyword.
        """
        #  The keyword is being reversed and then used as a new keyword in cipher operation which results in encrypted text
        reversed_keyword = [VigenereCipher.ALPHABET[(VigenereCipher.ALPHABET_LENGTH - (ord(keyword[i]) - 97)) % VigenereCipher.ALPHABET_LENGTH] for i in range(len(keyword))]
        return VigenereCipher.cipher(text=text, keyword=reversed_keyword)

    @staticmethod
    def break_cipher(text: str) -> str:
        chars_indexes = []
        for char in text:
            chars_indexes.append(str(VigenereCipher.ALPHABET.index(char)))
        return chars_indexes
