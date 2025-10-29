#core/hasing.py

import hashlib
from core import database

#hashes password using sha256 algorithm
def hashFunc(password: str) -> str: #makes password a string
    passwordBytes = password.encode('utf-8') #turn string into bytes
    return hashlib.sha256(passwordBytes).hexdigest() #hash the bytes, turn into hexidecimal representation, return

#Checks if input password matches the stored hash one
def hashCheck(inputword, username):
    hashword = database.gethashWord(username) #Get users stored hashword
    inputHash = hashFunc(inputword) #hash the input password
    if inputHash == hashword:
        return True
    else:
        return False
