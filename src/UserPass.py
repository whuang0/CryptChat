from encrypting import *
from Crypto.Cipher import AES 
username = 'candycane'
password = ''
username = encryption()
nonce, cipherText, tag = username.encrypt()
plainText = username.decrypt(nonce, cipherText, tag)

print(f"Cipher text: {cipherText}")
if not plainText: 
    print("Message is corrupted")
else: 
    print(f"Plaintext: {plainText}")
