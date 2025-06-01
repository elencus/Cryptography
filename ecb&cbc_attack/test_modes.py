from cipher_modes import encrypt_ecb, decrypt_ecb, encrypt_cbc, decrypt_cbc

key = b'8bytekey'
plaintext = b'This is a secret message!'

# Test ECB mode
ecb_cipher = encrypt_ecb(key, plaintext)
ecb_plain = decrypt_ecb(key, ecb_cipher)
print("ECB Test:", ecb_plain == plaintext)

# Test CBC mode
cbc_cipher = encrypt_cbc(key, plaintext)
cbc_plain = decrypt_cbc(key, cbc_cipher)
print("CBC Test:", cbc_plain == plaintext)