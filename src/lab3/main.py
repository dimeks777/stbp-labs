from my_rsa import RSA, RSAKey
import rsa

def my_rsa(text, bits):
    key = RSAKey(bits=bits)
    public_key = (key.e, key.N)
    private_key = (key.d, key.N)

    print(f'Public key       : {public_key}')
    print(f'Private key      : {private_key}')
    cipher = RSA(key)

    encrypted = cipher.encrypt_data(text.encode())

    print(f'Original text    : {text}')
    print(f'Encrypted text   : {encrypted.hex()}')

    decrypted = cipher.decrypt_data(encrypted)
    print(f'Decrypted text   : {decrypted.decode()}')


def rsa_lib(text, bits):
    public_key, private_key = rsa.newkeys(bits)
    print(f'Public key       : {public_key}')
    print(f'Private key      : {private_key}')

    encrypted = rsa.encrypt(text.encode(), public_key)

    print(f'Original text     : {text}')
    print(f'Encrypted text    : {encrypted.hex()}')

    decrypted = rsa.decrypt(encrypted, private_key)

    print(f'Decrypted text    : {decrypted.decode()}')


if __name__ == '__main__':
    TEXT = 'Hello world'
    BITS = 1024

    title1 = "Custom RSA implementation"
    print("="*(82 + len(title1)))
    print("="*40, title1, "="*40)
    print("="*(82 + len(title1)))
    my_rsa(TEXT, BITS)

    print()
    title2 = "RSA from lib"
    print("="*(82 + len(title2)))
    print("="*40, title2, "="*40)
    print("="*(82 + len(title2)))
    rsa_lib(TEXT, BITS)
