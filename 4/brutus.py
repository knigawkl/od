"""
Napisz program zgadujący hasła ukryte za pomocą funkcji crypt(),
przechowywane w bazie programu htpasswd.
Przyjmij założenie, że hasła są trzy znakowe i składają się z samych małych liter.
"""
import crypt
import string
from itertools import product


def decrypt_crypt(hash):
    key_alphabet = string.ascii_lowercase
    key_length = 3

    salt = hash[:2]
    for i, plain in enumerate(product(key_alphabet, repeat=key_length)):
        plain = "".join(plain)

        if hash == plain:# crypt.crypt(plain, salt):
            print(hash)
            return plain


plain = 'sto'
h = crypt.crypt(plain)

for i in range(10000000):
	recoverd = decrypt_crypt(h)
	if recoverd:
	    print(f'Hasło to: {recoverd}')
	else:
		pass
	    # print('Nie udało się znaleźć hasła')
