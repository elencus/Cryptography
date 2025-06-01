from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_ecb(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad(plaintext, DES.block_size)
    return cipher.encrypt(padded)

def decrypt_ecb(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(ciphertext)
        return unpad(plaintext, DES.block_size)
    except ValueError:
        return plaintext  # Го враќаме текстот без да го отстраниме padding-от ако е невалиден

def encrypt_cbc(key, plaintext, iv=None):
    if iv is None:
        iv = os.urandom(DES.block_size)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded = pad(plaintext, DES.block_size)
    return iv + cipher.encrypt(padded)

def decrypt_cbc(key, ciphertext):
    iv = ciphertext[:DES.block_size]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    try:
        plaintext = cipher.decrypt(ciphertext[DES.block_size:])
        return unpad(plaintext, DES.block_size)
    except ValueError:
        return plaintext  # Го враќаме текстот без да го отстраниме padding-от ако е невалиден