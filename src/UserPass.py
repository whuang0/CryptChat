from encrypting import *
from Crypto.Cipher import AES 
username = ''
password = ''

nonce, cipherText, tag = encrypt(password, key)
