import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
from lib import KeyGenUtils


# Demo
# By System
key = KeyGenUtils.get_key_by_system()
print(KeyGenUtils.__get_mac__() + "   " + key)
print(KeyGenUtils.verify_key_by_system(key))

# By Username
key = KeyGenUtils.get_key_by_username()
print(KeyGenUtils.__get_current_user__() + "   " + key)
print(KeyGenUtils.verify_key_by_username(key))

# By Username
key = KeyGenUtils.get_key_by_username()
print(KeyGenUtils.__get_current_user__() + "   " + key)
print(KeyGenUtils.verify_key_by_username(key))

# By Username and System
key = KeyGenUtils.get_key_by_username_and_system()
print(KeyGenUtils.__get_current_user__() + "   " +
      KeyGenUtils.__get_mac__() + "   " + key)
print(KeyGenUtils.verify_key_by_username_and_system(key))
