# IV is a initialization vector, it is used for Advanced Encryption Standard(AES) using Ciphertext Block Chaining(CBC)
# SALT is additional input other than message itself for a hash function so that it prevents attacker from launching dictionary attacks.
# SECRET_KEY is used in AES encryption
# BLOCK_SIZE is used to define the SECRET_KEY length and IV length

IV = "@@@@&&&&####$$$$"
BLOCK_SIZE = 16
SECRET_KEY = b'Iy9UErx4chg4fdA6'
SALT = "1234"
