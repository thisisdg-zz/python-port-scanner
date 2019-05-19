import random
import string
import socket

def randomize(stringLength = 10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


#def generateHash(systemIP, MAC):
    #generate Hash from random String and IP of the system