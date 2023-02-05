from encrypting import *
from Crypto.Cipher import AES 
import json
from testingjson import *

def encrypt_credentials(username, email, password):
    usernameObj = encryption(username) 
    emailObj = encryption(email)
    passwordObj = encryption(password)
    nonce_username, cipherText_username, tag_username = usernameObj.encrypt() 
    nonce_email, cipher_email, tag_email = emailObj.encrypt()
    nonce_password, cipher_password, tag_password = passwordObj.encrypt() 
    return cipherText_username, cipher_email, cipher_password

def encrypt_username(username):
    usernameObj = encryption(username)
    nonce_username, cipherText_username, tag_username = usernameObj.encrypt()
    return usernameObj, nonce_username, cipherText_username, tag_username

def encrypt_email(email):
    emailObj = encryption(email)
    nonce_email, cipherText_email, tag_email = emailObj.encrypt()
    return emailObj, nonce_email, cipherText_email, tag_email

def encrypt_password(password):
    passwordObj = encryption(password)
    nonce_password, cipherText_password, tag_password = passwordObj.encrypt()
    return passwordObj, nonce_password, cipherText_password, tag_password

with open("users.json", "r") as file:
    users = json.load(file)
    
    username = users["user_details"][0]["username"]
    email = users["user_details"][0]["email"]
    password = users["user_details"][0]["password"]

encrypted_username = encrypt_username(username)
encrypted_email = encrypt_username(email)
encrypted_password = encrypt_username(password)

plainText = encrypted_username[0].decrypt(encrypted_username[1], encrypted_username[2], encrypted_username[3])
print(plainText)

plainText1 = encrypted_email[0].decrypt(encrypted_email[1], encrypted_email[2], encrypted_email[3])
print(plainText1)

plainText2 = encrypted_password[0].decrypt(encrypted_password[1], encrypted_password[2], encrypted_password[3])
print(plainText2)
    



# with open("users.json", 'r') as file: 
#         users = json.load(file)
#         username = users["user_details"][0]["username"]
# usernameObj = encryption(username)
# nonce, cipherText, tag = usernameObj.encrypt()
# plainText = usernameObj.decrypt(nonce, cipherText, tag)
# print(f"Cipher text: {cipherText}")
# if not plainText: 
#     print("Message is corrupted")
# else: 
#     print(f"Plaintext: {plainText}")


# with open("users.json", 'r') as file: 
#         users = json.load(file)
#         password = users["user_details"][0]["password"]
# passwordObj = encryption(password)
# nonce1, cipherText1, tag1 = passwordObj.encrypt()
# plainText1 = passwordObj.decrypt(nonce1, cipherText1, tag1)
# print(f"Cipher text: {cipherText1}")
# if not plainText1: 
#     print("Message is corrupted")
# else: 
#     print(f"Plaintext: {plainText1}")

# y = {"username":cipherText,
#     "email": "sharansaha07@gmail.com",
#     "password" : cipherText1
#     }

# write_json(y)

