import Crypto
from ast import operator
from Crypto.Cipher import DES3
from hashlib import md5

while True:
    print('Choose one of the following operations: \n\t 1- Encrypt\n\t2 - Decrypt')
    operation = input('Your choice:')
    if operation not in ['1', '2']:
        break
    file_path = input('File path: ')
    key = input('TDES key: ')
