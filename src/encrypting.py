import json
from Crypto.Cipher import AES 
from secrets import token_bytes

def encrypt(msg, key): # return nonce, cipher text and tag
    cipher = AES.new(key, AES.MODE_EAX) #cipher object
    nonce = cipher.nonce #the nonce 
    cipherText, tag = cipher.encrypt_and_digest(msg.encode('ascii')) 
    
    return nonce, cipherText, tag 

def decrypt(nonce, cipherText, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce) 
    plainText = cipher.decrypt(cipherText)
    
    #check to see if our text was changed
    try: 
        cipher.verify(tag) 
        return plainText.decode('ascii') 
    except:
        return False #cipher text is not authentic


    
def main():
    
    key = token_bytes(16) #creating a 16 byte key
    nonce, cipherText, tag = encrypt(input("enter a message to encyrpt: "), key)
    plainText = decrypt(nonce, cipherText, tag, key)

    print(f"Cipher text: {cipherText}")
    if not plainText: 
        print("Message is corrupted")
    else: 
        print(f"Plaintext: {plainText}")
        
main()
    