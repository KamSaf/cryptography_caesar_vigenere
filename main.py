from caesar import CaesarCipher
from vigenere import VigenereCipher

### CAESAR ###

# text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
# shift = 3
# ciphered_text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"

# ciphered_text = CaesarCipher.cipher(text, shift)
# deciphered_text = CaesarCipher.decipher(ciphered_text, shift)
# broken_cipher = CaesarCipher.break_cipher(ciphered_text)

# print(f'Text: {text}\n\nCiphered text (shift = 3): {ciphered_text}\n\nDeciphered text (shift = 3): {deciphered_text}\n\nBroken cipher: {broken_cipher}')



### VIGNERE ###

# text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
# keyword = "secret"
# ciphered_text = VigenereCipher.cipher(text=text, keyword=keyword)


text = "vigenere"
keyword = "key"

print(VigenereCipher.cipher(text=text, keyword=keyword))
print(VigenereCipher.decipher(text=VigenereCipher.cipher(text=text, keyword=keyword), keyword=keyword))

# print(VigenereCipher.break_cipher(text=text))
