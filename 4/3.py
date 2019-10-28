"""
pierwsze 30 bitow takie samo
znajdz dwa pliki or oznej tresci i tym samym hashu sha 256
"""
from hashlib import sha256

from itertools import product
import string

key_alphabet = string.ascii_lowercase
key_length = 3


for i, plain in enumerate(product(key_alphabet, repeat=key_length)):
    plain = "".join(plain)
    hash1 = sha256(bytes(plain, 'utf-8'))
    for j, plaine in enumerate(product(key_alphabet, repeat=key_length)):
        plaine = "".join(plaine)
        hash2 = sha256(bytes(plaine, 'utf-8'))
        if(hash1.digest() == hash2.digest()):
            print(hash1.digest(), hash2.digest())


print(sha256(b'ala'))

