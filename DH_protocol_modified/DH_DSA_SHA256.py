import hashlib
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class User:
    def __init__(self, name):
        self.name = name
        self.dsa_private_key = DSA.generate(2048)
        self.dsa_public_key = self.dsa_private_key.publickey()
        self.shared_secret = None

    def sign(self, message):
        hash_obj = SHA256.new(message)
        signer = DSS.new(self.dsa_private_key, 'fips-186-3')
        return signer.sign(hash_obj)

    def verify(self, message, signature, public_key):
        hash_obj = SHA256.new(message)
        verifier = DSS.new(public_key, 'fips-186-3')
        try:
            verifier.verify(hash_obj, signature)
            return True
        except ValueError:
            return False

    def encrypt(self, key, message):
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(message, AES.block_size))
        return cipher.iv + ct_bytes

    def decrypt(self, key, ciphertext):
        iv = ciphertext[:16]
        ct = ciphertext[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size)

# Diffie-Hellman параметри
def diffie_hellman_key_exchange():
    p = 0xFD7F53811D75122952DF4A9C2EECE4E7F6112E7761B5D386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
    g = 2
    a = int.from_bytes(get_random_bytes(32), 'big') % p
    b = int.from_bytes(get_random_bytes(32), 'big') % p
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_key_alice = pow(B, a, p)
    shared_key_bob = pow(A, b, p)
    assert shared_key_alice == shared_key_bob
    shared_secret = hashlib.sha256(str(shared_key_alice).encode()).digest()[:16]
    return A, B, shared_secret


def protocol():
    alice = User("Alice")
    bob = User("Bob")

    # DH размена
    A, B, shared_key = diffie_hellman_key_exchange()
    print("Alice → Bob: A =", A)

    # Bob потпишува (B, A), го енкриптира и праќа
    signed_by_bob = bob.sign(f"{B},{A}".encode())
    encrypted_payload = bob.encrypt(shared_key, signed_by_bob)
    print("Bob → Alice: B =", B, ", Encrypted Sig =", encrypted_payload.hex())

    # Alice ја дешифрира пораката и верификува потписот
    decrypted_signature = alice.decrypt(shared_key, encrypted_payload)
    if alice.verify(f"{B},{A}".encode(), decrypted_signature, bob.dsa_public_key):
        print("Alice го верификува потписот на Bob.")
    else:
        print("Потписот на Bob е невалиден!")

    # Alice потпишува (A, B), енкриптира и праќа назад
    signed_by_alice = alice.sign(f"{A},{B}".encode())
    encrypted_response = alice.encrypt(shared_key, signed_by_alice)
    print("Alice → Bob: Encrypted Sig =", encrypted_response.hex())

    # Bob ја дешифрира пораката и верификува
    decrypted_response = bob.decrypt(shared_key, encrypted_response)
    if bob.verify(f"{A},{B}".encode(), decrypted_response, alice.dsa_public_key):
        print("Bob го верификува потписот на Alice.")
        print("🔐 Secure communication established.")
    else:
        print("Потписот на Alice е невалиден!")

protocol()