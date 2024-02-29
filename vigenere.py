from collections import Counter
from english_words import get_english_words_set
import enchant

# jeszcze walidacja danych

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
        KEYWORD_LENGTH = 3
        keys = [word for word in get_english_words_set(['web2'], lower=True, alpha=True) if len(word) == KEYWORD_LENGTH]
        dictionary = enchant.Dict("en_US")

        for key in keys:
            deciphered_text = VigenereCipher.decipher(text=text, keyword=key)

            if dictionary.check(max(deciphered_text.split(), key=len)):
                return deciphered_text
        return None


        # print('dupa')
        # characters = [char for char in text if char.isalpha()]
        # common_code_chars = {i: [i] for i in range(keyword_length)}
        # most_common_encrypted_char = Counter(characters).most_common(1)[0][0]

        # for value in common_code_chars.values():
            # while (value[-1] + keyword_length < len(characters)):
                # value.append(value[-1] + keyword_length)
        # return common_code_chars

        # text_segments = []
        # text_split_start = 0
        # text_split_stop = keyword_length
        # for _ in range(keyword_length):
            # text_segments.append(text[text_split_start:text_split_stop])
            # text_split_start = text_split_stop
            # if text_split_stop + keyword_length < len(text):
                # text_split_stop += keyword_length
            # else:
                # text_split_stop = len(text)
        # return text_segments




# 1: 0, 3, 6, 9
# 2: 1, 4, 7, 10
# 3: 2, 5, 8, 11