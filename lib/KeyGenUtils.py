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
def __get_mac__():
    mac = hex(uuid.getnode())
    return mac


# return system user login id @return type String
def __get_current_user__():
    username = getpass.getuser()
    return username


# One System -> One Key @return type String
def get_key_by_system():
    params = {
        'MAC': str(__get_mac__())
    }
    json_string = json.dumps(params)
    key = __generate_key__(json_string)
    return key


# One User -> One Key @return type String
def get_key_by_username():
    params = {
        'USERNAME': str(__get_current_user__())
    }
    json_string = json.dumps(params)
    key = __generate_key__(json_string)
    return key


# One User and One System -> One Key @return type String
def get_key_by_username_and_system():
    params = {
        'USERNAME': str(__get_current_user__()),
        'MAC': str(__get_mac__())
    }
    json_string = json.dumps(params)
    key = __generate_key__(json_string)
    return key


# @return type boolean
def verify_key_by_system(key):
    params = {
        'MAC': str(__get_mac__())
    }
    json_string = json.dumps(params)
    isVerified = __verify_key__(json_string, key)
    return isVerified


# @return type boolean
def verify_key_by_username(key):
    params = {
        'USERNAME': str(__get_current_user__())
    }
    json_string = json.dumps(params)
    isVerified = __verify_key__(json_string, key)
    return isVerified


# @return type boolean
def verify_key_by_username_and_system(key):
    params = {
        'USERNAME': str(__get_current_user__()),
        'MAC': str(__get_mac__())
    }
    json_string = json.dumps(params)
    isVerified = __verify_key__(json_string, key)
    return isVerified


# @argument type String and @return type String
def __generate_key__(json_string):
    hasher = __sha256_encode__(json_string)
    return __aes_encode__(hasher)


# @argument type tring and @return type boolean
def __verify_key__(hash_string, key_to_be_verify):
    provided_hash = __aes_decode__(key_to_be_verify)
    original_hash = __sha256_encode__(hash_string)
    return original_hash == provided_hash


# SHA-256 Cryptographic Hash Algorithm.
# SHA-256 generates an almost-unique 256-bit (32-byte) signature for a text.
# @return type String

def __sha256_encode__(toencode_string):
    # Appending SALT to toencode_string
    toencode_string = '%s|%s' % (toencode_string, KeyGenConst.SALT)
    return hashlib.sha256(toencode_string.encode()).hexdigest()


# Pad to make the to_encode string multiple of BLOCK_SIZE
def __pad__(s): return s + (KeyGenConst.BLOCK_SIZE - len(s) % KeyGenConst.BLOCK_SIZE) * \
    chr(KeyGenConst.BLOCK_SIZE - len(s) % KeyGenConst.BLOCK_SIZE)


# UnPad
def __unpad__(s): return s[0:-ord(s[-1])]


# Advanced Encryption Standard(AES) using Ciphertext Block Chaining(CBC)
def __aes_encode__(to_encode):
    to_encode = __pad__(to_encode)

    cipher = AES.new(KeyGenConst.SECRET_KEY, AES.MODE_CBC,
                     KeyGenConst.IV.encode('latin-1'))
    encrypted_bytes = cipher.encrypt(to_encode.encode('latin-1'))

    # Base 64 encode
    to_encode = base64.b64encode(encrypted_bytes)

    # decode UTF-8 is used to convert bytes in to the String
    return to_encode.decode("UTF-8")


def __aes_decode__(to_decode):
    # Base 64 decode
    to_decode = base64.b64decode(to_decode)

    # Decrypt
    cipher = AES.new(KeyGenConst.SECRET_KEY, AES.MODE_CBC,
                     KeyGenConst.IV.encode('latin-1'))
    to_decode = cipher.decrypt(to_decode)

    # decode UTF-8 is used to convert bytes in to the String
    if type(to_decode) == bytes:
        to_decode = to_decode.decode("UTF-8")

    # unpad the data
    return __unpad__(to_decode)
