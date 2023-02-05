import json
from Crypto.Cipher import AES 
from secrets import token_bytes

class EncryptionAlgorithm:

    def __init__(self, target):
        self.key = token_bytes(16)
        self.target = target

    def encrypt(self): # return nonce, cipher text and tag
        cipher = AES.new(self.key, AES.MODE_EAX) #cipher object
        nonce = cipher.nonce #the nonce 
        cipherText, tag = cipher.encrypt_and_digest(self.target.encode('ascii'))
                 
        return nonce, cipherText, tag 

    def decrypt(self, nonce, cipherText, tag):
        cipher = AES.new(self.key, AES.MODE_EAX, nonce) 
        plainText = cipher.decrypt(cipherText)
        
        #check to see if our text was changed
        try: 
            cipher.verify(tag) 
            return plainText.decode('ascii') 
        except:
            return False #cipher text is not authentic

    def __str__(self):
        return "hi"


        
# def main():
        
#     target = EncryptionAlgorithm('candycane')
#     nonce, cipherText, tag = target.encrypt()
#     plainText = target.decrypt(nonce, cipherText, tag)

#     print(f"Cipher text: {cipherText}")
#     if not plainText: 
#         print("Message is corrupted")
#     else: 
#         print(f"Plaintext: {plainText}")
            
# main()
    