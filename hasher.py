import base64
import hashlib
import os
import time

dots = '*****************************************************'

def welcome():
    os.system('cls')
    print(dots)
    print('[!] Welcome to Hasher 1.0')
    print('[!] A base85+sha384 encoder')
    print('[!] Please save your hash in a file, we dont decrypt.')
    print(dots)

def base85e():
    msg = input('\n[!] Type the message to hash: ')
    msgb = msg.encode('ascii') # enconding to ascii
    base64b = base64.b85encode(msgb) # enconding in base85
    base64m = base64b.decode('ascii') # decoding the ascii
    
    sha_signature = \
        hashlib.sha384(base64m.encode()).hexdigest()
    print('\nEncoded key: ' + sha_signature)
    time.sleep(15)
    return sha_signature


welcome()
base85e()