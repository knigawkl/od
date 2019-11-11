from collections import Iterable
from itertools import chain, takewhile, zip_longest

from Crypto.PublicKey import RSA


def numbers_to_text(numbers):
    fill_value = 0

    data = chain.from_iterable(map(separate_numbers, numbers))
    data = takewhile(lambda n: n != fill_value, data)  # Trim padding

    return bytes(data).decode()


def join_numbers(numbers):
    """Bijection that maps list of numbers to one big number"""
    return int(''.join(str(n + 100) for n in numbers))


def text_to_numbers(text: str, block_size=10):
    text = text.encode()
    fill_value = 0

    return (join_numbers(block) for block in grouper(text, block_size, fill_value))


def separate_numbers(number):
    """Bijection that one big number to maps list of numbers"""
    number = str(number)
    return (int(''.join(n)) - 100 for n in grouper(number, 3))


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


key = RSA.generate(2048)
private_key = key.exportKey()
file_out = open("private.pem", "wb")
file_out.write(private_key)

public_key = key.publickey().exportKey()
file_out = open("public.pem", "wb")
file_out.write(public_key)

data = None
file_to_encrypt = 'file.txt'
with open(file_to_encrypt) as file:
    data = file.read()

print('Dane do zaszyfrowania:')
print(data)
print()

encrypted = [key.publickey().encrypt(block, None)[0] for block in text_to_numbers(data)]


recovered = numbers_to_text((key.decrypt(block) for block in encrypted))
print('Odszyfrowane dane:')
print(recovered)