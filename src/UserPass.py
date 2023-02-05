from encrypting import *
from Crypto.Cipher import AES 
import json





with open("users.json", 'r') as file: 
        users = json.load(file)
        username = users["user_details"][0]["username"]

        print(username)
usernameObj = encryption(username)
nonce, cipherText, tag = usernameObj.encrypt()
plainText = usernameObj.decrypt(nonce, cipherText, tag)
print(f"Cipher text: {cipherText}")
if not plainText: 
    print("Message is corrupted")
else: 
    print(f"Plaintext: {plainText}")


with open("users.json", 'r') as file: 
        users = json.load(file)
        password = users["user_details"][0]["password"]
passwordObj = encryption(password)
nonce1, cipherText1, tag1 = passwordObj.encrypt()
plainText1 = passwordObj.decrypt(nonce1, cipherText1, tag1)
print(f"Cipher text: {cipherText1}")
if not plainText1: 
    print("Message is corrupted")
else: 
    print(f"Plaintext: {plainText1}")

# y = {"username":cipherText,
#     "email": "sharansaha07@gmail.com",
#     "password" : cipherText1
#     }

# cipherTextString = string(cipherText)
# print(cipherTextString)
