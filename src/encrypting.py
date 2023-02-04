import json
from Crypto.Cipher import AES 
from secrets import token_bytes

class encryption:

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


        
    # def main():
        
    #     key = token_bytes(16) #creating a 16 byte key
    #     nonce, cipherText, tag = encrypt(input("enter a message to encyrpt: "), key)
    #     plainText = decrypt(nonce, cipherText, tag, key)

    #     print(f"Cipher text: {cipherText}")
    #     if not plainText: 
    #         print("Message is corrupted")
    #     else: 
    #         print(f"Plaintext: {plainText}")
            
    # main()
    