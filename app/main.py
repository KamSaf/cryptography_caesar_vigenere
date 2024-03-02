from utils.caesar import CaesarCipher
from utils.vigenere import VigenereCipher


### CAESAR ###

# text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
# shift = 3
# ciphered_text = "wkh txlfn eurzq ira mxpsv ryhu d odcb grj dqg d vzliw kduh gdvkhv wkurxjk wkh juhhq phdgrz zkloh wkh zlqg jhqwob zklvshuv lq wkh wdoo judvv"

# ciphered_text = CaesarCipher.cipher(text=text, shift=shift)
# deciphered_text = CaesarCipher.decipher(text=ciphered_text, shift=shift)
# broken_cipher = CaesarCipher.break_cipher(text=ciphered_text)
# print(ciphered_text)
# print(deciphered_text)
# print(broken_cipher)

# print(f'Text: {text}\n\nCiphered text (shift = 3): {ciphered_text}\n\nDeciphered text (shift = 3): {deciphered_text}\n\nBroken cipher: {broken_cipher}')



### VIGNERE ###

# text = "the quick brown fox jumps over a lazy dog and a swift hare dashes through the green meadow while the wind gently whispers in the tall grass"
# text = "dlc mizfu fpkke iyb hqagv yzcn o cdjc bku rqn e qswww repa rrvriq pvirekf pvv jbicj avdnsu svzoo xfa kzqn kcjhcb glgodvuc ml pvv wkpj cfrvc"
# text2 = "dlc aygmo zbsux jmh nswtq yzcb e jkdw nse krb k wusjr repo hyclcc xfbssql rri ebicx qckhmg afspc dlc gmln kcxxji afswnovq sr rri rkpj qvycw"

# keyword = "key"

# ciphered_text = VigenereCipher.cipher(text=text, keyword=keyword)
# print(ciphered_text)
# print(VigenereCipher.decipher(text=text2, keyword=keyword))

# print(VigenereCipher.break_cipher(text=ciphered_text, keyword_length=3))
# deciphered_text = VigenereCipher.break_cipher(text=text2)
# print(text2)
# print(deciphered_text)


# f o b
