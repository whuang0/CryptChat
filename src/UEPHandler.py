from UEPEncryptionAlgorithm import *
from Crypto.Cipher import AES 
import json
from testingjson import *

def encrypt(target):
    Obj = EncryptionAlgorithm(target)
    nonce, cipherText, tag = Obj.encrypt()
    return Obj, nonce, cipherText, tag

def get_credentials(index):
    with open("users.json", "r") as file:
        users = json.load(file)
        username = users["user_details"][index]["username"]
        email = users["user_details"][index]["email"]
        password = users["user_details"][index]["password"]
        return [username, email, password]

def override_to_encrypted(index): 
    encrypted_username = encrypt(get_credentials(index)[0])
    encrypted_email = encrypt(get_credentials(index)[1])
    encrypted_password = encrypt(get_credentials(index)[2])
    with open("users.json", 'r+') as file:
        users = json.load(file)
        file.seek(0)
        users["user_details"][0].update({"username":str(encrypted_username[2]),"email" : str(encrypted_email[2]), "password" : str(encrypted_password[2])})
        json.dump(users, file, indent = 4)
        file.truncate()
        
def retrieve_username(index):
    
    with open("users.json", "r") as file:
        users = json.load(file)
        encryptedUsername = users["user_details"][index]["username"]
        
        myList= encrypt(encryptedUsername) #nonce
        nonce = myList[1] 
        tag = myList[3]
        decryptedUsername = myList[0].decrypt(nonce, myList[2], tag)
        
    return decryptedUsername
        
        
        
        
    #     decryptedUsername = myList[0].decrypt(myList[1], myList[2], myList[3])
    
    # print(myList[3])
    
    #return decryptedUsername    

    
    
    
    
    

def main():
<<<<<<< HEAD
    override_to_encrypted()
    #retrieve_username(0)
    username = retrieve_username(0)
    print(username)
=======
    override_to_encrypted(0)
>>>>>>> 6f0f662b0ba01f7749432aeb170262f0ba87d8ab
    #print(encrypted_username)
    # print(encrypted_email)
    # print(encrypted_password)
    # plainText = encrypted_username[0].decrypt(encrypted_username[1], encrypted_username[2], encrypted_username[3])
    # print(plainText)
    # plainText1 = encrypted_email[0].decrypt(encrypted_email[1], encrypted_email[2], encrypted_email[3])
    # print(plainText1)
    # plainText2 = encrypted_password[0].decrypt(encrypted_password[1], encrypted_password[2], encrypted_password[3])
    # print(plainText2)
main()
