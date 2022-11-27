import aes, os

text = 'Hello world'

key = os.urandom(16)

iv = os.urandom(16)

encrypted = aes.AES(key).encrypt_ctr(text.encode(), iv)
decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)

print(f'Input text              :{text}')
print(f'Input text in bytes     :{text.encode().hex()}')
print(f'Key                     :{key.hex()}')
print(f'IV                      :{iv.hex()}')
print(f'Encrypted text          :{encrypted.hex()}')
print(f'Decrypted text in bytes :{decrypted}')
print(f'Decrypted text          :{decrypted.decode()}')