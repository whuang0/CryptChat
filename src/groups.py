import json
from UEPEncryptionAlgorithm import *
from Crypto.Cipher import AES 
import json
from testingjson import *

def group_msg(msg):
    msgs = []
    msgs.append(msg)