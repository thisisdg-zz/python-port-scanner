import uuid
import getpass
import Checksum

# Every Time Key will be different but gets verify only from the source it generated.
# Key have the length of 108 characters ends with '=' symbol.
# Please install pycryptodome before run this file. Use cmd 'pip install pycryptodome'.
# Change the folder to Crypto from crypto.


def __get_mac__():
    mac = hex(uuid.getnode())
    return mac

def __get_current_user__():
    username = getpass.getuser()
    return username


#One System -> One Key
def get_key_by_system():
    params = {
        'MAC': str(__get_mac__())
    }
    checksum = Checksum.generate_checksum(params, b'Iy9UErx4chg4fdA6')  #Key used for encryption
    return checksum


#One User -> One Key
def get_key_by_username():
    params = {
        'USERNAME': str(__get_current_user__())
    }
    checksum = Checksum.generate_checksum(params, b'Iy9UErx4chg4fdA6', '45')  #Key used for encryption
    return checksum


#One User and One System -> One Key
def get_key_by_username_and_system():
    params = {
        'USERNAME'  : str(__get_current_user__()),
        'MAC'       : str(__get_mac__())
    }
    checksum = Checksum.generate_checksum(params, b'Iy9UErx4chg4fdA6')  #Key used for encryption
    return checksum


def verify_key_by_system(key):
    params = {
        'MAC': str(__get_mac__())
    }
    isVerified = Checksum.verify_checksum(params, b'Iy9UErx4chg4fdA6', key)
    return isVerified


def verify_key_by_username(key):
    params = {
        'USERNAME': str(__get_current_user__())
    }
    isVerified = Checksum.verify_checksum(params, b'Iy9UErx4chg4fdA6', key, '45')
    return isVerified

def verify_key_by_username_and_system(key):
    params = {
        'USERNAME'  : str(__get_current_user__()),
        'MAC'       : str(__get_mac__())
    }
    isVerified = Checksum.verify_checksum(params, b'Iy9UErx4chg4fdA6', key)
    return isVerified


# Demo
# By System
key = get_key_by_system()
print(__get_mac__() + "   " + key)
print(verify_key_by_system(key))

# By Username
key = get_key_by_username()
print(__get_current_user__() + "   " + key)
print(verify_key_by_username(key))

# By Username
key = get_key_by_username()
print(__get_current_user__() + "   " + key)
print(verify_key_by_username(key))

# By Username and System
key = get_key_by_username_and_system()
print(__get_current_user__() + "   " + __get_mac__() + "   " + key)
print(verify_key_by_username_and_system(key))