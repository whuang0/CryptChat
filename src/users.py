import json
from UEPEncryptionAlgorithm import *
from Crypto.Cipher import AES 
import json
from testingjson import *

class users:
    def __init__(self, id):
        self.id = id
        self.block = False
    
    def block(self):
        self.block = True

    def send_msg_to_be_encrypted(self, msg):
        self.user1 = users(self.id)
        self.msg = msg
        encryptObj = EncryptionAlgorithm(msg)
        nonce, ciphertext, tag = encryptObj.encrypt()

        with open("msgs.json", 'r+') as file: 

            file_data = json.load(file)
            file_data["message_details"][0]["user1_sent_content"].append(str(ciphertext))

            file.seek(0)

            json.dump(file_data, file, indent = 4)

def main():
    exuser = users(0)
    exuser.send_msg_to_be_encrypted('i love men so much')
main()
