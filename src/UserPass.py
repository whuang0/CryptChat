from encrypting import *
from Crypto.Cipher import AES 
password = ''
username = encryption('candycane')
nonce, cipherText, tag = username.encrypt()
plainText = username.decrypt(nonce, cipherText, tag)

print(f"Cipher text: {cipherText}")
if not plainText: 
    print("Message is corrupted")
else: 
    print(f"Plaintext: {plainText}")
