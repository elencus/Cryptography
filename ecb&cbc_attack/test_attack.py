from cipher_modes import encrypt_ecb, decrypt_ecb, encrypt_cbc, decrypt_cbc
from cut_and_paste import cut_and_paste_ecb, cut_and_paste_cbc

key = b'8bytekey'
plaintext = b'This is a secret message!'

# ECB напад
print("\nECB Исечи и залепи напад:")
ecb_cipher = encrypt_ecb(key, plaintext)
modified_ecb = cut_and_paste_ecb(ecb_cipher, blocks_to_reorder=[2, 1, 0, 3])
decrypted = decrypt_ecb(key, modified_ecb)
print("Оригинален текст:", plaintext)
print("Модифициран текст:", decrypted)


# CBC напад
print("\nCBC Исечи и залепи напад:")
cbc_cipher = encrypt_cbc(key, plaintext)
modified_cbc = cut_and_paste_cbc(cbc_cipher, blocks_to_reorder=[2, 1, 0, 3])
decrypted = decrypt_cbc(key, modified_cbc)
print("Оригинален текст:", plaintext)
print("Модифициран текст:", decrypted)
