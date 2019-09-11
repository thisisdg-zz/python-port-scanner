import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
from lib import KeyGenUtils


# Demo
# By System
key = KeyGenUtils.getKeyBySystem()
print(KeyGenUtils.__getMac__() + "   " + key)
print(KeyGenUtils.verifyKeyBySystem(key))

# By Username
key = KeyGenUtils.getKeyByUsername()
print(KeyGenUtils.__getCurrentUser__() + "   " + key)
print(KeyGenUtils.verifyKeyByUsername(key))

# By Username and System
key = KeyGenUtils.getKeyByUsernameAndSystem()
print(KeyGenUtils.__getCurrentUser__() + "   " +
      KeyGenUtils.__getMac__() + "   " + key)
print(KeyGenUtils.verifyKeyByUsernameAndSystem(key))
