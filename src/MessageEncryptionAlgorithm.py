#import pandas as pd
from Crypto.Cipher import AES 
from secrets import token_bytes

class MessageEncryptionAlgorithm: # Message Handler's purpose is to encrypt and decrypt messages.
    
   
    def __init__(self, message): # this is the constructor that sets up an instance of the object (self) to handle messages 
        self.key = token_bytes(16) # each object will have a particular key that will be used for both encryption and decryption
        self.message = message # each object will have a message to encrypt 
        
    def encrypt(self): # this method is to encrypt the MessageHandler object's target/message
        cipher = AES.new(self.key, AES.MODE_EAX) # creating the cipher object to do the work
        nonce = cipher.nonce # retrieving te nonce from the cipher object so that we can decrypt later 
        cipherText, tag = cipher.encrypt_and_digest(self.message.encode('ascii')) # cipherText is the encrypted text
                                                                                  # tag is sort of like a version history
                                                                                  
        return nonce, cipherText, tag
        
    def decrypt(self, nonce, cipherText, tag): # this method is to decrypt the MessageHandler object's decrypted text
        cipher = AES.new(self.key, AES.MODE_EAX, nonce) # creating another cipher object to do the work
        textToDecode = cipher.decrypt(cipherText) # textToDecode is the decrypted text
        
        try: # decode the text ONLY IF it was not "toyed" with 
            cipher.verify(tag) # check to see if anything was changed 
            return textToDecode.decode('ascii') # if nothing was changed, DECODE IT :)
        
        except: 
            return False #if not, return False 
        
        
            
        
        