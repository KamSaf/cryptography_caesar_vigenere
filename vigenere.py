# from collections import Counter
# import enchant

# jeszcze walidacja danych

class VigenereCipher:

    ALPHABET_LENGTH = 26
    ALPHABET = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def plain_text_colummn(char: str) -> str:
        char_index = VigenereCipher.ALPHABET.index(char)
        plain_text_column = VigenereCipher.ALPHABET[char_index:(VigenereCipher.ALPHABET_LENGTH)] + VigenereCipher.ALPHABET[0:char_index]
        return plain_text_column

    @staticmethod
    def cipher(text: str, keyword: str) -> str:
        """
            Function which encrypts given text with a Vigenere cipher
            using given keyword
        """
        ciphered_text = ''
        keyword_char_counter = 0
        for i in range(len(text)):
            if not text[i].isalpha():
                ciphered_text += text[i]
                continue

            keyword_char = keyword[keyword_char_counter]
            keyword_char_counter = (keyword_char_counter + 1) % len(keyword)

            plain_text_column = VigenereCipher.plain_text_colummn(text[i])
            ciphered_text += plain_text_column[VigenereCipher.ALPHABET.index(keyword_char)]
        return ciphered_text
