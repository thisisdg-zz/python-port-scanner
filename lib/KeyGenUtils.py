import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + './'))

import getpass
import uuid
from Crypto.Cipher import AES
import json
import hashlib
import random
import string
import base64
from constants import KeyGenConst


# Key have the length of 108 characters ends with '=' symbol.
# Please install pycryptodome before run this file. Use cmd 'pip install pycryptodome'.
# Change the folder to Crypto from crypto.
# Generated Key = (plain text + SALT) -> sha256_encryption -> AES encryption
# Verify Key = (provided key -> AES decryption) campare with ((plain text + SALT) -> sha256_encryption)


# return MAC address @return type String
def __getMac__():
    mac = hex(uuid.getnode())
    return mac


# return system user login id @return type String
def __getCurrentUser__():
    username = getpass.getuser()
    return username


# One System -> One Key @return type String
def getKeyBySystem():
    params = {
        'MAC': str(__getMac__())
    }
    jsonString = json.dumps(params)
    key = __generateKey__(jsonString)
    return key


# One User -> One Key @return type String
def getKeyByUsername():
    params = {
        'USERNAME': str(__getCurrentUser__())
    }
    jsonString = json.dumps(params)
    key = __generateKey__(jsonString)
    return key


# One User and One System -> One Key @return type String
def getKeyByUsernameAndSystem():
    params = {
        'USERNAME': str(__getCurrentUser__()),
        'MAC': str(__getMac__())
    }
    jsonString = json.dumps(params)
    key = __generateKey__(jsonString)
    return key


# @argument type String and @return type boolean
def verifyKeyBySystem(key):
    params = {
        'MAC': str(__getMac__())
    }
    jsonString = json.dumps(params)
    isVerified = __verifyKey__(jsonString, key)
    return isVerified


# @argument type String and @return type boolean
def verifyKeyByUsername(key):
    params = {
        'USERNAME': str(__getCurrentUser__())
    }
    jsonString = json.dumps(params)
    isVerified = __verifyKey__(jsonString, key)
    return isVerified


# @argument type String and @return type boolean
def verifyKeyByUsernameAndSystem(key):
    params = {
        'USERNAME': str(__getCurrentUser__()),
        'MAC': str(__getMac__())
    }
    jsonString = json.dumps(params)
    isVerified = __verifyKey__(jsonString, key)
    return isVerified


# @argument type String and @return type String
def __generateKey__(jsonString):
    hasher = __sha256Encode__(jsonString)
    return __aesEncode__(hasher)


# @argument type String and @return type boolean
def __verifyKey__(hashString, keyToBeVerify):
    providedHash = __aesDecode__(keyToBeVerify)
    originalHash = __sha256Encode__(hashString)
    return originalHash == providedHash


# SHA-256 Cryptographic Hash Algorithm.
# SHA-256 generates an almost-unique 256-bit (32-byte) signature for a text.
# @return type String

def __sha256Encode__(toEncodeString):
    # Appending SALT to toencode_string
    toEncodeString = '%s|%s' % (toEncodeString, KeyGenConst.SALT)
    return hashlib.sha256(toEncodeString.encode()).hexdigest()


# Pad to make the toEncode string multiple of BLOCK_SIZE
def __pad__(s): return s + (KeyGenConst.BLOCK_SIZE - len(s) % KeyGenConst.BLOCK_SIZE) * \
    chr(KeyGenConst.BLOCK_SIZE - len(s) % KeyGenConst.BLOCK_SIZE)


# UnPad
def __unpad__(s): return s[0:-ord(s[-1])]


# Advanced Encryption Standard(AES) using Ciphertext Block Chaining(CBC)
def __aesEncode__(toEncode):
    toEncode = __pad__(toEncode)

    cipher = AES.new(KeyGenConst.SECRET_KEY, AES.MODE_CBC,
                     KeyGenConst.IV.encode('latin-1'))
    encryptedBytes = cipher.encrypt(toEncode.encode('latin-1'))

    # Base 64 encode
    toEncode = base64.b64encode(encryptedBytes)

    # decode UTF-8 is used to convert bytes in to the String
    return toEncode.decode("UTF-8")


def __aesDecode__(toDecode):
    # Base 64 decode
    toDecode = base64.b64decode(toDecode)

    # Decrypt
    cipher = AES.new(KeyGenConst.SECRET_KEY, AES.MODE_CBC,
                     KeyGenConst.IV.encode('latin-1'))
    toDecode = cipher.decrypt(toDecode)

    # decode UTF-8 is used to convert bytes in to the String
    if type(toDecode) == bytes:
        toDecode = toDecode.decode("UTF-8")

    # unpad the data
    return __unpad__(toDecode)
